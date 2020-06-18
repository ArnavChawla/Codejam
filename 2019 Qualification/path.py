if __name__=="__main__":
    for i in range(1,int(input())+1):
        input()
        otherpath = str(input())
        myAnswer = ""
        for char in otherpath:
            if char == "E":
                myAnswer += "S"
            else:
                myAnswer +="E"
        print("Case #{}: {}".format(i,myAnswer))
