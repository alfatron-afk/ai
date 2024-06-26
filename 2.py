lM = 3  # Left side missionaries
lC = 3  # Left side cannibals
rM = 0  # Right side missionaries
rC = 0  # Right side cannibals

print("\nGame Start")
print("Now the task is to move all of them to the right side of the river.")
print("Rules:")
print("1. The boat can carry at most two people.")
print("2. If the number of cannibals is greater than the number of missionaries, the cannibals would eat the missionaries.")
print("3. The boat cannot cross the river by itself with no people on board.")

while True:
    print("\nLeft side -> Right side river travel")
    uM = int(input("Enter the number of missionaries to travel => "))
    uC = int(input("Enter the number of cannibals to travel => "))

    if uM == 0 and uC == 0:
        print("Empty travel is not possible. Re-enter:")
    elif (uM + uC) <= 2 and (lM - uM >= 0) and (lC - uC >= 0):
        lM -= uM
        lC -= uC
        rM += uM
        rC += uC
        break  # Correctly placed break statement when conditions are satisfied
    else:
        print("Wrong input or violating rules. Re-enter:")

    print("\nLeft side: ", end="")
    for _ in range(lM):
        print("M ", end="")
    for _ in range(lC):
        print("C ", end="")
    print("| --- |", end=" ")
    print("Right side: ", end="")
    for _ in range(rM):
        print("M ", end="")
    for _ in range(rC):
        print("C ", end="")
    print("\n")

print("\nLeft side: ", end="")
for _ in range(lM):
    print("M ", end="")
for _ in range(lC):
    print("C ", end="")
print("| --- |", end=" ")
print("Right side: ", end="")
for _ in range(rM):
    print("M ", end="")
for _ in range(rC):
    print("C ", end="")

print("\n\nAll missionaries and cannibals have crossed the river safely!")
