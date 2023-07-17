import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from mpl_toolkits.mplot3d import Axes3D
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.points = []
        self.node_names = []
        self.node_counter = 0

        self.init_ui() #Mengatur tampilan awal jendela dan label.

    def init_ui(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Transformasi Node")

        self.label = QLabel("Klik untuk menambah node", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

    # Meng-handle event ketika tombol "M" pada keyboard ditekan untuk menampilkan output dan plot 3D.
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_M:
            self.show_output()
            self.show_3d_plot()
            self.show_translated_3d_plot()

        # Meng-handle event ketika tombol "R" pada keyboard ditekan untuk menampilkan output dan plot 3D setelah melakukan refleksi.
        elif event.key() == Qt.Key_R:
            self.show_reflected_3d_plot()

        # Meng-handle event ketika tombol "T" pada keyboard ditekan untuk menampilkan output dan plot 3D setelah melakukan rotasi.
        elif event.key() == Qt.Key_T:
            self.show_rotated_3d_plot()

    # Menampilkan plot 3D dari titik-titik yang telah ditambahkan setelah melakukan refleksi pada sumbu X
    def show_reflected_3d_plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x_points = [point[0] for point in self.points]
        y_points = [point[1] for point in self.points]
        z_points = [0] * len(self.points)

        ax.scatter(x_points, y_points, z_points, color='r')

        # Menghubungkan setiap node dengan garis
        ax.plot(x_points, y_points, z_points, color='b')
        ax.plot([x_points[-1], x_points[0]], [y_points[-1], y_points[0]], [0, 0], color='b')

        # Melakukan refleksi pada sumbu X
        reflected_x_points = [-x for x in x_points]

        ax.scatter(reflected_x_points, y_points, z_points, color='g')

        # Menghubungkan setiap node yang telah direfleksi dengan garis
        ax.plot(reflected_x_points, y_points, z_points, color='m')
        ax.plot([reflected_x_points[-1], reflected_x_points[0]], [y_points[-1], y_points[0]], [0, 0], color='m')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()

    # Menampilkan plot 3D dari titik-titik yang telah ditambahkan setelah melakukan rotasi terhadap sumbu Z sebesar 45 derajat
    def show_rotated_3d_plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x_points = [point[0] for point in self.points]
        y_points = [point[1] for point in self.points]
        z_points = [0] * len(self.points)

        ax.scatter(x_points, y_points, z_points, color='r')

        # Menghubungkan setiap node dengan garis
        ax.plot(x_points, y_points, z_points, color='b')
        ax.plot([x_points[-1], x_points[0]], [y_points[-1], y_points[0]], [0, 0], color='b')

        # Melakukan rotasi terhadap sumbu Z sebesar 45 derajat
        theta = np.radians(45)
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        rotated_points = np.dot(rotation_matrix, np.column_stack((x_points, y_points)).T).T
        rotated_x_points = rotated_points[:, 0]
        rotated_y_points = rotated_points[:, 1]

        ax.scatter(rotated_x_points, rotated_y_points, z_points, color='g')

        # Menghubungkan setiap node yang telah dirotasi dengan garis
        ax.plot(rotated_x_points, rotated_y_points, z_points, color='m')
        ax.plot([rotated_x_points[-1], rotated_x_points[0]], [rotated_y_points[-1], rotated_y_points[0]], [0, 0], color='m')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()

    # Meng-handle event ketika tombol kiri mouse ditekan untuk menambahkan titik ke dalam daftar titik.
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = event.x()
            y = event.y()
            self.points.append((x, y))
            self.node_names.append(chr(65 + self.node_counter))
            self.node_counter += 1
            self.update_label()

    # Menampilkan output berupa posisi titik-titik yang telah ditambahkan.
    def show_output(self):
        if len(self.points) < 3:
            print("Minimal 3 node diperlukan")
            return

        output = f"pos:\n"
        for i, point in enumerate(self.points):
            output += f"Titik {i+1}: ({point[0]}, {point[1]})\n"

        print(output)

    # Meng-update teks label dengan koordinat setiap titik.
    def update_label(self):
        node_labels = [f"{name}: ({point[0]}, {point[1]})" for name, point in zip(self.node_names, self.points)]
        self.label.setText("\n".join(node_labels))

    # Menampilkan plot 3D dari titik-titik yang telah ditambahkan.
    def show_3d_plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x_points = [point[0] for point in self.points]
        y_points = [point[1] for point in self.points]
        z_points = [0] * len(self.points)

        ax.scatter(x_points, y_points, z_points, color='r')

        # Menghubungkan setiap node dengan garis
        ax.plot(x_points, y_points, z_points, color='b')
        ax.plot([x_points[-1], x_points[0]], [y_points[-1], y_points[0]], [0, 0], color='b')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()

    # Menampilkan plot 3D dari titik-titik yang telah ditambahkan setelah melakukan translasi pada sumbu X, Y, dan Z.
    def show_translated_3d_plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x_points = [point[0] for point in self.points]
        y_points = [point[1] for point in self.points]
        z_points = [0] * len(self.points)

        ax.scatter(x_points, y_points, z_points, color='r')

        # Menghubungkan setiap node dengan garis
        ax.plot(x_points, y_points, z_points, color='b')
        ax.plot([x_points[-1], x_points[0]], [y_points[-1], y_points[0]], [0, 0], color='b')

        # Melakukan translasi pada sumbu X, Y, dan Z
        dx, dy, dz = 5, 5, 5
        translated_x_points = [x + dx for x in x_points]
        translated_y_points = [y + dy for y in y_points]
        translated_z_points = [z + dz for z in z_points]

        ax.scatter(translated_x_points, translated_y_points, translated_z_points, color='g')

        # Menghubungkan setiap node yang telah di-translasi dengan garis
        ax.plot(translated_x_points, translated_y_points, translated_z_points, color='m')
        ax.plot([translated_x_points[-1], translated_x_points[0]], [translated_y_points[-1], translated_y_points[0]], [translated_z_points[-1], translated_z_points[0]], color='m')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
