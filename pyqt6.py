import sys
from itertools import cycle

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class ButtonFactory:
    """Батырмаларды бір орыннан жасайтын фабрика."""

    @staticmethod
    def apply_color(button, color):
        button.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                border-radius: 6px;
                font-weight: bold;
            }}
            QPushButton:hover {{ border: 2px solid #333333; }}
            QPushButton:pressed {{ padding-top: 3px; }}
            """
        )

    @staticmethod
    def create_button(text, color="gray", width=120, height=40, parent=None):
        button = QPushButton(text, parent)
        button.setFixedSize(width, height)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        ButtonFactory.apply_color(button, color)
        return button


COLORS = {
    "Жасыл": "green",
    "Қызыл": "crimson",
    "Көк": "royalblue",
    "Сары": "darkorange",
    "Күлгін": "purple",
    "Сұр": "gray",
}

ACTIONS = [
    "Хабарлама көрсету",
    "Санауыш (басқан сайын +1)",
    "Түсін ауыстыру",
    "Өзін жою",
]


class MainWindow(QMainWindow):
    COLUMNS = 3

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ButtonFactory — PyQt6")
        self.resize(560, 560)

        self.created_count = 0
        self.dynamic_buttons = []

        central = QWidget()
        root = QVBoxLayout(central)
        self.setCentralWidget(central)


        root.addWidget(self._build_fixed_buttons())

        root.addWidget(self._build_form())


        box = QGroupBox("Жасалған батырмалар")
        self.grid = QGridLayout(box)
        self.grid.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        root.addWidget(box, stretch=1)

  
        self.status = QLabel("Күту режимі...")
        root.addWidget(self.status)


    def _build_fixed_buttons(self):
        box = QGroupBox("Негізгі батырмалар")
        row = QHBoxLayout(box)

        save_btn = ButtonFactory.create_button("Сақтау", "green", 150, 40, self)
        clear_btn = ButtonFactory.create_button("Тазалау", "crimson", 150, 40, self)
        info_btn = ButtonFactory.create_button("Ақпарат", "royalblue", 150, 40, self)


        save_btn.clicked.connect(self.on_save)
        clear_btn.clicked.connect(self.on_clear)
        info_btn.clicked.connect(self.on_info)

        for b in (save_btn, clear_btn, info_btn):
            row.addWidget(b)
        return box

    def _build_form(self):
        box = QGroupBox("Жаңа батырма жасау")
        form = QFormLayout(box)

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Батырма мәтіні")

        self.color_combo = QComboBox()
        self.color_combo.addItems(COLORS.keys())

        self.width_spin = QSpinBox()
        self.width_spin.setRange(60, 300)
        self.width_spin.setValue(140)

        self.height_spin = QSpinBox()
        self.height_spin.setRange(25, 120)
        self.height_spin.setValue(40)

        self.action_combo = QComboBox()
        self.action_combo.addItems(ACTIONS)

        create_btn = ButtonFactory.create_button(
            "Батырма жасау", "seagreen", 160, 36, self
        )
        create_btn.clicked.connect(self.create_dynamic_button)

        form.addRow("Мәтін:", self.text_input)
        form.addRow("Түс:", self.color_combo)
        form.addRow("Ені:", self.width_spin)
        form.addRow("Биіктігі:", self.height_spin)
        form.addRow("Әрекет:", self.action_combo)
        form.addRow(create_btn)
        return box


    def on_save(self):
        self.status.setText("Деректер сақталды ✔")

    def on_clear(self):
        for btn in self.dynamic_buttons:
            self.grid.removeWidget(btn)
            btn.deleteLater()
        self.dynamic_buttons.clear()
        self.created_count = 0
        self.status.setText("Барлық жасалған батырмалар өшірілді.")

    def on_info(self):
        self.status.setText(
            f"Жасалған батырмалар саны: {len(self.dynamic_buttons)}"
        )

    def create_dynamic_button(self):
        self.created_count += 1
        text = self.text_input.text().strip() or f"Батырма {self.created_count}"
        color = COLORS[self.color_combo.currentText()]

        button = ButtonFactory.create_button(
            text=text,
            color=color,
            width=self.width_spin.value(),
            height=self.height_spin.value(),
            parent=self,
        )

        self._assign_action(button, self.action_combo.currentText())

        index = len(self.dynamic_buttons)
        self.grid.addWidget(button, index // self.COLUMNS, index % self.COLUMNS)
        self.dynamic_buttons.append(button)

        self.text_input.clear()
        self.status.setText(f"«{text}» батырмасы жасалды.")

    def _assign_action(self, button, action_name):
        if action_name == ACTIONS[0]:
            button.clicked.connect(
                lambda: self.status.setText(f"«{button.text()}» батырмасы басылды!")
            )

        elif action_name == ACTIONS[1]:
            state = {"count": 0, "title": button.text()}

            def count():
                state["count"] += 1
                button.setText(f"{state['title']} ({state['count']})")
                self.status.setText(f"Санауыш: {state['count']}")

            button.clicked.connect(count)

        elif action_name == ACTIONS[2]:
            palette = cycle(COLORS.values())

            def change_color():
                ButtonFactory.apply_color(button, next(palette))
                self.status.setText("Батырманың түсі өзгерді.")

            button.clicked.connect(change_color)

        else:  
            def remove_self():
                self.grid.removeWidget(button)
                self.dynamic_buttons.remove(button)
                button.deleteLater()
                self._relayout()
                self.status.setText("Батырма жойылды.")

            button.clicked.connect(remove_self)

    def _relayout(self):
        """Батырма жойылғаннан кейін торды қайта реттеу."""
        for btn in self.dynamic_buttons:
            self.grid.removeWidget(btn)
        for i, btn in enumerate(self.dynamic_buttons):
            self.grid.addWidget(btn, i // self.COLUMNS, i % self.COLUMNS)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
