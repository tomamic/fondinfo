from urllib.request import urlopen
with urlopen("http://tomamic.github.io/data/redbrick.bmp") as bmp:
    header = bmp.read(54)
    hsize = int.from_bytes(header[14:18], byteorder="little") + 14
    w = int.from_bytes(header[18:22], byteorder="little")
    h = int.from_bytes(header[22:26], byteorder="little")
    bpp = int.from_bytes(header[28:30], byteorder="little")
    pal = (int.from_bytes(header[10:14], byteorder="little") - hsize) // 4
    bmp.read(hsize - 54)
    
    print(f"Palette: {pal} colors ({bpp}bpp)")
    for i in range(pal):
        print(bmp.read(4).hex(" "))

    print(f"\nImage: {w}×{h} px")
    row_size = w * bpp // 8
    padding = 4 - row_size % 4 if row_size % 4 else 0  # 4-byte alignment
    for i in range(h):
        print(bmp.read(row_size + padding).hex(" "))
