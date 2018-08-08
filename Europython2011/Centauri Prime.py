f = open("A-small-practice-2.in")
o = open ("output2.txt","w+")
cases = f.readline()
the_vowel = ["a","e","i","o","u"]
for i in range(int(cases)):
    name = str(f.readline()).rstrip()
    print(name[-1].lower() == "y")
    if(name[-1].lower() == "y"):
        o.write("Case #{}: {} is ruled by nobody.\n".format(i+1,name))
    elif(name[-1].lower() not in the_vowel):
        print("Y")
        o.write("Case #{}: {} is ruled by a king.\n".format(i+1,name))
    else:
        #print("v")
        o.write("Case #{}: {} is ruled by a queen.\n".format(i+1,name))
o.close()
