# Assists with debugging Python programs
# Lulama Lingela
# 4 May 2023

import os
tracer_motto = '"""DEBUG"""'


def func_name(line):
    """Isolates function name."""
    line = line[4:]
    # accounts for if there is a space before brackets after name of func def
    space = line.find(" ")
    bracket = line.find("(")
    if (space < bracket) and (space != -1):
        name = line[:space]
    else:
        name = line[:bracket]
    return name


def tracer(file):
    global tracer_motto
    for line in file:
        if "def" in line:
            file[file.index(line)] = f"{line}    {tracer_motto};print('{func_name(line)}')\n"
    file.insert(0, tracer_motto + "\n")
    return file


def debugger(file):
    global tracer_motto
    file.remove(file[0])
    for line in file:
        if "def" in line:
            next_line = file.index(line) + 1
            file.remove(file[next_line])
    return file


def main():
    print("***** Program Trace Utility *****")
    og_filename = input("Enter the name of the program file:\n").strip()
    if os.path.isfile(og_filename):  # checks that text file exists
        og_file = open(f"{og_filename}", "r")
        copy = og_file.readlines()
        og_file.close()

        if copy[0].strip() == tracer_motto:   # program already traced
            # execute debug
            print("Program contains trace statements\nRemoving...Done")
            og_file = open(og_filename, "w")
            og_file.writelines(debugger(copy))
        else:
            # execute trace
            print("Inserting...Done")
            og_file = open(og_filename, "w")
            og_file.writelines(tracer(copy))
        og_file.close
    else:
        print(f"Sorry, could not find file '{og_file}'.")

if __name__ == "__main__":
    main()
