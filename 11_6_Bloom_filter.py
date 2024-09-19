from bitarray import bitarray

class BloomFilter(object):

    def __init__(self, size, number_expected_elements=100000):
        self.size = size
        self.number_expected_elements = number_expected_elements
        self.bloom_filter = bitarray(self.size)
        self.bloom_filter.setall(0)
        self.number_hash_functions = round(self.size/self.number_expected_elements)

    def _hash_djb2(self, s):
        hash = 5381
        for x in s:
            hash = ((hash << 5) + hash) + ord(x)
        return hash % self.size

    def _hash(self, item, K):
        return self._hash_djb2(str(K) + item)

    def add_to_filter(self, item):
        for i in range(self.number_hash_functions):
            self.bloom_filter[self._hash(item, i)] = 1

    def check_is_not_in_filter(self, item):
        for i in range(self.number_hash_functions):
            if self.bloom_filter[self._hash(item, i)] == 0:
                return True
        return False

bloom_filter = BloomFilter(1000000, 100000)
base_ip = "192.168.1."
bloom_filter.add_to_filter(base_ip + str(1))
bloom_filter.add_to_filter(base_ip + str(98))
bloom_filter.add_to_filter(base_ip + str(101))

for i in range(1, 100000):
    if not bloom_filter.check_is_not_in_filter(base_ip + str(i)):
        print(base_ip + str(i))

print(bloom_filter.number_hash_functions)