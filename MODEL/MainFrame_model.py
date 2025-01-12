import os

from PySide6.QtWidgets import QWidget
from MODEL import Stack


class MainFrameModel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent

    def open_dir(self):
        ''' Открытие дирректории '''
        self._parent.change_dir(Stack.Stack.get_path())

    def open_file(self, file_path: str):
        '''
        Открытие файла
        :param file_path: Путь до файла
        :return: None
        '''
        try:
            os.system(f"""cd {"/".join(file_path.split("/")[:-1])} && open ./{file_path.split("/")[-1]}""")
        except Exception:
            pass

    def open_dir_from_side_btn(self, path: str):
        ''' Открытие папки по кнопке на левой панели'''
        # Пересоздание стека
        Stack.Stack.stack = []

        # Добавление первого пути
        Stack.Stack.push(path.strip())
        self.open_dir()

    def open_back_dir(self):
        ''' Возврат к прошлой директории '''
        Stack.Stack.pop()
        self.open_dir()

    def detect_object_type(self):
        ''' Определение типа объекта Файл / Папка'''
        sender = self.sender()
        print(sender.accessibleName())
        path = "".join(str(sender.accessibleName()).split(";")[1])
        chosen_object_type = "".join(str(sender.accessibleName()).split(";")[0])

        # Проверка типа
        if chosen_object_type == "dir":
            # Если объект - Папка
            Stack.Stack.push(path.strip())
            self.open_dir()
        else:
            # Если объект - Файл
            self.open_file(path)


    def change_theme(self):
        ''' Отправка команды на смену темы '''
        self._parent.change_app_theme()

    def get_files(self, path):
        ''' Получение списка всех Объектов в директории '''
        # Получение ключей
        print("!!", path)
        keys = os.popen("cd " + path + " && ls -l | awk '{print $1}'").read().split('\n')

        # Получение имен
        files = os.popen(
            "cd " + path + """ && ls -l | awk '{for (i = 9; i <= NF; i++) {printf "%s ", $i}; printf "\\n"}'""").read().split(
            '\n')
        objects_data: list = []
        for index in range(1, len(keys[1:])):
            data: dict = {}
            if keys[index][0] == 'd':
                # Это папка
                data['text'] = f"'{files[index].strip()}'"
                data['type'] = 'dir'
                data['icon'] = f'{"/".join(path.split("/")[:3])}/Desktop/pyside6_project/VIEW/icons/dir.png'
            else:
                # Это файл
                data['text'] = f"'{files[index].strip()}'"
                data['type'] = 'file'
                data["format"] = files[index].strip().split(".")[-1]
                if len(files[index].strip().split(".")) == 2:

                    data['icon'] = f'{"/".join(path.split("/")[:3])}/Desktop/pyside6_project/VIEW/icons/{files[index].strip().split(".")[-1]}_icon.png'

                    # Проверка, что для указанного разрешения - существует иконка
                    is_icon_empty = os.popen(f'find {"/".join(path.split("/")[:3])}/Desktop/pyside6_project/VIEW/icons/{files[index].strip().split(".")[-1]}_icon.png').read()
                    if len(is_icon_empty) == 0:
                        # Если иконка не существует - Вставляется базовая
                        data['icon'] = f'{"/".join(path.split("/")[:3])}/Desktop/pyside6_project/VIEW/icons/_icon.png'
                else:
                    # Если файл не имеет разрешения - Вставляется базовая иконка
                    data['icon'] = f'{"/".join(path.split("/")[:3])}/Desktop/pyside6_project/VIEW/icons/_icon.png'

            objects_data.append(data)
        return objects_data
