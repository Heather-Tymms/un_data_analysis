import pandas as pd
import matplotlib.pyplot as plt


def visualise_gdp_per_capita(df: pd.DataFrame, country_names: list[str]):
    """Collect and visualise per capita GDP of a given country."""

    # Filter to correct data
    dfs = {}
    for country in country_names:
        df_country = df.loc[df["region_name"]==country]
        df_country_per_capita = df_country.loc[
            df_country["series"]=="GDP per capita (US dollars)"
        ]
        dfs[country] = df_country_per_capita

    # Create the plot
    fig, ax = plt.subplots()

    ax.set_xlabel("Year")
    ax.set_ylabel("GDP")

    for country_name, country_df in dfs.items():
        ax.plot(
            country_df["year"],
            country_df["value"],
            label=country_name,
        )

    ax.legend()
    fig.suptitle("GDP per capita of various countries")
