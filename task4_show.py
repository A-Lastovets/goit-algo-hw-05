from decorators import input_error2, input_error3

@input_error2
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        print(contacts[name])
    else:
        print(f"User '{name}' is not found in contacts: {contacts}")


@input_error3
def show_all(contacts):
    
    for info in contacts:
        print(f"User '{info}', phone number '{contacts[info]}'")