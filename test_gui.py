from PySide6.QtWidgets import QApplication, QWidget
import sys

print("Запускаем QApplication...")

app = QApplication(sys.argv)

print("Создаем окно...")

window = QWidget()
window.setWindowTitle("Тестовое окно")
window.resize(300, 200)
window.show()

print("Окно должно быть открыто.")

app.exec()
