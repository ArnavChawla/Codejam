def solve():
    hold = int(input())
    string = input().split(" ")
    nums = []
    for x in string:
        nums.append(int(x))
    count = 0
    for i in range(0,hold):
        if i != 0 and i != hold-1:
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    count +=1
    return count
if __name__ == "__main__":
    cases = int(input())
    for i in range(1,cases+1):
        print("Case #{}: {}".format(i,solve()))
