class Stack:
    stack: list = []

    @staticmethod
    def push(path: str):
        ''' Добавить элемент '''
        Stack.stack.append(path)

    @staticmethod
    def pop():
        ''' Удаление последнего добавленного пути '''
        if len(Stack.stack) == 1:
            return Stack.stack[0]
        Stack.stack.pop()
        return Stack.stack[-1]

    @staticmethod
    def get_path():
        return Stack.stack[-1]