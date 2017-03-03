def fib():
	series = [0,1]
	num = 100 
	i = 0 
	j = 1 
	sum = 0
	while sum <= num:
		sum = i + j
		i = j 
		j = sum
		series.append(sum)

	print series

fib()