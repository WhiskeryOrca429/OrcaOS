from fileinput import filename
import os 

global FOLDER_PATH
FOLDER_PATH = ".\\ODrive"


def ls():
    fileNames = os.listdir(FOLDER_PATH)
    for fileName in fileNames:
        print(f"FileName: {os.path.join(fileName)}")


if __name__ == "__main__":
    ls(FOLDER_PATH)