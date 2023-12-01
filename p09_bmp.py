import g2d
from urllib.request import urlopen

def ifb(data: bytes) -> int:
    return int.from_bytes(data, "little")

palette, rows = [], []
w = h = bpp = color = row_len = 0

with urlopen("http://tomamic.github.io/data/redbrick.bmp") as bmp:
    header = bmp.read(54)
    print("Header:", header.hex(" "))
    img_pos = ifb(header[10:14])
    pal_pos = ifb(header[14:18]) + 14
    w = ifb(header[18:22])
    h = ifb(header[22:26])
    bpp = ifb(header[28:30])
    colors = (img_pos - pal_pos) // 4
    row_len = -4 * (w * bpp // -32)  # `ceil div`, 4-byte align
    bmp.read(pal_pos - 54)  # consume remaining header, if any
    
    print(f"\nPalette: {colors} colors ({bpp}bpp)")
    for c in range(colors):
        color = bmp.read(4)
        print(f"Color {c:3}:", color.hex(" "))
        palette.append(ifb(color))

    print(f"\nImage: {w}×{h} px")
    for y in reversed(range(h)):
        row = bmp.read(row_len)
        print(f"Row {y:3}:", row.hex(" "))
        rows.append(row)

# masks are used later, for separating (r, g, b) values
masks = (palette[:3] if bpp > 8 and palette else
         [0x7c00, 0x3e0, 0x1f] if bpp == 16 else
         [0xff0000, 0xff00, 0xff])

# let's draw on the canvas
g2d.init_canvas((w, h), 10)  # 10x zoom
for y, row in enumerate(reversed(rows)):
    for x in range(w):
        pix = ifb(row[x * bpp // 8 : -((x + 1) * bpp // -8)])
        if bpp <= 8:  # sub-byte, shift right by `ceil reminder`
            pix = (pix >> -((x + 1) * bpp % -8)) % (2 ** bpp)
            pix = palette[pix]
        # use bit masks for separating (r, g, b) values
        rgb = ((pix & m) << 8 >> len(f"{m:b}") for m in masks)
        g2d.set_color(tuple(rgb))
        g2d.draw_rect((x, y), (1, 1))
g2d.main_loop()
