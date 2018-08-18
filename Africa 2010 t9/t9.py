chars = ["abc","def",
        "ghi","jkl","mno",
        "pqrs","tuv","wxyz"]
def find(message):
    toReturn = ""
    previous = 1
    for char in message:
        found = False
        i = 2
        if(char != " "):
            for segment in chars:
                x = 1
                for letter in segment:
                    if(letter == char):
                        if(found == False):
                            if(previous==i):
                                toReturn += " "
                        previous = i
                        found == True
                        for y in range(x):
                            toReturn += str(i)
                    else:
                        x+=1
                i+=1
        else:
            if(previous==0):
                toReturn += " 0"
            else:
                toReturn +="0"
            previous = 0
    return toReturn
a = open("t9-l.in","r")
f = open("t9.out","w+")
cases = int(a.readline())
for i in range(1,cases+1):
    f.write("Case #{}: {}\n".format(i,find(a.readline().rstrip('\n'))))
f.close()
