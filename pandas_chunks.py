import pandas as pd
import time
import os


start_time = time.time()

chunk_size = 100000

chunks = pd.read_csv("data1.csv", chunksize=chunk_size)

total_rows = 0

for chunk in chunks:
    total_rows += len(chunk)

end_time = time.time()

print("Total Rows:", total_rows)
print("Time using Pandas chunks:", end_time - start_time, "seconds")

file_size_gb = os.path.getsize("data1.csv") / (1024 ** 3)
print("Storage (original file):", file_size_gb, "GB")