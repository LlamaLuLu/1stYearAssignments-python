# To determine if you should eat the cupcake or not
# Lulama Lingela
# 2 March 2023

print("Welcome to the 30 Second Rule Expert\n------------------------------------\nAnswer the following questions by selecting from among the options.")

q1 = input("Did anyone see you? (yes/no)\n")

# expert system based on decision tree
# first main case
if q1 == 'yes':
    q2 = input("Was it a boss/lover/parent? (yes/no)\n")
    
    if q2 == 'yes':
        q3 = input("Was it expensive? (yes/no)\n")
        
        if q3 == 'yes':
            q4 = input("Can you cut off the part that touched the floor? (yes/no)\n")
            
            if q4 == 'yes':
                print("Decision: Eat it.")
                
            else:
                print("Decision: Your call.")
                
        else:
            q4 = input("Is it chocolate? (yes/no)\n")
            
            if q4 == 'yes':
                print("Decision: Eat it.")
                
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
        
# second main case        
else:
    q2 = input("Was it sticky? (yes/no)\n")
    
    if q2 == 'yes':
        q3 = input("Is it a raw steak? (yes/no)\n")
        
        if q3 == 'yes':
            q4 = input("Are you a puma? (yes/no)\n")
            
            if q4 == 'yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
                
        else:
            q4 = input("Did the cat lick it? (yes/no)\n")
            
            if q4 == 'yes':
                q5 = input("Is your cat healthy? (yes/no)\n")
                
                if q5 == 'yes':
                    print("Decision: Eat it.")
                else:          
                    print("Decision: Your call.")
                
            else: 
                print("Decision: Eat it.")
            
    else:
        q3 = input("Is it an Emausaurus? (yes/no)\n")
        
        if q3 == 'yes':
            q4 = input("Are you a Megalosaurus? (yes/no)\n")
            
            if q4 == 'yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
                
        else:        
            q4 = input("Did the cat lick it? (yes/no)\n")
            
            if q4 == 'yes':
                q5 = input("Is your cat healthy? (yes/no)\n")
                
                if q5 == 'yes':
                    print("Decision: Eat it.")
                else:          
                    print("Decision: Your call.")
                
            else: 
                print("Decision: Eat it.")