# -*-coding:UTF-8 -*-
import datetime

import colorama


class Logger():
    # Fail Error Warn Debug Info
    def __init__(self, LoggerFormat='[{0}:{1}:{2}/{3}] {4}') -> None:
        colorama.init(autoreset=True)
        self.LoggerFormat = LoggerFormat
        self.logs = []

    def _output(self, type_, text, color):
        _msg = self.LoggerFormat.format(
            str(datetime.datetime.now().hour),
            str(datetime.datetime.now().minute),
            str(datetime.datetime.now().second),
            str(type_),
            str(text),
        )
        self.logs.append(_msg)
        print(color + _msg)

    def info(self, t, safeLevel=4) -> int:
        self._output('INFO', t, colorama.Fore.GREEN)
        return safeLevel

    def debug(self, t, safeLevel=3) -> int:
        self._output('DEBUG', t, colorama.Fore.CYAN)
        return safeLevel

    def warn(self, t, safeLevel=2) -> int:
        self._output('WARN', t, colorama.Fore.YELLOW)
        return safeLevel

    def error(self, t, safeLevel=1) -> int:
        self._output('ERROR', t, colorama.Fore.RED)
        return safeLevel

    def fail(self, t, safeLevel=0) -> int:
        self._output('Fail', t, colorama.Fore.LIGHTRED_EX)
        return safeLevel