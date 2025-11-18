import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Test GUI")
    layout = QVBoxLayout()

    label = QLabel("Приложение работает!")
    layout.addWidget(label)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
