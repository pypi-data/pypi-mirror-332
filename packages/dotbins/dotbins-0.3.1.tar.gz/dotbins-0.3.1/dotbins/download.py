"""Download and extraction functions for dotbins."""

from __future__ import annotations

import logging
import os
import re
import shutil
import tarfile
import tempfile
import zipfile
from pathlib import Path
from typing import TYPE_CHECKING

import requests
from rich.console import Console

from .utils import get_latest_release

if TYPE_CHECKING:
    from .config import DotbinsConfig
# Initialize rich console
console = Console()
logger = logging.getLogger(__name__)


def find_asset(assets: list[dict], pattern: str) -> dict | None:
    """Find an asset that matches the given pattern."""
    regex_pattern = (
        pattern.replace("{version}", ".*")
        .replace("{arch}", ".*")
        .replace("{platform}", ".*")
    )
    console.print(f"🔍 [blue]Looking for asset with pattern: {regex_pattern}[/blue]")

    for asset in assets:
        if re.search(regex_pattern, asset["name"]):
            console.print(f"✅ [green]Found matching asset: {asset['name']}[/green]")
            return asset

    return None


def download_file(url: str, destination: str) -> str:
    """Download a file from a URL to a destination path."""
    console.print(f"📥 [blue]Downloading from {url}[/blue]")
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        with open(destination, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return destination  # noqa: TRY300
    except requests.RequestException as e:
        console.print(f"❌ [bold red]Download failed: {e}[/bold red]")
        console.print_exception()  # Replaces logger.exception
        msg = f"Failed to download {url}: {e}"
        raise RuntimeError(msg) from e


def extract_archive(archive_path: str, dest_dir: str) -> None:
    """Extract an archive to a destination directory."""
    try:
        # Check file type
        is_gzip = False
        with open(archive_path, "rb") as f:
            header = f.read(3)
            if header.startswith(b"\x1f\x8b"):
                is_gzip = True

        if is_gzip or archive_path.endswith((".tar.gz", ".tgz")):
            with tarfile.open(archive_path, mode="r:gz") as tar:
                tar.extractall(path=dest_dir)
        elif archive_path.endswith((".tar.bz2", ".tbz2")):
            with tarfile.open(archive_path, mode="r:bz2") as tar:
                tar.extractall(path=dest_dir)
        elif archive_path.endswith(".zip"):
            with zipfile.ZipFile(archive_path) as zip_file:
                zip_file.extractall(path=dest_dir)
        else:
            msg = f"Unsupported archive format: {archive_path}"
            raise ValueError(msg)  # noqa: TRY301
    except Exception as e:
        console.print(f"❌ [bold red]Extraction failed: {e}[/bold red]")
        console.print_exception()  # Replaces logger.error with exc_info=True
        raise


def extract_from_archive(
    archive_path: str,
    destination_dir: Path,
    tool_config: dict,
    platform: str,
) -> None:
    """Extract binaries from an archive."""
    console.print(f"📦 [blue]Extracting from {archive_path} for {platform}[/blue]")
    temp_dir = Path(tempfile.mkdtemp())

    try:
        # Extract the archive
        extract_archive(str(archive_path), str(temp_dir))
        console.print(f"📦 [green]Archive extracted to {temp_dir}[/green]")

        # Debug: List the extracted files
        _log_extracted_files(temp_dir)

        # Handle single binary or multiple binaries
        binary_names = tool_config.get("binary_name", [])
        binary_paths = tool_config.get("binary_path", [])

        # Convert to lists if they're strings for consistent handling
        if isinstance(binary_names, str):
            binary_names = [binary_names]
        if isinstance(binary_paths, str):
            binary_paths = [binary_paths]

        # Create the destination directory if needed
        destination_dir.mkdir(parents=True, exist_ok=True)

        # Process each binary
        for i, binary_path_pattern in enumerate(binary_paths):
            # Get corresponding binary name (use last name for extra paths)
            binary_name = binary_names[min(i, len(binary_names) - 1)]

            # Find and copy each binary
            source_path = find_binary_in_extracted_files(
                temp_dir,
                tool_config,
                binary_path_pattern,
            )
            copy_binary_to_destination(source_path, destination_dir, binary_name)

    except Exception as e:
        console.print(f"❌ [bold red]Error extracting archive: {e}[/bold red]")
        console.print_exception()
        raise
    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)


def _log_extracted_files(temp_dir: Path) -> None:
    """Log the extracted files for debugging."""
    try:
        console.print("📋 [blue]Extracted files:[/blue]")
        for item in temp_dir.glob("**/*"):
            console.print(f"  - {item.relative_to(temp_dir)}")
    except Exception as e:  # noqa: BLE001
        console.print(f"❌ Could not list extracted files: {e}")


def find_binary_in_extracted_files(
    temp_dir: Path,
    tool_config: dict,
    binary_path: str,
) -> Path:
    """Find a specific binary in the extracted files."""
    # Replace variables in the binary path
    binary_path = replace_variables_in_path(binary_path, tool_config)

    # Handle glob patterns in binary path
    if "*" in binary_path:
        matches = list(temp_dir.glob(binary_path))
        if not matches:
            msg = f"No files matching {binary_path} in archive"
            raise FileNotFoundError(msg)
        return matches[0]

    # Direct path
    source_path = temp_dir / binary_path
    if not source_path.exists():
        msg = f"Binary not found at {source_path}"
        raise FileNotFoundError(msg)

    return source_path


def copy_binary_to_destination(
    source_path: Path,
    destination_dir: Path,
    binary_name: str,
) -> None:
    """Copy the binary to its destination and set permissions."""
    dest_path = destination_dir / binary_name

    # Copy the binary and set permissions
    shutil.copy2(source_path, dest_path)
    dest_path.chmod(dest_path.stat().st_mode | 0o755)
    console.print(f"✅ [green]Copied binary to {dest_path}[/green]")


def replace_variables_in_path(path: str, tool_config: dict) -> str:
    """Replace variables in a path with their values."""
    if "{version}" in path and "version" in tool_config:
        path = path.replace("{version}", tool_config["version"])

    if "{arch}" in path and "arch" in tool_config:
        path = path.replace("{arch}", tool_config["arch"])

    return path


def download_tool(
    tool_name: str,
    platform: str,
    arch: str,
    config: DotbinsConfig,
    force: bool = False,  # noqa: FBT001, FBT002
) -> bool:
    """Download a tool for a specific platform and architecture."""
    # Validate tool configuration
    tool_config = validate_tool_config(tool_name, config)
    if not tool_config:
        return False

    # Check if we should skip this download
    if should_skip_download(tool_name, platform, arch, config, force):
        return True

    try:
        # Get release information
        release, version = get_release_info(tool_config)

        # Map platform and architecture
        tool_platform, tool_arch = map_platform_and_arch(
            platform,
            arch,
            tool_config,
        )

        # Find matching asset
        asset = find_matching_asset(
            tool_config,
            release,
            version,
            platform,
            tool_platform,
            tool_arch,
        )
        if not asset:
            return False

        # Download and install the asset
        return download_and_install_asset(
            asset,
            tool_name,
            platform,
            arch,
            tool_config,
            config,
        )

    except Exception as e:  # noqa: BLE001
        console.print(
            f"❌ [bold red]Error processing {tool_name} for {platform}/{arch}: {e!s}[/bold red]",
        )
        console.print_exception()
        return False


def validate_tool_config(tool_name: str, config: DotbinsConfig) -> dict | None:
    """Validate that the tool exists in configuration."""
    tool_config = config.tools.get(tool_name)
    if not tool_config:
        console.print(
            f"❌ [bold red]Tool '{tool_name}' not found in configuration[/bold red]",
        )
        return None
    return tool_config


def should_skip_download(
    tool_name: str,
    platform: str,
    arch: str,
    config: DotbinsConfig,
    force: bool,  # noqa: FBT001
) -> bool:
    """Check if download should be skipped (binary already exists)."""
    destination_dir = config.tools_dir / platform / arch / "bin"
    binary_names = config.tools[tool_name].get("binary_name", tool_name)

    # Convert to list if it's a string
    if isinstance(binary_names, str):
        binary_names = [binary_names]

    # Check if all binaries exist
    all_exist = True
    for binary_name in binary_names:
        binary_path = destination_dir / binary_name
        if not binary_path.exists():
            all_exist = False
            break

    if all_exist and not force:
        console.print(
            f"✅ [green]{tool_name} for {platform}/{arch} already exists (use --force to update)[/green]",
        )
        return True
    return False


def get_release_info(tool_config: dict) -> tuple[dict, str]:
    """Get release information for a tool."""
    repo = tool_config["repo"]
    release = get_latest_release(repo)
    version = release["tag_name"].lstrip("v")
    tool_config["version"] = version  # Store for later use
    return release, version


def map_platform_and_arch(
    platform: str,
    arch: str,
    tool_config: dict,
) -> tuple[str, str]:
    """Map platform and architecture names."""
    # Map architecture if needed
    tool_arch = arch
    arch_map = tool_config.get("arch_map", {})
    if arch in arch_map:
        tool_arch = arch_map[arch]
    tool_config["arch"] = tool_arch  # Store for later use

    # Map platform if needed
    tool_platform = platform
    platform_map = tool_config.get("platform_map", {})
    if isinstance(platform_map, dict) and platform in platform_map:
        tool_platform = platform_map[platform]

    return tool_platform, tool_arch


def find_matching_asset(
    tool_config: dict,
    release: dict,
    version: str,
    platform: str,
    tool_platform: str,
    tool_arch: str,
) -> dict | None:
    """Find a matching asset for the tool."""
    # Determine asset pattern
    asset_pattern = get_asset_pattern(tool_config, platform, tool_arch)
    if not asset_pattern:
        console.print(
            f"⚠️ [yellow]No asset pattern found for {platform}/{tool_arch}[/yellow]",
        )
        return None

    # Replace variables in pattern
    search_pattern = asset_pattern.format(
        version=version,
        platform=tool_platform,
        arch=tool_arch,
    )

    # Find matching asset
    asset = find_asset(release["assets"], search_pattern)
    if not asset:
        console.print(
            f"⚠️ [yellow]No asset matching '{search_pattern}' found[/yellow]",
        )
        return None

    return asset


def get_asset_pattern(  # noqa: PLR0911
    tool_config: dict,
    platform: str,
    arch: str,
) -> str | None:
    """Get the asset pattern for a tool, platform, and architecture."""
    # No asset patterns defined
    if "asset_patterns" not in tool_config:
        console.print("⚠️ [yellow]No asset patterns defined[/yellow]")
        return None

    patterns = tool_config["asset_patterns"]

    # Case 1: String pattern (global pattern for all platforms/architectures)
    if isinstance(patterns, str):
        return patterns

    # Case 2: Dict of patterns by platform
    if isinstance(patterns, dict):
        # If platform not in dict or explicitly set to null, no pattern for this platform
        if platform not in patterns or patterns[platform] is None:
            console.print(
                f"⚠️ [yellow]No asset pattern defined for platform {platform}[/yellow]",
            )
            return None

        platform_patterns = patterns[platform]

        # Case 2a: String pattern for this platform
        if isinstance(platform_patterns, str):
            return platform_patterns

        # Case 3: Dict of patterns by platform and architecture
        if isinstance(platform_patterns, dict):
            # If arch not in dict or explicitly set to null, no pattern for this arch
            if arch not in platform_patterns or platform_patterns[arch] is None:
                console.print(
                    f"⚠️ [yellow]No asset pattern defined for {platform}/{arch}[/yellow]",
                )
                return None

            return platform_patterns[arch]

    # No valid pattern found
    console.print(f"⚠️ [yellow]No asset pattern found for {platform}/{arch}[/yellow]")
    return None


def download_and_install_asset(
    asset: dict,
    tool_name: str,
    platform: str,
    arch: str,
    tool_config: dict,
    config: DotbinsConfig,
) -> bool:
    """Download and install an asset."""
    destination_dir = config.tools_dir / platform / arch / "bin"
    destination_dir.mkdir(parents=True, exist_ok=True)

    # Handle binary_name as string or list
    binary_names = tool_config.get("binary_name", tool_name)
    if isinstance(binary_names, str):
        binary_names = [binary_names]

    # Create a temporary file for download
    tmp_dir = Path(tempfile.gettempdir())
    temp_path = tmp_dir / asset["browser_download_url"].split("/")[-1]

    try:
        # Download the asset
        download_file(asset["browser_download_url"], temp_path)

        if tool_config.get("extract_binary", False):
            # Extract the binary using the explicit path
            extract_from_archive(temp_path, destination_dir, tool_config, platform)
        else:
            # For direct downloads with multiple binaries, we can only copy one
            # Just use the first binary name
            binary_name = binary_names[0]
            # Copy the file directly
            shutil.copy2(temp_path, destination_dir / binary_name)
            # Make executable
            dest_file = destination_dir / binary_name
            dest_file.chmod(dest_file.stat().st_mode | 0o755)

        console.print(
            f"✅ [green]Successfully downloaded {tool_name} for {platform}/{arch}[/green]",
        )
        return True

    finally:
        # Cleanup
        if os.path.exists(temp_path):
            os.unlink(temp_path)


def make_binaries_executable(config: DotbinsConfig) -> None:
    """Make all binaries executable."""
    for platform in config.platforms:
        for arch in config.architectures:
            bin_dir = config.tools_dir / platform / arch / "bin"
            if bin_dir.exists():
                for binary in bin_dir.iterdir():
                    if binary.is_file():
                        binary.chmod(binary.stat().st_mode | 0o755)
