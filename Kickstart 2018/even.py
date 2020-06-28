def solve():
    odd = [x if x % 2 != 0 else 1 for x in range(0,11)]
    odd = list(set(odd))
    num = int(input())
    count = 0
    small = num
    large = num
    while True:
        if any(str(digit) in str(small) for digit in odd) and any(str(digit) in str(large) for digit in odd):
            count += 1
            small -= 1
            large +=1
        else:
            return count


if __name__ == "__main__":
    cases = int(input())+1
    for i in range(1,cases):
        print("Case #{}: {}".format(i,solve()))
