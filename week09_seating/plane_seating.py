# Contributors: Alise Braick, Benjamin Eckley

#  The Airplane Seating program asks the user for the seat they would like to reserve.
#  A layout of the plane is printed and an X is placed in the reserved seat. Cols A and A are windows, Ciols B and C are Aisle.
#  The program finds if the seat is available and if the entry is valid.  An input of 'q'
#  ends the program.

#  After a lot of difficulty we decided to go with an algorithm that went back to the days
#  when reserving a seat on an airplane actually counted for something and overbooked flights
#  didn't exist!

#  Obviously the algorithm we wanted to produce was beyond our coding prowess. After many
#  attempts we ended up finding a simple plane reservation code in Java and did our best
#  to translate it into Python.

#  The original Java source can be found here by author Quang Pham:
#  https://stackoverflow.com/questions/60895270/airplane-seating-program-2-dimensional-array

# Things we could NOT account for accessibility wise:
#	* Although families can choose their own seats, there is a possibility that no more twin seats are left
#	* People in need of special seating for physical disabilities


def printSeats(seats):
    for i in range(len(seats)):
        # Use end  parameter to modify what gets printed at the end so its not a new line
        print(i+1, end=" ")
        print(seats[i][0], end=" ")
        print(seats[i][1], end="  ")# space
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

