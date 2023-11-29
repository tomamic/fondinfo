from urllib.request import urlopen
with urlopen("http://tomamic.github.io/data/redbrick.bmp") as bmp:
    header = bmp.read(54)
    img_pos = int.from_bytes(header[10:14], "little")
    pal_pos = int.from_bytes(header[14:18], "little") + 14
    w = int.from_bytes(header[18:22], "little")
    h = int.from_bytes(header[22:26], "little")
    bpp = int.from_bytes(header[28:30], "little")
    row_len = -4 * (-w  * bpp // 32)  # ceil division, 4-byte alignment
    bmp.read(pal_pos - 54)  # consume remaining header, if any

    colors = (img_pos - pal_pos) // 4
    print(f"Palette: {colors} colors ({bpp}bpp)")
    for i in range(colors):
        print(bmp.read(4).hex(" "))

    print(f"\nImage: {w}×{h} px")
    for i in range(h):
        print(bmp.read(row_len).hex(" "))
