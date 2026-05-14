import pandas as pd

from config import filepath

def init_raw(filepath: str):
    """Initialise raw dataset."""
    df = pd.read_csv(
        filepath, encoding="latin-1", skiprows=1
    )
    return df


def clean_dataset(df):
    """Clean raw data."""
    cols_to_change = {
        "Region/Country/Area": "region_code",
        "Unnamed: 1": "region_name",
    }
    df = df.rename(cols_to_change, axis=1)
    df.columns = [c.lower() for c in df.columns]
    return df


def get_raw_dataset(filepath):
    """Initialise and clean dataset."""

    df = init_raw(filepath=filepath)

    df = clean_dataset(df)

    return df


if __name__=="__main__":
    get_raw_dataset(filepath=filepath)