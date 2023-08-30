
"""
Modus Ponens

Baruc Gutiérrez Quirarte - 7F1 
Sistemas Expertos
"""

# Premisas

ProsicionA = True #Si un pez pasa mas de 5 minutos fuera del agua
ProsicionB = True #Muere

Premisa1 = ProsicionA and ProsicionB # Si un pez pasa mas de 5 minutos fuera del agua, muere
Premisa2 = ProposicionA # Mi pez paso mas de 5 minutos fuera del agua

#Modus Ponens

if Premisa2:
    ProsicionB = True
    conclusion = "Mi pez ha muerto"
    print(conclusion)

