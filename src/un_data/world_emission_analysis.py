# %% [markdown]
"""
# Emission analysis

The UN publishes a lot of data for around the world.
"""

# %%
import pandas as pd
import matplotlib.pyplot as plt

from src.un_data.config import emissions_filepath
from src.un_data.read_data import get_raw_dataset

# %%
df = get_raw_dataset(filepath=emissions_filepath, type_of_data="Emission")
df.head(3)

# %% [markdown]
"""
## Look into GDP data
This is where

"""
# %%
