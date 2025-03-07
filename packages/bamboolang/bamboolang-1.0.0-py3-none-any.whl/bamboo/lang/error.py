class Loc:
    def __init__(self, file: str = "", func: str = "", line: int = 0) -> None:
        self.file = file
        self.line = line
        self.func = func

    def __str__(self) -> str:
        return f"{self.file}:{self.func}:{self.line}"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __o: object) -> bool:
        return type(__o) == Loc

    def __ne__(self, __o: object) -> bool:
        return type(__o) != Loc


class LangTypeError(Exception):
    def __init__(self, loc: Loc, msg: str) -> None:
        super().__init__(loc, msg)


class LangSyntaxError(Exception):
    def __init__(self, loc: Loc, msg: str) -> None:
        super().__init__(loc, msg)


class LangResolveError(Exception):
    def __init__(self, loc: Loc, msg: str) -> None:
        super().__init__(loc, msg)
