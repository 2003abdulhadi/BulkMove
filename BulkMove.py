import shutil
import os
import pywin32_system32
from pyuac import main_requires_admin

def moveFiles(src: str):
    confirm = False
    while(not confirm):
        fileType = input("What item's would you like to group: ")
        confirm = True if input("Confirm you're choice (Y/N): ") == 'Y' else False

    destDir = ""
    while(not os.path.isdir(destDir)):
        destDir = input("Provide a destination directory: ")

    for root, dirs, files in os.walk(src):
        if(root == destDir):
            continue
        for file in files:
            if(fileType.lower() in file.lower()):
                print(f'moving: {file} from {root}')
                shutil.move((root + '\\' + file), (destDir + '\\' + file))

def cleanDirectory(src: str):

    fullyCleared = False

    while(not fullyCleared):
        fullyCleared = True
        for root, dirs, files in os.walk(src):
            with os.scandir(root) as it:
                if not any(it):
                    fullyCleared = False
                    print(f'{root} is empty')
                    os.rmdir(root)


'''
uncomment the line below if you run into permission issues
this will launch the script as an admin
'''
# @main_requires_admin
def main():
    
    srcDir = ""
    while(not os.path.isdir(srcDir)):
        srcDir = input("Provide a source directory: ")

    moveFiles(srcDir)
    cleanDirectory(srcDir)

if __name__ == "__main__":
    main()