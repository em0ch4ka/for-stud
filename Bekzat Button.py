
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QCheckBox,
    QVBoxLayout,
    QMessageBox
)


class ButtonBuilder:
    def build(self, text="Кнопка", width=150, height=40,
              color="lightblue", enabled=True, parent=None):
        button = QPushButton(text, parent)
        button.setFixedSize(width, height)
        button.setStyleSheet(
            f"background-color: {color}; border-radius: 6px;"
        )
        button.setEnabled(enabled)
        return button


class LineEditBuilder:
    def build(self, text="", placeholder="Введите текст",
              width=200, read_only=False, parent=None):
        field = QLineEdit(parent)
        field.setText(text)
        field.setPlaceholderText(placeholder)
        field.setFixedWidth(width)
        field.setReadOnly(read_only)
        return field


class ComboBoxBuilder:
    def build(self, items=None, current_index=0,
              width=200, enabled=True, parent=None):
        combo = QComboBox(parent)
        combo.addItems(items or [])
        combo.setFixedWidth(width)
        combo.setEnabled(enabled)

        if combo.count() > 0:
            index = max(0, min(current_index, combo.count() - 1))
            combo.setCurrentIndex(index)

        return combo


class CheckBoxBuilder:
    def build(self, text="Выбрать", checked=False,
              enabled=True, parent=None):
        checkbox = QCheckBox(text, parent)
        checkbox.setChecked(checked)
        checkbox.setEnabled(enabled)
        return checkbox


class WidgetDirector:
    def __init__(self, builder):
        self.builder = builder

    def create_widget(self, **params):
        return self.builder.build(**params)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Builder Pattern - PyQt6")
        self.resize(400, 420)

        layout = QVBoxLayout(self)

        title = QLabel("Создание виджетов через Builder")
        layout.addWidget(title)

        self.button_builder = ButtonBuilder()
        self.input_builder = LineEditBuilder()
        self.combo_builder = ComboBoxBuilder()
        self.checkbox_builder = CheckBoxBuilder()

        self.button_director = WidgetDirector(self.button_builder)
        self.input_director = WidgetDirector(self.input_builder)
        self.combo_director = WidgetDirector(self.combo_builder)
        self.checkbox_director = WidgetDirector(self.checkbox_builder)

        self.name_input = self.input_director.create_widget(
            text="",
            placeholder="Введите имя",
            width=300,
            parent=self
        )
        layout.addWidget(self.name_input)

        self.combo = self.combo_director.create_widget(
            items=["Python", "Java", "C++"],
            current_index=0,
            width=300,
            parent=self
        )
        layout.addWidget(self.combo)

        self.checkbox = self.checkbox_director.create_widget(
            text="Я согласен с условиями",
            checked=False,
            parent=self
        )
        layout.addWidget(self.checkbox)

        self.button = self.button_director.create_widget(
            text="Показать результат",
            width=200,
            height=40,
            color="lightgreen",
            parent=self
        )
        layout.addWidget(self.button)

        self.button.clicked.connect(self.show_result)

    def show_result(self):
        name = self.name_input.text().strip()
        language = self.combo.currentText()
        agreed = self.checkbox.isChecked()

        if not name:
            QMessageBox.warning(
                self, "Ошибка", "Введите своё имя!"
            )
            return

        QMessageBox.information(
            self,
            "Результат",
            f"Имя: {name}\n"
            f"Язык программирования: {language}\n"
            f"Согласие: {'Да' if agreed else 'Нет'}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
