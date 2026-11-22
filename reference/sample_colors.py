import os
from PIL import Image

base = os.path.dirname(os.path.abspath(__file__))

def avg(im, x, y, r=18):
    px = im.load()
    W, H = im.size
    rs = gs = bs = n = 0
    for dx in range(-r, r+1):
        for dy in range(-r, r+1):
            xx, yy = min(W-1, max(0, x+dx)), min(H-1, max(0, y+dy))
            p = px[xx, yy]
            rs += p[0]; gs += p[1]; bs += p[2]; n += 1
    return (rs//n, gs//n, bs//n)

day = Image.open(os.path.join(base, "frames_p", "p_001.png")).convert("RGB")
sun = Image.open(os.path.join(base, "frames_p", "p_016.png")).convert("RGB")

day_pts = {
    "sky_top": (960, 70),
    "sky_cloud": (1300, 120),
    "grass_sun": (1650, 960),
    "grass_shadow": (280, 820),
    "tree_sun": (180, 180),
    "tree_dark": (1500, 250),
    "path": (1010, 720),
}
sun_pts = {
    "sky_top": (450, 90),
    "sky_mid": (700, 300),
    "horizon": (1150, 600),
    "blossom": (1780, 320),
    "meadow_flower": (900, 860),
    "grass_shadow": (260, 920),
}

print("DAY", day.size)
for k, xy in day_pts.items():
    print(f"  {k:14s} {avg(day, *xy)}")
print("SUNSET", sun.size)
for k, xy in sun_pts.items():
    print(f"  {k:14s} {avg(sun, *xy)}")
