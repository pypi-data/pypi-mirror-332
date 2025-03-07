from dataclasses import dataclass
from typing import Generic, Optional, Tuple, Type, TypeVar


_T = TypeVar("_T")


@dataclass
class DictTuple(Generic[_T]):
    items: Tuple[Tuple[str, _T], ...]

    def __post_init__(self):
        self.items_dict = dict((k, (id, v)) for id, (k, v) in enumerate(self.items))

    def __len__(self):
        return len(self.items)

    def has(self, name: str):
        return name in self.items_dict

    def get(self, name: str, default: Optional[_T] = None):
        if name in self.items_dict:
            return self.items_dict[name][1]
        else:
            return default

    def __iter__(self):
        return self.items.__iter__()

    def __getitem__(self, key: int):
        return self.items[key]


class ObjId:
    id = -1

    @staticmethod
    def new_id():
        ObjId.id += 1
        return ObjId.id


def mangle(name: str):
    symbs = ("<", ">", "%", ".")
    for id, sym in enumerate(symbs):
        name = name.replace(sym, f"${id}$")
    return name


def demangle(name: str):
    symbs = ("<", ">", "%", ".")
    sp = name.split("$")
    return "".join(symbs[int(i)] if i[0].isdigit() else i for i in sp)
