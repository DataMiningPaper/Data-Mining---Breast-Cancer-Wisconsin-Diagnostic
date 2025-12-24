import pandas as pd
import matplotlib.pyplot as plt

#loading of the Breastcancer Dataset
df = pd.read_csv("data_bereinigt.csv")  #if needed adjust the path

#features used in the graph
features = [
    "radius_mean",
    "texture_mean",
    "perimeter_mean",
    "area_mean",
    "concavity_mean"
]

#font sizes
plt.rcParams.update({
    "font.size": 20,
    "axes.titlesize": 28,
    "axes.titleweight": "bold",
    "xtick.labelsize": 24,
    "ytick.labelsize": 22,
})

#creating of the figure
fig = plt.figure(figsize=(18, 12))

for i, feature in enumerate(features, 1):
    ax = fig.add_subplot(2, 3, i)

    data = [
        df[df["diagnosis"] == "B"][feature],
        df[df["diagnosis"] == "M"][feature]
    ]

    #violin plot
    vp = ax.violinplot(data, showmeans=True, showmedians=False)
    for body in vp["bodies"]:
        body.set_facecolor("#f2d9a6")  # light beige
        body.set_edgecolor("black")
        body.set_alpha(0.95)

    #box plot overlay
    ax.boxplot(data, widths=0.15)

    #x-axis labes
    ax.set_xticks([1, 2])
    ax.set_xticklabels(["Benign (B)", "Malignant (M)"])

    #removing y-axis lables
    ax.set_ylabel("")

    #title
    ax.set_title(feature.replace("_", " ").title())

    ax.grid(True, alpha=0.3)

fig.tight_layout()


plt.show()
