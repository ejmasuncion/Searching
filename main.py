import searching as search

def main():
    dna_sequence = "taccaccaccatag"
    k_size = 6


    print(f"DNA String (n={len(dna_sequence)}): {dna_sequence}")
    print(f"k-mer size: {k_size}")

    distribution_table = search.compute_kmer_distribution(dna_sequence, k_size)

    for kmer, count in distribution_table.items():
        print(f"  '{kmer}': {count}")

if __name__ == "__main__":
    main()