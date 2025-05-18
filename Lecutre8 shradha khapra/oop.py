class Students:

    def __init__(self, fullname):
        self.name = fullname
        print('adding a new student in database')


s1 = Students('Samad')
print(s1.name) # Samad
