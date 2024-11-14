#esnquanto o numero for menor que 100
#se o numero for divisivel por dois com resto zero ou divisivel por três

for i in range(1,101):
    if i % 2 == 0 or i % 3 == 0:
        print(f"O número {i} é divisivel por 2 ou por 3")

input("Pressione Enter para sair...")