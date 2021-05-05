people = [ 
          
        {"name":"Harry", "house":"Bucaramanga"},
        {"name":"Pedro", "house":"Bucaramanga"},
        {"name":"Gabriel", "house":"Bucaramanga"},      
        {"name":"Maria", "house":"Bucaramanga"}       
    ]

def f(person):
    return person["name"]

people.sort(key=lambda person: person["name"])
print(people)