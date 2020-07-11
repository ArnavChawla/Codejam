def solve():
    A,B = map(int,input().split())
    ans = (A-B)/(A+B)
    return ('%.8f'%ans)
if __name__ == "__main__":
    cases = int(input())+1
    for i in range(1,cases):
        print("Case #{}: {}".format(i,solve()))
