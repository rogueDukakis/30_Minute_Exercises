users = {"bighead":"password", "richard":"algorithm","dinesh":"gilfoyle", "gilfoyle":"satan", "jian":"erlich"}

username = input("What is your username? ")
password = input("What is your password? ")
if username in users.keys():
    expected_password = users[username]
    if expected_password == password:
        print ("Welcome to Pied Piper!")
    else:
        print("You Huli bastard!")
else:
    print("Unknown user")