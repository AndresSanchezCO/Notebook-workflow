import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



def covid_time_series(df):
    print("Hellooooooooooo World!")
    sns.lineplot(
        data=df,
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series");


def get_top_countries(processed_covid_df, countries, num_rows=5):
    top_countries_df = (
        processed_covid_df
        .select_columns(["country_region", "value"])
        .groupby(["country_region"])
        .aggregate("sum")
        .sort_values("value", ascending=False)
        .reset_index()
        .head(num_rows)
        .transform_column(
            column_name="country_region",
            function=lambda x: "red" if x in countries else "lightblue",
            dest_column_name="color"
        )
    )
    return top_countries_df


