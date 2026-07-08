import pandas as pd


def init_raw_csv(filepath: str):
    """Initialise raw dataset."""
    df = pd.read_csv(
        filepath, encoding="latin-1", skiprows=1
    )

    return df


def clean_gdp_dataset(df):
    """Clean raw data."""
    cols_to_change = {
        "Region/Country/Area": "region_code",
        "Unnamed: 1": "region_name",
    }
    df = df.rename(cols_to_change, axis=1)
    df.columns = [c.lower() for c in df.columns]
    return df


def clean_emission_dataset(df:pd.DataFrame):
    """Clean emission dataset."""



    return df

def get_raw_dataset(filepath, type_of_data):
    """Initialise and clean dataset."""

    df = init_raw_csv(filepath=filepath)


    if type_of_data =="GDP":
        df = clean_gdp_dataset(df)
    elif type_of_data == "Emission":
        df = clean_emission_dataset(df)
    return df
