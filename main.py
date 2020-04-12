#! /usr/bin/python3
import os




def main():
    input_folder='/home/lindsay/Projects/MovieOrganizer/testData/input'
    output_folder='/home/lindsay/Projects/MovieOrganizer/testData/output'

    # List everything in the working folder
    folder_contents= os.system('ls '+input_folder)
    print(folder_contents)


if __name__=="__main__":
    main()
