# Logic


**1) While parsing through the torrent download folder, is this a file? or a folder? or skip?**
- Be sure to show folder and contents

## Folder Logic
- Find video file(s) (size? known file endings?)
- Prompt if list is good (Later, give option to modify the list)
- Prompt for numbers to select what to keep?(comma seperated or space)
- Move to **2)**

## File Logic
- Move to **2)**



**2) Is is a Movie or a show**

## Movie Logic
- Part of an existing series of movies? (Helps prompt for title)
- call `new_title_generaor()`
- Pass file or Folder to **3)**

## Show Logic
- Is it one of these pre-existing shows? (Show list and pick)
- If not pre-existing, type a new show title. (Fill in sugested with "." seperated version of existing name)
- Season? (Show list and pick if existing. Prompt for season number if new.)
- call `New_title_generator()`
- Pass file/Folder and show info and season info to **3)**

**3) Put video/video folder Somewhere**
- Use aquired info to make the template in **Desired Result** happen.


**New_title_generator()**
## 2.A
- break on what character? 
- Default "." 
- Then rename.

## 2.B
- Braketize Year?
- ... RegEx?
- Then rename

## 2.C
- cut to where (number) 
- Display result. 
- New number = New length and display again. 
- bank or 0 = good to rename





# Desired Reslt
## Movies
Plex Folder
|
| Movies
| | Movie 1 Folder (year)
| | | Movie (year).mov
| | | Other_file.whatever
| | | Other_file_2.whatever

## Shows
Plex Folder
|
| Shows
| | Show 1 Folder
| | | Season 1
| | | | Show Name Episode 1 - Episode Title.mov
| | | | Show Name Episode 2 - Episode Title 2.mov
| | | | Other File.Whatever
| | | Season 2
| | | | Show Name Episode 1 - Episode Title.mov
| | | | Show Name Episode 2 - Episode Title 2.mov
| | | | Other File.Whatever


#Known defficiencies to work on:
- a folder insde one of the movie folders will be treated like a file. IE, we don't do recursion to see whats inside and delete parts.

#known movie extensions
- mkv
- mp4
- mov
- wmv
- avi
- 
