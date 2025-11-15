class LogMixin:
    def __init__(self, *args, **kwargs):
        print(f'Создание объекта класса {type(self).__name__}: args={args}, kwargs={kwargs}')
        super().__init__(*args, **kwargs)
