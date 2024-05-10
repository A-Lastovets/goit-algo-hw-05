#decorator
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"ValueError: {str(e)}\nPlease provide correct arguments."
        except KeyError as k:
            return f"KeyError: {str(k)}\nEnter a valid command again\n"
        except IndexError as i:
            return f"IndexError: {str(i)} Invalid number of arguments."
        
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Give me name and phone please, try again.")
    name, phone = args
    if name in contacts:
        raise KeyError(f"User '{name}'  is already in the contacts: {contacts}")
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Give me name and phone please, try again.")
    name, phone = args
    if name not in contacts:
        raise KeyError(f"User '{name}' is not found in contacts: {contacts}")
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        print(contacts[name])
    else:
        print(f"User '{name}' is not found in contacts: {contacts}")


@input_error
def show_all(contacts):

    for info in contacts:
        print(f"User '{info}', phone number '{contacts[info]}'")


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
            case "phone" if len(args) == 1:   show_phone(args, contacts)
            case "all"   if len(args) < 1:    show_all(contacts)    
            case _:          print("Invalid command, please try again. \nIf you want to exit the bot : type 'exit' or 'close'\n ")

if __name__ == "__main__":
    main()