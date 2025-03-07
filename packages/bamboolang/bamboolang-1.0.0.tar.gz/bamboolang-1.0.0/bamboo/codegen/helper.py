from bamboo.lang.dtype import NumT, FloatT, IntT


def CutFuncName(prefix: str) -> str:
    funcname: str = ""
    for x in prefix:
        if x != "<":
            funcname += x
        else:
            return funcname


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


def ConnectFieldName(name: str) -> str:
    fieldname: str = ""
    for x in name:
        if x == "%" or x == "-" or x == ">":
            pass
        else:
            fieldname += x

    return fieldname


def FieldNametoAsync(name: str) -> str:
    cname: str = ""
    for x in name:
        if x == "%":
            cname += "_"
        else:
            cname += x

    return cname


def StructPtoC(name: str) -> str:
    cname: str = ""
    for x in name:
        if x == "%":
            cname += "->"
        else:
            cname += x

    return cname


def AddSlidingWindowIndex(ctx: str, DSLname: str, fieldname: str) -> str:
    res: str = ""
    pos = 0

    # print("IN AddSlidingWindowIndex!!!" , ctx)

    index = ctx.find(DSLname)
    while index != -1:
        for i in range(pos, index):
            res += ctx[i]
        pos = index
        res += fieldname
        while ctx[pos] != "[":
            pos += 1
        # 加入原[
        pos += 1

        res += "swindex["

        while ctx[pos] != "]":
            res += ctx[pos]
            pos += 1

        # 加入原]
        res += ctx[pos]
        pos += 1

        res += "]"

        index = ctx.find(DSLname, pos)
        # print(res)
        # print(pos)
        # print(index)

    for i in range(pos, len(ctx)):
        res += ctx[i]

    return res


def ListToArray(s: str) -> str:
    res = "{" + s[1 : len(s) - 1] + "}"

    return res


def BoolListToC(s: str) -> str:
    res = s[1 : len(s) - 1]
    res = res.replace("T", "t")
    res = res.replace("F", "f")
    return res


def BoolToC(s: str) -> str:
    s = s.replace("T", "t")
    s = s.replace("F", "f")
    return s


def IntListToC(s: str) -> str:
    res = s[1 : len(s) - 1]
    return res


def DtypeToC(dtype: NumT) -> str:
    if isinstance(dtype, FloatT):
        if dtype.bits_width == 64:
            return "double"
        elif dtype.bits_width == 32:
            return "float"
    elif isinstance(dtype, IntT):
        if dtype.bits_width == 32:
            return "int"
    else:
        return "NAN"


def Lowercase(value: str) -> str:
    res = ""

    for x in value:
        if x == "T":
            res += "t"
        elif x == "F":
            res += "f"
        else:
            res += x

    return res
