def compute():
    size = int(input())
    string = input()
    odd = []
    even = []
    split = string.split(" ")
    for i in range(0, len(split)):
        if i % 2 == 0:
             even.append(int(split[i]))
        else:
            odd.append(int(split[i]))
    odd.sort()
    even.sort()
    new = []
    for i in range(0,len(split)):
        if i % 2 == 0:
            new.append(even[0])
            even.pop(0)
        else:
            new.append(odd[0])
            odd.pop(0)
    max = -999999
    for i in range(0,len(new)):
        num = new[i]
        if num > max:
            max = num
        elif num < max:
            return new.index(max)
    return "OK"
if __name__ == "__main__":
    cases = (int(input()))
    for i in range(0,cases):
        print("Case #{}: {}".format(i+1,compute()))
