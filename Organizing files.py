import os
import shutil

DOWNLOAD_FILE = r'C:\\Users\\ashis\\Downloads'
STORING_FILE = r'D:\\Download\\'

paths = []
def get_path():
    os.chdir(DOWNLOAD_FILE)
    for file in os.listdir():
            f = os.path.splitext(file)
            print(f[1][1:])
            try:
                os.chdir(STORING_FILE)
                if os.path.exists(f[1][1:]):
                    print(f[1][1:])
                    os.chdir(DOWNLOAD_FILE)
                    shutil.move(file, STORING_FILE+f[1][1:])
                else:
                    PC = os.makedirs(f[1][1:])
                    dirs = os.getcwd() +'\\'+f[1][1:]
                    paths.append(dirs)
            except Exception as e:
                print('File Alraedy Exist')

def moving_file():
    os.chdir(DOWNLOAD_FILE)
    for file in os.listdir():
        f = os.path.splitext(file)
        #print(f[1][1:])
        for i in range(len(paths)):
            if os.path.basename(paths[i]) == f[1][1:]:
                shutil.move(file, paths[i])
        

get_path()
moving_file()