import os
import Functions.LIST as ddd
import Functions.Changedir as vvv

def FILE():
    print("FILE SYSTEM")
    print("File Commands:")
    print("[1]List Dir")
    print("[2]CD Dir")
    print(f"Your Current Directory: {ddd.FOLDER_PATH}")
    jooo = input("What Would You Like to do?")
    
    
    if jooo == "1":
        ddd.ls()

    if jooo == "2":
        vvv.cd()
