#1 тапсырма

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QLineEdit,
    QComboBox, QSpinBox, QVBoxLayout, QHBoxLayout, QFormLayout,
    QGroupBox, QMessageBox,
)

class ButtonFactory:
    @staticmethod
    def create_button(text, color, width, height, parent=None):
        button = QPushButton(text, parent)
        button.setFixedSize(width, height)
        button.setStyleSheet(f"background-color: {color}; color: white;")
        return button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Factory")
        self.resize(450, 650)

        central = QWidget()
        main_layout = QVBoxLayout(central)
        self.setCentralWidget(central)

        self.status = QLabel("Батырма жасаңыз")
        main_layout.addWidget(self.status)

        self.actions = {
            "Хабарлама көрсету": self.action_message,
            "Санауыш": self.action_counter,
            "Өзін жою": self.action_delete,
        }

        form_box = QGroupBox("Жаңа батырма жасау")
        form = QFormLayout(form_box)

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Батырма мәтіні")
        self.color_input = QComboBox()
        self.color_input.addItems(["green", "red", "blue", "orange", "purple"])
        self.width_input = QSpinBox()
        self.width_input.setRange(50, 400)
        self.width_input.setValue(150)
        self.height_input = QSpinBox()
        self.height_input.setRange(20, 200)
        self.height_input.setValue(40)
        self.action_input = QComboBox()
        self.action_input.addItems(self.actions.keys())

        form.addRow("Мәтін:", self.text_input)
        form.addRow("Түс:", self.color_input)
        form.addRow("Ені:", self.width_input)
        form.addRow("Биіктігі:", self.height_input)
        form.addRow("Әрекет:", self.action_input)

        create_btn = ButtonFactory.create_button("Батырма жасау", "gray", 150, 35)
        create_btn.clicked.connect(self.create_custom_button)
        form.addRow(create_btn)
        main_layout.addWidget(form_box)

        quick_box = QGroupBox("Жылдам батырмалар")
        quick_layout = QHBoxLayout(quick_box)

        quick_buttons = [
            ("Сақтау", "green", "Хабарлама көрсету"),
            ("Санау", "blue", "Санауыш"),
            ("Жою", "red", "Өзін жою"),
        ]
        for text, color, action in quick_buttons:
            btn = ButtonFactory.create_button(text, color, 100, 35)
            btn.clicked.connect(
                lambda checked=False, t=text, c=color, a=action:
                    self.add_button(t, c, 150, 40, a)
            )
            quick_layout.addWidget(btn)
        main_layout.addWidget(quick_box)

        self.created_box = QGroupBox("Жасалған батырмалар")
        self.created_layout = QVBoxLayout(self.created_box)
        main_layout.addWidget(self.created_box)
        main_layout.addStretch()

    # ----- Батырма жасау -----
    def create_custom_button(self):
        text = self.text_input.text().strip()
        if not text:
            self.status.setText("Алдымен батырма мәтінін енгізіңіз!")
            return
        self.add_button(
            text,
            self.color_input.currentText(),
            self.width_input.value(),
            self.height_input.value(),
            self.action_input.currentText(),
        )

    def add_button(self, text, color, width, height, action_name):
        # Батырма ButtonFactory арқылы жасалады
        btn = ButtonFactory.create_button(text, color, width, height, self.created_box)
        btn.setProperty("base_text", text)
        btn.setProperty("count", 0)
        action = self.actions[action_name]
        btn.clicked.connect(lambda checked=False, b=btn, f=action: f(b))
        self.created_layout.addWidget(btn)
        self.status.setText(f"«{text}» батырмасы жасалды")

    def action_message(self, btn):
        QMessageBox.information(self, "Хабарлама", f"«{btn.text()}» батырмасы басылды")

    def action_counter(self, btn):
        count = btn.property("count") + 1
        btn.setProperty("count", count)
        btn.setText(f"{btn.property('base_text')} ({count})")

    def action_delete(self, btn):
        self.created_layout.removeWidget(btn)
        btn.deleteLater()
        self.status.setText("Батырма жойылды")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
