import mmh3

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = []
        for i in range(capacity):
            self.table.append([])
    
    def _hash_function_1(self, key: str, seed: int = 0) -> int:
        ## uses murmurhash3_32
        data_bytes = key.encode('utf-8')
        hash_value = mmh3.hash(data_bytes, seed)
        hash_value = hash_value & 0xFFFFFFFF
        return hash_value % self.capacity
    
    def _hash_function_2(self, key: str) -> int:
        ## uses fnv1a32
        FNV_OFFSET_BASIS = 2166136261
        FNV_PRIME = 16777619  

        hash_value = FNV_OFFSET_BASIS

        data_bytes = key.encode('utf-8')

        for byte in data_bytes:
            hash_value = hash_value ^ byte
            hash_value = hash_value * FNV_PRIME
            hash_value &= 0xFFFFFFFF
        
        return hash_value % self.capacity
    
    def put(self, key: str, value: int):
        index = self._hash_function_1(key)
        chain = self.table[index]
        
        ## for collitions
        for i, (k, v) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return
        
        chain.append((key, value))
        
    def get(self, key: str) -> int:
        index = self._hash_function_1(key)
        chain = self.table[index]
        
        for k, v in chain:
            if k == key:
                return v
        
        return 0
    
    def items(self):
        for chain in self.table:
            for key, value in chain:
                yield key, value