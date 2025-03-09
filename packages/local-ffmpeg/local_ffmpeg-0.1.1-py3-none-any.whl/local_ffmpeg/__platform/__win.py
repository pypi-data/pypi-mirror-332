"""
Windows-specific implementation for FFmpeg installation
"""

import os
import platform
import shutil
import subprocess
import zipfile
from typing import Optional

__all__ = ["WindowsHandler"]


class WindowsHandler:
    """Handler for Windows platform"""

    def get_download_url(self) -> str:
        """
        Get the appropriate FFmpeg download URL for Windows

        Returns:
            URL to download FFmpeg from

        Raises:
            RuntimeError: If architecture is unsupported
        """
        # Check if x64 architecture
        if platform.machine().endswith("64"):
            return "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
        else:
            raise RuntimeError("Only 64-bit Windows is supported")

    def install(self, download_path: str, install_path: str) -> None:
        """
        Install FFmpeg from downloaded archive to the specified path

        Args:
            download_path: Path to the downloaded archive
            install_path: Directory where FFmpeg binaries will be installed

        Raises:
            RuntimeError: If installation fails
        """
        try:
            print(f"Extracting FFmpeg archive...")

            # Extract ZIP file
            with zipfile.ZipFile(download_path, "r") as zip_ref:
                # Extract only bin directory (usually in a subdirectory)
                for file_info in zip_ref.infolist():
                    if (
                        "/bin/ffmpeg.exe" in file_info.filename
                        or "/bin/ffprobe.exe" in file_info.filename
                        or "/bin/ffplay.exe" in file_info.filename
                    ):
                        # Extract to temporary location
                        zip_ref.extract(file_info, path=os.path.dirname(download_path))

            # Find and move the binaries to the install path
            extracted_dir = os.path.dirname(download_path)
            for root, _, files in os.walk(extracted_dir):
                for file in files:
                    if file in ("ffmpeg.exe", "ffprobe.exe", "ffplay.exe"):
                        src = os.path.join(root, file)
                        dst = os.path.join(install_path, file)
                        shutil.move(src, dst)

            # Clean up temporary files
            if os.path.exists(download_path):
                os.remove(download_path)

            print(f"FFmpeg installed successfully to {install_path}")

        except Exception as e:
            raise RuntimeError(f"Failed to install FFmpeg: {e}")

    def uninstall(self, install_path: str) -> None:
        """
        Uninstall FFmpeg from the specified path

        Args:
            install_path: Directory where FFmpeg binaries are installed
        """
        for binary in ("ffmpeg.exe", "ffprobe.exe", "ffplay.exe"):
            binary_path = os.path.join(install_path, binary)
            if os.path.exists(binary_path):
                os.remove(binary_path)

    def check_installed(self, path: Optional[str] = None) -> bool:
        """
        Check if FFmpeg is installed at the specified path

        Args:
            path: Directory to check for FFmpeg binaries

        Returns:
            True if FFmpeg is installed, False otherwise
        """
        if not path:
            return False

        ffmpeg_path = os.path.join(path, "ffmpeg.exe")

        if not os.path.exists(ffmpeg_path):
            return False

        try:
            # Try running the binary to verify it works
            result = subprocess.run(
                [ffmpeg_path, "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5
            )
            return result.returncode == 0
        except (subprocess.SubprocessError, OSError):
            return False
