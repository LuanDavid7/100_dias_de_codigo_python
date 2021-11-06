# Band Name Generator

print("Seja muito bem vindo ao gerador de nome de bandas.")

# Iniciando variaveis como espaço vazio
city = ""
pet_name = ""

# simple check to make sure the user has entered something
while True:
    print("Qual é o nome da cidade em que você cresceu?")
    city = input("> ")
    # if there's no input, ask again
    if city == "":
        print("Você não digitou nada. Por favor tente novamente.")
    # if there's any input at all, break out of the loop
    else:
        break

# do the same for the pet name
while True:
    print("Qual é o nome do seu pet?")
    pet_name = input("> ")
    if pet_name == "":
        print("Você não digitou nada. Por favor tente novamente.")
    else:
        break

# output using f-strings makes the code much more readable
print(f"O nome da sua banda é {city} {pet_name}.")
