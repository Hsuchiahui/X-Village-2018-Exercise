class RelationException(Exception):
    def __init__(self,p1arg,p2arg):
        self.person_a =  p1arg
        self.person_b =  p2arg
    def __str__(self):
        return "Are you sure that " + self.person_a+" and "+self.person_b+" are in love with each other?"

relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}
def check(pa, pb):
    # TODO: raise exception
    # TIPS: 這個地方會需要 raise 兩種 exception
    if pa in relation.values() and pb in  relation.values():
        if  relation[pa] != pb:
            raise RelationException(pa,pb)
            
    else:
        print("No relation found")
        raise RelationException(pa,pb)
        
    
           
try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2)) 
except RelationException as e:
    print(e)

    