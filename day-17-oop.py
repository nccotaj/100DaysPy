#Create our own class (usuallyt pascal case for classes)

class User:
    def __init__(self, user_id, username): #Constructor called everytime we create a new object from class. Can add other params after self
        self.id = user_id #The user id provided when a new object is created is passed into object
        self.username = username
        self.followers = 0 #initialized number do not need to pass it in when creating object
        self.following = 0

    #defining a method
    #this method increments its own following count and the other users followers count
    def follow(self, user):
        user.followers += 1
        self.following += 1




# user1 = User() #Empty Constructor
# user1.id = "001"  #adds the attribute id to the class
# user1.username = "Nick"

# print(user1.username) #"Nick"

user1 = User("001","Sam") #using constructor to pass attributes
print(user1.followers) 

user2 = User("001","Nick")

#calling the method
user1.follow(user2) #will increment followers of user2 and following of user1

print(user1.following)
print(user2.followers)

