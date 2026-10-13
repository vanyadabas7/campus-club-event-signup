event_name = input("Enter event name: ")
capacity = int(input("Enter event capacity: "))

participants = []

try:
  with open("participants.txt", "r") as file:
    saved_event = file.readline().strip()
    saved_capacity = int(file.readline().strip())

    if saved_event == event_name and saved_capacity == capacity:

      for line in file:
        name = line.strip()

        if len(participants) < capacity:
          participants.append(name)
        else:
          break

      print("Previous responses loaded.", len(participants), "participant(s) registered.")

    else:
      print("Event not found. Creating a new list.")

except FileNotFoundError:
  print("No data found")

while True:
  print(event_name)
  print("1. Register participant")
  print("2. Remove participant")
  print("3. List participants")
  print("4. Show remaining spaces")
  print("5. Save")
  print("6. Exit")
  choice = int(input("Choose an option (1-6): "))

  def spaces_remaining():
    spaces_remaining = capacity - len(participants)
    print("Spaces remaining:", spaces_remaining)

  if choice == 1:
    if len(participants) < capacity:
      name = input("Enter participant name: ")
      participants.append(name)
      print("Participant registered!")
    else:
      print("Sorry, the event is full :(")

    spaces_remaining()

  elif choice == 2:
    name = input("Enter participant name: ")
    if name in participants:
      participants.remove(name)
      print("Participant removed!")
    else:
      print("Participant not found")

    spaces_remaining()

  elif choice == 3:
    print("Participants:")
    number = 1
    for name in participants:
      print(number, ".", name)
      number += 1

    spaces_remaining()

  elif choice == 4:
    if len(participants) == 0:
      print("No participants registered yet.")
    else:
      spaces_remaining()

  elif choice == 5:
    with open("participants.txt", "w") as file:
      file.write(event_name + "\n")
      file.write(str(capacity) + "\n")
      for name in participants:
        file.write(name + "\n")
      print("Data saved successfully!")

    spaces_remaining()

  elif choice == 6:
    break

  else:
    print("Invalid option. Please select a number from 1-6.")
