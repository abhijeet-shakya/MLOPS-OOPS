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
            self.writePost()
        elif  user_input == "4":
            self.sendMessage()
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

    def writePost(self):
        if self.loggedIn:
            txt = input("Enter your message here ->")
            print(f"Following content has beed posted -> {txt}")
        else:
            print("You need to signin first to psot something")
        print('\n')
        self.menu()
    
    def sendMessage(self):
        if self.loggedIn:
            friend = input("Whom to send to msg? -> ")
            msg = input("Write message here -> ")
            print(f"Your message has been sent to {friend}")
        else:
            print("You need to Sign in for send message")
        print('\n')
        self.menu()


# user = Chatbook()