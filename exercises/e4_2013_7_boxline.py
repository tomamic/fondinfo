from e3_2013_3_box import Box

class BoxLine:
    def __init__(self):
        self._boxes = []

    def add_box(self, b: Box):
        self._boxes.append(b)

    def sum_areas(self) -> int:
        area = 0
        for b in self._boxes:
            area += b.area()
        return area

    def containing_box(self) -> Box:
        width, height = 0, 0
        for b in self._boxes:
            w, h = b.dimensions()
            height += h
            if w > width:
                width = w
        return Box(width, height)

def main():
    line = BoxLine()
    w = int(input('w? '))
    h = int(input('h? '))
    while w > 0 and h > 0:
        b = Box(w, h)
        line.add_box(b)
        w = int(input('w? '))
        h = int(input('h? '))
    box = line.containing_box()
    area = line.sum_areas()
    print('Sum of areas:', area)
    print('Containing box:', box.dimensions())
    print('Wasted space (ratio):', 1 - area / box.area())

if __name__ == '__main__':
    main()
