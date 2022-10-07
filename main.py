
paisesStrings=input("ingresa una lista de paises separados por una coma ")
                          
paisesCleanList=paisesStrings.replace(" ", "").split(",")

paisesListOrdenado=sorted(list(set(paisesCleanList)))



print(paisesListOrdenado)