from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QHBoxLayout,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Zhir AI")
        self.resize(1100, 700)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        title = QLabel("Zhir AI")
        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        self.prompt = QTextEdit()
        self.prompt.setPlaceholderText("Введите описание изображения...")
        self.prompt.setFixedHeight(120)

        layout.addWidget(self.prompt)

        buttons = QHBoxLayout()

        self.generate_btn = QPushButton("🎨 Сгенерировать")
        self.settings_btn = QPushButton("⚙ Настройки")

        buttons.addWidget(self.generate_btn)
        buttons.addWidget(self.settings_btn)

        layout.addLayout(buttons)

        self.status = QLabel("Готово")

        layout.addWidget(self.status)
