import Error

def init_person(p):
    colors=["green", "brown", "blue","red","yellow"]
    names=["Tom","Alice","Bob","Ariel"]
    
    try:
        p.set_age(random.randint(50,200))
        p.set_eye_color(random.randint(0,len(colors)))
        p.set_name(random.randint(0,len(names)))
    except Exception:
        pass

person = [Person() for i in range(5)]

for p in people:
    init_person(p)

for p in people:
    print(p)