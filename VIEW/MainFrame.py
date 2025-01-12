from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget)

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap

from VIEW.widgets_dir import ListWidget, Toggle


class MainFrame(QFrame):
    def __init__(self, model, path="/", parent=None, user_name=None):
        super().__init__(parent)
        self._model = model
        self._path = path
        self._user_name = user_name
        self.theme_bool = parent.theme_bool

        # Создание разметки
        self.frame_layout = QHBoxLayout(self)
        self.frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.fill_frame()

    def fill_frame(self):
        '''
        Функция заполнения фрейма виджетами
        :return: None
        '''

        # LEFT SIDE
        left_side = QWidget()
        left_side.setMinimumWidth(200)
        self.left_vertical_side_vbox = QVBoxLayout(left_side)
        self.left_vertical_side_vbox.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Fill
        self.fill_left_widget()
        left_side.setFixedHeight(self.left_vertical_side_vbox.count() * 55)
        left_side.setFixedWidth(250)

        self.frame_layout.addWidget(left_side)

        # CENTRAL SIDE
        central_side = QWidget()
        self.central_side_vbox = QVBoxLayout(central_side)
        self.fill_central_widget()

        self.frame_layout.addWidget(central_side)

    def fill_central_widget(self):
        '''
        Функция заполнения центрального виджета
        :return: None
        '''

        adaptive_view = ListWidget.FlowContainer()
        self.central_side_vbox.addWidget(adaptive_view)

        for data in self._model.get_files(self._path):
            # Создание элемента списка
            item = adaptive_view.create_item()

            # Создание области для хранения объектов
            object_button = QPushButton()
            object_button.setObjectName("object_button")
            object_button.setFixedSize(QSize(100, 100))
            object_button.setAccessibleName(data["type"] + ";" + self._path + "/" + data["text"])
            object_button.clicked.connect(
                self._model.detect_object_type
            )

            # Создание лейбла под фото
            file_icon = QLabel()
            file_icon.setPixmap(QPixmap(data['icon']))
            file_icon.setScaledContents(True)
            file_icon.setFixedSize(52, 52)

            # Создание горизонтальной разметки, чтобы центровать фото
            icon_hbox = QHBoxLayout()
            icon_hbox.addWidget(QWidget())
            icon_hbox.addWidget(file_icon)
            icon_hbox.addWidget(QWidget())

            # Создание виджета с названием
            file_name = QLabel(data["text"][:8] + "...")
            file_name.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)

            # Добавление виджетов в разметку
            layout = QVBoxLayout(object_button)
            layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addLayout(icon_hbox)
            layout.addWidget(file_name)

            # Добавление элемента в общий список
            adaptive_view.addItem(item)
            item.setSizeHint(object_button.sizeHint())
            adaptive_view.setItemWidget(item, object_button)

        back_btn = QPushButton("Прошлая папка")
        back_btn.setFixedHeight(30)
        back_btn.setObjectName("back_btn")
        back_btn.clicked.connect(
            lambda: self._model.open_back_dir()
        )

        self.central_side_vbox.addWidget(QLabel(self._path, objectName="currentPath"))
        self.central_side_vbox.addWidget(back_btn)

    def fill_left_widget(self):
        '''
        Заполнение вертикальной левой области виджетами
        :return: None
        '''

        def create_btn_pattern(data: dict):
            '''
            Паттерн создания кнопки для левой области
            :param text: Текст в кнопке
            :param name: Имя кнопки
            :return: QPushButton()
            '''
            btn = QPushButton()
            btn.setText(data["text"])
            btn.setObjectName("left_side_btn")
            btn.setFixedHeight(40)
            btn.clicked.connect(
                lambda: (self._model.open_dir_from_side_btn(data["_path"])))
            return btn

        buttons_data = [
            {"text": "Desktop",
             "_path": ""f'/home/{self._user_name}/Desktop'},
            {"text": "Documents",
             "_path": ""f'/home/{self._user_name}/Documents'},
            {"text": "Downloads",
             "_path": ""f'/home/{self._user_name}/Downloads'},
            {"text": "Music",
             "_path": ""f'/home/{self._user_name}/Music'},
            {"text": "Pictures",
             "_path": ""f'/home/{self._user_name}/Pictures'},
            {"text": "Videos",
             "_path": ""f'/home/{self._user_name}/Videos'},
            {"text": "Trash",
             "_path": ""f'/home/{self._user_name}/Trash'},
        ]

        self.left_vertical_side_vbox.addWidget(QLabel("Переключить тему", objectName="theme_change_label"))

        # Создание переключателя для темы
        toggle = Toggle.Toggle().return_toggle()
        if not self.theme_bool:  # Если до этого тема была изменена - Оставить тумблер на месте
            toggle.setChecked(True)

        # Считывание переключения тумблера
        toggle.stateChanged.connect(self._model.change_theme)
        self.left_vertical_side_vbox.addWidget(toggle)  # Добавление тумблера на экран

        # Создание кнопок левой панели
        for button_data in buttons_data:
            self.left_vertical_side_vbox.addWidget(create_btn_pattern(button_data))
