
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'h']
]
def flat_generator(nested_list):
	for i in nested_list:
		for y in i:
			yield y
	
for item in  flat_generator(nested_list):
	print(item)