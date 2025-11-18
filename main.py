import searching as search

def main(search_function: str):
    dna_sequence = "taccaccaccatag"
    k_size = 6

    print(f"DNA String (n={len(dna_sequence)}): {dna_sequence}")
    print(f"k-mer size: {k_size}")

    if search_function == 'HT':
        distribution_table = search.compute_kmer_distribution_ht(dna_sequence, k_size)
    
        print("Root sequence: ",distribution_table.search("accacc"))
        for kmer, count in distribution_table.items():
            print(f"  '{kmer}': {count}")


    else:
        distribution_table = search.compute_kmer_distribution_bst(dna_sequence, k_size)
        distribution_table.inorder_traversal()

if __name__ == "__main__":
    search_function = 'BST'
    main(search_function)



