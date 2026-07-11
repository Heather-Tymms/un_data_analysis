import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from transform_data import create_dfs_for_gdp_visual


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
