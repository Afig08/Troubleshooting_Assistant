# Rule-Based Coding Troubleshooting Coach
# This program uses rules, menus, and if/elif logic to help users troubleshoot coding problems.
# It does not use machine learning. It works like an early expert system.


def show_intro():
    """
    Displays the welcome message.
    This explains what the system does.
    """

    print("============================================")
    print(" Rule-Based Coding Troubleshooting Coach")
    print("============================================")
    print("Welcome!")
    print("This system helps you troubleshoot common coding problems.")
    print("It uses rules and logic instead of machine learning.")


def show_main_menu():
    """
    Displays the main menu.
    The user chooses what kind of problem they are having.
    """

    print("\nWhat type of coding problem are you having?")
    print("1. I have an error message")
    print("2. My code runs, but the output is wrong")
    print("3. My code runs, but nothing prints")
    print("4. I do not know where to start")
    print("5. I want a study recommendation")
    print("6. Exit")


def handle_error_message():
    """
    Handles the case where the user has an error message.
    This function asks what kind of error they are seeing.
    """

    print("\nWhat type of error are you seeing?")
    print("1. SyntaxError")
    print("2. NameError")
    print("3. TypeError")
    print("4. IndexError")
    print("5. IndentationError")
    print("6. I am not sure")

    error_choice = input("Choose an option from 1-6: ")

    if error_choice == "1":
        print("\nDiagnosis: SyntaxError")
        print("A SyntaxError usually means Python cannot understand your code structure.")
        print("Check for missing colons, parentheses, quotation marks, commas, or brackets.")
        print("Example: if statements and loops usually need a colon at the end.")

    elif error_choice == "2":
        print("\nDiagnosis: NameError")
        print("A NameError usually means Python does not recognize a name you used.")
        print("Check if your variable or function name is spelled correctly.")
        print("Also check that the variable was created before you tried to use it.")

    elif error_choice == "3":
        print("\nDiagnosis: TypeError")
        print("A TypeError usually means you are using incompatible data types.")
        print("For example, Python may not allow you to add a string and an integer directly.")
        print("Check your variables and convert data types if needed.")

    elif error_choice == "4":
        print("\nDiagnosis: IndexError")
        print("An IndexError usually means you tried to access a list position that does not exist.")
        print("Remember that Python lists start at index 0.")
        print("Check the length of your list before accessing an item.")

    elif error_choice == "5":
        print("\nDiagnosis: IndentationError")
        print("An IndentationError means your code spacing is not aligned correctly.")
        print("Check the lines inside if statements, loops, and functions.")
        print("Make sure you are using consistent spaces.")

    elif error_choice == "6":
        print("\nGeneral Debugging Advice")
        print("Look at the last line of the error message first.")
        print("Python usually tells you the error type and the line number.")
        print("Read the error slowly and check the line mentioned.")

    else:
        print("\nInvalid choice. Please choose a number from 1 to 6.")


def handle_wrong_output():
    """
    Handles the case where the code runs, but the answer is wrong.
    This usually means there is a logic problem.
    """

    print("\nWrong Output Troubleshooting")
    expected = input("What output did you expect? ")
    actual = input("What output did you actually get? ")

    print("\nRule-Based Advice:")
    print("Your code runs, so this is probably a logic issue.")
    print("Compare your expected output with your actual output.")

    if expected == actual:
        print("Interesting — your expected and actual outputs match.")
        print("Double-check whether the issue is somewhere else in your program.")
    else:
        print("Since the outputs are different, try these steps:")
        print("1. Print important variables before and after calculations.")
        print("2. Check your formulas or conditions.")
        print("3. Test one small part of the program at a time.")
        print("4. Check if your loop is running too many or too few times.")


def handle_no_output():
    """
    Handles the case where the program runs but prints nothing.
    """

    print("\nNo Output Troubleshooting")
    print("Answer these questions:")

    has_print = input("Did you use a print statement? yes/no: ").lower()
    inside_function = input("Is your code inside a function? yes/no: ").lower()

    print("\nRule-Based Advice:")

    if has_print == "no":
        print("You may need to add a print statement.")
        print("Python does not automatically show values unless you tell it to.")

    elif has_print == "yes" and inside_function == "yes":
        print("Check if you actually called the function.")
        print("Defining a function does not run it automatically.")
        print("Example:")
        print("def greet():")
        print("    print('Hello')")
        print("")
        print("greet()  # This calls the function")

    elif has_print == "yes" and inside_function == "no":
        print("Check whether your print statement is inside a condition that never becomes true.")
        print("Also check that you are running the correct file.")

    else:
        print("Check your print statements, function calls, and program flow.")


def handle_do_not_know_where_to_start():
    """
    Helps the user break a programming problem into smaller pieces.
    """

    print("\nStarting Point Helper")
    print("When you do not know where to start, break the problem into three parts:")

    problem = input("Briefly describe the problem you are trying to solve: ")

    print("\nBased on your problem:")
    print(problem)

    print("\nUse this structure:")
    print("1. Inputs: What information does the program need?")
    print("2. Process: What steps should the program follow?")
    print("3. Output: What should the program display or return?")

    print("\nExample:")
    print("If the task is to calculate an average:")
    print("- Inputs: numbers")
    print("- Process: add the numbers, then divide by the count")
    print("- Output: the average")


def handle_study_recommendation():
    """
    Gives a study recommendation based on what the user struggles with.
    """

    print("\nStudy Recommendation")
    print("What topic are you struggling with?")
    print("1. Variables")
    print("2. Loops")
    print("3. Functions")
    print("4. Lists")
    print("5. If statements")
    print("6. Debugging")

    topic_choice = input("Choose an option from 1-6: ")

    if topic_choice == "1":
        print("\nRecommendation: Review variables and data types.")
        print("Practice creating variables that store strings, integers, floats, and booleans.")

    elif topic_choice == "2":
        print("\nRecommendation: Review loops.")
        print("Practice for loops, while loops, counters, and loop conditions.")

    elif topic_choice == "3":
        print("\nRecommendation: Review functions.")
        print("Practice writing functions with parameters and return values.")

    elif topic_choice == "4":
        print("\nRecommendation: Review lists.")
        print("Practice indexing, appending, removing, and looping through lists.")

    elif topic_choice == "5":
        print("\nRecommendation: Review if statements.")
        print("Practice if, elif, and else logic with comparison operators.")

    elif topic_choice == "6":
        print("\nRecommendation: Practice debugging step by step.")
        print("Read error messages carefully and use print statements to check variable values.")

    else:
        print("\nInvalid choice. Please choose a number from 1 to 6.")


def main():
    """
    The main controller of the program.
    This keeps the program running until the user chooses to exit.
    """
    print("Program Started!")

    show_intro()

    running = True

    while running:
        show_main_menu()

        choice = input("Choose an option from 1-6: ")

        if choice == "1":
            handle_error_message()

        elif choice == "2":
            handle_wrong_output()

        elif choice == "3":
            handle_no_output()

        elif choice == "4":
            handle_do_not_know_where_to_start()

        elif choice == "5":
            handle_study_recommendation()

        elif choice == "6":
            print("\nGoodbye! Keep debugging one step at a time.")
            running = False

        else:
            print("\nInvalid choice. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()