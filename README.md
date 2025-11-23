# Searching
## MCO2 of DSALG @ De La Salle University

Before running, run the following commands:
```bash
python -m venv venv
pip install -r requirements.txt
```

To run,
```bash
./main.py
```
To change parameters,
```bash
Inside if __name__ == "__main__":
Update search_function to change whether to run 'BST' or 'HT'
Update hash_func_key to change wheter to run 'FNV1A' or 'MMH3' (Use 'N/A' for BST)
Update file_name to change the csv filename it will output (ex. 'test.csv')
```

# Authors
Enrico Jose Asuncion
Kaizen Edwin Rodriguez
