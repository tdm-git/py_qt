"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только
последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
"""
from ipaddress import ip_address
from task_1 import host_ping


def host_range_ping():

    start_ip = input('Введите первоначальный адрес: ')
    try:
        las_octet = int(start_ip.split('.')[3])
    except Exception as e:
        print(e)

    kol_ip = input('Сколько адресов проверить?: ')
    if not kol_ip.isnumeric():
        print('Необходимо ввести число: ')
    else:
        if (las_octet+int(kol_ip)) > 254:
            print(f"максимальное число хостов для проверки, не более: {254-las_octet}")

    host_list = [str(ip_address(start_ip)+i) for i in range(int(kol_ip))]
    return host_ping(host_list)


if __name__== "__main__":
    host_range_ping()
