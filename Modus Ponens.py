
"""
Modus Ponens

Baruc Gutiérrez Quirarte - 7F1 
Sistemas Expertos
"""

# Premisas

ProposicionA = True #Si un pez pasa mas de 5 minutos fuera del agua
ProposicionB = True #Muere

Premisa1 = ProposicionA and ProposicionB # Si un pez pasa mas de 5 minutos fuera del agua, muere
Premisa2 = ProposicionA # Mi pez paso mas de 5 minutos fuera del agua

#Modus Ponens

if Premisa2:
    ProposicionB = True
    conclusion = "Mi pez ha muerto"
    print(conclusion)

