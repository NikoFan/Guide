

from PySide6.QtCore import QObject


from MODEL import MainFrame_model

class MainFrameViewModel(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._model = MainFrame_model.MainFrameModel(parent=parent)


    def model(self):
        return self._model