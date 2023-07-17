import matplotlib.pyplot as plt

def liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    p = [-1 * (x2 - x1), x2 - x1, -1 * (y2 - y1), y2 - y1]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]
    t1 = 0
    t2 = 1

    for i in range(4):
        if p[i] != 0:
            t = q[i] / p[i]
            if p[i] < 0:
                t1 = max(t1, t)
            else:
                t2 = min(t2, t)
        elif q[i] < 0:
            return None

    if t1 < t2:
        xx1 = x1 + t1 * (x2 - x1)
        yy1 = y1 + t1 * (y2 - y1)
        xx2 = x1 + t2 * (x2 - x1)
        yy2 = y1 + t2 * (y2 - y1)
        return xx1, yy1, xx2, yy2
    else:
        return None

def draw_objects(objects):
    for obj in objects:
        x, y, w, h = obj
        plt.plot([x, x+w, x+w, x, x], [y, y, y+h, y+h, y], color='green')

def windowing_tipe_1(objects, xmin, ymin, xmax, ymax):
    new_objects = []
    for obj in objects:
        x, y, w, h = obj
        if x >= xmin and y >= ymin and (x + w) <= xmax and (y + h) <= ymax:
            new_objects.append(obj)
    return new_objects

def windowing_tipe_2(objects, xmin, ymin, xmax, ymax):
    new_objects = []
    for obj in objects:
        x, y, w, h = obj
        if (x + w) >= xmin and (y + h) >= ymin and x <= xmax and y <= ymax:
            new_objects.append(obj)
    return new_objects

def main():
    objects = [(1, 1, 3, 3), (2, 2, 4, 4), (5, 5, 2, 2), (7, 7, 3, 3)]

    xmin = float(input("Enter xmin: "))
    ymin = float(input("Enter ymin: "))
    xmax = float(input("Enter xmax: "))
    ymax = float(input("Enter ymax: "))

    plt.figure(figsize=(6, 6))
    plt.xlim(xmin-1, xmax+1)
    plt.ylim(ymin-1, ymax+1)

    draw_objects(objects)

    for obj in objects:
        x, y, w, h = obj
        plt.text(x, y, f'({x}, {y})', color='red')
        plt.text(x + w, y, f'({x + w}, {y})', color='red')
        plt.text(x + w, y + h, f'({x + w}, {y + h})', color='red')
        plt.text(x, y + h, f'({x}, {y + h})', color='red')

    plt.title("Original Objects")
    plt.show()

    new_objects_tipe_1 = windowing_tipe_1(objects, xmin, ymin, xmax, ymax)
    new_objects_tipe_2 = windowing_tipe_2(objects, xmin, ymin, xmax, ymax)

    plt.figure(figsize=(6, 6))
    plt.xlim(xmin-1, xmax+1)
    plt.ylim(ymin-1, ymax+1)

    draw_objects(new_objects_tipe_1)

    for obj in new_objects_tipe_1:
        x, y, w, h = obj
        plt.text(x, y, f'({x}, {y})', color='red')
        plt.text(x + w, y, f'({x + w}, {y})', color='red')
        plt.text(x + w, y + h, f'({x + w}, {y + h})', color='red')
        plt.text(x, y + h, f'({x}, {y + h})', color='red')

    plt.title("Windowing Type 1")
    plt.show()

    plt.figure(figsize=(6, 6))
    plt.xlim(xmin-1, xmax+1)
    plt.ylim(ymin-1, ymax+1)

    draw_objects(new_objects_tipe_2)

    for obj in new_objects_tipe_2:
        x, y, w, h = obj
        plt.text(x, y, f'({x}, {y})', color='red')
        plt.text(x + w, y, f'({x + w}, {y})', color='red')
        plt.text(x + w, y + h, f'({x + w}, {y + h})', color='red')
        plt.text(x, y + h, f'({x}, {y + h})', color='red')

    plt.title("Windowing Type 2")
    plt.show()

if __name__ == "__main__":
    main()