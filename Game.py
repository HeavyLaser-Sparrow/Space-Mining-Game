import time
import threading

class Game:
    def __init__(self):
        self.money = 0
        self.mining_rate = 1
        self.upgrades = {
            "mining_drone": {"cost": 10, "mining_rate_increase": 0.1},
            "mining_truck": {"cost": 500, "mining_rate_increase": 7},
            "mining_rover": {"cost": 1000, "mining_rate_increase": 15},
            "mining_station": {"cost": 5000, "mining_rate_increase": 100},
            "mining_platform": {"cost": 10000, "mining_rate_increase": 250}
        }
        self.owned_upgrades = set()
        self.running = True

    def mine(self):
        while self.running:
            self.money += self.mining_rate
            time.sleep(1)  # Mine money every second

    def purchase_upgrade(self, upgrade_name):
        if upgrade_name in self.upgrades:
            upgrade = self.upgrades[upgrade_name]
            #if upgrade_name in self.owned_upgrades:
             #  print(f"You already own the {upgrade_name}.")
              # return
            if self.money >= upgrade["cost"]:
                self.money -= upgrade["cost"]
                self.mining_rate += upgrade["mining_rate_increase"]
                self.owned_upgrades.add(upgrade_name)
                print(f"Purchased {upgrade_name}!")
            else:
                print("Not enough money to purchase upgrade.")
        else:
            print("Invalid upgrade name.")

    def display_status(self):
        print(f"Money: ${self.money}")
        print(f"Mining Rate: {self.mining_rate} money/second")
        print(self.upgrades)
        print(f"Owned Upgrades: {', '.join(self.owned_upgrades)}")

def game_loop(game):
    while True:
        game.display_status()
        command = input("Enter command (buy [upgrade_name] or quit): ").strip().lower()
        if command == "quit":
            game.running = False
            break
        elif command.startswith("buy "):
            _, upgrade_name = command.split(maxsplit=1)
            game.purchase_upgrade(upgrade_name)
        else:
            print("Unknown command. Use 'buy [upgrade_name]' or 'quit'.")

if __name__ == "__main__":
    game = Game()

    # Start mining in a separate thread
    mining_thread = threading.Thread(target=game.mine)
    mining_thread.start()

    # Run the game loop in the main thread
    game_loop(game)
    
    # Ensure the mining thread stops before exiting
    game.running = False
    mining_thread.join()
