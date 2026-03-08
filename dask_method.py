import dask.dataframe as dd
import time
import os


start_time = time.time()

df = dd.read_csv("data1.csv")

row_count = df.shape[0].compute()

end_time = time.time()

print("Total Rows:", row_count)
print("Time using Dask:", end_time - start_time, "seconds")


file_size_gb = os.path.getsize("data1.csv") / (1024 ** 3)
print("Storage (original file):", file_size_gb, "GB")