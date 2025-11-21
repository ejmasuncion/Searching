import random
import time
import sys
import searching as search

DNA_BASES = ['a', 'c', 'g', 't']
def generate_random_dna(length: int) -> str:
    return ''.join(random.choice(DNA_BASES) for _ in range(length))

def run_performance_test_bst(sequence_lengths: list, k_values: list):
    csv_output = "Search_Algo,Seq_Length_n,K_Size,Collision_Count,Execution_Time_sec\n"
    
    print(f"Starting performance test with BST Search: ")
    print("--------------------------------------------------")

    search_iterations = 1000

    for n in sequence_lengths:
        dna_sequence = generate_random_dna(n)
        
        for k in k_values:
            if k >= n:
                print(f"Skipping n={n}, k={k} (k must be less than n)")
                continue
            
            start_time_insert = time.time()
            
            distribution_table = search.compute_kmer_distribution_bst(dna_sequence, k)

            end_time_insert = time.time()
            time_insert = end_time_insert - start_time_insert

            start_time_search = time.time()
            
            max_start_index = n - k
            
            for _ in range(search_iterations):
                random_start = random.randint(0, max_start_index)
                search_key = dna_sequence[random_start : random_start + k]
                distribution_table.search(search_key)
            
            end_time_search = time.time()
            
            time_search = end_time_search - start_time_search

            collision_count = " "
            
            csv_output += f"'BST Search',{n},{k},{collision_count},{time_insert:.6f}, {time_search:.6f}\n"
            
            print(f"Finished n={n}, k={k}")

    return csv_output

def run_performance_test_ht(sequence_lengths: list, k_values: list, hash_func_key: str):
    csv_output = "Hash_Algo,Seq_Length_n,K_Size,Collision_Count,Insert_Table_Time_sec,Search_Time_sec\n"
    
    print(f"Starting performance test with Hash Algo: {hash_func_key}")
    print("--------------------------------------------------")

    search_iterations = 1000

    for n in sequence_lengths:
        dna_sequence = generate_random_dna(n)

        for k in k_values:
            if k >= n:
                print(f"Skipping n={n}, k={k} (k must be less than n)")
                continue
            
            start_time_insert = time.time()
            
            distribution_table = search.compute_kmer_distribution_ht(dna_sequence, k, hash_func_key)

            end_time_insert = time.time()
            time_insert = end_time_insert - start_time_insert

            start_time_search = time.time()
            
            max_start_index = n - k
            
            for _ in range(search_iterations):
                random_start = random.randint(0, max_start_index)
                search_key = dna_sequence[random_start : random_start + k]
                distribution_table.search(search_key)
            
            end_time_search = time.time()
            
            time_search = end_time_search - start_time_search

            collision_count = distribution_table.collision_count
            
            csv_output += f"{hash_func_key},{n},{k},{collision_count},{time_insert:.6f}, {time_search:.6f}\n"
            
            print(f"Finished n={n}, k={k}")

    return csv_output

def save_results_to_csv(csv_data: str, file_name: str):
    while True:
        try:
            filename = file_name

            with open(filename, 'w') as f:
                f.write(csv_data)
            
            print(f"\nSuccess! Performance data saved to: {filename}")
            break
            
        except Exception as e:
            print(f"Error writing file.")

def main(search_function: str, hash_func_key: str, file_name: str):
    TEST_SEQUENCE_LENGTHS = [10000, 100000, 1000000]
    TEST_K_VALUES = [5, 6, 7]

    print(f"DNA String (n={len(TEST_K_VALUES)}): {TEST_K_VALUES}")
    print(f"k-mer size: {TEST_K_VALUES}")

    if search_function == 'HT':
        csv_results = run_performance_test_ht(TEST_SEQUENCE_LENGTHS, TEST_K_VALUES, hash_func_key)
        
        save_results_to_csv(csv_results, file_name)

    elif search_function == 'BST':
        csv_results = run_performance_test_bst(TEST_SEQUENCE_LENGTHS, TEST_K_VALUES)
        
        save_results_to_csv(csv_results, file_name)
    else:
        print(f"Unknown search function: {search_function}. Please choose 'HT' or 'BST'.")

if __name__ == "__main__":
    search_function = 'BST' # Options: 'HT' or 'BST'
    hash_func_key='N/A' # Options: 'MMH3' or 'FNV1A or N/A for BST'
    file_name = "performance_results_bst.csv"
    main(search_function, hash_func_key, file_name)



