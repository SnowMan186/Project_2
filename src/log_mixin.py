import logging

class LogMixin:
    def __init__(self, *args, **kwargs):
        logger = logging.getLogger('local')  # Назначаем корневой логгер
        logger.setLevel(logging.INFO)  # Уровень логирования
        ch = logging.StreamHandler()  # Обработчик для вывода в консоль
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)  # Привязываем обработчик к логгеру
        logger.info(f'Создание объекта класса {type(self).__name__}: args={args}, kwargs={kwargs}')
        super().__init__(*args, **kwargs)
