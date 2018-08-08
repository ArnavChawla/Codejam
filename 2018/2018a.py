def swaps(damage, sequence):
    if(int(damage)<sequence.count('S')):
        return "IMPOSIBLE"
    total = 0
    strength = 1
    for char in sequence:
        if(char == 'S'):
            total += strength
        else:
            strength *=2
    if(int(damage) >= total):
        return "0"
    return recurse(damage,sequence,len(sequence)-1)

def recurse(damage, string,index):
    print("here")
    totalswaps = 0
    if(index >= 1):
        index = index
    else:
        index = len(string)-1
    charfound = False
    char = ""
    num = len(string)-1
    while(charfound == False):
        string = list(string)
        char = string[num]
        print(char)
        if char == "S":
            print("found")
            charfound=True
            if string[index-1] == "C":
                print("c foun")
                totalswaps+=1
                tmp = string[index]
                string[index] = string[index-1]
                string[index-1] = tmp
                index-=1
                string = ''.join(string)
                print(string)
                charfound=True
            else:
                string = ''.join(string)
                print(string)
                index-=1
        else:
            num -=1
    print(calculate(string))
    if(calculate(string) >  damage):

        return totalswaps + recurse(damage,string,index)
    else:
        return totalswaps
def calculate(string):
    total = 0
    strength = 1
    dealt = 0
    for char in string:
        if(char == 'C'):
            strength *=2
        else:
            dealt += strength
    return dealt
print(swaps(1,"SS"))
# T = int(input())
# for case in range(1, T+1):
#     D, P = input().split()
#     D = int(D)
#     print("Case #{}: {}".format(case, swaps(D,P)))
