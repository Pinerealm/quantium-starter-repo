from glob import glob

import numpy as np
import pandas as pd


# Get names of csv files
data_files = glob('data/*.csv')

frames = [pd.read_csv(file) for file in data_files]
df = pd.concat(frames, ignore_index=True)

# Change `price` to floats
df["price"] = df.price.str.replace('$', '').astype('float32')

# Change `quantity` to integers
df["quantity"] = df.quantity.astype('int32')

# Create a mask of only 'Pink Morsel' products
mask_pink_morsel = df["product"] == 'pink morsel'
pink_morsel = df[mask_pink_morsel].reset_index(drop=True)
pink_morsel["sales"] = pink_morsel.price * pink_morsel.quantity


cols = ["sales", "date", "region"]
daily_sales_conv = pink_morsel[cols].copy()
# Save as csv file
daily_sales_conv.to_csv('daily_sales_conv.csv', index=False)


