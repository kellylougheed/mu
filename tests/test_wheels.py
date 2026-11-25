import os
import sys
from unittest import mock

from mu.wheels import os_compatibility_flags


def test_macos_compatibility_flags_default_to_apple_intel():
    with mock.patch.object(sys, "platform", "darwin"):
        with mock.patch.dict(os.environ, {}, clear=True):
            assert os_compatibility_flags() == [
                "--platform=macosx_10_12_x86_64",
                "--only-binary=:all:",
            ]


def test_macos_compatibility_flags_honor_configured_platform():
    with mock.patch.object(sys, "platform", "darwin"):
        with mock.patch.dict(
            os.environ,
            {"MACOS_PIP_PLATFORM": "macosx_11_0_arm64"},
            clear=True,
        ):
            assert os_compatibility_flags() == [
                "--platform=macosx_11_0_arm64",
                "--only-binary=:all:",
            ]
