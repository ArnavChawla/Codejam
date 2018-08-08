def check(num):
    digitarr=[]
    for i in str(num):
        digitarr.append(int(i))
    prev = digitarr[0]
    start = digitarr
    for i in range(len(digitarr)):
        print(str(digitarr[i]) + " " + str(prev))
        if(digitarr[i] < prev):
            digitarr[i-1] = digitarr[i-1] -1
            x = i
            for x in range(i,len(digitarr)):
                print(x)
                digitarr[x] = 9
        prev = digitarr[i]
    x = ""
    if(digitarr[0] == 0):
        digitarr.pop(0)
    for last in digitarr:
        x += str(last)

    prev = digitarr[0]
    for inte in digitarr:
        if(inte < prev):
            return check(x)
    return x

f = open("B-large-practice.in","r")
cases = f.readline()
o = open ("output_tidy.txt","w+")
for i in range(int(cases)):
    o.write("Case #{}: {}\n".format(i+1,check(str(f.readline()).rstrip())))
