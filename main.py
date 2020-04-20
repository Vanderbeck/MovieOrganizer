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
        folders= str(  os.popen('ls -p '+self.input_folder+' | grep /').read()  ).split('\n')
        self.folders= [x for x in folders if x] #Strip empty entries
        files  = str(  os.popen('ls -p '+self.input_folder+' | grep -v /').read()  ).split('\n')
        self.files= [x for x in files if x]
        while folders:
            tmp=folders.pop()
            print("folder: ", tmp)
        while files:
            tmp = files.pop()
            print("Files: ", tmp)

    def handleFolders(self):
        try:
            self.foldername = self.folders[0]
            loop=True
        except:
            print("No More Folders")
            loop = False

        while loop:
            # List contents of folder
            print("Which of these is the video file?")
            print("CMD: ", "ls " + self.input_folder + "/" + self.foldername)
            ls = os.popen("ls \"" + self.input_folder + "/" + self.foldername + "\"").read().split('\n')
            # If the folder is empty, skip
            if len(ls) == 0:
                break
            # Loop through the folder contents and display them
            idx=0
            for l in ls:
                if l == '':
                    continue
                print( "(",idx, ") ", l )
                idx += 1
            # Ask user to select which file is the video
            tmp = input('? --> ')
            if not self.correctInput(tmp, idx-1):
                print("\n\n\n")
                continue
            # Set filename and do the renaming
            self.filename=str( ls[int(tmp)] )
            break

        self.splitNameAndExtension()
        while loop:
            # Prompt for input: Movie or Show
            print("\n\nFile to change: ", self.new_filename)
            tmp = input('Is it a Movie (1) or a TV Show (2)? Press (0) to skip\n')
            if not self.correctInput(tmp, 2):
                continue
            input_int = int(tmp)
            #Use input as intiger
            if input_int==0:
                print("\nSKIP\n")
                loop=False #break
            elif input_int==1:
                loop = self.movie()
                print("\nMovie\n")
            elif input_int==2:
                loop = self.show()
                print("\nTV Show\n")
            # Prompt user to change filename and move OR restart
            if loop:
                continue #Ignore if the other methods failed
            #Prompt to Restart process or move to output folder
            print('Output folder: ', self.output_folder+'/'+self.new_filename)
            tmp = input('\n\nThe new name will be: \"' +self.new_filename+self.year+self.ext+ '\" \
            \nIs this correct? (Y/n) --> ')
            if tmp=='n' or tmp=='N':
                loop=True
            else:
                #Make destination folder
                os.system("mkdir -p " + "\"" + self.output_folder + '/' + self.new_filename +"\"")
                #Move Entire Folder Contents
                os.system("mv " + "\"" + self.input_folder +"/" +self.foldername + "\"" + "/* " + \
                    "\"" + self.output_folder + "/" + self.new_filename + "\"")
                #Rename Movie File
                os.system("mv " + "\"" + self.output_folder + "/" + self.new_filename + "/" + self.filename + "\"" + " " + \
                    "\"" + self.output_folder + "/" + self.new_filename + "/" + self.new_filename+self.year+self.ext + "\"")
                # os.system("mv " + "\"" + self.input_folder + "/" + self.foldername + "/" + self.filename + "\"" + " " + \
                #     "\"" + self.output_folder + "/" + self.new_filename + "/" + self.new_filename+self.year+self.ext + "\"")

    def handleFiles(self):
        while self.files:
            self.filename = self.files.pop()
            self.splitNameAndExtension()
            loop=True
            while loop:
                # Prompt for input: Movie or Show
                print("\n\nFile to change: ", self.new_filename)
                tmp = input('Is it a Movie (1) or a TV Show (2)? Press (0) to skip\n')
                if not self.correctInput(tmp, 2):
                    continue
                input_int = int(tmp)
                #Use input as intiger
                if input_int==0:
                    print("\nSKIP\n")
                    loop=False
                    break
                elif input_int==1:
                    loop = self.movie()
                    print("\nMovie\n")
                elif input_int==2:
                    loop = self.show()
                    print("\nTV Show\n")
                # Prompt user to change filename and move OR restart
                if loop:
                    continue #Ignore if the other methods failed
                #Prompt to Restart process or move to output folder
                print('Output folder: ', self.output_folder,'/',self.new_filename)
                tmp = input('\n\nThe new name will be: \"' +self.new_filename+self.year+self.ext+ '\" \
                \nIs this correct? (Y/n) --> ')
                if tmp=='n' or tmp=='N':
                    loop=True
                else:
                    os.system("mkdir -p " + "\"" + self.output_folder + '/' + self.new_filename +"\"")
                    os.system("mv " + "\"" + self.input_folder + "/" + self.filename + "\"" + " " + \
                        "\"" + self.output_folder + "/" + self.new_filename + "/" + self.new_filename+self.year+self.ext + "\"")


    def splitNameAndExtension(self):
        idx = len(self.filename) #file is the filename string
        while True:
            idx-=1
            tmp = self.filename[idx]
            if tmp!='.':
                continue
            else:
                # Takes the extension including the period and stores it
                self.ext=self.filename[idx:len(self.filename)]
                self.new_filename=self.filename[0:idx]
                break


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
        outer_loop_continue=True
        while True:
            TD_out=self.titleDelimiter()
            if TD_out:
                break
        while True:
            TR_out=self.trimRight()
            if TR_out:
                break
        while True:
            TL_out=self.trimLeft()
            if TL_out:
                break
        while True:
            YB_out=self.yearBraket()
            if YB_out:
                break
        outer_loop_continue=False
        return outer_loop_continue # Return False to break the outer loop in handleFiles()

    def show(self):
        #
        pass

    def titleDelimiter(self):
        out=False
        # Request Input from User
        delim=input('Filename so far: '+ self.filename +
                    '\nSplit with delimeter --> ')
        # Sanitize delimeter input
        try:
            delim=str(delim)
            delim.strip()
        except:
            return out
        #Check if input was a proper delimeter
        if delim not in self.delims:
            print("Not a recognized delimeter.")
            return out
        # Split title or dont if the delimiter is ''
        if delim != '':
            filename_split = self.filename.replace(delim, " ")
        else:
            filename_split = self.filename
        # Show resultant title and confirm with user
        print("New Filename: ", filename_split)
        user_input=input("Was the title broken up correctly? (y/N) --> ")
        if user_input == 'y' or user_input=='Y':
            self.new_filename = filename_split
            print(self.new_filename)
            out = True
        else:
            out = False

            # os.system("mkdir -p "+self.output_folder+"/"+file_folder)
        # Return
        return out

    def trimRight(self):
        out=False
        # Request Input from User
        nTrim=input('Filename so far: '+ self.new_filename +
                    '\nTrim the right by how many chars? (guess) --> ')
        # Sanitize trim number input
        try:
            nTrim=int(nTrim)
        except:
            print("Not a number")
            return out
        #Check if input was a proper trim value
        if nTrim <0 or nTrim>=len(self.new_filename):
            print("Try another trim input. Too big? Too small?")
            return out
        # Shorten the filename
        filename_short = str(self.new_filename[0:len(self.new_filename)-nTrim])
        # Display filename to the User and confirm
        print("New Filename: ", filename_short)
        user_input=input("Was the title shortened correctly? (y/N) --> ")
        if user_input == 'y' or user_input=='Y':
            self.new_filename = filename_short
            print(self.new_filename)
            out = True
        else:
            out = False
            # os.system("mkdir -p "+self.output_folder+"/"+file_folder)
        # Return
        return out

    def trimLeft(self):
        out=False
        # Request Input from User
        nTrim=input('Filename so far: '+ self.new_filename +
                    '\nTrim the right by how many chars? (guess) --> ')
        # Sanitize trim number input
        try:
            nTrim=int(nTrim)
        except:
            print("Not a number")
            return out
        #Check if input was a proper trim value
        if nTrim <0 or nTrim>=len(self.new_filename):
            print("Try another trim input. Too big? Too small?")
            return out
        # Shorten the filename
        filename_short = str(self.new_filename[nTrim:len(self.new_filename)])
        # Display filename to the User and confirm
        print("New Filename: ", filename_short)
        user_input=input("Was the title shortened correctly? (y/N) --> ")
        if user_input == 'y' or user_input=='Y':
            self.new_filename = filename_short
            print(self.new_filename)
            out = True
        else:
            out = False
        # Return
        return out

    def yearBraket(self):
        out=False
        # Request Input from User
        year=input('Filename so far: '+ self.new_filename +
                    '\nAdd year to the end of title (hit enter for no year) --> ')
        # Sanitize trim number input
        try:
            self.year = ' ('+str(year)+')'
        except:
            print("Input Error")
            return out
        # Add year to filename
        filename_year = self.new_filename + self.year
        # Display filename to the User and confirm
        print("New Filename: ", filename_year)
        user_input=input("Was the year added correctly? (y/N) --> ")
        if user_input == 'y' or user_input=='Y':
            out = True
        else:
            out = False
        # Return
        return out

    def episodeNumber(self):
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
    # MO.handleFiles()
    MO.handleFolders()
