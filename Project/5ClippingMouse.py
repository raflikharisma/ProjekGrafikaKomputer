from graphics import *

#Implementasi algoritma liang barsky
def liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    p = [-1 * (x2 - x1), x2 - x1, -1 * (y2 - y1), y2 - y1]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]
    t1 = 0
    t2 = 1

#Menghitung titik potong antar garis dengan batas window yang sudah ditentukan
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
        xx1 = int(x1 + t1 * (x2 - x1))
        yy1 = int(y1 + t1 * (y2 - y1))
        xx2 = int(x1 + t2 * (x2 - x1))
        yy2 = int(y1 + t2 * (y2 - y1))
        return xx1, yy1, xx2, yy2
    else:
        return None

from graphics import *

#Menggambar sumbu kartesius dan menampilkan koordinat window pada tampilan grafis
def draw_cartesian(win, xmin, ymin, xmax, ymax):
    # Garis vertikal sumbu y
    vertical_axis = Line(Point(0, ymin), Point(0, ymax))
    vertical_axis.setOutline("black")
    vertical_axis.draw(win)

    # Garis horizontal sumbu x
    horizontal_axis = Line(Point(xmin, 0), Point(xmax, 0))
    horizontal_axis.setOutline("black")
    horizontal_axis.draw(win)

    # Menampilkan koordinat window
    xmin_label = Text(Point(xmin, ymin - 20), f"({xmin}, {ymin})")
    xmin_label.setTextColor("green")
    xmin_label.draw(win)

    ymin_label = Text(Point(xmin, ymax + 20), f"({xmin}, {ymax})")
    ymin_label.setTextColor("green")
    ymin_label.draw(win)

    xmax_label = Text(Point(xmax, ymin - 20), f"({xmax}, {ymin})")
    xmax_label.setTextColor("green")
    xmax_label.draw(win)

    ymax_label = Text(Point(xmax, ymax + 20), f"({xmax}, {ymax})")
    ymax_label.setTextColor("green")
    ymax_label.draw(win)


def main():

    #Membuat tampilan grafis dengan ukuran 700 x 700 pixel
    win = GraphWin("Line Clipping", 700, 700)

    #Menentukan batas window 
    xmin, ymin, xmax, ymax = 100, 100, 400, 400

    #Menggambar sumbu kartesius dan persegi window
    draw_cartesian(win, xmin, ymin, xmax, ymax)
    rectangle = Rectangle(Point(xmin, ymin), Point(xmax, ymax))
    rectangle.setOutline("red")
    rectangle.draw(win)

    while True:
        click_point1 = win.getMouse()  # Mengambil posisi klik pertama
        x1, y1 = click_point1.getX(), click_point1.getY()

        click_point2 = win.getMouse()  # Mengambil posisi klik kedua
        x2, y2 = click_point2.getX(), click_point2.getY()

        line = Line(Point(x1, y1), Point(x2, y2))
        line.draw(win)

        # Menampilkan koordinat ujung garis pertama
        p1_label = Text(Point(x1, y1 - 20), f"({x1}, {y1})")
        p1_label.setTextColor("green")
        p1_label.draw(win)

        # Menampilkan koordinat ujung garis kedua
        p2_label = Text(Point(x2, y2 - 20), f"({x2}, {y2})")
        p2_label.setTextColor("green")
        p2_label.draw(win)

        clipped_points = liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
        if clipped_points is not None:
            xx1, yy1, xx2, yy2 = clipped_points
            clipped_line = Line(Point(xx1, yy1), Point(xx2, yy2))
            clipped_line.setWidth(10)
            clipped_line.setOutline("blue")
            clipped_line.draw(win)

            # Menampilkan koordinat perpotongan garis dengan sumbu/window
            intersection_x = [xx1, xx2]
            intersection_y = [yy1, yy2]
            for i in range(len(intersection_x)):
                intersection_label = Text(Point(intersection_x[i], intersection_y[i] - 20), f"({intersection_x[i]}, {intersection_y[i]})")
                intersection_label.setTextColor("green")
                intersection_label.draw(win)

        else:
            print("Line lies outside the window")

        # Menunggu klik mouse lagi untuk menggambar garis baru
        win.getMouse()
        win.clear()

        # Menggambar ulang sumbu cartesius dan persegi window
        draw_cartesian(win, xmin, ymin, xmax, ymax)
        rectangle.draw(win)

        # Menghapus garis-garis dan teks sebelumnya
        line.undraw()
        p1_label.undraw()
        p2_label.undraw()
        if clipped_points is not None:
            clipped_line.undraw()

if __name__ == "__main__":
    main()
