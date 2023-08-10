def ask_choices(choices):
    """
    Ask the user to choose between a list of choices.

    :param choices: A list of choices.
    :return: The choice of the user.
    """
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice['text']}")
    while True:
        try:
            choice = int(input("Please choose one of the above: "))
            print()
            if choice < 1 or choice > len(choices):
                raise ValueError
            return choices[choice - 1]
        except ValueError:
            print("Invalid choice. Please try again.")
            continue
