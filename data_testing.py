import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb
import netCDF4 as nc


def max_of_years(data: pd.DataFrame, column_name):
    """Data's index is indices, has years, and starts on January 1"""
    first_index = 0
    last_index = 0
    if (data["year"].iloc(first_index) % 4 == 0):
        pass

breck_data: pd.DataFrame = pd.read_csv("C:\\Users\\swguo\\VSCode Projects\\Climate Research\\Snow Research\\Breckenridge Iowa Dataset.txt", comment="#")
breck_data.set_index("day", drop=False, inplace=True)
leadville_data: pd.DataFrame = pd.read_csv("C:\\Users\\swguo\\VSCode Projects\\Climate Research\\Snow Research\\Leadville 2SW Iowa Dataset.txt", comment="#")
leadville_data.set_index("day", drop=False, inplace=True)

# Get breck_data index in years
breck_data['year'] = breck_data['day'].str.slice(0, 4)
breck_data['year'] = breck_data['year'].astype('int32')
breck_data.set_index('year', drop=True, inplace=True)
print(breck_data)

# Get data
# precip "cut" from 8/26/1913, snow "cut" from 8/31/1913
# Data "good" from 7/1/1947
# Start from 1948
exact_precip_data = breck_data[(breck_data["precip_estimated"] == False) ]
exact_precip = exact_precip_data["precip"]


breck_data["snow"] = breck_data["snow"].replace("M", np.nan)
exact_snow = breck_data["snow"]


# Plot Precip (FIGURE OUT HOW TO PLOT WITH DATE)
plt.plot(exact_precip, label = "Exact Melted Precip")
plt.title("Exact Melted Precip vs Time")
plt.legend()
plt.show()

plt.plot(exact_snow, label = "Filtered Snowfall")
plt.title("Snowfall vs Time")
plt.legend()
plt.show()
