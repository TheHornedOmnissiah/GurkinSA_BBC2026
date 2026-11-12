from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox, QGridLayout

def v():
    try:
        x = float(b.text())
        y = float(d.text())
    except ValueError:
        QMessageBox.warning(w, "Сбой", "Только цифры!")
        return

    if x <= 0 or y <= 0:
        QMessageBox.warning(w, "Сбой", "Больше нуля!")
        return

    z = x * y if e.currentText() == "Прямоугольник" else 0.5 * x * y
    g.setText(f"Итог: {z:.2f}")
    QMessageBox.information(w, "Ок", "Готово!")

m = QApplication([])
w = QWidget()

a = QLabel("A:")
b = QLineEdit()
c = QLabel("B:")
d = QLineEdit()
e = QComboBox()
e.addItems(["Прямоугольник", "Треугольник"])
f = QPushButton("Счет")
g = QLabel("Итог: -")

h = QGridLayout()
h.addWidget(a, 0, 0)
h.addWidget(b, 0, 1)
h.addWidget(c, 1, 0)
h.addWidget(d, 1, 1)
h.addWidget(e, 2, 0, 1, 2)
h.addWidget(f, 3, 0, 1, 2)
h.addWidget(g, 4, 0, 1, 2)

w.setLayout(h)
f.clicked.connect(v)
w.show()
m.exec()