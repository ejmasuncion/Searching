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
    
    def _collision(self, chain: list, key: str, value: int) -> bool:
        for i, (k, v) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return True
        return False
    
    def insert(self, key: str, value: int):
        index = self._hash_function_1(key)
        chain = self.table[index]
        
        was_updated = self._collision(chain, key, value)

        if not was_updated:
            chain.append((key, value))
        
    def search(self, key: str):
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