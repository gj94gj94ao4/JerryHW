def plus(*args):
    return sum(args)

def sub(*args):
    if len(args)%2==1:
        return "Exception"
    outlist = []
    for nu in range(int(len(args)/2)):
        outlist.append(args[nu*2] - args[nu*2+1])
    return outlist

def mul(*args):
    out = 1
    for i in range(len(args)):
        out = out * args[i]
    return out

def dev(*args):
    if len(args)%2==1:
        return "Exception"
    outlist = []
    for nu in range(int(len(args)/2)):
        outlist.append(args[nu*2] / args[nu*2+1])
    return outlist

def run(func,*args):
    funcdist = {
        "+":plus,
        "-":sub,
        "*":mul,
        "/":dev
    }
    return funcdist[func](*args)