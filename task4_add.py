from decorators import input_error1

@input_error1
def add_contact(args, contacts):
    
    name, phone = args
    if name in contacts:
        return f"User '{name}'  is already in the contacts: {contacts}"
    contacts[name] = phone
    return "Contact added."

@input_error1
def change_contact(args, contacts):

    name, phone = args
    if name not in contacts:
        return f"User '{name}' is not found in contacts: {contacts}"
    contacts[name] = phone
    return "Contact updated."
