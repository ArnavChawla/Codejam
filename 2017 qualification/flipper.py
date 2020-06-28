def solve():
    hold = input()
    cakes = list(hold.split(" ")[0])
    answer = 0
    num = int(hold.split(" ")[1])
    for i in range(len(cakes)+1-num):
        if cakes[i] != "+":
            for j in range(i,i+num):
                if cakes[j] == '-':
                    cakes[j] = '+'
                else:
                    cakes[j] = '-'
            answer +=1
    if '-' not in cakes:
        return answer
    return "IMPOSSIBLE"

if __name__ == "__main__":
    cases = int(input())
    for i in range(0,cases):
        print("Case #{}: {}".format(i+1,solve()))
