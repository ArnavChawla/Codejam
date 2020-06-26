def solve(s):
    x = 1
    y = 1
    string = ""
    solution = []
    for w in s:
        if w.isdigit():
            string+=w
        elif w == '(':
            solution.append(string)
            solution.append('(')
            string = ''
        elif w == ')':
            res = ''
            while(solution and solution[-1]!='('):
                res= solution.pop()+res
            solution.pop()
            solution.append(res*int(solution.pop()))
        else:
            solution.append(w)
    solution = ''.join(solution)
    x = 1 + solution.count("S") - solution.count("N")
    if x <= 0:
        x = 1000000000 + x
    elif x > 1000000000:
        x -= 1000000000
    y = 1 + solution.count("E") - solution.count("W")
    if y <= 0:
        y = 1000000000 + y
    elif y > 1000000000:
        y -= 1000000000
    # I switched the coordinates
    return ("{} {}".format(y,x))
if __name__ == "__main__":
    cases = int(input())
    for i in range(1,cases+1):
        print("Case #{}: {}".format(i,solve(input())))
