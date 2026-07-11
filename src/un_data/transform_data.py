import math
import pandas as pd


def round_up(n, decimals=0):
    multiplier = 10**decimals
    return math.ceil(n * multiplier) / multiplier


def find_max_value(dfs: dict[str, pd.DataFrame]) -> int:
    """Find maximum value for a group of dataframes."""

    value_maximums = [df["value"].max() for df in dfs.values()]
    max_value = max(value_maximums)
    return round_up(max_value, decimals=-(abs(len(str(max_value))) - 1))


def filter_region_and_series(
    df: pd.DataFrame, region: str, series: str
) -> pd.DataFrame:
    """Filter df with region and series."""

    df = df.loc[
        (df["region_name"] == region)  # filter region name
        & (df["series"] == series)  # filter series column
    ]
    return df[["year", "value"]]


def create_dfs_for_gdp_visual(
    df: pd.DataFrame,
    region_names: list[str],
    series_choice: str,
) -> dict[str, pd.DataFrame]:
    """Transform df to specific region dfs."""

    # Filter to correct data - getting a df for each country
    dfs = {
        region: filter_region_and_series(df, region=region, series=series_choice)[
            ["year", "value"]
        ]
        for region in region_names
    }

    return dfs
