class Users:
    def __init__(self, userId: int, user_name: str):
        self.userId = userId
        self.user_name = user_name
        self.followers = 0
        self.following = 0
    
    def get_user_profile(self):
        return {
            "id": self.userId,
            "Name": self.user_name,
            "Age": self.age,
            "ProfileImage": self.profile_image
        }

    def follow(self, user):
        user.followers += 1
        self.following += 1



class Car:
    def __init__(self, seats):
        self.seats = seats
    
    def get_car_detail(self):
        return self.seats

    def enter_race_mode(self):
        self.seats = 2


user_one = Users(1, "Pavan Pattinson")
user_two = Users(2, "Abhishek JN")

user_one.follow(user_two)
print(user_one.followers)
print(user_one.following)
print(user_two.followers)
print(user_two.following)


