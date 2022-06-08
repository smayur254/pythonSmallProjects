
response =  "Y"
user_email = input("Enter your email address.\n").strip()
while response == "Y":
    username = user_email[:user_email.index("@")]
    domain = user_email[user_email.index("@")+1:]

    print(f"\nYour username is {username}.")
    print(f"Your domain is {domain}.\n" )

    question = input("Want to try again, press Y or N?\n")
    if question.upper() ==  "Y":
        user_email = input("Enter your email address again.\n").strip()
    else:
        response ="N"