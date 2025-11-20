import searching as search

def main(search_function: str, hash_func_key: str):
    dna_sequence = "taccaccaccatagataccaccaccataggccttaccaccacc"
    k_size = 6

    print(f"DNA String (n={len(dna_sequence)}): {dna_sequence}")
    print(f"k-mer size: {k_size}")

    if search_function == 'HT':
        distribution_table = search.compute_kmer_distribution_ht(dna_sequence, k_size, hash_func_key)
    
        print("Root sequence: ",distribution_table.search("accacc"))
        for kmer, count in distribution_table.items():
            print(f"  '{kmer}': {count}")

        # print(distribution_table)


    else:
        distribution_table = search.compute_kmer_distribution_bst(dna_sequence, k_size)
        distribution_table.inorder_traversal()

if __name__ == "__main__":
    search_function = 'HT' # Options: 'HT' or 'BST'
    hash_func_key='MMH3' # Options: 'MMH3' or 'FNV1A'
    main(search_function, hash_func_key)



