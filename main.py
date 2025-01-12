from PySide6.QtWidgets import (
    QApplication,
    QMainWindow)
from PySide6.QtCore import QSize
import sys
import os

from VIEW import MainFrame
from VIEW_MODEL import MainFrame_viewModel
from MODEL import Stack
import styles


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(QSize(800, 600))
        self.setMinimumSize(QSize(500, 400))

        self.user_name: str = self.take_current_user_name()
        Stack.Stack.push(f"/home/{self.user_name}/Desktop")

        # Объявление Представления и Посредника
        self.theme_bool = True
        main_frame_view_model = MainFrame_viewModel.MainFrameViewModel(parent=self)
        main_frame_view = MainFrame.MainFrame(path=f"/home/{self.user_name}/Desktop",
                                              model=main_frame_view_model.model(),
                                              parent=self,
                                              user_name=self.user_name)

        self.setStyleSheet(styles.styles_dict["light"])
        self.setCentralWidget(main_frame_view)

    def change_app_theme(self):
        ''' Смена темы '''
        if self.theme_bool:
            self.setStyleSheet(styles.styles_dict["dark"])
            self.theme_bool = False
            return
        self.setStyleSheet(styles.styles_dict["light"])
        self.theme_bool = True
        return

    def take_current_user_name(self):
        '''
        Получение имени пользователя, для создания абсолютного пути
        :return: str()
        '''
        return os.popen('cd /home/ && ls').read().replace('\n', '')

    def change_dir(self, path: str):
        '''
        Функция смены папки
        :param path: Путь до папки
        :return: None
        '''

        print("stack:", Stack.Stack.get_path())

        main_frame_view_model = MainFrame_viewModel.MainFrameViewModel(parent=self)
        main_frame_view = MainFrame.MainFrame(path=path,
                                              parent=self,
                                              model=main_frame_view_model.model(),
                                              user_name=self.user_name)

        self.setCentralWidget(main_frame_view)


if __name__ == "__main__":
    application = QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(application.exec())
