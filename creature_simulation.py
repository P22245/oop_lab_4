class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"

# ===============================
# FlyingCreature Branch
# ===============================


class FlyingCreature(Creature):
    def __init__(self, name, hp, attack_power,altitude = 0):
        super().__init__(name, hp, attack_power)
        self.altitude = altitude

    def fly_to(self,new_altitude):
        self.altitude = (new_altitude)
        print(f"{self.name} flies to altitude {self.altitude} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return
        
        print(f"{self.name} swoops down from altitude {self.altitude}!")
        print(f"{self.name} performs an aerial attack on {target.name} for {self.attack_power} damage!") 
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0
        print(f"{target.name} HP is now {target.hp}")
        

# ===============================
# SwimmingCreature Branch
# ===============================

class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power,depth = 0):
        super().__init__(name, hp, attack_power)
        self.depth = depth


    def dive_to(self,newdepth):
        print(f"{self.name} dives to depth {newdepth} meters.")
        self.depth += newdepth

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return
        
        print(f"{self.name} attacks from underwater at depth {self.depth}!")
        print(f"It splashes {target.name} for {self.attack_power} damage!") 
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0
        print(f"{target.name} HP is now {target.hp}")


# ===============================
# FireCreature Branch
# ===============================

class FireCreature(Creature):
    def __init__(self, name, hp, attack_power, fire_level=0, temperature=0):
        super().__init__(name, hp, attack_power)
        self.fire_level = fire_level
        self.temperature = temperature

    def ignite(self, level):
        """Set fire_level (0–100)"""
        self.fire_level = max(0, min(100, level))
        print(f"{self.name} ignites to fire level {self.fire_level}!")

    def heat(self, amount):
        """Set temperature (can boost attack)"""
        self.temperature = amount
        print(f"{self.name} is heated to {self.temperature}!")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return
        bonus = int(self.attack_power * (self.fire_level/100)) + int(self.attack_power * (self.temperature/100))
        total_damage = self.attack_power + bonus

        print(f"{self.name} attacks with fire level {self.fire_level} and temperature {self.temperature} → +{bonus} fire damage!")
        target.hp = max(0, target.hp - total_damage)
        print(f"{target.name} HP is now {target.hp}")

# main code
if __name__ == "__main__":
    print("=== Creature Class Tests ===\n")

    # Test 1: Initialization
    goblin = Creature("Goblin", 30, 5)
    print("Test 1: Initialization")
    print(goblin)  # Expected: Goblin (HP: 30)
    print()

    # Test 2: Basic attack
    wolf = Creature("Wolf", 40, 10)
    sheep = Creature("Sheep", 25, 3)
    print("Test 2: Wolf attacks Sheep")
    wolf.attack(sheep)
    print(f"Sheep HP should now be 15 → Actual: {sheep.hp}")
    print()

    # Test 3: HP does not go below zero
    dragon = Creature("Dragonling", 50, 100)
    mouse = Creature("Mouse", 20, 1)
    print("Test 3: Dragonling overkills Mouse")
    dragon.attack(mouse)
    print(f"Mouse HP should now be 0 → Actual: {mouse.hp}")
    print()

    # Test 4: is_alive()
    slime = Creature("Slime", 10, 2)
    print("Test 4: Slime alive?")
    print("Slime should be alive →", slime.is_alive())
    slime.hp = 0
    print("Slime should NOT be alive →", slime.is_alive())
    print()

    # Test 5: Dead creature cannot attack
    ghost = Creature("Ghost", 0, 10)
    knight = Creature("Knight", 50, 7)
    print("Test 5: Ghost tries to attack Knight")
    ghost.attack(knight)
    print(f"Knight HP should remain 50 → Actual: {knight.hp}")
    print()

    # Test 6: Multiple attacks
    print("Test 6: Goblin attacks Slime twice")
    slime.hp = 10
    goblin.attack(slime)
    goblin.attack(slime)
    print(f"Slime should be at HP 0 → Actual: {slime.hp}")
    print()
    print("=== Tests Completed ===")
    print()

    print("=== FlyingCreature Tests ===\n")
    hawk = FlyingCreature("Sky Hawk", 50, 8)
    hawk.fly_to(120)
    print(f"Altitude should be 120 → Actual: {hawk.altitude}")

    dummy = Creature("Practice Dummy", 40, 0)
    hawk.attack(dummy)
    print(f"Dummy HP should be 32 → Actual: {dummy.hp}")
    dummy.attack(hawk)
    print()   
    print("=== Tests Completed ===")
    print()

    print("=== SwimmingCreature Tests ===\n")
    serpent = SwimmingCreature("Aqua Serpent", 60, 7)
    serpent.dive_to(30)
    print(f"Depth should be 30 → Actual: {serpent.depth}")

    dummy = Creature("Practice Dummy", 40, 0)
    serpent.attack(dummy)
    print(f"Dummy HP should be 33 → Actual: {dummy.hp}")
    print()
    print("=== Tests Completed ===")
    print()

    print("=== FireCreature Tests ===\n")
    flame = FireCreature("Blaze Drake", 60, 10)
    flame.heat(30)
    print(f"Temperature should be 30 → Actual: {flame.temperature}")

    dummy = Creature("Practice Dummy", 50, 0)
    flame.attack(dummy)
    print(f"Dummy HP should be 40 → Actual: {dummy.hp}")
    dummy.attack(flame)
    print()
    print("\n=== Tests Completed ===\n")
    print()
    