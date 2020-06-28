from fractions import gcd
def solve():
    input()
    arr = list(map(int,input.split()))

    hold = []
    for i in range(0,len(arr)-1):
        if arr[i] != arr[i+1]:
            if len(hold) <= 26:
                factor = gcd(arr[i],arr[i+1])
                hold.append(factor)
                hold.append(arr[i]/factor)
                hold.append(arr[i+1]/factor)
            else:
                break
    sort = sorted(list(set(hold)))
    check = []
    for j in range(0,len(sort)):
        check[j] = char(ord('A')+j)

    
if __name__ == "__main__":
    cases = int(input())+1
    for i in range(1,cases):
        print("Case {}: {}".format(i,solve()))
