def display_greeting():
    print("="*50)
    print("✨ Welcome to PEGASUS! ✨")
    print("="*50)

def get_user_credentials():
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    return user, password

def authenticate_user(user, password):
    return user == "1" and password == "1"

def display_main_menu():
    print("\nPlease choose an option:")
    print("1. Lack of Motivation")
    print("2. Test Marks Problem")
    print("3. Track Me")
    print("4. Exit")
    return input("Enter your choice: ")

def handle_lack_of_motivation():
    print("\nDealing with Lack of Motivation:")
    print("1. Tired 😥")
    print("2. Procrastinating 😓")
    print("3. Don't Know ☹️")
    choice = input("Choose your reason: ")

    if choice == "1":
        print("Advice: Take a nap and recharge your energy!")
    elif choice == "2":
        print("Advice: Procrastination kills dreams. Focus and take action!")
    elif choice == "3":
        print("Advice: Remember the hard work of your parents and stay motivated!")
    else:
        print("Invalid choice. Please try again.")

def handle_test_marks_problem():
    print("\nAdvice: Analyze your test results, identify mistakes, and give your best in the next test. Never skip a test!")

def handle_track_me():
    print("\nTracking Options:")
    print("1. Lectures 😥")
    print("2. Daily Question Solving 😓")
    print("3. Revision ☹️")
    choice = input("What would you like to track? ")

    if choice == "1":
        track_lectures()
    elif choice == "2":
        track_daily_question_solving()
    elif choice == "3":
        track_revision()
    else:
        print("Invalid choice. Please try again.")

def track_lectures():
    lectures = int(input("Enter the number of lectures you completed today: "))
    if lectures < 2 and lectures != 0:
        print("Today, something is stopping you from reaching your potential. Identify it now and start working!")
        print("Advice: Block the next 3 hours and focus on your lectures. All the best!")
    elif lectures == 0:
        print("Advice: Completing 3 lectures daily will compound over time. Keep going! ⚡️")

def track_daily_question_solving():
    questions = int(input("Enter the number of questions you solved today: "))
    if questions < 5:
        print("Advice: Aim to solve at least 5 questions daily to keep your skills sharp. Keep pushing!")
    else:
        print("Great job! Keep up the good work and aim for even more!")

def track_revision():
    hours = int(input("Enter the number of hours you spent on revision today: "))
    if hours < 2:
        print("Advice: Spend at least 2 hours on revision daily to retain what you've learned.")
    else:
        print("Excellent! Regular revision helps in better retention and understanding.")

def main():
    display_greeting()
    user, password = get_user_credentials()

    if authenticate_user(user, password):
        while True:
            choice = display_main_menu()

            if choice == "1":
                handle_lack_of_motivation()
            elif choice == "2":
                handle_test_marks_problem()
            elif choice == "3":
                handle_track_me()
            elif choice == "4":
                print("Thank you for using PEGASUS. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()
