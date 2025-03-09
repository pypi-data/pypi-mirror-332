import os
import pytest
import local_ffmpeg


def test_ffmpeg_install():
    local_ffmpeg.install_ffmpeg()
    ffmpeg_path = local_ffmpeg.get_ffmpeg_path()
    assert os.path.exists(ffmpeg_path), "FFmpeg should be installed"
