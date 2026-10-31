"""Render the README banner (light and dark) as HTML, then PNG via Playwright."""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

FONTDIR = Path(sys.argv[1])          # fontsource package/files
OUT = Path(sys.argv[2])
PLATE_LIGHT = sys.argv[3] if len(sys.argv) > 3 else ""
PLATE_DARK = sys.argv[4] if len(sys.argv) > 4 else ""
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1600, 560
rng = np.random.default_rng(11)

# Chart area on the right half
X0, X1, Y0, Y1 = 840, 1340, 110, 430
n = 24
xs = np.linspace(X0, X1, n)


def path(points):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in points)


noise = []
for k in range(15):
    level = rng.uniform(0.35, 0.8)
    walk = level + np.cumsum(rng.normal(0, 0.035, n))
    walk = np.clip(walk, 0.12, 0.95)
    ys = Y1 - walk * (Y1 - Y0) * 0.75
    noise.append(path(zip(xs, ys)))

signal_v = np.concatenate([np.linspace(0.30, 0.34, 9), np.linspace(0.36, 0.98, n - 9) ** 1.05])
signal_v += rng.normal(0, 0.012, n)
sy = Y1 - signal_v * (Y1 - Y0)
signal = path(zip(xs, sy))
end_x, end_y = xs[-1], sy[-1]
AXIS = max(Y1 - 0.12 * (Y1 - Y0), sy.max()) + 34

THEMES = {
    "light": dict(bg="#F7F7F5", ink="#18191B", sub="#4B4F55", faint="#7A7F86", line="#D3D5D8", axis="#B9BCC1", accent="#1F5AA6", plate=PLATE_LIGHT, tex=0.55),
    "dark": dict(bg="#101113", ink="#F3F4F5", sub="#C2C6CC", faint="#8D939B", line="#33373D", axis="#4A4F56", accent="#6FA3EE", plate=PLATE_DARK, tex=0.6),
}

for name, t in THEMES.items():
    plate = ""
    noise_svg = "\n".join(f'<path d="{d}" fill="none" stroke="{t["line"]}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>' for d in noise)
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: "LF"; font-weight: 500; src: url("file://{FONTDIR}/libre-franklin-latin-500-normal.woff2"); }}
@font-face {{ font-family: "LF"; font-weight: 600; src: url("file://{FONTDIR}/libre-franklin-latin-600-normal.woff2"); }}
@font-face {{ font-family: "LF"; font-weight: 800; src: url("file://{FONTDIR}/libre-franklin-latin-800-normal.woff2"); }}
@font-face {{ font-family: "LF"; font-weight: 900; src: url("file://{FONTDIR}/libre-franklin-latin-900-normal.woff2"); }}
html,body {{ margin:0; }}
.b {{ width:{W}px; height:{H}px; position:relative; overflow:hidden; background:{t["bg"]}; {plate} font-family:"LF",sans-serif; }}
.copy {{ position:absolute; left:96px; top:0; bottom:0; width:700px; display:flex; flex-direction:column; justify-content:center; }}
h1 {{ margin:0; font-weight:900; font-size:96px; line-height:0.95; letter-spacing:-0.035em; color:{t["ink"]}; }}
h1 span {{ color:{t["accent"]}; }}
p.tag {{ margin:28px 0 0; font-weight:600; font-size:30px; line-height:1.25; letter-spacing:-0.01em; color:{t["ink"]}; max-width:600px; }}
p.meta {{ margin:22px 0 0; font-weight:500; font-size:17px; line-height:1.45; color:{t["faint"]}; max-width:620px; }}
svg {{ position:absolute; left:0; top:0; }}
.tex {{ position:absolute; inset:0; background-image:url("file://{t["plate"]}"); background-size:cover; background-position:center; opacity:{t.get("tex", 0)}; }}
</style></head><body><div class="b">
{'<div class="tex"></div>' if t["plate"] else ''}
<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <line x1="{X0}" y1="{AXIS:.1f}" x2="{X1}" y2="{AXIS:.1f}" stroke="{t["axis"]}" stroke-width="1.5"/>
  {noise_svg}
  <path d="{signal}" fill="none" stroke="{t["accent"]}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="{end_x:.1f}" cy="{end_y:.1f}" r="11" fill="{t["accent"]}"/>
  <text x="{end_x + 24:.1f}" y="{end_y + 11:.1f}" font-family="LF" font-weight="800" font-size="30" fill="{t["accent"]}">the point</text>
</svg>
<div class="copy">
  <h1>data<br>story<span>craft</span></h1>
  <p class="tag">Turn analysis into charts, slides and reports that make the point.</p>
  <p class="meta">An Agent Skill for Claude Code, Claude.ai and Codex</p>
</div>
</div></body></html>"""
    hp = OUT / f"banner-{name}.html"
    hp.write_text(html)

js = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  for (const n of ['light','dark']) {{
    const p = await b.newPage({{ viewport: {{ width: {W}, height: {H} }}, deviceScaleFactor: 2 }});
    await p.goto('file://{OUT}/banner-' + n + '.html');
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    await p.screenshot({{ path: '{OUT}/banner-' + n + '.png', clip: {{ x: 0, y: 0, width: {W}, height: {H} }} }});
  }}
  await b.close();
}})();
"""
(OUT / "shot.js").write_text(js)
subprocess.run(["node", str(OUT / "shot.js")], check=True)
print("banners rendered")
