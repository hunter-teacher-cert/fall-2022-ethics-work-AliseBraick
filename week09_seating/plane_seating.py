def printSeats(seats):
    for i in range(len(seats)):
        # Use end  parameterto modify what gets printed at the end so its not a new line
        print(i+1, end=" ")
        print(seats[i][0], end=" ")
        print(seats[i][1], end=" ")
        print(seats[i][2], end=" ")
        print(seats[i][3])



seats = []
for i in range(7):
    seats.append(["A", "B", "C", "D"])

print("Welcome to the Airplane Seating Reservation System.")


filled = 0

    
# Keep looping until all seats are filled
while filled < 28:
    print("Please enter the seat (e.g.- 1A) you wish to reserve.")
    print("Enter q to exit.")
    print("")
    printSeats(seats)
    
    seatNumber = input("")
    if seatNumber == "q":
        print("Program ended.")
        break
    row = int(seatNumber[0]) - 1
    # Convert Column (e.g. A) to ascii value and substract 'A' value of 65 to get 0 based value    =
    col = ord(seatNumber[1]) - 65
    if (row < 0 or row > 7 or col < 0 or col > 4):
        print("Input error. Enter seat to assign (e.g., '1A')," + "or q to quit.")
        continue
    else:
        if (seats[row][col] != 'X'):
            seats[row][col] = 'X'
            filled += 1 # Increment counter for number of filled seats
            print(" ")
        else:
            print("This seat is already reserved. Please select a different seat.")




    
