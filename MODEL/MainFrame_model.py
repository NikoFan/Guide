import os

from PySide6.QtWidgets import QWidget

class MainFrameModel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent

    def open_dir(self, path: str):
        self._parent.change_dir(path)



    def open_file(self, path="/"):
        sender = self.sender()
        print(sender.accessibleName())
        print("open", path)

    def get_files(self, path):
        # ls -l | awk '{print $9} {print $1}'

        keys = os.popen("cd "+path+" && ls -l | awk '{print $1}'").read().split('\n')
        files = os.popen("cd "+path+""" && ls -l | awk '{for (i = 9; i <= NF; i++) {printf "%s ", $i}; printf "\\n"}'""").read().split('\n')
        objects_data: list = []
        for index in range(1, len(keys[1:])):
            data: dict = {}
            if keys[index][0] == 'd':
                # Это папка
                data['text'] = files[index]
                data['type'] = 'dir'
                data['icon'] = '/home/spirit2/Desktop/pyside6_project/VIEW/icons/dir.png'
            else:
                # Это файл
                data['text'] = files[index]
                data['type'] = 'file'
                data['icon'] = '/home/spirit2/Desktop/pyside6_project/VIEW/icons/file.png'

            objects_data.append(data)
        return objects_data


