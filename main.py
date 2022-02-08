import random


def test_lottery_generator(iterations_limit):
	trueCounter = 0
	flaseCounter = 0

	for i in range(0, iterations_limit):
		x = lottery_generator(10)
		if x:
			trueCounter += 1
		else:
			flaseCounter += 1

	print("True count: {} False count: {}".format(trueCounter/iterations_limit, flaseCounter/iterations_limit))



def lottery_generator(rangeEnd) -> bool:
	rangeStart = 1
	x = random.randint(rangeStart, rangeEnd)
	if rangeStart == x:
		return True
	else:
		return False


def check_uniform_distribution(rangeStart, rangeEnd, iterations_limit):
	int_buckets_array = [0 for x in range(rangeStart, rangeEnd + 1)]

	#print('created buckets')
	#print(int_buckets_array)

	num_of_iterations = iterations_limit;
	print('checking Uniform Distribution')
	print('iterations limit: {}'.format(iterations_limit));

	for i in range(0, num_of_iterations) :
		x = random.randint(rangeStart, rangeEnd)
		#print(x)
		int_buckets_array[x - 1] += 1
	
	print('finished generation. Dumping Result')

	sum = 0
	for i in range(rangeStart, rangeEnd + 1) : 
		print("{} : {}".format(i, int_buckets_array[i]/(iterations_limit/10)))
		sum += int_buckets_array[i]

	print('checksum: {}'.format(sum))

iterations_limit = 10000;

# rangeStart = 0
# rangeEnd = 9
# check_uniform_distribution(rangeStart, rangeEnd, iterations_limit)

test_lottery_generator(iterations_limit)




