class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show(self):
        return '{} is {} year old and {} gender'.format(self.name,self.age,self.gender)
   

import pickle

p=person('aditya',25,'male')
with open('person.pkl','wb') as f:
    pickle.dump(p,f)

with open('person.pkl','rb') as f:
    p1=pickle.load(f)
    print(p1.show())

