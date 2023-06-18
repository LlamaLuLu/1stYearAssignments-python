# Allows user to input int values & query a 2-dimensional array of size 9 X 9
# Lulama Lingela
# 14 April 2023

grid = []
end = False

print("Enter an array:")
for row in range(9):   # creates 9x9 grid from user input
    new_row = input()
    grid.append(new_row)

# template_grid = ['359716482', '867345912', '413928675', '398574126', '546281739', '172639548', '984163257',
# '621857394', '735492861']

while not end:
    co_ords = input("Enter coordinates:\n").split(" ")
    if "-1" in co_ords:
        print("DONE")
        end = True
    else:
        x_coord = int(co_ords[0])   # row
        y_coord = int(co_ords[1])   # element in list
        value = grid[x_coord][y_coord]
        print(f"Value = {value}")
