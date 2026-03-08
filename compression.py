import gzip
import shutil
import time
import os
import pandas as pd


start_time = time.time()

input_file = "data1.csv"
output_file = "data1.csv.gz"

with open(input_file, 'rb') as f_in:
    with gzip.open(output_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

end_time = time.time()

print("Compression time:", end_time - start_time, "seconds")

compressed_size = os.path.getsize("data1.csv.gz") / (1024 ** 3)

print("Compressed size (GB):", compressed_size)


