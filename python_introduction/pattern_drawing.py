# Prompt User for pattern size
size = int(input("Enter the size of the pattern: "))
# Generate and print a simple pattern based on the size
i = 1 # outer loop (rows)
while i <= int(size):
    j = 1 # inner loop (columns)
    while j <= int(size):
        print("*", end=" ") # Print star without newline
        j += 1
    print() # Move to the next line after each row
    i += 1