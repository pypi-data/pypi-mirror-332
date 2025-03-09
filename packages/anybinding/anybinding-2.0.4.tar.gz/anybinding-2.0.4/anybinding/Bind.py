# -*-coding:utf8;-*-
import subprocess
import os
from typing import Union, Optional, Any, Callable, List


class CalledProcessError(Exception):
    pass


class Bind:
    def __init__(
        self,
        bin: str,
        path: Optional[str] = None,
        direct_output: bool = False,
        timeout: Optional[int] = None,
    ) -> None:
        self.bin: str = bin
        self.pid: int = 0
        self.timeout: Optional[int] = timeout
        self.direct_output: bool = direct_output

        if path is None:
            self.path: str = os.getcwd()
        else:
            if os.path.isdir(path):
                self.path = path
            else:
                raise IOError("path isn't exists!")
        self.prompt: Optional[str] = None

    def _evaluate(self, commands: List[str]) -> str:
        if self.direct_output:
            p = subprocess.Popen(
                commands,
                cwd=self.path,
                universal_newlines=True,
            )
            self.pid = p.pid
            p.communicate(input=self.prompt)
            p.wait(timeout=self.timeout)
            if p.poll() != 0:
                raise CalledProcessError(f"exit code: {p.poll()}")
        else:
            p = subprocess.Popen(
                commands,
                cwd=self.path,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
            self.pid = p.pid
            stdout, _ = p.communicate(input=self.prompt)
            p.wait(timeout=self.timeout)
            if p.poll() != 0:
                raise CalledProcessError(stdout)
            return stdout
        return ""

    def _(self, *args: Any, **kwargs: Any) -> str:
        command: List[str] = [str(i) for i in args]
        for k, v in kwargs.items():
            if k == "_":
                if len(v):
                    command.append(v)
                continue
            elif len(k) > 1:
                k = "--" + str(k).replace("_", "-")
            else:
                k = "-" + str(k).replace("_", "-")

            command.append(k)
            if len(v):
                command.append(v)

        command.insert(0, self.bin)

        if self.direct_output:
            p = subprocess.Popen(command, cwd=self.path, universal_newlines=True)
            self.pid = p.pid
            p.communicate(input=self.prompt)
            p.wait(timeout=self.timeout)
            if p.poll() != 0:
                raise CalledProcessError(f"exit code: {p.poll()}")
        else:
            p = subprocess.Popen(
                command,
                cwd=self.path,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
            self.pid = p.pid
            stdout, _ = p.communicate(input=self.prompt)
            p.wait(timeout=self.timeout)
            if p.poll() != 0:
                raise CalledProcessError(stdout)
            return stdout
        return ""

    def __getattr__(self, name: str) -> Callable[..., str]:
        def call_cmd(*args: Any, **kwargs: Any) -> str:
            args_list: List[str] = [str(i) for i in args]

            for k, v in kwargs.items():
                if k == "_":
                    if len(v):
                        args_list.append(str(v))
                    continue
                elif len(k) > 1:
                    k = "--" + str(k).replace("_", "-")
                else:
                    k = "-" + str(k).replace("_", "-")

                args_list.append(k)
                if len(v):
                    args_list.append(v)

            args_list.insert(0, name.replace("_", "-"))
            args_list.insert(0, self.bin)

            return self._evaluate(args_list)

        return call_cmd


def sh(
    commands: List[str],
    cwd: Optional[str] = None,
    input: Optional[str] = None,
    timeout: Optional[int] = None,
    direct_output: bool = False,
    output_path: Optional[str] = None,
) -> Union[str, None]:
    if output_path or not direct_output:
        p = subprocess.Popen(
            commands,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            cwd=cwd,
        )
    else:
        p = subprocess.Popen(commands, universal_newlines=True, cwd=cwd)
    stdout, stderr = p.communicate(input=input)
    p.wait(timeout=timeout)
    if p.poll() != 0:
        if direct_output:
            raise CalledProcessError(f"exit code: {p.poll()}")
        else:
            if not output_path:
                raise CalledProcessError(stdout)
    else:
        if output_path:
            with open(output_path, "w") as f:
                f.write(stdout)
        else:
            return stdout
    return None
