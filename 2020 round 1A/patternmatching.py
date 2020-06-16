def compute(case):
    number = int(input())
    strings = []
    prefixes = []
    suffixes = []
    middle = []
    for i in range(0,number):
        strings.append(input())
    for string in strings:
        new = string.split("*")
        if string.count("*") == 1:
            if new[0] != "":
                prefixes.append(new[0])
            if new[1] != "":
                suffixes.append(new[1])
        else:
            prefixes.append(new[0])
            suffixes.append(new[-1])
            for i in range(1,len(new)-1):
                middle.append(new[i])


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
            for j in range(0,len(prefixes)):
                if prefixes[i][j] != basepre[j]:
                    return "Case #{}: *".format(case)
    except:
        pass
    return "Case #{}: {}{}{}".format(case,"".join(basepre[x] for x in range(0,len(basepre))),"".join(item for item in middle),"".join(basesuff[x] for x in range(0,len(basesuff))))
if __name__ == "__main__":
    cases = int(input())
    for i in range(1,cases+1):
        print(compute(i))
