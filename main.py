import random
import time
import sys
import searching as search

DNA_BASES = ['a', 'c', 'g', 't']
def generate_random_dna(length: int) -> str:
    return ''.join(random.choice(DNA_BASES) for _ in range(length))

def run_performance_test_ht(sequence_lengths: list, k_values: list, hash_func_key: str):
    csv_output = "Hash_Algo,Seq_Length_n,K_Size,Execution_Time_sec\n"
    
    print(f"Starting performance test with Hash Algo: {hash_func_key}")
    print("--------------------------------------------------")

    for n in sequence_lengths:
        dna_sequence = generate_random_dna(n)
        
        for k in k_values:
            if k >= n:
                print(f"Skipping n={n}, k={k} (k must be less than n)")
                continue
            
            start_time = time.time()
            
            distribution_table = search.compute_kmer_distribution_ht(dna_sequence, k, hash_func_key)
            
            search_key = dna_sequence[:k]
            search_iterations = 1000 
            
            for _ in range(search_iterations):
                distribution_table.search(search_key)
            
            end_time = time.time()
            
            elapsed_time = end_time - start_time
            
            csv_output += f"{hash_func_key},{n},{k},{elapsed_time:.6f}\n"
            
            print(f"Finished n={n}, k={k}: {elapsed_time:.6f} sec")

    return csv_output

def save_results_to_csv(csv_data: str, file_name: str):
    """Prompts user for a filename and saves the data."""
    # Loop until a valid filename is provided
    while True:
        try:
            # Prompt the user for the desired filename
            filename = file_name
            
            if not filename.strip():
                print("Filename cannot be empty. Please try again.")
                continue

            # Ensure the filename ends with .csv
            if not filename.lower().endswith(".csv"):
                filename += ".csv"

            # Write the data to the file
            with open(filename, 'w') as f:
                f.write(csv_data)
            
            print(f"\n✅ Success! Performance data saved to: {filename}")
            break # Exit the loop upon successful file write
            
        except Exception as e:
            print(f"❌ Error writing file: {e}. Please try a different filename or location.")

def main(search_function: str, hash_func_key: str, sequence_length: int, k_size: int):
    TEST_SEQUENCE_LENGTHS = [1000, 5000, 10000]
    TEST_K_VALUES = [5, 10, 15]
    dna_sequence = generate_random_dna(sequence_length)
    k = k_size
    file_name = 'performance_results.csv'

    print(f"DNA String (n={len(dna_sequence)}): {dna_sequence}")
    print(f"k-mer size: {k}")

    if search_function == 'HT':
        csv_results = run_performance_test_ht(TEST_SEQUENCE_LENGTHS, TEST_K_VALUES, hash_func_key)
        
        # Output the results
        # print("\n" + "=" * 50)
        # print("PERFORMANCE RESULTS (CSV Format)")
        # print("=" * 50)
        # print(csv_results)
        save_results_to_csv(csv_results, file_name)
        # print(distribution_table)

    else:
        distribution_table = search.compute_kmer_distribution_bst(dna_sequence, k)
        distribution_table.inorder_traversal()

if __name__ == "__main__":
    search_function = 'HT' # Options: 'HT' or 'BST'
    hash_func_key='FNV1A' # Options: 'MMH3' or 'FNV1A'
    sequence_length = 100
    k = 5
    main(search_function, hash_func_key, sequence_length, k)



