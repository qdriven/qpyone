#!/usr/bin/env python
import subprocess
import time


"""
Most Shell Command could be replaced by:
1. shutil
2. Path
"""

__all__ = ["ShellResult", "wait_process_end", "shell"]


class ShellResult:
    def __init__(self, return_code, stdout, stderr):
        self.return_code = return_code
        self.stdout = stdout
        self.stderr = stderr


def wait_process_end(process, timeout):
    if timeout <= 0:
        process.wait()
        return 0
    start_time = time.time()
    end_time = start_time + timeout
    while 1:
        ret = process.poll()
        if ret == 0:
            return 0
        elif ret is None:
            cur_time = time.time()
            if cur_time >= end_time:
                return 1
            time.sleep(0.1)
        else:
            return 2


def shell(command, capture=False) -> ShellResult:
    """execute local shell command
    @return (returncode)
    """
    if capture:
        proc = subprocess.run(
            command,
            stdin=subprocess.PIPE,
            capture_output=True,
            shell=True,
        )
    else:
        proc = subprocess.run(command, shell=True)
    print(proc.returncode, proc.stdout.decode("utf-8"))
    if capture:
        return ShellResult(
            proc.returncode,
            proc.stdout.decode("utf-8") if proc.stdout else None,
            proc.stderr.decode("utf-8") if proc.stderr else None,
        )
    else:
        return ShellResult(proc.returncode, None, None)
