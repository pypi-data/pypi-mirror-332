def GetSpace(s: str) -> int:
    if s == "o" or s == "x" or s == "y" or s == "xy":
        return 1
    elif s == "z" or s == "xz":
        return 2
    else:
        return 3


def Sizeof(s: str) -> int:  # B
    if s == "int":
        return 4
    elif s == "float":
        return 4
    elif s == "double":
        return 8
    else:
        return 0


def CutFieldName(name: str) -> str:
    f = False
    fieldname: str = ""
    for x in name:
        if x == "%" or x == "-" or x == ">":
            f = True
        else:
            if f:
                fieldname += x
    if f:
        return fieldname
    else:
        return name
