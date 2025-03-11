class Course:

    def __init__(self, name, duration, link):
        self.name = name
        self.duration = duration
        self.link = link

    #def __str__(self): #Con este metodo especial podemos reprentar la lista de objetos

    #    return f"{self.name} [{self.duration} horas] ({self.link})" 

    def __repr__(self): #Funcion especial para representar la lista de objetos
        return f"{self.name} [{self.duration} horas] ({self.link})" 

courses = [
        Course("Introduccion a Linux", 15, "https://hack4u.io/cursos/introduccion-a-linux/"),
        Course("Personalizacion de Linux", 3, "https://hack4u.io/cursos/personalizacion-de-entorno-en-linux/"),
        Course("Introduccion al Hacking", 53, "https://hack4u.io/cursos/introduccion-al-hacking/")

        ]

#for course in courses:

#    print(course) Listando la lista de objetos

#print(courses[1]) #Representamos la lista de objetos gracias al metodo especial __repr__

def list_courses():

    for course in courses:
        print(course)

def serach_by_name(name):

    for course in courses:
        if course.name == name:
            return course

    return None
