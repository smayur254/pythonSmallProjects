import time
def scene():
    print("""WELCOME TO THE ADVENTURE GAME!
        Let's start the action! ☆-🎬-☆
        
        Lily wakes up in her bedroom in the middle of the night. She heard a loud BAN outside the house.
        Now she has two choices she can either stay in the room or check what the sound might be about.
        
        Type your choice: Stay or Evaluate?
    """)

    user_input =  (input())
    ans = "incorrect"
    time.sleep(2)
    while ans=='incorrect':
        if user_input.upper() ==  "STAY":
            print("\nLily decides to stay in the room and ends up staying inside forever as noone seems to come to help her.")
            ans = 'correct'
        elif user_input.upper() == "EVALUATE":
            print("Lily exits the room silently and reaches the main hall.")
            ans = 'correct'
            scene2()
        else:
            print("Enter correct choice: Stay or Evaluate?")
            user_input = input()

def scene2():
    print("""
            In the main hall, she finds a strange but cute teddy bear on the floor. 
            She wanted to pick the teddy up. 
            But should she? It doesn't belong to her. (•˳̂•̆)
            Type your choice: Pick or Ignore?
            """)

    time.sleep(2)
    user_input = input()
    ans = "incorrect"
    while ans=='incorrect':
        if user_input.upper() ==  "PICK":
            print("""\nThe moment Lily picked up the the teddy bear. 
            The Teddy bear starts TALKING!The bear tells Lily that 
            she is in grave danger as there is a monster in the house.
            And the monster has captured her PARENTS as well!
            But he hugged her and told her not to get scared as he knows how to beat the moster!""")

            time.sleep(2)

            print("""\nThe bear handed lily a magical potion which can weaken the monster 
            and make him run away! He handed her the potion and then DISAPPEARED! Lily moved forward.""")

            ans = 'correct'

            pick="True"

        elif user_input.upper()=='IGNORE':
            print("""\nLily decided not to pick up the bear and walked forward.""")
            ans='correct'
            pick="False"
        else:
            print("Wrong Input! Enter pick or ignore?")
            user_input=input()
    time.sleep(2)
    scene3(pick)

def scene3(pick_value):

    print("""\n\nAfter walking for a while, Lily saw the MONSTOR in front of her!
    It had red eyes and evil looks. She got very scared! """)

    time.sleep(2)

    if pick_value == "True":
        time.sleep(2)
        print("""But then she remembered! She had the magic portion and she threw it on the moster!
              Well she had nothing to lose!""")
        time.sleep(2)
        print("\n The monster SCREAMED in pain but he managed to make a portal and pushed Lily to a new world!")
    elif(pick_value=="False"):
        print("The monster attacked Lily and hurt her! She was then thrown to the new world by the monster!")

scene()
print("\n\n")
print("Story ends here.")