#!/usr/bin/env python3
"""news-image-20261124 entry: deliver the 24 November 2026 front page.

The front page image (entry.png) sits beside this file; it was drawn
in-session for this entry with Pillow. This program just copies it to
the grader's output directory and refuses to finish unless the copy
is a valid 1024x1024 PNG under the 1 MiB cap. No network, no
randomness, so repeated runs write identical bytes. Outside the
grader, MAKEFUN_OUTPUT_DIR stands in for /output.
"""
import hashlib
import os
import shutil
import struct
import sys

LIMIT = 1048576
MAGIC = b"\x89PNG\r\n\x1a\n"

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
TARGET = os.path.join(TARGET_DIR, "entry.png")


def fail(message):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def inspect_png(path):
    """Return (width, height, size, sha256) or fail with a clear reason."""
    with open(path, "rb") as handle:
        blob = handle.read()
    if blob[:8] != MAGIC:
        fail("output is not a PNG file")
    width, height = struct.unpack(">II", blob[16:24])
    if (width, height) != (1024, 1024):
        fail("output is %dx%d, want 1024x1024" % (width, height))
    if len(blob) > LIMIT:
        fail("output is %d bytes, over the 1 MiB cap" % len(blob))
    if blob[-12:-8] != b"\x00\x00\x00\x00" or blob[-8:-4] != b"IEND":
        fail("output is missing its IEND chunk")
    return width, height, len(blob), hashlib.sha256(blob).hexdigest()


def main():
    os.makedirs(TARGET_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    width, height, size, digest = inspect_png(TARGET)
    print("entry.png OK: %dx%d, %d bytes, sha256 %s"
          % (width, height, size, digest[:16]))


if __name__ == "__main__":
    main()
