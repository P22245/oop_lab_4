## Project Overview
This project is a simple creature battle simulation using Python. The base class Creature defines
common attributes like name, health, and attack power. Subclasses such as FlyingCreature,
SwimmingCreature, and FireCreature extend Creature with special abilities like flying, diving, and using fire to boost attacks.

### Types of Creatures
1. **Creature** – The base class with basic attack and health.
2. **FlyingCreature** – Can fly and perform aerial attacks.
3. **SwimmingCreature** – Can dive and attack underwater.
4. **FireCreature** – Can ignite fire and use it to boost attack power.

## How the Classes Work

### Creature (Base Class)
- **Attributes:**  : name, hp, attack_power  
- **Methods:**  
  - attack(target) – deal damage to another creature  
  - is_alive() – check if the creature is still alive  
  - __str__() – display creature info  

### FlyingCreature
- **Extra Attribute:** : altitude  
- **Extra Method:** : fly_to(new_altitude) 
- **Attack:** Aerial attack that uses altitude info  

### SwimmingCreature
- **Extra Attribute:** : depth
- **Extra Method:** : dive_to(new_depth)  
- **Attack:** Underwater attack that uses depth info  

### FireCreature
- **Extra Attributes:** : fire_level, temperature  
- **Extra Methods:**  
  - ignite(level) – increase fire level  
  - heat(amount) – increase temperature  
- **Attack:** Base attack + bonus from fire level and temperature

## Project Structure
oop_creature_simulation/
│
├── creature_simulation.py # class, sub class, test code
└── README.md # This file

## How to Run
1. open vs code
2. run
