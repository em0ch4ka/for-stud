#2 тапсырма

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox,
    QCheckBox, QVBoxLayout, QGroupBox,
)

class ButtonBuilder:

    def __init__(self):
        self.reset()

    def reset(self):
        self._widget = QPushButton()
        return self

    def set_text(self, text):
        self._widget.setText(text)
        return self

    def set_size(self, width, height):
        self._widget.setFixedSize(width, height)
        return self

    def set_color(self, color):
        self._widget.setStyleSheet(f"background-color: {color}; color: white;")
        return self

    def set_enabled(self, enabled):
        self._widget.setEnabled(enabled)
        return self

    def get_result(self):
        result = self._widget
        self.reset()
        return result

class LineEditBuilder:

    def __init__(self):
        self.reset()

    def reset(self):
        self._widget = QLineEdit()
        return self

    def set_text(self, text):
        self._widget.setText(text)
        return self

    def set_placeholder(self, placeholder):
        self._widget.setPlaceholderText(placeholder)
        return self

    def set_width(self, width):
        self._widget.setFixedWidth(width)
        return self

    def set_read_only(self, read_only):
        self._widget.setReadOnly(read_only)
        return self

    def get_result(self):
        result = self._widget
        self.reset()
        return result

class ComboBoxBuilder:

    def __init__(self):
        self.reset()

    def reset(self):
        self._widget = QComboBox()
        return self

    def set_items(self, items):
        self._widget.addItems(items)
        return self

    def set_current_index(self, index):
        self._widget.setCurrentIndex(index)
        return self

    def set_width(self, width):
        self._widget.setFixedWidth(width)
        return self

    def set_enabled(self, enabled):
        self._widget.setEnabled(enabled)
        return self

    def get_result(self):
        result = self._widget
        self.reset()
        return result

class CheckBoxBuilder:

    def __init__(self):
        self.reset()

    def reset(self):
        self._widget = QCheckBox()
        return self

    def set_text(self, text):
        self._widget.setText(text)
        return self

    def set_checked(self, checked):
        self._widget.setChecked(checked)
        return self

    def set_enabled(self, enabled):
        self._widget.setEnabled(enabled)
        return self

    def get_result(self):
        result = self._widget
        self.reset()
        return result

class WidgetDirector:
    def __init__(self, builder=None):
        self.builder = builder

    def set_builder(self, builder):
        """Қажетті Builder-ді қабылдау."""
        self.builder = builder

    def build_button(self, text="", width=150, height=40,
                     color="gray", enabled=True):
        self.builder.set_text(text)
        self.builder.set_size(width, height)
        self.builder.set_color(color)
        self.builder.set_enabled(enabled)
        return self.builder.get_result()

    def build_line_edit(self, text="", placeholder="", width=250,
                        read_only=False):
        self.builder.set_text(text)
        self.builder.set_placeholder(placeholder)
        self.builder.set_width(width)
        self.builder.set_read_only(read_only)
        return self.builder.get_result()

    def build_combo_box(self, items=(), current_index=0, width=250,
                        enabled=True):
        self.builder.set_items(list(items))
        self.builder.set_current_index(current_index)
        self.builder.set_width(width)
        self.builder.set_enabled(enabled)
        return self.builder.get_result()

    def build_check_box(self, text="", checked=False, enabled=True):
        self.builder.set_text(text)
        self.builder.set_checked(checked)
        self.builder.set_enabled(enabled)
        return self.builder.get_result()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Builder паттерні")
        self.resize(400, 600)
        layout = QVBoxLayout(self)

        self.status = QLabel("Виджеттермен әрекет жасап көріңіз")
        layout.addWidget(self.status)

        director = WidgetDirector()

        director.set_builder(ButtonBuilder())
        btn_active = director.build_button("Белсенді", 150, 40, "green", True)
        btn_disabled = director.build_button("Белсенді емес", 150, 40, "red", False)
        btn_active.clicked.connect(lambda: self.status.setText("Батырма басылды"))
        layout.addWidget(self._group("QPushButton", btn_active, btn_disabled))

        director.set_builder(LineEditBuilder())
        edit_normal = director.build_line_edit("", "Атыңызды енгізіңіз", 250, False)
        edit_readonly = director.build_line_edit("Тек оқуға арналған", "", 250, True)
        edit_normal.textChanged.connect(
            lambda t: self.status.setText(f"Енгізілген мәтін: {t}"))
        layout.addWidget(self._group("QLineEdit", edit_normal, edit_readonly))

        director.set_builder(ComboBoxBuilder())
        combo_active = director.build_combo_box(
            ["Алматы", "Астана", "Қарағанды"], 2, 250, True)
        combo_disabled = director.build_combo_box(
            ["Бірінші", "Екінші"], 0, 250, False)
        combo_active.currentTextChanged.connect(
            lambda t: self.status.setText(f"Таңдалды: {t}"))
        layout.addWidget(self._group("QComboBox", combo_active, combo_disabled))

        director.set_builder(CheckBoxBuilder())
        check_on = director.build_check_box("Келісемін", True, True)
        check_disabled = director.build_check_box("Қолжетімсіз опция", False, False)
        check_on.toggled.connect(
            lambda c: self.status.setText(f"Белгі: {'қосулы' if c else 'өшірулі'}"))
        layout.addWidget(self._group("QCheckBox", check_on, check_disabled))

    @staticmethod
    def _group(title, *widgets):
        box = QGroupBox(title)
        box_layout = QVBoxLayout(box)
        for w in widgets:
            box_layout.addWidget(w)
        return box

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
