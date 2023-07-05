def run_chatgpt4_version():
    # import and run the RockPaperScissors_ChatGPT4.py script
    import RockPaperScissors_ChatGPT4
    RockPaperScissors_ChatGPT4.game()


def run_googlebard_version():
    # import and run the RockPaperScissors_GoogleBard.py script
    import RockPaperScissors_GoogleBard
    RockPaperScissors_GoogleBard.main()


# TODO: Fix imaginary bug

if __name__ == "__main__":
    print("Choose the version of rock, paper, scissors game you want to play:")
    print("1: chatgpt4 version")
    print("2: googlebard version")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        run_chatgpt4_version()
    elif choice == "2":
        run_googlebard_version()
    else:
        print("Invalid choice.")
