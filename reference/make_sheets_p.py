import os, glob
from PIL import Image, ImageDraw

base = os.path.dirname(os.path.abspath(__file__))
fdir = os.path.join(base, "frames_p")
files = sorted(glob.glob(os.path.join(fdir, "p_*.png")))
cols, rows = 5, 3
tw, th = 384, 216
label_h = 22
per = cols * rows

def sheet(batch, idx):
    W = cols * tw
    H = rows * (th + label_h)
    canvas = Image.new("RGB", (W, H), (20, 20, 20))
    d = ImageDraw.Draw(canvas)
    for k, f in enumerate(batch):
        im = Image.open(f).resize((tw, th))
        r, c = divmod(k, cols)
        x, y = c * tw, r * (th + label_h)
        canvas.paste(im, (x, y + label_h))
        n = int(os.path.basename(f).split("_")[1].split(".")[0])
        t = (n - 1)
        d.text((x + 6, y + 4), f"#{n}  {t:02d}s", fill=(255, 255, 0))
    out = os.path.join(base, f"psheet{idx}.jpg")
    canvas.save(out, quality=88)
    print(out, len(batch))

for i in range(0, len(files), per):
    sheet(files[i:i+per], i // per + 1)
