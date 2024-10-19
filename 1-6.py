my_dict={'Ivan':1999,'Luka':2000, 'Maria':1997}
print("Dict: ", my_dict)
print("Existing value: ",my_dict['Ivan'])
print("Not existing value: ",my_dict.get('Stepan'))
my_dict.update({"Ilya":1973,'Irina':1974})
print("Deleted value:", my_dict.pop("Ilya"))
print("Modified dict: ", my_dict)
print()
my_set={1,2,3,'5',2,3,False,(1,2,3)}
print("Set: ",my_set)
my_set.add("Хрюша")
my_set.add(55)
my_set.discard(False)
print("Modified set: ",my_set)
