
from task4_add import add_contact, change_contact
from task4_show import show_phone, show_all
from decorators import input_error1

@input_error1
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":    print("How can I help you?")
            case "add":      print(add_contact(args, contacts))
            case "change":   print(change_contact(args, contacts))
            case "phone":    show_phone(args, contacts)
            case "all" if len(args) < 1:  show_all(contacts)       # замість декоратора перевірка відбувається тут
            case _:          print("Invalid command, please try again. \nIf you want to exit the bot : type 'exit' or 'close'\n ")

if __name__ == "__main__":
    main()