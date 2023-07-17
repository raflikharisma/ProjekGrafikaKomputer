import matplotlib.pyplot as plt

# Fungsi untuk menempatkan piksel pada titik-titik berurutan
def putpixels(x, y):
    plt.scatter(x, y, color='green', s=5)

# Implementasi Algoritma Mid-Point Circle Drawing
def midPointCircleDraw(x_centre, y_centre, r):
    # titik awal pada sumbu x = radius dan y = 0
    x = r
    y = 0
    # Menampilkan titik awal pada sumbu setelah translasi
    putpixels(x + x_centre, y + y_centre)
    # Jika radius lebih besar dari 0, maka hanya akan ada satu titik yang ditampilkan
    if r > 0:
        putpixels(x + x_centre, -y + y_centre)
        putpixels(y + y_centre, x + x_centre)
        putpixels(-y + y_centre, x + x_centre)

    P = 1 - r
    while x > y:
        y += 1
        # Mid-point berada di dalam atau di atas perimeter
        if P <= 0:
            P = P + 2 * y + 1
        # Mid-point berada di luar perimeter
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1
        # Semua titik perimeter sudah ditampilkan
        if x < y:
            break
        # Menampilkan titik yang dihasilkan dan pantulannya di oktan lain setelah translasi
        putpixels(x + x_centre, y + y_centre)
        putpixels(-x + x_centre, y + y_centre)
        putpixels(x + x_centre, -y + y_centre)
        putpixels(-x + x_centre, -y + y_centre)
        # Jika titik yang dihasilkan berada pada garis x = y,
        # maka titik-titik perimeter sudah ditampilkan
        if x != y:
            putpixels(y + y_centre, x + x_centre)
            putpixels(-y + y_centre, x + x_centre)
            putpixels(y + y_centre, -x + x_centre)
            putpixels(-y + y_centre, -x + x_centre)

# Membuat figure dan axis
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

h = 600
w = 800

# Axis
plt.plot([-w/2, w/2], [0, 0], color='black', linewidth=0.5)
plt.plot([0, 0], [-h/2, h/2], color='black', linewidth=0.5)

# Masukkan radius melalui keyboard
radius = float(input("Masukkan radius lingkaran: "))

midPointCircleDraw(0, 0, radius)

# Tampilkan koordinat radius dan titik pusat
plt.text(radius, 0, f'({radius}, 0)', ha='center', va='bottom')
plt.text(0, 0, '(0, 0)', ha='right', va='bottom')

# Atur batas plot dan tampilkan plot
plt.xlim(-w/2, w/2)
plt.ylim(-h/2, h/2)
plt.show()
