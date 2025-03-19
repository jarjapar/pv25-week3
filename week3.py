import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Week 3 - F1D022072 - Muhammad Fajar Maulana")
        self.setGeometry(100, 100, 500, 350)
        self.label = QLabel(self)
        self.label.setStyleSheet("font-size: 15px;")
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.label.setText(f"x: {event.x()}, y: {event.y()}")
        self.label.adjustSize()
        if self.mouseMoveEnter(event.x(), event.y()):
            self.mouseMove()

    def mouseMoveEnter(self, x, y):
        labelx, labely, width, height = self.label.geometry().getRect()
        margin = 20
        xrange = (labelx - margin) <= x <= (labelx + width + margin)
        yrange = (labely - margin) <= y <= (labely + height + margin)
        return xrange and yrange

    def mouseMove(self):
        xmax = self.width() - self.label.width()
        ymax = self.height() - self.label.height()
        newx = random.randint(0, xmax)
        newy = random.randint(0, ymax)
        self.label.move(newx, newy)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec_())
