def compute():
    var = input()
    max = int(var.split(" ")[0])
    string = str(var.split(" ")[1])
    if max < string.count("S"):
        return "IMPOSSIBLE"
    dealt = 0
    power = 1
    for char in string:
        if char == "S":
            dealt += power
        else:
            power *= 2
    if max - dealt >= 0:
        return 0
    swaps = 0
    solved = False
    hold = ""
    i = len(string) - 1
    while i >=0:
        if string[i] == "S" and string[i-1]== "C":
            swaps +=1
            for j in range(0,len(string)):
                if j == i:
                    hold += string[i-1]
                elif j ==i-1:
                    hold += string[i]
                else:
                    hold+=string[j]
            dealt = 0
            power = 1
            i = len(string) - 1
            for char in hold:
                if char == "S":
                    dealt += power
                else:
                    power *= 2
            if max - dealt >= 0:
                solved = True
                return swaps
            else:
                string = hold
                hold = ""
        else:
            i-=1
if __name__ == "__main__":
    cases = int(input())
    for i in range(1,cases+1):
        print("Case #{}: {}".format(i,compute()))
