class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        if self.is_alive():
            other.health -= self.attack_power
            print(f"{self.name} атакует {other.name} на {self.attack_power} урона.")
        else:
            print(f"{self.name} не может атаковать, потому что мертв.")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: {self.health} здоровья"

class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
        if self.computer.is_alive():
            self.computer_turn()
            self.declare_winner()

    def player_turn(self):
        self.player.attack(self.computer)
        self.print_status()

    def computer_turn(self):
        self.computer.attack(self.player)
        self.print_status()

    def print_status(self):
        print(self.player)
        print(self.computer)
        print("-" * 20)

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

# Пример использования
if __name__ == "__main__":
    game = Game(player_name="Игрок")
    game.start()