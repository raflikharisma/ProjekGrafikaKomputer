import matplotlib.pyplot as plt

# Fungsi implementasi metode Bresenham
def bresenham(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    err = dx - dy

    points = []

    while True:
        points.append((x0, y0))

        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    return points

# Fungsi event handler ketika tombol mouse diklik
def onclick(event):
    if event.button == 1:
        global x0, y0, x1, y1
        if x0 is None and y0 is None:
            x0, y0 = event.xdata, event.ydata
        else:
            x1, y1 = event.xdata, event.ydata
            points = bresenham(int(x0), int(y0), int(x1), int(y1))
            x_vals, y_vals = zip(*points)
            plt.plot(x_vals, y_vals)
            plt.draw()

            # Menampilkan koordinat garis
            for i, point in enumerate(points):
                plt.text(point[0], point[1], f'({point[0]}, {point[1]})', ha='center', va='bottom')

            x0, y0, x1, y1 = None, None, None, None

# Inisialisasi variabel titik awal dan akhir garis
x0, y0, x1, y1 = None, None, None, None

# Membuat objek grafik
fig, ax = plt.subplots()

# Mengatur batas sumbu x dan y
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

# Mengatur aspek rasio grafik agar persegi
plt.gca().set_aspect('equal', adjustable='box')

# Menghubungkan event handler dengan mouse click event
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
