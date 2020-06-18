def compute(case):
    full = input()
    num1 = "".join("2" if cint == "4" else cint for cint in full)
    num2 = "".join("2" if cint == "4" else "0" for cint in full)
    print("Case #{}: {} {}".format(case,num1,num2))
if __name__ == "__main__":
    cases = int(input())
    for i in range(1,cases+1):
        compute(i)
