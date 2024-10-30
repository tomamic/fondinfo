#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def intb(data: bytes) -> int:
    return int.from_bytes(data, "little")

def read_bmp(fname: str) -> tuple:
    image, palette, w, h, bpp = [], [], 0, 0, 0
    with open(fname, "rb") as bmp:
        head = bmp.read(54)
        img_pos = intb(head[10:14])
        head_len = intb(head[14:18]) + 14
        w = intb(head[18:22])
        h = intb(head[22:26])
        bpp = intb(head[28:30])
        colors = (img_pos - head_len) // 4
        row_len = -4 * (w * bpp // -32)  # `ceil div`, 4-byte align
        bmp.read(head_len - 54)  # consume remaining header, if any
        palette = [bmp.read(4) for _ in range(colors)]
        image = [bmp.read(row_len) for _ in range(h)]
    return image, palette, w, h, bpp

def dump_bmp(image, palette, w, h, bpp):
    print(f"\nPalette: {len(palette)} colors ({bpp}bpp)")
    for i, v in enumerate(palette):
        print(f"Color {i:3}:", v.hex(" "))

    print(f"\nImage: {w}×{h} px")
    for i, v in enumerate(image):
        print(f"Row {i:3}:", v.hex(" "))

def draw_4bpp(image, palette, w, h, bpp):
    import g2d
    g2d.init_canvas((w, h), 10)  # 10x zoom
    for y, row in enumerate(reversed(image)):
        for x in range(w):
            if bpp == 4:
                pix = row[x // 2]  # 2 pixels per byte
                pix = pix // 16 if x % 2 == 0 else pix % 16
                b, g, r, _ = palette[pix]
                g2d.set_color((r, g, b))
            g2d.draw_rect((x, y), (1, 1))
    g2d.main_loop()

def draw_bmp(image, palette, w, h, bpp):
    import g2d
    g2d.init_canvas((w, h), 10)  # 10x zoom
    palette_ = [intb(p) for p in palette]
    masks = (palette_[:3] if bpp > 8 and palette_ else
             [0x1f<<10, 0x1f<<5, 0x1f] if bpp == 16 else  # R5.G5.B5
             [0xff0000, 0xff00, 0xff])  # default: R8.G8.B8

    for y, row in enumerate(reversed(image)):
        for x in range(w):
            xbyte, xbit = divmod(x * bpp, 8)
            pix = intb(row[xbyte : xbyte + max(1, bpp // 8)])
            if bpp <= 8:  # sub-byte, color from palette
                shr = 8 - xbit - bpp  # align pixel bits to right
                msk = 2 ** bpp - 1    # keep lowest bpp bits
                pix = palette_[(pix >> shr) & msk]
            # use a bit mask for filtering R, G, or B bits
            # then align the relevant 8 bits to right
            rgb = ((pix & m) << 8 >> m.bit_length() for m in masks)
            g2d.set_color(tuple(rgb))
            g2d.draw_rect((x, y), (1, 1))
    g2d.main_loop()

if __name__ == "__main__":
    image, palette, w, h, bpp = read_bmp("redbrick.bmp")
    dump_bmp(image, palette, w, h, bpp)
    draw_4bpp(image, palette, w, h, bpp)  # or, draw_bmp
