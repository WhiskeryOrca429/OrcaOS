import base64

def changep():
    with open('.\OFB', "r") as myfile:
        data = myfile.read()
    ch = input("Would you like to change your password?\n[Y-N]\n")
    if ch == "y":
        changing = input("Please enter your new password\n")
        with open('.\OFB', "w") as myfile:
            data = myfile.write(changing)
        print(f"Your Password Has Been Changed To {changing}\n Please Note You Will Use This Password From Now On (Dont Forget It)")

    