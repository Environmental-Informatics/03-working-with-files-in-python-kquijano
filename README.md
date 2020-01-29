# Environmental Informatics

## Assignment 03 - Using Files and Simple Data Structures with Python

### Lab Objectives

On completion of this lab, students will be able to:
1. Use Python's built-in file functions and methods to open, read and write the contents of data files; and
2. Use Python's built-in data structures to organize and summarize data.

### Reading Assignment

Original reading assignment
- [Think Python 2e](https://greenteapress.com/wp/think-python-2e/)
  - Chapter 8 Strings,
  - Chapter 14 Files, plus review 
    - Chapter 10 Lists, 
    - Chapter 11 Dictionaries, and 
    - Chapter 12 Tuples.

But in further research, I have found that this set of document is a better overview of the material being covered this week:
- [Think Python 2e](https://greenteapress.com/wp/think-python-2e/): Chapter 8 Strings
- [Python for Data Analysis, 2e](https://learning.oreilly.com/library/view/python-for-data/9781491957653/): [Chapter 3. Built-in Data Structures, Functions, and Files](https://learning.oreilly.com/library/view/python-for-data/9781491957653/ch03.html)

### Practical Practice

- Complete the [Introduction to Working with Files in Python](https://wiki.itap.purdue.edu/display/environmentalinformatics/Introduction+to+working+with+files+in+Python) tutorial at the [Environmental Informatics Wiki](https://wiki.itap.purdue.edu/display/environmentalinformatics) site.
- Complete example exercises as needed from the reading materials.

### The Lab Assignment

Write a Python code named **"Evaluate_Raccoon_Life.py"** to do the following:
1. Open the data file 2008Male00006.txt (available in this GitHub repository) using the built-in file open function as described in [Introduction to Working with Files in Python](https://wiki.itap.purdue.edu/display/environmentalinformatics/Introduction+to+working+with+files+in+Python).  
   - This file contains output from a Raccoon behavior model which describes the movement of a simulated raccoon named George over the course of a day.  
   - The file is comma separated, expect for the last line which contains only one field that provides George's status at the end of the model simulation.
   
2. Store data from the file in a Dictionary, where key terms are the headers of each column and each key term refers to the list of values in the column.
   - Note that your program will need to catch that the last line is different, and store that information separately.
   
3. Your program should convert columns of numbers into lists of the correct number type (int, float, complex).
   - Do not try to work with date and time related columns (including the year column).
   - Leave string values alone.
   - This step should result in a data dictionary with each key term refering to a list of values stored as the most appropriate data type.
   
4. Write functions to:
   1. Compute the mean or average of a list.
   1. Compute the cumulative sum of a list.
   1. Compute the distance between two points, when X and Y coordinates are provided as two lists, one of X-coordinates and one of Y-coordinates.
      - You will pass this function the lists for "X" and "Y", and it should compute the distance between each subsequent set of coordinates, for example compute the distance between ( X\[0\], Y\[0\] ) and ( X\[1\], Y\[1\] ), then the distance between ( X\[1\], Y\[1\] ) and ( X\[2\], Y\[2\] ).
      - Return the distances as a list, and add to the dictionary using the key word "Distance".
      - The first value in the list should be "0", since the raccoon has not yet moved from its starting position.
      - Here is a link to [the distance formula](https://www.mathwarehouse.com/algebra/distance_formula/index.php).
      
5. Use the functions to:
   1. Add George's movement to the data dictionary.
   1. Compute George's average energy level, and location (average X and Y).
   1. Compute the total distance George moved in his life.
   
6. Finally, the program should:
   1. Create a new output file called "Georges_life.txt".
   1. The file should have a new header block that is formatted as (replace terms in <> with values you got from the file):
   ```
      Raccoon name: <raccoon name>
      Average location: <X average>, <Y average>
      Distance traveled: <sum of distances>
      Average energy level: <average Energy Level>
      Raccoon end state: <Dead or Alive message>
   ```
   1. There should be a blank line in between this header block and the next section of the file.
   1. Finally, Write select contents of data dictionary to a new TAB delimited section of the file.  This section should include the columns:
      - Date, Time, X and Y coordinates, the Asleep flag, the behavior mode, and the distance traveled (in that order).
      - The columns names should be labeled in the first row.
      - Data from each hour of the raccoon's life should be printed on each subsequent row.
      
#### What to turn in...

1. **Source code file named "Evaluate_Raccoon_Life.py"**

   - Should be appropriately documented with header and in-line comments, and
   - Should produce the required output file, when a file named "2008Male00006.txt" is in the same driectory as the source code.

2. **A separate metadata file** 

   - Metadata file should be named **README.raccoon.txt**.
   - It should describe:
     - the name of the processing script, 
     - a description of the processing being completed by the script, and 
     - the names of the input (required) and output (created) files.  
   - This is a preliminary Metadata file, these will get more important as we progress with assignments.
   
3. **The output file named "Georges_life.txt"**
   
