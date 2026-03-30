from user import User

user1 = User("john",1234786)
user2 = User("kaviya",456321)
user3 = User("livin",768543)


user1.register()
user2.login()


print(User.users)