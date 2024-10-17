immutable_var = 1,2,'we',['q','w']
print("immutable tuple: ",immutable_var)

#immutable_var[0]="Modified" ошибка: кортеж содержит неизменные ссылки

immutable_var[3][1] = 3 #нет ошибки - объекты по ссылке изменяемы

mutable_var = list(immutable_var) #список
mutable_var[0]="Modified"
print("Mutable list: ",mutable_var)
#Mutable list:  ['Modified', 2, 'we', ['q', 3]]

