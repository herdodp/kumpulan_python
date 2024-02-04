from kanren.facts import Relation, facts
from kanren.core import var, run

def get_anak(x,y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))

def get_cucu(x,y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))

if __name__== '__main__':    
    parent = Relation()
    facts(parent,("Slamet", "Amin"),
                ("Slamet", "Anang"),
                ("Amin", "Badu"),
                ("Amin", "Budi"),
                ("Anang", "Didi"),
                ("Anang", "Dadi"))
x = var()
 
kakek = Relation()
facts(kakek, ( "slamet" , "Badu"))
output = run(0, x, kakek(x, "Badu"))
print("\nNama kakek dari Badu :", output[0])