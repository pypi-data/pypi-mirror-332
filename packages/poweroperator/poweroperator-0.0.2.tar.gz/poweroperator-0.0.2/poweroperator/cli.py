#!/usr/bin/env python3
import sys
import traceback
import tempfile
import os
import atexit
import getpass
import socket
from scalene import scalene_profiler
from .poweroperator_api import upload_mark_with_file


def should_trace(s: str) -> bool:
    # TODO: is this used? the sclane_profiler.__main__.main function has it
    if scalene_profiler.Scalene.is_done():
        return False
    return scalene_profiler.Scalene.should_trace(s)


def get_temp_profile_path() -> str:
    temp_file = tempfile.NamedTemporaryFile(
        suffix=".json", prefix="profile_", delete=False
    )
    temp_filename = temp_file.name
    temp_file.close()  # close but keep the name

    def cleanup():
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

    atexit.register(cleanup)
    return temp_filename


def fix_cmdline_args(profile_path: str):
    sys.argv[1:1] = ["--cli", "--no-browser", "--json", f"--outfile={profile_path}"]


def file_exists_and_not_empty(file_path: str):
    return os.path.isfile(file_path) and os.path.getsize(file_path) > 0


def main():
    print("[poweroperator] Starting program under benchmarking...")
    profile_path = get_temp_profile_path()
    fix_cmdline_args(profile_path)

    try:
        from scalene import scalene_profiler

        try:
            scalene_profiler.Scalene.main()
        finally:
            if not file_exists_and_not_empty(profile_path):
                print(
                    "[poweroperator] Benchmarked program exited but no benchmarks available, skipping upload."
                )
            else:
                print(
                    "[poweroperator] Benchmarked program exited. Uploading benchmarks..."
                )
                user = getpass.getuser()
                hostname = socket.gethostname()
                cwd = os.getcwd()
                upload_mark_with_file(
                    user,
                    "function-1",
                    profile_path,
                    hostname,
                    sys.argv,
                    [],  # don't send `os.environ` for now,
                    cwd,
                )
                print("[poweroperator] Upload successful")
    except Exception as exc:
        sys.stderr.write(
            "[poweroperator] Error: calling Scalene profiler main function failed: %s\n"
            % exc
        )
        traceback.print_exc()


if __name__ == "__main__":
    main()
