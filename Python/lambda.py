people = [
    {"name":"Henry", "house":"Gryffindor"},
    {"name":"Cho","house":"ravenclaw"},
    {"name":"Draco","house":"Slytherin"},
    
]


#def f(person):
    #return person["name"]


#people.sort(key=f)

people.sort(key=lambda person:person["name"])

print(people)