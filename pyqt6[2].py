import sys
from abc import ABC, abstractmethod

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSpinBox,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
    QFormLayout,
)



class WidgetBuilder(ABC):
    """Барлық Builder-лер үшін ортақ интерфейс."""

    def __init__(self):
        self._widget = None
        self.reset()

    @abstractmethod
    def reset(self):
        """Жаңа виджет құруға дайындау."""

    def get_result(self) -> QWidget:
        """Дайын виджетті қайтарады және builder-ді тазалайды."""
        widget = self._widget
        self.reset()
        return widget


class ButtonBuilder(WidgetBuilder):
    """Тек QPushButton құрады."""

    def reset(self):
        self._widget = QPushButton()

    def set_text(self, text: str):
        self._widget.setText(text)
        return self

    def set_size(self, width: int, height: int):
        if width > 0:
            self._widget.setFixedWidth(width)
        if height > 0:
            self._widget.setFixedHeight(height)
        return self

    def set_color(self, color: str):
        self._widget.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                border-radius: 6px;
                font-weight: bold;
            }}
            QPushButton:disabled {{ background-color: #aaaaaa; }}
            QPushButton:hover:enabled {{ border: 2px solid #333333; }}
            """
        )
        return self

    def set_enabled(self, enabled: bool):
        self._widget.setEnabled(enabled)
        return self


class LineEditBuilder(WidgetBuilder):
    """Тек QLineEdit құрады."""

    def reset(self):
        self._widget = QLineEdit()

    def set_text(self, text: str):
        self._widget.setText(text)
        return self

    def set_placeholder(self, placeholder: str):
        self._widget.setPlaceholderText(placeholder)
        return self

    def set_width(self, width: int):
        if width > 0:
            self._widget.setFixedWidth(width)
        return self

    def set_read_only(self, read_only: bool):
        self._widget.setReadOnly(read_only)
        return self


class ComboBoxBuilder(WidgetBuilder):
    """Тек QComboBox құрады."""

    def reset(self):
        self._widget = QComboBox()

    def set_items(self, items: list[str]):
        self._widget.addItems(items)
        return self

    def set_current_index(self, index: int):
        count = self._widget.count()
        if count:
            self._widget.setCurrentIndex(max(0, min(index, count - 1)))
        return self

    def set_width(self, width: int):
        if width > 0:
            self._widget.setFixedWidth(width)
        return self

    def set_enabled(self, enabled: bool):
        self._widget.setEnabled(enabled)
        return self


class CheckBoxBuilder(WidgetBuilder):
    """Тек QCheckBox құрады."""

    def reset(self):
        self._widget = QCheckBox()

    def set_text(self, text: str):
        self._widget.setText(text)
        return self

    def set_checked(self, checked: bool):
        self._widget.setChecked(checked)
        return self

    def set_enabled(self, enabled: bool):
        self._widget.setEnabled(enabled)
        return self


class WidgetDirector:
    """
    Builder-ді қабылдап, оған параметрлерді береді және
    құру процесін басқарады. Виджеттің ішкі құрылымын
    білмейді: тек Builder әдістерін шақырады.
    """

    def __init__(self, builder: WidgetBuilder | None = None):
        self._builder = builder

    def set_builder(self, builder: WidgetBuilder):
        self._builder = builder

    def _require_builder(self) -> WidgetBuilder:
        if self._builder is None:
            raise RuntimeError("Builder берілмеген. set_builder() шақырыңыз.")
        return self._builder

    def construct_button(self, text, width, height, color, enabled=True):
        b = self._require_builder()
        b.reset()
        b.set_text(text).set_size(width, height).set_color(color).set_enabled(enabled)
        return b.get_result()

    def construct_line_edit(self, text, placeholder, width, read_only=False):
        b = self._require_builder()
        b.reset()
        b.set_text(text).set_placeholder(placeholder).set_width(width).set_read_only(
            read_only
        )
        return b.get_result()

    def construct_combo_box(self, items, current_index, width, enabled=True):
        b = self._require_builder()
        b.reset()
        b.set_items(items).set_current_index(current_index).set_width(
            width
        ).set_enabled(enabled)
        return b.get_result()

    def construct_check_box(self, text, checked=False, enabled=True):
        b = self._require_builder()
        b.reset()
        b.set_text(text).set_checked(checked).set_enabled(enabled)
        return b.get_result()




COLORS = {
    "Жасыл": "green",
    "Қызыл": "crimson",
    "Көк": "royalblue",
    "Сары": "darkorange",
    "Күлгін": "purple",
    "Сұр": "gray",
}


def make_spin(maximum, value, special="Авто"):
    spin = QSpinBox()
    spin.setRange(0, maximum)
    spin.setValue(value)
    spin.setSpecialValueText(special)
    return spin


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Builder + Director — PyQt6")
        self.resize(560, 620)


        self.button_builder = ButtonBuilder()
        self.line_edit_builder = LineEditBuilder()
        self.combo_builder = ComboBoxBuilder()
        self.check_builder = CheckBoxBuilder()
        self.director = WidgetDirector()

        self._init_ui()

    def _init_ui(self):
        root = QVBoxLayout(self)

        settings = QGroupBox("Виджет параметрлері")
        s_layout = QVBoxLayout(settings)

        self.type_combo = QComboBox()
        self.type_combo.addItems(
            ["Батырма (QPushButton)", "Енгізу өрісі (QLineEdit)",
             "Ашылмалы тізім (QComboBox)", "Белгілеу өрісі (QCheckBox)"]
        )
        s_layout.addWidget(QLabel("Виджет түрі:"))
        s_layout.addWidget(self.type_combo)

        self.stack = QStackedWidget()
        self.stack.addWidget(self._build_button_form())
        self.stack.addWidget(self._build_line_edit_form())
        self.stack.addWidget(self._build_combo_form())
        self.stack.addWidget(self._build_check_form())
        s_layout.addWidget(self.stack)
        self.type_combo.currentIndexChanged.connect(self.stack.setCurrentIndex)

        buttons = QHBoxLayout()
        create_btn = QPushButton("Виджет жасау")
        create_btn.clicked.connect(self.create_widget)
        clear_btn = QPushButton("Тазалау")
        clear_btn.clicked.connect(self.clear_widgets)
        buttons.addWidget(create_btn)
        buttons.addWidget(clear_btn)
        s_layout.addLayout(buttons)

        root.addWidget(settings)

        # Жасалған виджеттер аймағы
        root.addWidget(QLabel("Жасалған виджеттер:"))
        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.container)
        root.addWidget(scroll, stretch=1)

    def _build_button_form(self):
        page = QWidget()
        form = QFormLayout(page)
        self.btn_text = QLineEdit("Батырма")
        self.btn_width = make_spin(400, 150)
        self.btn_height = make_spin(150, 40)
        self.btn_color = QComboBox()
        self.btn_color.addItems(COLORS.keys())
        self.btn_enabled = QCheckBox("Белсенді")
        self.btn_enabled.setChecked(True)
        form.addRow("Мәтін:", self.btn_text)
        form.addRow("Ені:", self.btn_width)
        form.addRow("Биіктігі:", self.btn_height)
        form.addRow("Түс:", self.btn_color)
        form.addRow("", self.btn_enabled)
        return page

    def _build_line_edit_form(self):
        page = QWidget()
        form = QFormLayout(page)
        self.le_text = QLineEdit()
        self.le_placeholder = QLineEdit("Мәтін енгізіңіз")
        self.le_width = make_spin(500, 250)
        self.le_read_only = QCheckBox("Тек оқуға арналған")
        form.addRow("Бастапқы мәтін:", self.le_text)
        form.addRow("Placeholder:", self.le_placeholder)
        form.addRow("Ені:", self.le_width)
        form.addRow("", self.le_read_only)
        return page

    def _build_combo_form(self):
        page = QWidget()
        form = QFormLayout(page)
        self.cb_items = QLineEdit("Алма, Алмұрт, Шие")
        self.cb_items.setPlaceholderText("Элементтерді үтірмен бөліңіз")
        self.cb_index = make_spin(50, 0, special="")
        self.cb_index.setSpecialValueText("")
        self.cb_width = make_spin(500, 200)
        self.cb_enabled = QCheckBox("Белсенді")
        self.cb_enabled.setChecked(True)
        form.addRow("Элементтер:", self.cb_items)
        form.addRow("Таңдалған индекс:", self.cb_index)
        form.addRow("Ені:", self.cb_width)
        form.addRow("", self.cb_enabled)
        return page

    def _build_check_form(self):
        page = QWidget()
        form = QFormLayout(page)
        self.ch_text = QLineEdit("Келісемін")
        self.ch_checked = QCheckBox("Белгіленген болсын")
        self.ch_enabled = QCheckBox("Белсенді")
        self.ch_enabled.setChecked(True)
        form.addRow("Мәтін:", self.ch_text)
        form.addRow("", self.ch_checked)
        form.addRow("", self.ch_enabled)
        return page

    def create_widget(self):
        index = self.type_combo.currentIndex()

        if index == 0:
            self.director.set_builder(self.button_builder)
            widget = self.director.construct_button(
                text=self.btn_text.text() or "Батырма",
                width=self.btn_width.value(),
                height=self.btn_height.value(),
                color=COLORS[self.btn_color.currentText()],
                enabled=self.btn_enabled.isChecked(),
            )

        elif index == 1:
            self.director.set_builder(self.line_edit_builder)
            widget = self.director.construct_line_edit(
                text=self.le_text.text(),
                placeholder=self.le_placeholder.text(),
                width=self.le_width.value(),
                read_only=self.le_read_only.isChecked(),
            )

        elif index == 2:
            items = [i.strip() for i in self.cb_items.text().split(",") if i.strip()]
            if not items:
                items = ["Элемент 1", "Элемент 2", "Элемент 3"]
            self.director.set_builder(self.combo_builder)
            widget = self.director.construct_combo_box(
                items=items,
                current_index=self.cb_index.value(),
                width=self.cb_width.value(),
                enabled=self.cb_enabled.isChecked(),
            )

        else:
            self.director.set_builder(self.check_builder)
            widget = self.director.construct_check_box(
                text=self.ch_text.text() or "Белгі",
                checked=self.ch_checked.isChecked(),
                enabled=self.ch_enabled.isChecked(),
            )

        self.container_layout.addWidget(widget)

    def clear_widgets(self):
        while self.container_layout.count():
            item = self.container_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())