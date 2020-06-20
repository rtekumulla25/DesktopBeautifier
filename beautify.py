import os
import shutil

def destination_path():  # Where to move the files  (default = Documents)
    
    reply = input("Do you want to move your files to the Documents folder?(Y/N): ")
    if(reply == 'Y'):
        path = "C:/Users/rteku/Documents/Desktop test"
    else:
        path = input(r"Specify the exact path of the Destination folder: ")
    return path

#def std_files():    # Which files to keep   (default = Recycle Bin)
    #root_ext = os.path.splitext(pathway)

#def get_username():  #returns the username which is used to specify the path

def categorize():
    reply = input("Do you want to categorize the files based on their extensions?(Y/N): ")
    if reply == 'Y':
        return True
    else:
        return False
    


def file_move(source, path, categorize):    # Move the unneccessary files
    if (categorize == False):
        for filename in os.listdir(source):
            if filename == "Recycle Bin":
                continue
            else:
                shutil.move(os.path.join(source, filename), path, copy_function = shutil.copytree)
    else:
        for filename in os.listdir(source):
            if filename == "Recycle Bin":
                continue
            elif os.path.splitext(filename) == ".txt":
                shutil.move(os.path.join(source, filename), os.path.join(path, "text files"), copy_function = shutil.copytree)
            elif os.path.splitext(filename) == ".jpg" or os.path.splitext(filename) == ".png" or os.path.splitext(filename) == ".gif":
                shutil.move(os.path.join(source, filename), os.path.join(path, "image files"), copy_function = shutil.copytree)
            elif os.path.splitext(filename) == ".doc" or os.path.splitext(filename) == ".docx" or os.path.splitext(filename) == ".pdf" or os.path.splitext(filename) == ".ppt":
                shutil.move(os.path.join(source, filename), os.path.join(path, "doc files"), copy_function = shutil.copytree)
            elif os.path.splitext(filename) == ".avi" or os.path.splitext(filename) == ".mp4" or os.path.splitext(filename) == ".3gp" or os.path.splitext(filename) == ".wmv" or os.path.splitext(filename) == ".ogg":
                shutil.move(os.path.join(source, filename), os.path.join(path, "video files"), copy_function = shutil.copytree)
            elif os.path.splitext(filename) == ".wav" or os.path.splitext(filename) == ".mp3" or os.path.splitext(filename) == ".flac" or os.path.splitext(filename) == ".aac":
                shutil.move(os.path.join(source, filename), os.path.join(path, "audio files"), copy_function = shutil.copytree)
            elif os.path.splitext(filename) == ".exe":
                shutil.move(os.path.join(source, filename), os.path.join(path, ".exe files"), copy_function = shutil.copytree)
            elif os.path.splitext(filename) == ".zip" or os.path.splitext(filename) == ".rar" or os.path.splitext(filename) == ".7z":
                shutil.move(os.path.join(source, filename), os.path.join(path, "compressed files"), copy_function = shutil.copytree)
            else:
                shutil.move(os.path.join(source, filename), os.path.join(path, "miscellaneous"), copy_function = shutil.copytree)




def file_loc():     # Where the files are located (default = Desktop)
    reply = input("Are your files located on Desktop?(Y/N): ")
    if(reply == 'Y'):
        source = "C:/Users/rteku/Desktop/source test"
    else:
        source = input(r"Specify the exact path of the folder you have your files in: ")
    return source


def main():
    
  """  source = file_loc()
    path = destination_path()
    cat = categorize()
    file_move(source, path, cat) """
    

main()