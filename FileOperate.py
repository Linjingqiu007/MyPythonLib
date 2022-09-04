# Date 2022/09/04
# Author Lin jingqiu
# This Lib is for File Operation

import os

class fileOperation(object):

    def __init__(self):
        self.fileName = None
        self.filePath = None

    def newDir(self,path,name):
        a = os.path.exists(os.path.join(path,name))
        if a:
            print("The folder is already exists")
        else:
            os.mkdir(os.path.join(path,name))
            a = os.path.exists(os.path.join(path,name))
            if a:
                print("The folder built success")
            else:
                print("The folder built fail")

    def delDir(self,path,name):
        a = os.path.exists(os.path.join(path,name))
        if a:
            os.rmdir(os.path.join(path,name)) 
        else:
            print("The folder is not exists")
        a = os.path.exists(os.path.join(path,name))
        if a:
            print("The folder deleted fail")
        else:
            print("The folder deleted success")


# if __name__ == "__main__":
#     myfile = fileOperation()
#     myfile.newDir("D:\git codebase\MyPythonLib","abc")
#     myfile.delDir("D:\git codebase\MyPythonLib","abc")
#     del myfile