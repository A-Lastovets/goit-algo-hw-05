
def input_error1(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please, try again."

    return inner


def input_error2(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print("Please enter 'phone' command and add the user name, try again.")

    return inner


# з цим декоратором трохи затряг, не розумію як перевірити правильно цю помилку "KeyError", по суті цей декоратор не працює. 
#Здаю дз бо вже часу мало, але я далі буду наматися в тому розібратися)))
def input_error3(func):
    def inner(*args, **kwargs):
        try:    
                return func(*args, **kwargs)
        except KeyError:
            print("Please enter only 'all' command if you want to see list of contacts, try again.")
            
    return inner
