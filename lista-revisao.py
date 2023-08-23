feira = ["Uva","Maça","Banana"]
#index menos -1 um puxa o ultimo valor da lista.
#1: puxaria de maça ate a banana  
#pode colocar somente : para puxa todos os valores da lista 

# for frutas in range(len(feira)):
#     print(frutas)

# for index,frutas in enumerate(feira):
#     print(index , feira)



#Dicionarios valores:Chave
            #valor    #chave
# studants = {"Michael":"Guadalupe", "Renan":"Sao jao","Vitinho":"Mora mal"}
# for student in studants:
#     print(student,studants[student])   


studants = [
    {"Name":"Michael", "Home":"Guadalupe"},
    {"Name":"Renan", "Home":"Sao Jao"},
    {"Name":"Jose", "Home":"Mora mal"}
]
for s in studants:

    print(s ["Name"], s ["Home"])