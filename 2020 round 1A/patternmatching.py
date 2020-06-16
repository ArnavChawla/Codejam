def compute(case):
    number = int(input())
    strings = []
    prefixes = []
    suffixes = []
    for i in range(0,number):
        strings.append(input())
    for filter in strings:
        new = filter.split("*")
        if new[0] != "":
            prefixes.append(new[0])
        if new[1] != "":
            suffixes.append(new[1])

    prefixes.sort(key = len)
    prefixes.reverse()
    suffixes.sort(key = len)
    suffixes.reverse()
    try:
        basepre= prefixes[0]
    except:
        basepre= ""
    try:
        basesuff = suffixes[0]
    except:
        basesuff = ""
    try:
        for i in range(1,len(suffixes)):
            for j in range(-1,-len(suffixes[i])-1,-1):
                if suffixes[i][j] != basesuff[j]:
                    return "Case #{}: *".format(case)
    except:
        pass
    try:
        for i in range(1,len(prefixes)):
            for j in range(len(prefixes),0):
                if prefixes[i][j] != basepre[j]:
                    return "Case #{}: *".format(case)
    except:
        pass
    if basepre == basesuff:
        basepre=""
    return "Case #{}: {}{}".format(case,"".join(basepre[x] for x in range(0,len(basepre))),"".join(basesuff[x] for x in range(0,len(basesuff))))
if __name__ == "__main__":
    cases = int(input())
    for i in range(1,cases+1):
        print(compute(i))
