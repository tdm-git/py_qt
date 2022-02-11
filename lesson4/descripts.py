import logging
import re

logger = logging.getLogger('server')

class Port:
    def __set__(self, instance, value):
        if not 1023 < value < 65536:
            logger.critical(
                f'Попытка запуска сервера с указанием неподходящего порта {value}. Допустимы адреса с 1024 до 65535.')
            exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

# class IpAddress:
#     def __set__(self, instance, value):
#         # match = re.fullmatch(r'\d+\.\d+\.\d+\.\d+', value)
#         # if not bool(match):
#         #     logger.critical(f'IP адрес не прошел валидацию - {value}. ')
#         #     exit(1)
#         instance.__dict__[self.name] = value
