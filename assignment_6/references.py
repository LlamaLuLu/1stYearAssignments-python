# To reformat references
# Lulama Lingela
# 17 March 2023

user_ref = input("Enter the reference:\n")

# identifies text before ')'; capitalises first letter per word
bracket_i = user_ref.find(")")
author = user_ref[:bracket_i + 1].title()
new_ref = user_ref.replace(user_ref[:bracket_i + 1], author)

# isolates title from ref
section = user_ref[bracket_i + 2:]
comma = section.find(",")
title = user_ref[bracket_i + 2:comma + bracket_i + 3]

new_ref = new_ref.replace(new_ref[bracket_i + 2:comma + bracket_i + 3], title.capitalize())
print(f"Reformatted reference:\n{new_ref}")