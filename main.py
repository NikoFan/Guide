from PySide6.QtWidgets import (
    QApplication,
    QMainWindow)
from PySide6.QtCore import QSize
import sys
import os

from VIEW import MainFrame
from VIEW_MODEL import MainFrame_viewModel

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(QSize(800, 600))
        self.setMinimumSize(QSize(500, 400))

        self.user_name: str = self.take_current_user_name()

        # Объявление Представления и Посредника
        main_frame_view_model = MainFrame_viewModel.MainFrameViewModel(parent=self)
        main_frame_view = MainFrame.MainFrame(path=f"/home/{self.user_name}/Desktop/",
                                              model=main_frame_view_model.model(),
                                              user_name=self.user_name)


        self.setCentralWidget(main_frame_view)

    def take_current_user_name(self):
        '''
        Получение имени пользователя, для создания абсолютного пути
        :return: str()
        '''
        return os.popen('cd /home/ && ls').read().replace('\n', '')

    def change_dir(self, path: str):
        '''
        Функция смены папки
        :param terminal_text: Стартовый текст в теримнале
        :param path: Путь до папки
        :return: None
        '''

        main_frame_view_model = MainFrame_viewModel.MainFrameViewModel(parent=self)
        main_frame_view = MainFrame.MainFrame(path=path,
                                              model=main_frame_view_model.model(),
                                              user_name=self.user_name)

        self.setCentralWidget(main_frame_view)



styles = """
QScrollArea {
background: #f0f0f0;
color: #000000;
}

#asdas {
background: 'red';
}


QTextEdit {
background: #000000;
font-style: Ubuntu;
font-size: 18px;
}
"""

if __name__ == "__main__":
    application = QApplication(sys.argv)
    application.setStyleSheet(styles)

    main = Main()
    main.show()

    sys.exit(application.exec())




