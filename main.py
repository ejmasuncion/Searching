from bst import BST,TreeNode

import searching as search

# def main():
#     dna_sequence = "taccaccaccatag"
#     k_size = 6

#     print(f"DNA String (n={len(dna_sequence)}): {dna_sequence}")
#     print(f"k-mer size: {k_size}")

#     distribution_table = search.compute_kmer_distribution(dna_sequence, k_size)

#     for kmer, count in distribution_table.items():
#         print(f"  '{kmer}': {count}")

def main():
    # print("hEllo")
    tree = BST()
    tree.create()

    # tree.insert(tree.root, TreeNode(6))
    tree.insert(2)
    # tree.insert(TreeNode(8))
    print(tree.search(1))
    # tree.insert(TreeNode(2))

if __name__ == "__main__":
    main()



