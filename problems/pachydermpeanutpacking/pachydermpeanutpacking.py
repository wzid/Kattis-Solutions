n = int(input())

class Box:

    def __init__(self, corner1, corner2, desc) -> None:
        self.x1 = corner1[0]
        self.y1 = corner1[1]
        self.x2 = corner2[0]
        self.y2 = corner2[1]
        self.desc = desc

    def is_inside(self, x, y):
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2
    
while n != 0:

    boxes = []
    for i in range(n):
        x1, y1, x2, y2, desc = input().split()
        x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
        box = Box((x1, y1), (x2, y2), desc)
        boxes.append(box)
    
    m = int(input())
    for i in range(m):
        x, y, desc = input().split()
        x, y = float(x), float(y)
        found = False
        for box in boxes:
            if box.is_inside(x, y):
                if box.desc == desc:
                    print(desc, 'correct')
                else:
                    print(desc, box.desc)
                found = True
                break
        if not found:
            print(desc, 'floor')
    
    n = int(input())
    if n != 0:
        print()