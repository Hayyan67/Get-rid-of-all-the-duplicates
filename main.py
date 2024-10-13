student={
'id1':{'name' : 'abc','city' : 'London','age':12,'subject':['phy,chem,bio']},
'id2':{'name' : 'abc','city' : 'London','age':12,'subject':['phy,chem,bio']},
'id3':{'name' : 'abc','city' : 'London','age':12,'subject':['phy,chem,bio']},
'id4':{'name' : 'abc','city' : 'London','age':12,'subject':['phy,chem,bio']},
'id5':{'name' : 'abc','city' : 'London','age':12,'subject':['phy,chem,bio']},
'id6':{'name' : 'abc','city' : 'London','age':12,'subject':['phy,chem,bio']},
}
result={}
for c,d in student.items():
    if d not in result.values():
        result [c]=d

print('result')