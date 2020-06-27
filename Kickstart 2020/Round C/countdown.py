def solve():
    length, total = map(int,input().split())
    numbers = list(map(int,input().split()))
    count = 0
    counter = 1
    for i in range(1,len(numbers)):

        if numbers[i] == numbers[i-1]-1 and numbers[i] <= total:
            counter += 1
        if counter == total:
            count +=1
            counter = 1
        if numbers[i] != numbers[i-1]-1 or numbers[i] > total:
            counter = 1
    return count

if __name__ == "__main__":
    cases = int(input())
    for i in range(1,cases+1):
        print("Case #{}: {}".format(i,solve()))
