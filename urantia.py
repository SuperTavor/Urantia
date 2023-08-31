from operator import truediv
import os
import fileinput
import sys

def replace_keyword(folder_path, old_keyword, new_keyword, reverse=False):
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
                for line in file:
                    if reverse:
                        print(line.replace(new_keyword, old_keyword), end='')
                    else:
                        print(line.replace(old_keyword, new_keyword), end='')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: urantia [extractedFaPath] [original mod region]")
        sys.exit(1)

    folder_path = sys.argv[1]
    old_keyword = "engb"
    new_keyword = "en"
    usa = False
    eur = False
    
    if len(sys.argv) == 4 and sys.argv[3].lower() == "usa":
        usa = True
    if len(sys.argv) == 4 and sys.argv[3].lower() == "eur":
        eur = True
    replace_keyword(folder_path, old_keyword, new_keyword, usa)
    if usa:
        print("Ported from US to EUR.")
    else:
        print("Ported from EUR to US.")
