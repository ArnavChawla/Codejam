def solve():
    num = int(input())
    words = []
    for i in range(0,num):
        words.append(input())
    words = sorted(words)
    large = 0
    answer = ""
    for word in words:
        temp = word.lower()
        temp = temp.replace(" ","")
        count = len(set(list(temp)))
        if count > large:
            large = count
            answer = word
    return answer
if __name__ == "__main__":
    cases = int(input())+1
    for i in range(1,cases):
        print("Case #{}: {}".format(i,solve()))
