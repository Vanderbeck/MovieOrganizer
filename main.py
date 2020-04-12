#! /usr/bin/python3
import os
import subprocess

class MovieOrganizer():
    """docstring for ."""

    def __init__(self, arg1, arg2):
        super(MovieOrganizer, self).__init__()
        self.input_folder = arg1
        self.output_folder = arg2
        if arg1 is None or arg2 is None:
            print("must specify an input directory and an output directory.")
        print("New MovieOrganizer Class")
        # Initialize recognized filename delimeters
        self.delims= ' . , _ - \t '

    def parseInput(self):
        # List everything in the working folder
        folders= str(  os.popen('ls '+self.input_folder+'/*/').read()  ).split('\n')
        self.folders= [x for x in folders if x]
        files  = str(  os.popen('ls -p '+self.input_folder+' | grep -v /').read()  ).split('\n')
        self.files= [x for x in files if x]
        while folders:
            tmp=folders.pop()
            print("folder: ", tmp)
        while files:
            tmp = files.pop()
            print("Files: ", tmp)

    def handleFolders(self):
        pass

    def handleFiles(self):
        while self.files:
            self.filename = self.files.pop()
            print("File to change: ", self.filename)
            while True:
                # Prompt for input: Movie or Show
                tmp = input('\n\nIs it a Movie (1) or a TV Show (2)?\nPress 0 to skip\n')
                if not self.correctInput(tmp, 2):
                    continue
                input_int = int(tmp)
                #Use input as intiger
                if input_int==0:
                    print("\nSKIP\n")
                    break
                elif input_int==1:
                    out = self.movie(self.filename)
                    print("\nMovie\n")
                    if out == True:
                        break
                elif input_int==2:
                    out = self.show(self.filename)
                    print("\nTV Show\n")
                    if out == True:
                        break


    def splitNameAndExtension(self, file):
        idx = len(self.filename) #file is the filename string
        while True:
            idx-=1
            tmp = self.filename[idx]
            if tmp!=".":
                continue
            else:
                # Takes the extension including the period and stores it
                self.ext=self.filename[idx:len(self.filename)]
                self.filename=self.filename[0:idx]


    def correctInput(self, input, max):
        out =False
        # Is it an intiger?
        try:
            input_int = int(input)
            max_int = int(max)
        except:
            print("\n Input must be a number from 1 to ", max)
            return out
        # Intiger in range?
        if input_int >= 0 and input_int <= max_int:
            out = True
        # Return True or False
        return out

    def movie(self):
        out=False
        delim=Input('File: '+ self.filename +
                    '\nSplit with delimeter: ?\n')
        # Sanitize delimeter input
        try:
            delim=str(delim)
            delim.strip()
        except:
            return out

        if delim not in self.delims:
            print("Not a recognized delimeter.")
            return out

        file_split = self.filename.replace(delim, " ")
        os.system("mkdir -p "+self.output_folder+"/"+file_folder)
        pass

    def show(self, file):
        pass






if __name__=="__main__":
    # main()
    #Paths
    input_folder='/home/lindsay/Projects/MovieOrganizer/testData/input'
    output_folder='/home/lindsay/Projects/MovieOrganizer/testData/output'
    # Init Class
    MO = MovieOrganizer(input_folder, output_folder)
    MO.parseInput()
    print('\n \n \n')
    MO.handleFiles()
