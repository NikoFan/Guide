from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem)





class FlowContainer(QListWidget):
    def __init__(self):
        super().__init__()
        self.setFlow(self.Flow.LeftToRight)
        self.setMinimumWidth(100)

        self.setWrapping(True)
        self.setMovement(self.Movement.Static)
        self.setResizeMode(self.ResizeMode.Adjust)

        self.setHorizontalScrollMode(self.ScrollMode.ScrollPerPixel)
        self.setVerticalScrollMode(self.ScrollMode.ScrollPerPixel)
        self.setSpacing(50)



    def create_item(self):
        return QListWidgetItem()
