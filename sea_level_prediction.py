import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Observed Data")
    
    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = pd.Series(range(1880, 2051))
    sea_levels_predicted = slope * years_extended + intercept
    ax.plot(years_extended, sea_levels_predicted, 'r', label="Best Fit Line (1880-2050)")
    
    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent_predicted = slope_recent * years_recent + intercept_recent
    ax.plot(years_recent, sea_levels_recent_predicted, 'g', label="Best Fit Line (2000-2050)")
    
    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    
    fig.savefig('sea_level_plot.png')
    plt.show()
    return fig

draw_plot()
