from random import randrange


def simulation():
  print("Running Simulation...")
  with open("simulation_results.txt", "w") as f:
    for i in range(1,1001):
      PLAYERS_COMPLETED = randrange(1,1000)
      PLAYERS_IN_ZONE_NOW = randrange(1,200)
      PLAYERS_COMPLETED_AVG_LEVEL = randrange(1,100)
      PLAYER_LVL = randrange(1,100)
      ZONE_LEVEL = 30

      FACTOR_1 = PLAYERS_COMPLETED / PLAYERS_IN_ZONE_NOW
      FACTOR_2 = PLAYERS_COMPLETED_AVG_LEVEL
      FACTOR_3 = PLAYER_LVL - ZONE_LEVEL
      DIFFICULTY = int(FACTOR_1 + FACTOR_2 - FACTOR_3)

      if DIFFICULTY < 0:
        DIFFICULTY *= -1
      if DIFFICULTY == 0:
        DIFFICULTY = 25
      f.write("\n\nSIMULATION "+ str(i) + " RESULTS " + "DIFFICULTY =" + str(DIFFICULTY) + "\nPlayers Completed " + str(PLAYERS_COMPLETED) + "\nPlayers in zone now "+ str(PLAYERS_IN_ZONE_NOW) + "\nAverage Player LVL " + str(PLAYERS_COMPLETED_AVG_LEVEL) + "\nPlayer LVL "+ str(PLAYER_LVL) + "\nZone Level " + str(ZONE_LEVEL))
  print("Simulation Completed")

def find_difficulties():
  array = []
  with open("simulation_results.txt", "r") as f:
    for line in f:
      if "=" in line:
        toappend = line[len(line)-4:len(line)-1].replace("=", "")
        array.append(int(toappend))
    return array

def count(option):

  if option == 1:
    c = 0
    sum = mid = low = high = 0
    for i in find_difficulties():
      c += 1
      sum += i

      if 25 < i < 50:
        mid += 1
      if i < 25:
        low += 1
      if i > 50:
        high +=1


    avg = sum / c
    print("Average Difficulty LVL based on Simulation", avg, "")
    print("Count of difficulties > 50", high)
    print("Count of difficulties 25 - 50", mid)
    print("Count of difficulties < 25", low) 
  if option == 2:
    pass


#Program Start
while True:
  option = int(input("\n\nSimulation or Avg (choose 1 or 2)"))

  if option == 1:
    simulation()
  elif option == 2:
    count(1)
  elif option == 0:
    print("Exiting...")
    break
  else:
    while option not in range(1,3):
      print("Incorrect Input")
      option = input("Simulation or Count (choose 1 or 2)")