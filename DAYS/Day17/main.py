class User:
    def __init__(self, user_id, name):
        # CREATING ATTRIBUTES
        # self --> refers to current object
        self.id = user_id
        self.name = name
        # setting default value
        self.follower = 0
        self.following = 0

    # function to update value
    def upgrade_my_followers(self, user):
        print(user.id, user.name)
        user.follower +=1
        self.following +=1




# constructor : used to initialize an object whenever we are creating an object. Named as  __init__

user_1 = User('001', 'sanjay rana')
user_2 = User('002','venkatesh aiyer')
# print(user_1.id, user_1.name, user_1.follower)

# user-1 decided to follow user 2
user_1.upgrade_my_followers(user_2)
# result
print(f'\nuser 1: following - {user_1.following} || followers - {user_1.follower}\n')
print(f'user 2: following - {user_2.following} || followers - {user_2.follower}')