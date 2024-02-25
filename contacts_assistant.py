def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Invalid arguments of 'add' command."


def change_contact(args, contacts):
    try:
        name, phone = args

        if name not in contacts:
            return f"Contact with name '{name}' not found."

        contacts[name] = phone
        return "Contact updated."
    except ValueError:
        return "Invalid arguments of 'change' command."


def show_phone(args, contacts):
    try:
        name, *_ = args
        return contacts[name]
    except ValueError:
        return "Invalid arguments of 'add' command."
    except KeyError:
        return f"Contact not found."


def show_all(contacts):
    contacts_msg = "\n".join(f"{name} - {number}" for name, number in contacts.items())
    return contacts_msg or "Contacts empty."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
