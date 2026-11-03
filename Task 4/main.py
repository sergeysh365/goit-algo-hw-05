# Декоратор input_error для обробки помилок ValueError, KeyError, IndexError
from os import name


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
          return "Contact not found."
        except IndexError:
          return "Enter contact name pleace."

    return inner

# Парсер команд відповідає за розбір введених користувачем рядків
def parse_input(user_input):
    if not user_input.strip():
        return "", []
    # Розділяємо рядок на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# Функції-обробники команд (handlers)
@input_error
def add_contact(args, contacts):
    # Якщо аргументів < 2, викликає ValueError -> перехоплює декоратор
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    # Якщо аргументів < 2, викликає ValueError -> перехоплює декоратор
    name, phone = args
    contacts[name] = phone
    return "Contact updated."
    
@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"
    
def show_all(contacts):
    if not contacts:
        return "No contacts saved yet."
    result = "All contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

# Головна функція керування ботом
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            # Функція show_phone сама валідує наявність аргументів
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()