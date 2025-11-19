import mmh3

class HashTable:
    def __init__(self, capacity: int, hash_function):
        self.capacity = capacity
        self.hash_function = hash_function
        self.table = []
        for i in range(capacity):
            self.table.append([])
    
    def _hash_function(self, key: str) -> int:
        """
        Calculates the array index by delegating to the selected hashing algorithm.
        """
        if self.hash_function == 'MMH3':
            # MurmurHash3_32 (Algorithm 1)
            data_bytes = key.encode('utf-8')
            hash_value = mmh3.hash(data_bytes, seed=0)
            hash_value = hash_value & 0xFFFFFFFF
            
        elif self.hash_function == 'FNV1A':
            # FNV1a_32 (Algorithm 2)
            FNV_OFFSET_BASIS = 2166136261
            FNV_PRIME = 16777619  

            hash_value = FNV_OFFSET_BASIS
            data_bytes = key.encode('utf-8')

            for byte in data_bytes:
                hash_value = hash_value ^ byte
                hash_value = hash_value * FNV_PRIME
                hash_value &= 0xFFFFFFFF
        
        else:
            raise ValueError(f"Unknown hash algorithm: {self.hash_function}")

        # The final modulo operation is performed once for both algorithms
        return hash_value % self.capacity
    
    def _collision(self, chain: list, key: str, value: int) -> bool:
        for i, (k, v) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return True
        return False
    
    def insert(self, key: str, value: int):
        # Calls the unified hash function
        index = self._hash_function(key)
        chain = self.table[index]
        
        was_updated = self._collision(chain, key, value)

        if not was_updated:
            chain.append((key, value))
        
    def search(self, key: str):
        # Calls the unified hash function
        index = self._hash_function(key)
        chain = self.table[index]
        
        for k, v in chain:
            if k == key:
                return v
        
        return 0
    
    def items(self):
        for chain in self.table:
            for key, value in chain:
                yield key, value