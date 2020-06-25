def solve():
    hold = input()
    num = int(hold.split(" ")[0])
    day = int(hold.split(" ")[1])
    hold = input()
    trains = []
    for x in hold.split(" "):
        trains.append(int(x))
    trains.reverse()
    temp = 0
    for train in trains:
        if(day % train == 0):
            pass
        else:
            day -=day%train
    return day

if __name__ == "__main__":
    cases = int(input())
    for i in range(1,cases+1):
        print("Case #{}: {}".format(i,solve()))
