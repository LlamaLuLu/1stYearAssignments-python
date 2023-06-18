# To do basic vector calculations in 2 dimensions: addition, dot product and cross product
# Lulama Lingela
# 14 April 2023

from math import sqrt


def obtain_mag(vec):
    """Returns magnitude of vector."""
    vector = vec.split(" ")
    vec_new = 0
    for comp in vector:   # calculation
        vec_new += int(comp) ** 2
    vec_new = sqrt(vec_new)
    return f"Magnitude of the vector is: {round(vec_new, 1)}"


def vector_add(v1, v2):
    """Returns result of adding 2 vectors."""
    vec_1 = v1.split(" ")
    vec_2 = v2.split(" ")
    vec_new = ""
    for comp in range(len(vec_1)):   # calculation
        comp_sum = int(vec_1[comp]) + int(vec_2[comp])
        vec_new += str(comp_sum) + ", "
    return f"Sum of the vectors is: ({vec_new[:-2]})"


def scalar_multiply(vec, m):
    """Returns product of vector & value 'm'."""
    vector = vec.split(" ")
    vec_new = ""
    for comp in vector:   # calculation
        comp_new = int(comp) * m
        vec_new += str(comp_new) + ", "
    return f"Scalar multiplication of the vector is: ({vec_new[:-2]})"


def dot_product(v1, v2):
    """Returns product of 2 vectors with 2 components."""
    vec_1 = v1.split(" ")
    vec_2 = v2.split(" ")
    vec_new = 0
    for comp in range(len(vec_1)):   # calculation
        comp_product = int(vec_1[comp]) * int(vec_2[comp])
        vec_new += comp_product
    return f"Dot product of the vectors is: {vec_new}"


def cross_product(v1, v2):
    """Returns product of 2 vectors with 3 components."""
    vec_1 = v1.split(" ")
    vec_2 = v2.split(" ")
    # calculation
    vx = int(vec_1[1]) * int(vec_2[2]) - int(vec_1[2]) * int(vec_2[1])
    vy = int(vec_1[2]) * int(vec_2[0]) - int(vec_1[0]) * int(vec_2[2])
    vz = int(vec_1[0]) * int(vec_2[1]) - int(vec_1[1]) * int(vec_2[0])
    vec_new = str(vx) + ", " + str(vy) + ", " + str(vz)
    return f"Cross product of the vectors is: ({vec_new})"


end = False
options = ['1', '2', '3', '4', '5', '6']

while not end:
    print("""Choose an option:
1. Magnitude of a vector
2. Vector addition
3. Scalar multiplication
4. Dot product of two vectors
5. Cross product of two 3-dimensional vectors
6. Exit""")
    user_opt = input()

    if user_opt in options:
        if user_opt == '1':
            vector = input("Enter the components of the vector separated by spaces:\n")
            print(obtain_mag(vector))

        elif user_opt == '2':
            vec_1 = input("Enter the components of the first vector separated by spaces:\n")
            vec_2 = input("Enter the components of the second vector separated by spaces:\n")
            if vec_1.count(" ") != vec_2.count(" "):
                print("Error: Vectors must have the same length.")
            else:
                print(vector_add(vec_1, vec_2))

        elif user_opt == '3':
            vector = input("Enter the components of the vector separated by spaces:\n")
            scalar = int(input("Enter the scalar:\n"))   # working
            print(scalar_multiply(vector, scalar))

        elif user_opt == '4':
            vec_1 = input("Enter the components of the first vector separated by spaces:\n")
            vec_2 = input("Enter the components of the second vector separated by spaces:\n")
            if vec_1.count(" ") != vec_2.count(" "):
                print("Error: Vectors must have the same length.")
            else:
                print(dot_product(vec_1, vec_2))

        elif user_opt == '5':
            vec_1 = input("Enter the components of the first 3-dimensional vector separated by spaces:\n")
            vec_2 = input("Enter the components of the second 3-dimensional vector separated by spaces:\n")
            if vec_1.count(" ") != 2 or vec_2.count(" ") != 2:
                print("Error: Vectors must have the same length and 3-dimensional.")
            else:
                print(cross_product(vec_1, vec_2))

        elif user_opt == '6':
            print("Exiting...")
            end = True

    else:
        print("Invalid choice. Please choose a valid option.")
