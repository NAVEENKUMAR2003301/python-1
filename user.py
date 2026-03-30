class User:

    user_name : None
    pwd       : None
    users = 0

    def __init__(self,user_name,pwd):
        self.user_name = user_name
        self.pwd       = pwd
        User.users += 1
        
    def register(self):
        print("registering...." + self.user_name)
        print("password : " ,(self.pwd) )

    def login(self) :
        print("logining..." + self.user_name)

