import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from transform_data import create_dfs_for_gdp_visual

COLORS = [
    "#FF0000",
    "#00FF00",
    "#800080",
    "#800000",
    "#008000",
    "#0000FF",
    "#FF00FF",
    "#00FFFF",
    "#FF4500",
    "#4B0082",
    "#008080",
]
SERIES_CHOICES = [
    "GDP in current prices (millions of US dollars)",  # 0
    "GDP per capita (US dollars)",  # 1
    "GDP in constant 2015 prices (millions of US dollars)",  # 2
    "GDP real rates of growth (percent)",  # 3
]


def visualise_gdp_per_capita(
    df: pd.DataFrame, country_names: list[str], series_choice: str
) -> None:
    """Collect and visualise per capita GDP of given countries."""
    sns.set()

    for region in country_names:
        if region not in df["region_name"].unique():
            country_names.remove(region)
            warn_message = (
                f"{region} not in the Data Frame. Please check REGION_NAMES and the CHECK_NAME. "
                "This region will be removed from the run."
            )
            raise Warning(warn_message)

    # Filter to correct data - getting a df for each country
    dfs = create_dfs_for_gdp_visual(
        df=df, region_names=country_names, series_choice=series_choice
    )

    # Create the plot
    fig, ax = plt.subplots()

    ax.set_xlabel("Year")
    ax.set_ylabel("GDP")

    for region_name, df_region in dfs.items():
        ax.plot(
            df_region["year"],
            df_region["value"],
            label=region_name,
        )

    ax.legend()
    fig.suptitle(f"{series_choice} for some regions in the world.")


def visualise_comparison_gdp(
    df: pd.DataFrame, region_names: list[str], year: int = 2010
) -> None:
    """Create a graph that compares some regions."""
    sns.set()

    # filter to correct year and regions
    df = df.loc[(df["year"] == year) & (df["region_name"].isin(region_names))]

    # Create the plot
    fig, axs = plt.subplots(2, 2, figsize=(9, 12))

    for ax, series in zip(axs.flatten(), SERIES_CHOICES):
        # filter to series
        df_series = df.loc[df["series"] == series]

        # create subplot
        ax.bar(
            df_series["region_name"],
            df_series["value"],
            color=COLORS[: len(region_names)],
        )
        ax.tick_params(axis="x", labelrotation=45)
        ax.set_xlabel("Year")
        ax.set_ylabel("GDP")
        ax.set_title(f"{series}")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.suptitle(f"Comparing regions for the year {year}")
