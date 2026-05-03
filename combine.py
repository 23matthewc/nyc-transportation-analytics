import pandas as pd

files = [
    '/Users/matthewchen/Downloads/JC-202301-citibike-tripdata.csv',
    '/Users/matthewchen/Downloads/JC-202302-citibike-tripdata.csv',
    '/Users/matthewchen/Downloads/JC-202303-citibike-tripdata.csv',
    '/Users/matthewchen/Downloads/JC-202304-citibike-tripdata.csv',
    '/Users/matthewchen/Downloads/JC-202305-citibike-tripdata.csv',
    '/Users/matthewchen/Downloads/JC-202306-citibike-tripdata.csv'
]

print("Reading and joining files...")

# 1. Read each file
df_list = [pd.read_csv(f) for f in files]

# 2. Concatenate them
combined_df = pd.concat(df_list, ignore_index=True)

# 3. SAFETY CHECK: Remove any rows that are accidental duplicates of the header
# (This filters out any row where the 'ride_id' is literally the word 'ride_id')
combined_df = combined_df[combined_df['ride_id'] != 'ride_id']

# 4. Save the result
combined_df.to_csv('real_citibike.csv', index=False)

print(f"Successfully joined {len(files)} files into 'citibike.csv'.")
print(f"Final row count: {len(combined_df)}")