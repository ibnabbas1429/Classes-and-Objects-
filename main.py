class Student:
    def __init__(self,name,age,tracks,score):
        self.name = (name)
        self.age = (age)
        self.tracks = tracks
        self.score = (score)

    

    def change_name(self,new_name):
        
        self.new_name = new_name
        

    def change_age(self,new_age):
        
        if not isinstance(new_age, int):
            raise ValueError(f"new_age must be an integer, got {new_age} ")
        self.new_age = new_age
        

    def add_track(self,new_track):
        
        self.new_track = new_track   
        

    def get_score(self):
        
        return self.score





Bob = Student(name="Bob", age=29.6, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

