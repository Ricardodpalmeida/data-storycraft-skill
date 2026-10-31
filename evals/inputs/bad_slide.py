# Generates the "Market Overview" slide image (bad_slide.png)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa

suppliers = ["Supplier A", "Supplier B", "Supplier C", "Supplier D", "Us"]
share = [24, 31, 14, 11, 20]
quarters = ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25"]
revenue_m = [4.1, 4.3, 4.2, 4.6, 4.4, 4.5, 4.3, 4.2]
sales_reps = [38, 40, 41, 44, 47, 50, 52, 55]

fig = plt.figure(figsize=(14, 6))
fig.suptitle("Market Overview 2025", fontsize=22, fontweight="bold", ha="center")

ax1 = fig.add_subplot(1, 2, 1)
ax1.pie(share, labels=suppliers, autopct="%1.1f%%", startangle=140, shadow=True,
        explode=[0, 0.1, 0, 0, 0.05], colors=["red", "orange", "yellow", "green", "purple"])
ax1.set_title("Market Share by Supplier", loc="center")

ax2 = fig.add_subplot(1, 2, 2)
ax2.bar(quarters, revenue_m, color=["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33", "#a65628", "#f781bf"])
ax2.set_ylabel("Revenue ($M)")
ax2.set_ylim(4.0, 4.7)
ax2.grid(True, linestyle="--")
ax2.tick_params(axis="x", rotation=45)
ax3 = ax2.twinx()
ax3.plot(quarters, sales_reps, color="green", marker="o", linewidth=3)
ax3.set_ylabel("# Sales Reps")
ax2.set_title("Revenue vs Sales Reps", loc="center")
ax2.legend(["Revenue"], loc="upper left"); ax3.legend(["Sales reps"], loc="upper right")

plt.tight_layout()
plt.savefig("bad_slide.png", dpi=120)
