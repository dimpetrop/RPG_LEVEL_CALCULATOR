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
      f.write("\n\nSIMULATION "+ str(i) + " RESULTS " + "DIFFICULTY =" + str(DIFFICULTY) + "\nPlayers Completed " + str(PLAYERS_COMPLETED) + "\nPlayers in zone now "+ str(PLAYERS_IN_ZONE_NOW) + "\nAverage Player LVL " + str(PLAYERS_COMPLETED_AVG_LEVEL) + "\nPlayer LVL +"+ str(PLAYER_LVL) + "\nZone Level " + str(ZONE_LEVEL))
  print("Simulation Completed")

def find_difficulties():
  array = []
  with open("simulation_results.txt", "r") as f:
    for line in f:
      if "=" in line:
        toappend = line[len(line)-4:len(line)-1].replace("=", "")
        array.append(int(toappend))
    return array

def find_player_level():
  array = []
  with open("simulation_results.txt", "r") as f:
    for line in f:
      if "+" in line:
        toappend = line[len(line)-4:len(line)-1].replace("+", "")
        array.append(int(toappend))
  return array

def calculate_values(option):
  c = 1
  sum = mid = low = high = 0
  if option == 1:
    #print("Option 1: difficulties (calculate_values)")  #DEBUG
    array = find_difficulties()
  else:
    #print("Option 2: player lvl (calculate_values)")  #DEBUG
    array = find_player_level()
  for i in array:
    c += 1
    sum += i

    if 25 < i < 50:
      mid += 1
    if i < 25:
      low += 1
    if i > 50:
      high +=1
  avg = sum // c
  return [avg, low, mid, high]

def count(option):
  all = False

  while True:

    if option == 3:
      option = 1
      all =  True
    if option == 0:
      return
    
    if option == 1:
      array = calculate_values(1)
      print("\nAverage Difficulty LVL based on Simulation", array[0], "")
      print("Count of difficulties > 50", array[3])
      print("Count of difficulties 25 - 50", array[2])
      print("Count of difficulties < 25", array[1]) 
      if all:
        option = 2
    if option == 2:
      array = calculate_values(2)
      print("\nAverage Player LVL based on Simulation", array[0], "")
      print("Count of Player LVL > 50", array[3])
      print("Count of Player LVL 25 - 50", array[2])
      print("Count of Player LVL < 25", array[1]) 
      if all:
        option = 0



#Program Start
while True:
  option = int(input("\n\nSimulation [1]\nCount [2]\n"))

  if option == 1:
    simulation()
  elif option == 2:
    count(int(input("\nCount of Difficulties [1]\nCount of Player LVL [2]\nAll [3]\n")))
  elif option == 0:
    print("Exiting...")
    break
  else:
    while option not in range(1,3):
      print("\nIncorrect Input")
      option = int(input("\n\nSimulation [1]\nCount [2]\n"))