import shutil, re, os, time, functions, sys
from colorama import init, Fore

init()
lyellow = Fore.LIGHTYELLOW_EX
green, red, yellow, purple, cyan, rest = Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.RESET

def center_text(text):
    """Центрирует текст с учётом ANSI-кодов"""
    terminal_width = shutil.get_terminal_size().columns
    visible_len = get_visible_length(text)
    padding = (terminal_width - visible_len) // 2
    return ' ' * padding + text

def get_visible_length(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return len(ansi_escape.sub('', text))

def soon_draw():
    terminal_width = shutil.get_terminal_size().columns
    soon_lines = [
        yellow + '███████╗ ██████╗  ██████╗ ███╗   ██╗',
        yellow + '██╔════╝██╔═══██╗██╔═══██╗████╗  ██║',
        yellow + '███████╗██║   ██║██║   ██║██╔██╗ ██║',
        yellow + '╚════██║██║   ██║██║   ██║██║╚██╗██║',
        yellow + "███████║╚██████╔╝╚██████╔╝██║ ╚████║",
        yellow + "╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝" + rest
    ]
    for line in soon_lines:
        soon_visible_len = get_visible_length(line)
        soon_padding = (terminal_width - soon_visible_len) // 2
        print(' ' * soon_padding + line)

def logo_draw():
    terminal_width = shutil.get_terminal_size().columns
    logo_lines = [
        purple + '███████╗███████╗ ██████╗  ██████╗',
        purple + '██╔════╝██╔════╝██╔═══██╗██╔════╝',
        purple + '█████╗  ███████╗██║   ██║██║     ',
        purple + '██╔══╝  ╚════██║██║   ██║██║     ',
        purple + "██║     ███████║╚██████╔╝╚██████╗",
        purple + "╚═╝     ╚══════╝ ╚═════╝  ╚═════╝" + rest
    ]
    for line in logo_lines:
        visible_len = get_visible_length(line)
        padding = (terminal_width - visible_len) // 2
        print(' ' * padding + line)
    
  
    update_info = f"{yellow}Last Update on {green}18 February{rest}"
    with open(functions.conf_path, 'r', encoding="utf-8") as file:
        content = file.read().split()
        login = content[0].strip()
    hello = f'{yellow}Hello, {login}!'
    visible_hello = get_visible_length(update_info)
    padding_hello = (terminal_width - visible_hello) // 2
    print(' ' * padding_hello + hello)

    visible_update = get_visible_length(update_info)
    padding_update = (terminal_width - visible_update) // 2
    print(' ' * padding_update + update_info)

def draw_centered_menu(menu_items, title=" FSOCIETY MENU "):
    term_width = shutil.get_terminal_size().columns
    
   
    max_content_len = max(max(get_visible_length(i) for i in menu_items), len(title))
    box_width = max_content_len + 4
    left_indent_len = (term_width - box_width - 2) // 2
    left_indent = " " * max(0, left_indent_len)

    side_line = (box_width - len(title)) // 2
    print(left_indent + yellow + "┌" + "─" * side_line + title + "─" * (box_width - side_line - len(title)) + "┐")
    
    for item in menu_items:
       
        spaces_after = " " * (box_width - get_visible_length(item) - 2)
        print(left_indent + yellow + "│ " + rest + item + spaces_after + yellow + " │")
        
       
        if "Status:" in item:
            print(left_indent + yellow + "├" + "─" * box_width + "┤")

    print(left_indent + yellow + "└" + "─" * box_width + "┘" + rest)
    return left_indent + cyan + "Выбор > " + rest

def usr_choise():
    menu_items = [
        f"{lyellow}1. Network Tools",
        f"{lyellow}2. Crypto / Hash Tools",
        f"{lyellow}3. Brute Force",
        f"{lyellow}4. Anonymity",
        f"{lyellow}5. System Info",
        f"{lyellow}6. Settings",
        f"{lyellow}0. Exit"
    ]

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        logo_draw()
        print("\n")
        
       
        input_prompt = draw_centered_menu(menu_items)
        
        
        user_input = input(input_prompt)

        
        if user_input == '0':
            print(Fore.RED + "\nВыход..." + rest)
            sys.exit()
            
        elif user_input == '1':
            functions.clear()
            
            print(f"\n{yellow}--- Network Tools ---{rest}")
            print("1. Scanner (Soon)")
            print('2. Ping')
            f1 = input(f"\n{cyan}Нажми Enter для возврата...{rest}")
            if f1 == '2':
                functions.check()
                input("\nНажми Enter...")
        elif user_input == '2':
            functions.clear()
          
            print(f"\n{yellow}--- Crypto Tools ---{rest}")
            functions.writer('\n1. Hash Identifier\n2. Encoder/Decoder\n', yellow, 0.05)
          
            sub_choice = input(f"\n{cyan}Выбор > {rest}")
            if sub_choice == '1':
                functions.clear()
                functions.hash_ident()
                input("\nНажми Enter...")
            elif sub_choice == '2':             
                functions.clear()
                functions.writer('1. Encoder', yellow, 0.5)
                functions.writer('\n2. Decoder', yellow, 0.5)
                decenc = input(f"\n{cyan}Выбор > {rest}")
                if decenc == '1':
                    functions.encoder_interface()
                elif decenc == '2':
                    functions.decoder_interface()
                input("\nНажми Enter...")
        elif user_input == '5':
            functions.clear()
            functions.system_info()
            input(f"\n{cyan}Нажми Enter для возврата...{rest}")
            
        elif user_input == '6':
            functions.clear()
            functions.settings()
            
        else:
            os.system('cls')
            print('\n'* 7)
            soon_draw()
            time.sleep(2)
            pass