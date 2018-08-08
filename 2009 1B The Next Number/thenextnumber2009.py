def calculate(number):
    #first step is to get the digits in the number
    #use a while loop to increment
    #check and return
    digits = []
    # for digit in str(number):
    #     if(int(digit) != 0):
    #         digits.append(int(digit))
    #digits.sort()
    new = digits
    #print("num "+ str(digits))
    i = number +1
    deal = False
    while deal == False:
        for digit in str(number):
            if(int(digit) != 0):
                digits.append(int(digit))
        #print(digits)
        newdigits=[]
        for a in str(i):
            newdigits.append(int(a))
        #print(newdigits)
        remove = False
        for x in range(0,len(digits)):
            #print(x)
            if(remove == True):
                x-=2
            while(x > len(digits)-1):
                 x-=1
            while(x < 0):
                x+=1
            #print(newdigits)
            #print("index: "+ str(x))
            digit = digits[x]
            #print("digit: " + str(digit))
            if(int(digit) in newdigits):
                #print("here")
                digits.remove(digit)
                newdigits.remove(digit)
                remove = True
            else:
                remove = False
        nums = 0
        if(len(newdigits) > 0 and len(digits) ==0):
            for digit in newdigits:
                if int(digit) == 0:
                    nums +=1
        if(len(newdigits) == 0 or (nums==len(newdigits))):
            return i
        else:
            digits = []
            i+=1
        #deal = True

a = open("B-small-practice(2009).in","r")
cases = int(a.readline())
#print(cases)
for i in range(1,cases+1):
    print("Case #{}: {}".format(i,calculate(int(a.readline().rstrip()))))
