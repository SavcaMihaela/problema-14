S1=str(input("Introduceti primul sir:"))
S2=str(input("Introduceti al doilea sir:"))
##Caracterile care se intalnesc in cel putin un sir
print(f'{set(S1)&set(S2)}')
##Caracterele care apar in ambele siruri
print(f'{set(S1)|set(S2)}')
##Caracterele care apar doar in primul sir
print(f'{set(S1)-set(S2)}')