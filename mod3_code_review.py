
class Person:
    def __init__(self, fname, lname, gender, birthday, fav_color):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        # Format should be 'YYYY-MM-DD'.
        self.birthday = birthday
        self.fav_color = fav_color

    def describe_user(self):
        print(f"Full Name: {self.fname} {self.lname}")
        print(f"Gender: {self.gender}")
        print(f"Birthday: {self.birthday}")
        print(f"Favorite Color: {self.fav_color}")

    def greet_user(self):
        print(f"Hello {self.fname}! I hope you are having a wonderful day!")

kylee = Person('Kylee', 'Parker', 'Female', '2006-12-22', 'Purple')
obeth = Person('Obeth', 'Cruz', 'Male', '2007-02-09', 'Red')
turo =  Person('Arturo', 'Cruz Jr.', 'Male', '2000-06-03', 'Blue')
arturo = Person('Arturo', 'Cruz', 'Male', '1962-12-15', 'Orange')
kailen = Person('Kailen', 'Barnes', 'Male', '2006-09-06', 'Purple')

people = [kylee, obeth, turo, arturo, kailen]

for person in people:
    print("\nPerson Info:")
    person.describe_user()
    person.greet_user()
