nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i', 'k'],
    ['m', 'v']
]


class FlatIterator:

    def __init__(self, _list):
        self.list = _list

    def __iter__(self):
        self.index2 = -1
        self. index1 = 0

        return self

    def __next__(self):
        self.index2 += 1
        self.list2 = self.list[self.index1]
        self.len = len(self.list2) - 1
        if self.index1 == len(self.list)-1 and self.index2 > self.len:
            raise StopIteration
        if self.index2 > self.len:
            self.index2 = 0
            self.index1 += 1
        self.el = self.list[self.index1][self.index2]
        return self.el


for item in FlatIterator(nested_list):
	print(item)

