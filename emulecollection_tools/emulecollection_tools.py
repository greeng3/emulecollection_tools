from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtCore import Qt

def main() -> None:
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()

    label = QLabel("Welcome to the app!")
    layout.addWidget(label)

    def say_hello():
        label.setText("Hello, World!")

    button = QPushButton("Say Hello")
    button.clicked.connect(say_hello)
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()