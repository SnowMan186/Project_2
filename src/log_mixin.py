class LogMixin:
    def __init__(self, *args, **kwargs):
        print(f"Создание объекта {type(self).__name__}")
        super().__init__(*args, **kwargs)

    def __repr__(self):
        attrs = ', '.join(f'{key}={value}' for key, value in vars(self).items())
        return f"<{type(self).__name__}({attrs})>"
