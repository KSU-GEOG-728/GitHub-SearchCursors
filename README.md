# GitHub-SearchCursors
Exercise for GEOG 728 Programming for Geographic Analysis at Kansas State University

### Instructions:

Accept the GitHub Classroom assignment <code>GitHub-SearchCursor</code> and clone the new repository as a local personal repository.  Uncompress the provided ZIP file to access the ArcGIS Pro project file in your local repository workspace.  The only file which needs to be pushed to origin at the conclusion of the exercise is a single Python script.  There is no requirement this week to prepare and submit a script-based tool.  Should you encounter difficulties during the week, seek assistance by posting an issue in GitHub.

### Task:

Edit the provided Python file called <code>GitHub-SearchCursor.py</code> to create a stand-alone script based on your corrected submission from the midterm practical exam.  As a reminder, that script should ___ that loops through all feature classes in the <code>ExerciseData.gdb</code> geodatabase.  Your script should also accomplish the following objectives and/or include these specific features:

1. Declares only one local variable which should specify as the workspace the <code>ExerciseData.gdb</code> geodatabase.
2. Uses that local variable to set the current workspace environment.
3. Allows script users the ability to supply the workspace value using the Python <code>input()</code> function.
4. Prints (to console) a custom message at the end of the script using Python's <code>format</code> function that includes the name, type, and spatial reference name for each feature class in the user-specified workspace.

For this assignment, modify the script to include a search cursor that sums the total population of all counties in Kansas and the total population of counties through which a major river passes.  Then use these sums to "automate" the final print statement by computing the percentage of the total Kansas population that lives in counties intersected by a major river. 

All code requirements outlined in the midterm practical exam also apply here.  The new features of your script will include creation of one or more a search cursor objects and any additional code and variables needed to automate adding the populations of all Kansas counties and calculating the percentage of the total population that lives in a "river county".

## Rubric:

Review the assignment rubric available on Canvas for additional details on how your work will be assessed. Double-check that your script includes a complete header section, uses good commenting, incorporates line spaces between blocks of code, and reads input and writes output to current workspace.

## Submission:

Commit your code changes for <code>GitHub-SearchCursor</code> to your assignment repository on GitHub.
