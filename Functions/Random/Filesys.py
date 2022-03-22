import os
import Functions.Settings.LIST as ddd
import Functions.Settings.Changedir as vvv
import Functions.Settings.CAT as kkjh

def FILE():
    print("FILE SYSTEM")
    print("File Commands:")
    print("[1]List Dir")
    print("[2]CD Dir")
    print("[3]cat <Coming soon>")
    print(f"Your Current Directory: {ddd.FOLDER_PATH}")
    jooo = input("What Would You Like to do?")
    
    
    if jooo == "1":
        ddd.ls()

    if jooo == "2":
        vvv.cd()
    
    if jooo == "3":
        kkjh.cat()
