if __name__ == "__main__":
    cases = int(input())
    for i in range(0,cases):
        budget = int(input().split(" ")[1])
        prices = input().split(" ")
        prices = [int(x) for x in prices]
        prices.sort()
        cost = 0
        count = 0
        for price in prices:
            if cost + price <= budget:
                cost += price
                count += 1
        print("Case #{}: {}".format(i+1,count))
