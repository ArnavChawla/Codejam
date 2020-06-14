class task():
    def __init__(self,start,end,place):
        self.start = int(start)
        self.end = int(end)
        self.place = int(place)
    def __lt__(self,other):
         return self.start < other.start
def compute(z):
    size = int(input())
    tasks = []
    current = ""
    for i in range(0, size):
        new = input().split(" ")
        tasks.append(task(new[0],new[1],i))
    place = [None]*size
    tasks.sort()
    c = [task(0,0,0)]
    j = [task(0,0,0)]
    for item in tasks:
        if current == "":
            c.append(item)
            place[item.place] = "C"
            current = "C"
        elif c[-1].end <= item.start:
            c.append(item)
            place[item.place] = "C"
        elif j[-1].end <= item.start:
            j.append(item)
            place[item.place] = "J"
        else:
            return("Case #{}: IMPOSSIBLE".format(z+1))
    answer = "".join(str(x) for x in place)
    return("Case #{}: {}".format(z+1, answer))



if __name__ == "__main__":
    cases = int(input())
    for z in range(0,cases):
        print(compute(z))
