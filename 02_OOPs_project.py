class Chatbook:
    def __init__(self) -> None:
        self.username = ''
        self.password = ''
        self.loggedIn = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to the Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signIn
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           """)

        if user_input == "1":
            self.signUp()
        elif  user_input == "2":
            self.signIn()
        elif  user_input == "3":
            pass
        elif  user_input == "4":
            pass
        else:
            exit()

    def signUp(self):
        email = input("Enter your email here -> ")
        password = input("Setup your password here -> ")
        self.username = email
        self.password = password
        print("You have signed up successfully!!")
        print("\n")
        self.menu()

    def signIn(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in the menu")
        else:
            email = input("Enter your email/username here -> ")
            password = input("Enter your password here -> ")

            if self.username == email and self.password == password:
                print("You have signed in successfully")
                self.loggedIn = True
            else:
                print("Please input correct credentials...")
        print('\n')
        self.menu()



obj = Chatbook()