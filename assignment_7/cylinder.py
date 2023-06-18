# Calculates the volume of cylinder given integer values for its diameter and height.
# Lulama Lingela
# 3 April 2023

from math import pi


def circle_area(diameter):
    """Calculates & returns area of circle with that diameter"""
    area = .25 * pi * diameter ** 2
    return area


def cylinder_volume(diameter, height):
    """Calculates & returns volume of cylinder with that diameter and height. Obtains A value from circle_area func."""
    volume = circle_area(diameter) * height
    return volume


def main():
    """ask the user to input diameter and height and will call cylinder_volume, printing out the result"""
    diameter = int(input("Enter diameter:\n"))
    height = int(input("Enter height:\n"))
    cylinder_volume(diameter, height)
    print(f"The volume of the cylinder is {format(cylinder_volume(diameter, height), '.2f')}")


if __name__ == '__main__':
    main()
