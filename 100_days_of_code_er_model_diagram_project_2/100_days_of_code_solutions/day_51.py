myEvents = []

# Will crash on first run if file doesn't exist
#f = open("calendar.txt","r")
#myEvents = eval(f.read())
#f.close() # Forgot to close the file


def prettyPrint():
  print()
  for row in myEvents:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()


while True:
  menu = input("1: Add, 2: Remove\n")

  if menu == "1":
    event = input("What event?: ").capitalize()
    date = input("What date?: ")
    row = [event, date]
    myEvents.append(row)
    prettyPrint()

  else:
    criteria = input("What event do you want to remove?: ").title()
    for row in myEvents:
      if criteria in row:
        myEvents.remove(row)  # List identifier wasn't correct

  # Lines below weren't indented to make them part of the loop.
  f = open("calendar.txt", "w")
  f.write(str(myEvents))
  f.close()
