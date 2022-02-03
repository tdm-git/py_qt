"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""
from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(ip_addreses, timeout=100, requests=1):
    results = {
        'Узел доступен': "",
        'Узел недоступен': ""
    }
    for ip_addres in ip_addreses:
        try:
            ip_addres = ip_address(ip_addres)
        except ValueError:
            pass
        proc = Popen(f"ping {ip_addres} -w {timeout} -n {requests}", shell=False, stdout=PIPE)
        proc.wait()

        key = 'Узел доступен'  if (proc.returncode == 0) else 'Узел недоступен'
        results[key] += f'{str(ip_addres)}\n'
        res_string = f'{ip_addres} - {key}'
        print(res_string)
    # print(results)
    return results


if __name__ == '__main__':
    list_ip = ['yandex.ru', 'mail.ru', '10.0.0.1']
    host_ping(list_ip)
