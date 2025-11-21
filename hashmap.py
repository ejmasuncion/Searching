import mmh3

class HashTable:
    def __init__(self, capacity: int, hash_function):
        self.capacity = capacity
        self.hash_function = hash_function
        self.table = []
        for i in range(capacity):
            self.table.append([])
        
        self.collision_count = 0

    def __repr__(self) -> str:
        output = f"<{self.__class__.__name__} Capacity={self.capacity} Algorithm={self.hash_function}>\n"
        output += "--- Hash Table Array Structure (Index : Chain) ---\n"
        
        for i, chain in enumerate(self.table):
            chain_str = ", ".join([f"('{k}': {v})" for k, v in chain])
            
            output += f"[{i:02d}]: [{chain_str}]\n"
            
        return output
    
    def _hash_function(self, key: str) -> int:
        if self.hash_function == 'MMH3':
            # MMH3
            data_bytes = key.encode('utf-8')
            hash_value = mmh3.hash(data_bytes, seed=0)
            hash_value = hash_value & 0xFFFFFFFF
            
        elif self.hash_function == 'FNV1A':
            # FNV1a_32
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
        
        return hash_value % self.capacity
    
    def _collision(self, chain: list, key: str, value: int) -> bool:
        ## seperate chaining collision resolution

        for i, (k, v) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return True
        
        return False
    
    def insert(self, key: str, value: int):
        index = self._hash_function(key)
        chain = self.table[index]
        
        # print(f"Inserting key: '{key}' with value: {value} at index: {index}")
        was_updated = self._collision(chain, key, value)

        if not was_updated:
            self.collision_count += 1
            # print("Collision! inserting new key-value pair into hash table.")
            chain.append((key, value))
        
    def search(self, key: str):
        index = self._hash_function(key)
        chain = self.table[index]
        
        for k, v in chain:
            if k == key:
                return v
        
        return 0
    
    def items(self):
        # To generate all key-value pairs in the hash table
        for chain in self.table:
            for key, value in chain:
                yield key, value