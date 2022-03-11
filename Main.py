import Functions.Help as a
import Functions.Clear as g
import Functions.Color as b
import Functions.Filesys as f
import Functions.CPassword as c
import Functions.Calculator as d
import Functions.HeadsandTails as e
import sys
import time


Run = True

# ##Password Verify## #
print("""

░█████╗░██████╗░░█████╗░░█████╗░  ░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
██║░░██║██████╔╝██║░░╚═╝███████║  ██║░░██║╚█████╗░
██║░░██║██╔══██╗██║░░██╗██╔══██║  ██║░░██║░╚═══██╗
╚█████╔╝██║░░██║╚█████╔╝██║░░██║  ╚█████╔╝██████╔╝
░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ░╚════╝░╚═════╝░
""")
pas = input("Please Enter Your Password:\n")
with open('OFB', "r") as myfile:
    data = myfile.read()
    
if pas != data:
    print("You Have Currently Entered The Wrong Password!")
    time.sleep(1)
    sys.exit()
else:
  a.help0()


# ## Main Loop ## #
def main():
    while Run is True:
        global lo
        lo = input("Please Enter A Command:\n")

        if lo == "1":
            a.help0()
        if lo == "2":
            d.Calc()
        if lo == "3":
            b.Color()
        if lo == "4":
            e.ht()
        if lo == "5":
            c.changep()
        if lo == "6":
            f.FILE()
        if lo == "7":
            g.Clear()

        #if keypre:
            #sys.exit()


main()
