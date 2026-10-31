"""Render the README benchmark chart (light and dark) from a small JSON file."""
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

FONTS, DATA, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
OUT.mkdir(parents=True, exist_ok=True)
for ttf in FONTS.glob("LibreFranklin-*.ttf"):
    font_manager.fontManager.addfont(str(ttf))

d = json.loads(DATA.read_text())
rows = d["rows"]  # [{"label":..., "control":[pass,total], "skill":[pass,total]}]

THEMES = {
    "light": dict(bg="white", ink="#18191B", sub="#4B4F55", faint="#8A8F96", line="#D3D5D8", accent="#1F5AA6"),
    "dark": dict(bg="#0D1117", ink="#F0F2F4", sub="#B8BEC6", faint="#7D848D", line="#3A3F46", accent="#6FA3EE"),
}

for name, t in THEMES.items():
    plt.rcdefaults()
    plt.rcParams.update({"font.family": "Libre Franklin", "font.size": 12})
    h = 1.55 + 0.55 * len(rows)
    fig = plt.figure(figsize=(8, h), facecolor=t["bg"])
    ax = fig.add_axes([0.25, 0.5 / h, 0.63, (h - 1.1 - 0.5) / h], facecolor=t["bg"])
    for i, r in enumerate(reversed(rows)):
        c = 100 * r["control"][0] / r["control"][1]
        s = 100 * r["skill"][0] / r["skill"][1]
        ax.plot([c, s], [i, i], color=t["line"], lw=3, solid_capstyle="round", zorder=1)
        ax.scatter([c], [i], s=110, color=t["faint"], zorder=2)
        ax.scatter([s], [i], s=150, color=t["accent"], zorder=3)
        ax.text(c - 2.2, i, f"{c:.0f}%", ha="right", va="center", color=t["faint"], fontsize=11)
        ax.text(s + 2.2, i, f"{s:.0f}%", ha="left", va="center", color=t["accent"], fontsize=12, fontweight=800)
        ax.text(-0.02, i, r["label"], transform=ax.get_yaxis_transform(), ha="right", va="center",
                color=t["ink"], fontsize=12, fontweight=600)
    ax.set_xlim(40, 108)
    ax.set_ylim(-0.6, len(rows) - 0.4)
    ax.axis("off")
    fig.text(0.04, 1 - 0.15 / h, d["title"], ha="left", va="top", fontsize=16, fontweight=800, color=t["ink"])
    fig.text(0.04, 1 - 0.55 / h, d["subtitle"], ha="left", va="top", fontsize=11, color=t["sub"])
    # legend as text, in the series colors
    fig.text(0.25, 0.14 / h, "Without the skill", color=t["faint"], fontsize=10.5, fontweight=600)
    fig.text(0.45, 0.14 / h, "With the skill", color=t["accent"], fontsize=10.5, fontweight=800)
    fig.savefig(OUT / f"benchmark-{name}.png", dpi=200, facecolor=t["bg"])
    plt.close(fig)
print("benchmark charts rendered")
