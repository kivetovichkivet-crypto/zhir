from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QSpinBox,
    QDoubleSpinBox,
    QLineEdit,
    QGroupBox,
    QFormLayout,
    QListWidget,
)

from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Zhir AI")
        self.resize(1200, 750)

        self.setup_ui()
        self.apply_theme()

    def setup_ui(self):
        main = QWidget()
        self.setCentralWidget(main)

        root = QHBoxLayout(main)

        # Левая панель
        left = QVBoxLayout()

        title = QLabel("🎨 Zhir AI")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(
            "font-size: 28px; font-weight: bold;"
        )

        left.addWidget(title)

        prompt_box = QGroupBox("Prompt")

        prompt_layout = QVBoxLayout()

        self.prompt = QTextEdit()
        self.prompt.setPlaceholderText(
            "Опишите изображение..."
        )

        prompt_layout.addWidget(self.prompt)

        prompt_box.setLayout(prompt_layout)

        left.addWidget(prompt_box)


        negative_box = QGroupBox("Negative Prompt")

        negative_layout = QVBoxLayout()

        self.negative_prompt = QTextEdit()
        self.negative_prompt.setPlaceholderText(
            "Что исключить..."
        )

        negative_layout.addWidget(
            self.negative_prompt
        )

        negative_box.setLayout(
            negative_layout
        )

        left.addWidget(
            negative_box
        )


        settings = QGroupBox("Настройки")

        form = QFormLayout()

        self.width = QSpinBox()
        self.width.setValue(512)

        self.height = QSpinBox()
        self.height.setValue(512)

        self.steps = QSpinBox()
        self.steps.setValue(20)

        self.cfg = QDoubleSpinBox()
        self.cfg.setValue(7.5)

        self.seed = QLineEdit()
        self.seed.setPlaceholderText(
            "Random"
        )

        form.addRow(
            "Ширина:",
            self.width
        )

        form.addRow(
            "Высота:",
            self.height
        )

        form.addRow(
            "Steps:",
            self.steps
        )

        form.addRow(
            "CFG:",
            self.cfg
        )

        form.addRow(
            "Seed:",
            self.seed
        )

        settings.setLayout(form)

        left.addWidget(settings)


        self.generate = QPushButton(
            "🎨 Generate"
        )

        self.generate.setMinimumHeight(
            45
        )

        left.addWidget(
            self.generate
        )


        left.addStretch()


        # Правая часть
        right = QVBoxLayout()

        preview_title = QLabel(
            "Preview"
        )

        preview_title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        preview_title.setStyleSheet(
            "font-size:20px;"
        )

        right.addWidget(
            preview_title
        )


        self.preview = QLabel(
            "Здесь будет изображение"
        )

        self.preview.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.preview.setMinimumSize(
            500,
            500
        )

        self.preview.setStyleSheet(
            """
            border: 2px solid #555;
            border-radius: 10px;
            """
        )

        right.addWidget(
            self.preview
        )


        history_title = QLabel(
            "История"
        )

        right.addWidget(
            history_title
        )

        self.history = QListWidget()

        right.addWidget(
            self.history
        )


        root.addLayout(
            left,
            1
        )

        root.addLayout(
            right,
            2
        )


    def apply_theme(self):
        self.setStyleSheet(
            """
            QWidget {
                background-color: #202124;
                color: white;
                font-size: 14px;
            }

            QTextEdit,
            QLineEdit,
            QSpinBox,
            QDoubleSpinBox {
                background-color: #303134;
                border: 1px solid #555;
                padding: 5px;
                color: white;
            }

            QPushButton {
                background-color: #3c78ff;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #5a8cff;
            }

            QGroupBox {
                border: 1px solid #555;
                border-radius: 8px;
                margin-top: 10px;
                padding: 10px;
            }
            """
        )
