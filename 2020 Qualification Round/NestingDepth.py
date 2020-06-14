def compute(z):
	digits = [int(i) for i in str(input())]
	solution = []
	for i in digits:
		if (solution.count('(')-solution.count(')'))<= i:
			while (solution.count('(') - solution.count(')')) < i:
				solution.append('(')
			solution.append(i)
		elif (solution.count('(')-solution.count(')'))> i:
			while (solution.count('(')-solution.count(')'))!= i:
				solution.append(')')
			solution.append(i)
		while (solution.count('(') != solution.count(')')):
			solution.append(')')
	final = str(''.join(str(x) for x in solution))
	final = str(final).replace(")(","")
	print("Case #{}: {}".format(z+1,final))
if __name__ == "__main__":
	cases = int(input())
	for z in range(0,cases):
		compute(z)
