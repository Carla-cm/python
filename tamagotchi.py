import time

class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.felicidade = 100
        self.fome = 0

    def alimentar(self):
        if self.fome > 0:
            self.fome -= 10
            print(f"\n{self.nome} foi alimentado e sua fome diminuiu.")
        else:
            print(f"\n{self.nome} não está com fome.")

    def carinho(self):
        self.felicidade += 10
        print(f"\n{self.nome} recebeu carinho e ficou mais feliz.")

    def passear(self):
        self.felicidade += 20
        self.fome += 10
        print(f"\n{self.nome} foi passear e ficou mais feliz, mas também ficou com fome.")

    def mudar_emoji(self):
        print("Escolha um emoji para o seu bichinho:")
        print("1. 🐷")
        print("2. 🐱")
        print("3. 🐻")
        choice = input("Digite o número do emoji desejado: ")
        if choice == "1":
            self.emoji = "🐷"
        elif choice == "2":
            self.emoji = "🐱"
        elif choice == "3":
            self.emoji = "🐻"
        else:
            print("Emoji inválido!")

    def mudar_name(self):
        new_nome = input("Digite o novo nome para o seu bichinho: ")
        self.name = new_nome
        print(f"\nO nome de {self.name} foi alterado para {new_nome}.")

    def update(self):
        self.felicidade -= 1
        self.fome += 1

    def esta_vivo(self):
        return self.fome < 100 and self.felicidade > 0


def main():
    nome = input("Digite o nome do seu bichinho virtual: ")
    tamagotchi = Tamagotchi(nome)
    tamagotchi.emoji = "🐶"  # Emoji padrão

    start_time = time.time()

    while tamagotchi.esta_vivo():
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= 15 :
            tamagotchi.update()
            start_time = time.time()

        print("\n Ações disponíveis: ")
        print("1. Alimentar")
        print("2. Dar carinho")
        print("3. Levar para passear")
        print("4. Trocar de roupa (emoji)")
        print("5. Mudar de nome")
        print("0. Sair")

        choice = input("\n Escolha uma ação (0-5): ")

        if choice == "1":
            tamagotchi.alimentar()
        elif choice == "2":
            tamagotchi.carinho()
        elif choice == "3":
            tamagotchi.passear()
        elif choice == "4":
            tamagotchi.mudar_emoji()
        elif choice == "5":
            tamagotchi.mudar_name()
        elif choice == "0":
            break
        else:
            print("Opção inválida!")

    print(f"\n{tamagotchi.name} morreu. Fim do jogo.")


if __name__ == "__main__":
    main()
