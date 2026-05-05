# Log Analysis Program

file = open("CS4.txt", "r")

info = 0
error = 0
warning = 0

for line in file:
    if "INFO" in line:
        info += 1
    elif "ERROR" in line:
        error += 1
    elif "WARNING" in line:
        warning += 1

print("INFO count:", info)
print("ERROR count:", error)
print("WARNING count:", warning)

file.close()
