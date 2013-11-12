with open("file1.dat") as f1:
    with open("file2.dat") as f2:
        with open("merge.dat", "w") as out:
            a = f1.readline().strip()
            b = f2.readline().strip()
            while a != '' or b != '':
                if a != '' and (b == '' or float(a) < float(b)):
                    print(a, file=out)
                    a = f1.readline().strip()
                else:
                    print(b, file=out)
                    b = f2.readline().strip()
