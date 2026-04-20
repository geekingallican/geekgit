import time, requests, os, sys, re, platform, cpuinfo, GPUtil, subprocess, platform, base64, tldextract # type: ignore
from colorama import init, Fore 
from ping3 import ping
init()
green, red, yellow, purple, cyan, rest = Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.RESET
found = False
file_path = os.path.dirname(os.path.abspath(__file__))
conf_path = os.path.join(file_path, "Config.txt")
white_path = os.path.dirname(os.path.abspath(__file__))
white_list_path = os.path.join(file_path, "white_list.txt")

def writer(text, color, speed):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    sys.stdout.write(rest)

def clear():
    os.system('cls')

def animated(text, durantion=3):
    start_time = time.time()
    while time.time() - start_time < durantion:
        for dots in range(5):
            sys.stdout.write(f"\r{text}{'.' * dots} ")
            sys.stdout.flush()
            time.sleep(0.4)

def conf():
    if os.path.exists(conf_path):
        writer('Файл конфигурации найден', green, 0.5)
    else:
        writer('Файл конфигурации не был найден, давай пройдем первичную настройку', red, 0.5)
        time.sleep(1)
        username = input('\nВведи свой никнейм ')
        password = input('Введи свой пароль ')
        with open(conf_path, 'w', encoding="utf-8") as file:
            file.write(username + '\n' + password)
    time.sleep(1)
    with open(conf_path, 'r', encoding="utf-8") as file:
        content = file.read().split()
        login = content[0].strip()
    writer(f'\nДобро пожаловать, {login}!\n', yellow, 1)

def white_list():
    with open(white_list_path, 'a', encoding="utf-8") as file:
        pass
    found = False
    animated('Проверка IP адреса в white_lixt.txt')
    ip = requests.get('https://api.ipify.org').text.strip() 
    with open(white_list_path, 'r', encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if clean_line == ip:
                found = True
                break
    if found == True:
        time.sleep(1)
        writer('\nIP В белом списке.........Вход разрешен', green, 2)
    else:
        time.sleep(1)
        writer('\nСовпадений нет, пропускаю...', red, 0.5)
        check_pswrd = input('\nВведите пароль ')
        with open(conf_path, 'r', encoding="utf-8") as file:
            content = file.read().split()
            usr_paswrd = content[1].strip()
            while check_pswrd not in usr_paswrd:
                if check_pswrd != usr_paswrd:
                    writer('Неверный пароль', red, 0.5)
                    check_pswrd = input('\nПопробуйте еще раз ')
            writer('Успешный вход!', green, 2)
            time.sleep(1)

def main_menu():
    with open(conf_path, 'r', encoding="utf-8") as file:
        content = file.read().split()
        login = content[0].strip()
    writer(f'Добро пожаловать, {login}!\n', green, 1)
    writer('FSOC v0.1', purple, 0.1)
    writer('\nMAIN MENU',yellow, 0.1)
    writer('\n1. Network tools',yellow, 0.1)
    writer('\n2. Crypto & Hash tools',yellow, 0.1)
    writer('\n3. Brute Force',yellow, 0.1)
    writer('\n4. Anonymity',yellow, 0.1)
    writer('\n5. System Info',yellow, 0.1)
    writer('\n6. Settings',yellow, 0.1)
    writer('\n0. Exit', yellow, 0.1)
def hash_ident():
    cont = ''
    while cont != "нет":
        h = input(f"\n{cyan}Введите хеш.. {rest}").strip()
        if len(h) == 32:
            writer('\nType: MD5', green, 0.5)
        elif len(h) == 40:
            writer('\nType: SHA-1', green, 0.5)
        elif len(h) == 64:
            writer('\nType: SHA-256', green, 0.5)
        elif len(h) == 56:
            writer('\nType: SHA3-224', green, 0.5)
        elif len(h) == 96:
            writer('\nType: SHA3-384', green, 0.5)
        elif len(h) == 128:
            writer('\nType: SHA3-512', green, 0.5)
        elif len(h) == 60:
            writer('\nType: bcrypt', green, 0.5)
        elif len(h) == 64:
            writer('\nType: SHA-256', green, 0.5)
        else:
            writer('\nUnknow hash type', red, 0.5)
        cont = input(f"\n{purple}Хотите проверить еще один хеш? ")
        if cont.lower() == "нет":
            break
def system_info():
    writer("\n--- SYSTEM INFO ---", green, 0.5)
    with open(conf_path, 'r', encoding="utf-8") as file:
        content = file.read().split()
        login = content[0].strip()
    print(f'\n{yellow}Login: {login}')
    print(f'{yellow}OS: {platform.system()} {platform.release()}')
    print(f"{yellow}Ip: {requests.get('https://api.ipify.org').text}")
    cpu_name = cpuinfo.get_cpu_info()['brand_raw']
    print(f"{yellow}Процессор: {cpu_name}")
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        print(f"{yellow}Видеокарта: {gpu.name}")
        print(f"{yellow}Память: {gpu.memoryTotal}MB {rest}")
    input(f'{cyan}Нажмите Enter для возврата...')


def settings():
    writer('\n1. Изменить параметры Config.txt', yellow, 0.5)
    writer('\n2. Настройка white_list', yellow, 0.5)
    Schoise = input(f"\n{cyan}Выбери пункт меню, или нажмите Enter, что бы вернуться.. {rest}")
    if Schoise == "1":
        username = input(f'\n{purple}Введи свой никнейм ')
        password = input(f'\n{purple}Введи свой пароль {rest}')
        with open(conf_path, 'w', encoding="utf-8") as file:
            file.write(username + '\n' + password)
    elif Schoise == '2':
        os.system('cls')
        writer("1. Очистить файл", yellow, 0.5)
        writer("\n2. Добавить IP в файл", yellow, 0.5)
        writer("\n3. Изменить IP", yellow, 0.5)
        IPchoise = input(f"\n{cyan}Выбери пункт меню, или нажмите Enter, что бы вернуться.. {rest}")
        if IPchoise == '1':
            with open(white_list_path, 'w', encoding="utf-8") as file:
                pass
        elif IPchoise == '2':
            os.system('cls')
            newip = input(f'{cyan}Введите IP ')
            with open(white_list_path, 'a', encoding="utf-8") as file:
                file.write(f'\n{newip}')
                print(f'{green}Ip успешно добавлен'+rest)
                time.sleep(1)
        elif IPchoise == '3':
            os.system('cls')
            reip = input(f'{cyan}Введите новый IP ')
            with open(white_list_path, 'w', encoding="utf-8") as file:
                file.write(f'{reip}')
                print(f'{green}Ip успешно добавлен'+rest)
                time.sleep(1)
print(tldextract.extract('https://ya.ru'))
def check_site(url):
    try:
        extracted = tldextract.extract(url)
        need_url = f"{extracted.domain}.{extracted.suffix}"
        response = requests.head(url, timeout=5, allow_redirects=True)
        if response.status_code < 400:
            print(f"Пинг с сайта: {ping(need_url)}")
            print(f"Сайт {url} доступен (Статус: {response.status_code})")
        else:
            print(f"Сайт {url} не отвечает (Статус: {response.status_code})")
            
    except requests.exceptions.RequestException:
        print(f"Сайт {url} не отвечает в вашем регионе или недоступен.")

def check():
    writer('---PING CHECKER---', yellow, 0.5)
    usr_url = input('Введите ссылку на сайт (обязательно указывайте http:// или https://): ')
    check_site(usr_url)

def encode_base64(data):
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')
def encode_hex(data):
    return data.encode('utf-8').hex()
def encode_binary(data):
    return ' '.join(format(ord(x), '08b') for x in data)
def decode_base64(data):
    return base64.b64decode(data).decode('utf-8')
def decode_hex(data):
    return bytes.fromhex(data).decode('utf-8')
def encoder_interface():
    os.system('cls')
    writer('--- ВЫБОР ---', yellow, 0.5)
    writer('\n1. Text to base64', yellow, 0.5)
    writer('\n2. Text to HEX', yellow, 0.5)
    writer('\n3. Text to binary', yellow, 0.5)
    fmt = input(f'\n{cyan}>> ')
    text = input(f'{cyan}Введите текст >> {rest}')
    try:
        if fmt == '1':
            res = encode_base64(text)
        elif fmt == '2':
            res = encode_hex(text)
        elif fmt == '3':
            res = encode_binary(text)
        else:
            res = 'Ощибка формата'
        writer(f'Результат: {res}', green, 0.3)
    except Exception as e:
        writer(f'Ошибка: {str(e)}', red, 0.3)

def decoder_interface():
    os.system('cls')
    writer('--- ВЫБОР ---', yellow, 0.5)
    writer('\n1. Base64 to Text', yellow, 0.5)
    writer('\n2. HEX to Text', yellow, 0.5)
    fmt = input(f'\n{cyan}>> ')
    text = input(f'{cyan}Введите текст >> {rest}')
    try:
        if fmt == '1':
            res = decode_base64(text)
        elif fmt == '2':
            res = decode_hex(text)
        else:
            res = 'Ошибка формата'
        writer(f'Результат: {res}', green, 0.3)
    except Exception as e:
        writer(f'Ошибка: {str(e)}', red, 0.3)