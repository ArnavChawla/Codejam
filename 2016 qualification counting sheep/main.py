f = open("A-large-practice.in","r")
a = open('output.txt',"w+")
cases = int(f.readline())
print(cases)
for i in range(cases):
    print(i)
    num = int(f.readline())
    count = 0
    x = 1
    solved = False
    digits= []
    while solved == False:
        newnum = num * x
        if(newnum==0):
            a.writelines("Case #{}: INSOMNIA\n".format(i+1))
            solved=True
        digitarr= [int(d) for d in str(newnum)]
        for digit in digitarr:
            if(digit not in digits):
                digits.append(digit)
                count+=1
        if(count==10):
            a.writelines("Case #{}: {}\n".format(i+1,newnum))
            solved=True
        else:
            x+=1
