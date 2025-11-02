from hashmap import HashTable

def compute_kmer_distribution(dna_string: str, k: int) -> HashTable:
    n = len(dna_string)
    kmer_counts = HashTable(capacity=n)

    for i in range(n - k + 1):
        kmer = dna_string[i:i + k]
        current_count = kmer_counts.get(kmer)
        new_count = current_count + 1
        kmer_counts.put(kmer, new_count)   
    return kmer_counts