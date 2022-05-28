class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.track = tracks
        self.score = score

    def change_name(self, new_name):
        self.name = new_name
        return self.name
    def change_age(self, new_age):
        self.age = new_age
        return self.age
    def add_track(self, new_track):
        self.track = new_track
        return self.track
    def get_score(self, new_score):
        
        self.score = int(new_score)
        return self.score
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
print(Bob.change_name("Peter"))
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
