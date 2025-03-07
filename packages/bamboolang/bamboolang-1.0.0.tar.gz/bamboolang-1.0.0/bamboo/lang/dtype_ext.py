from typing import Generic, Tuple, TypeVar
from bamboo.lang.annot import Field
from bamboo.lang.dtype import FieldDesc, ValT

T = TypeVar("T")


class LonLatFieldDesc(FieldDesc):
    def __init__(self, pos: Tuple[bool, bool, bool], const: bool):
        super().__init__("LonLatField")
        self.pos = pos
        self.const = const


class LonLatField(Field, Generic[T]):
    def __init__(
        self,
        dtype,
        shape: Tuple[int, ...],
        pos: Tuple[bool, bool, bool] = [True, True, True],
        const: bool = False,
    ) -> None:
        super().__init__(dtype, shape, LonLatFieldDesc(pos, const))


class CubedSphereFieldDesc(FieldDesc):
    def __init__(self, pos: Tuple[bool, bool, bool], const: bool, usepanel: bool):
        super().__init__("CubedSphereField")
        self.pos = pos
        self.const = const
        self.usepanel = usepanel


class CubedSphereField(Field, Generic[T]):
    def __init__(
        self,
        dtype,
        shape: Tuple[int, ...],
        pos: Tuple[bool, bool, bool] = [True, True, True],
        const: bool = False,
        usepanel: bool = False,
    ) -> None:
        super().__init__(dtype, shape, CubedSphereFieldDesc(pos, const, usepanel))
