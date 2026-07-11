from pathlib import Path, PosixPath
from typing import Literal

import pandas as pd


def generate_input_filepath(
    input_folder_structure: str, input_filename: str
) -> PosixPath:
    """Generate input filepath with filename."""
    input_folder = Path.cwd().parent.parent / Path(input_folder_structure)

    return input_folder / input_filename


def init_raw_csv(input_folder_structure: str, input_filename: str):
    """Initialise raw dataset."""

    # get input filepath
    filepath = generate_input_filepath(
        input_folder_structure=input_folder_structure, input_filename=input_filename
    )

    # read csv with filename associated with variable
    df = pd.read_csv(filepath, encoding="latin-1", skiprows=1)

    return df


def clean_gdp_dataset(df) -> pd.DataFrame:
    """Clean raw data associated with gdp."""
    cols_to_change = {
        "Region/Country/Area": "region_code",
        "Unnamed: 1": "region_name",
    }

    # clean columns names
    df = df.rename(cols_to_change, axis=1)
    df.columns = [c.lower() for c in df.columns]

    # clean value
    df["value"] = df["value"].str.replace({",": ""})
    df["value"] = df["value"].astype(float)

    # clean year
    df["year"] = df["year"].astype(int)

    return df


def clean_emission_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Clean emission dataset."""
    # TODO: Find what columns need to be cleaned for emissions dataset

    return df


def get_raw_dataset(
    input_folder_structure: str,
    input_filename: str,
    type_of_data: Literal["gdp", "emissions"],
) -> pd.DataFrame:
    """Initialise and clean dataset."""

    df = init_raw_csv(
        input_folder_structure=input_folder_structure, input_filename=input_filename
    )

    # clean df with correct columns
    if type_of_data == "gdp":
        df = clean_gdp_dataset(df)
    elif type_of_data == "Emission":
        df = clean_emission_dataset(df)

    return df
