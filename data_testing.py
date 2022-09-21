import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

breck_data: pd.DataFrame = pd.read_csv("C:\\Users\\swguo\\VSCode Projects\\Climate Research\\Snow Research\\Breckenridge Iowa Dataset.txt", comment="#")
print(breck_data)
test_precip = breck_data["precip"]
print(test_precip)

# Filtering estimated and non estimated
booleans_for_estimated_precip = (breck_data["precip_estimated"] == True)
booleans_for_exact_precip = (breck_data["precip_estimated"] == False) 
booleans_for_estimated_snowfall = ((breck_data["precip_estimated"] == True) & (breck_data["snow"] != "M"))
booleans_for_exact_snowfall = ((breck_data["precip_estimated"] == False) & (breck_data["snow"] != "M"))

estimated_precip_data = breck_data[booleans_for_estimated_precip]
exact_precip_data = breck_data[booleans_for_exact_precip]
estimated_snowfall_data = breck_data[booleans_for_exact_precip]
exact_snowfall_data = breck_data[booleans_for_exact_precip]


# Get different data
exact_precip = exact_precip_data["precip"]
estimated_precip = estimated_precip_data["precip"]

exact_snowfall = exact_snowfall_data["snow"]
estimated_snowfall = estimated_snowfall_data["snow"]


# Plot Precip
plt.plot(estimated_precip, label = "Estimated Melted Precip")
plt.plot(exact_precip, label = "Exact Melted Precip")
plt.title("Melted Precip vs Time")
plt.legend()
plt.show()

plt.plot(estimated_snowfall, label = "Estimated Snowfall")
plt.plot(exact_snowfall, label = "Exact Snowfall")
plt.title("Snowfall vs Time")
plt.ylim(50)
plt.legend()
plt.show()



