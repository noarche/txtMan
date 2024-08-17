import os
import shutil
from colorama import Fore, Style, init

init(autoreset=True)

main_logo = '''

                                                              
\033[94m████████╗██╗  ██╗████████╗███╗   ███╗ █████╗ ███╗   ██╗\033[0m
\033[94m╚══██╔══╝╚██╗██╔╝╚══██╔══╝████╗ ████║██╔══██╗████╗  ██║\033[0m
\033[94m   ██║    ╚███╔╝    ██║   ██╔████╔██║███████║██╔██╗ ██║\033[0m
\033[94m   ██║    ██╔██╗    ██║   ██║╚██╔╝██║██╔══██║██║╚██╗██║\033[0m
\033[94m   ██║   ██╔╝ ██╗   ██║   ██║ ╚═╝ ██║██║  ██║██║ ╚████║\033[0m
\033[94m   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝\033[0m
                                                      
      \033[95m****************************\033[0m
      \033[96m github.com/noarche/txtMan   \033[0m
      \033[94m    .txt Manipulation     \033[0m
      \033[95m****************************\033[0m

\033[94m Visit the github for more information. \033[0m

'''
print(main_logo)

def load_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def save_file(filename, lines):
    temp_filename = filename + "_1"
    with open(temp_filename, 'w') as file:
        file.writelines(lines)
    os.remove(filename)
    os.rename(temp_filename, filename)

def split_lines(lines, delimiter, part):
    return [line.split(delimiter)[0] + '\n' if part == 'first' else line.split(delimiter)[1] + '\n' for line in lines]

def add_prefix_suffix(lines, text, mode):
    return [text + line if mode == 'prefix' else line + text for line in lines]

def remove_instances(lines, text):
    return [line.replace(text, '') for line in lines]

def replace_instances(lines, old_text, new_text):
    return [line.replace(old_text, new_text) for line in lines]

def organize_shortest_to_longest(lines):
    return sorted(lines, key=len)

def organize_alphabetically(lines):
    return sorted(lines)

def remove_duplicates(lines):
    seen = set()
    result = []
    for line in lines:
        if line not in seen:
            seen.add(line)
            result.append(line)
    return result

def display_menu():
    print(Fore.CYAN + "Choose an option:")
    print(Fore.GREEN + "1. Split lines by delimiter and return first or second half")
    print(Fore.YELLOW + "2. Add text as prefix or suffix")
    print(Fore.MAGENTA + "3. Remove all instances of text")
    print(Fore.RED + "4. Replace all instances of text")
    print(Fore.BLUE + "5. Organize lines shortest to longest")
    print(Fore.LIGHTBLUE_EX + "6. Organize lines alphabetically")
    print(Fore.LIGHTGREEN_EX + "7. Remove duplicate lines")
    print(Fore.LIGHTCYAN_EX + "8. Exit")

def main():
    filename = input(Fore.LIGHTCYAN_EX + "Enter the filename: ")
    lines = load_file(filename)
    
    while True:
        display_menu()
        choice = input(Fore.LIGHTCYAN_EX + "Enter your choice: ")
        
        if choice == '1':
            delimiter = input(Fore.LIGHTCYAN_EX + "Enter the delimiter: ")
            part = input(Fore.LIGHTCYAN_EX + "Return 'first' or 'second' part: ").strip().lower()
            lines = split_lines(lines, delimiter, part)
        elif choice == '2':
            text = input(Fore.LIGHTCYAN_EX + "Enter the text to add: ")
            mode = input(Fore.LIGHTCYAN_EX + "Add as 'prefix' or 'suffix': ").strip().lower()
            lines = add_prefix_suffix(lines, text, mode)
        elif choice == '3':
            text = input(Fore.LIGHTCYAN_EX + "Enter the text to remove: ")
            lines = remove_instances(lines, text)
        elif choice == '4':
            old_text = input(Fore.LIGHTCYAN_EX + "Enter the text to replace: ")
            new_text = input(Fore.LIGHTCYAN_EX + "Enter the new text: ")
            lines = replace_instances(lines, old_text, new_text)
        elif choice == '5':
            lines = organize_shortest_to_longest(lines)
        elif choice == '6':
            lines = organize_alphabetically(lines)
        elif choice == '7':
            lines = remove_duplicates(lines)
        elif choice == '8':
            break
        else:
            print(Fore.RED + "Invalid choice, please try again.")
            continue

        save_file(filename, lines)
        lines = load_file(filename)
        print(Fore.LIGHTGREEN_EX + "Operation completed and file saved.")
        print(Fore.LIGHTCYAN_EX + "Returning to menu...")

if __name__ == "__main__":
    main()
