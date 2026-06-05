import random

class DetectiveGame:
    def __init__(self):
        self.ages = [22, 28, 35, 42, 50, 65]
        self.jobs = ["Doctor", "Artist", "Hacker", "Chef", "Spy", "Pilot"]
        self.actions = ["reading", "drinking coffee", "typing fast", "looking around", "whispering"]

    def generate_person(self):
        return {
            "age": random.choice(self.ages),
            "job": random.choice(self.jobs),
            "action": random.choice(self.actions)
        }

    def start(self):
        print("=== WHO IS THE TARGET? ===")
        try:
            pool_size = int(input("Enter number of suspects (e.g., 5, 10, 20): "))
            attempts = int(input("Enter number of attempts allowed: "))
        except ValueError:
            print("Invalid input. Using defaults: 5 suspects, 3 attempts.")
            pool_size = 5
            attempts = 3

        suspects = []
        while len(suspects) < pool_size:
            person = self.generate_person()
            if person not in suspects:
                suspects.append(person)

        target = random.choice(suspects)

        print("\n--- TARGET DESCRIPTION ---")
        print(f"Age: {target['age']}")
        print(f"Job: {target['job']}")
        print(f"Action: {target['action']}")
        print("--------------------------\n")

        print("--- SUSPECT LIST ---")
        for i, suspect in enumerate(suspects, 1):
            print(f"[{i}] Age: {suspect['age']} | Job: {suspect['job']} | Doing: {suspect['action']}")
        print("--------------------\n")

        while attempts > 0:
            print(f"Attempts left: {attempts}")
            try:
                guess = int(input(f"Enter the suspect number (1-{pool_size}): "))
                if guess < 1 or guess > pool_size:
                    print("Invalid suspect number. Try again.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue

            if suspects[guess - 1] == target:
                print("\nCORRECT! You found the target! Game Over.")
                return
            else:
                print("Wrong suspect! Look closer.")
                attempts -= 1

        print(f"\nGAME OVER! You ran out of attempts.")
        print(f"The correct target was Suspect #{suspects.index(target) + 1}")

if __name__ == "__main__":
    game = DetectiveGame()
    game.start()
