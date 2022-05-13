PLEASE REFERENCE: 2022-01-Spring-CSE-Team324-report.pdf for more detailed instructions


This app lets you scan a spring using a detachable webcam camera, and outputs whether the logo is legible or not.




EQUIPMENT:
You will need the following:
A windows PC
A detachable webcam (of good quality)

DEPENDENCIES:
You need the following libraries installed:

pip (installer)
https://www.liquidweb.com/kb/install-pip-windows/

Python

Opencv2


PIL


imutils

numpy


mySQL (install this regardless of whether you will use a database)



The SQL Server: (OPTIONAL, only if you want a database! May not work)
Step 1 (Download):
https://dev.mysql.com/downloads/installer/

Step 2:
Follow this tutorial to setup your local server: 
https://www.youtube.com/watch?v=3vsC05rxZ8c 

Step 3: 
Uncomment the database instructions in main.py (Delete the '#' from the bottom lines which implement the database).
  1st:
    Uncomment the createDATABASE then run program completely.
  2nd:
    Re-comment the createDATABASE and then uncomment the insertDATA. You are now ready to go!


TO DOWNLOAD THE APP:
Simply download the GitHub repository as a zip folder, and extract to wherever you please


TO USE THE APP:

1. Open a terminal, navigate to the app folder, and run "main.py"


2. A window should pop up, labeled "SCANNER". This is where the webcam is fed


3. Move the webcam as close as you can to the spring logo, and press SPACEBAR to capture the spring shown on the feed

4. An image of the captured spring will pop up, as well as a message on if it is legible or not.


5. The captured springs will be shown in the "springs" folder.


6. A text file called "results.txt" will store the time of the captures and the results

7. CLOSE the app (when finished) by closing the terminal


7. OPTIONAL: If you would like to use a database, uncomment line 97 in main.py. The database may not work.





FIXING SMALL ISSUES:

1. If the wrong camera is being read, the number after "Video.Capture() can be changed in line 23 of "main.py".
2. If the legibility scanning is being deemed inaccurate, line 53 of "main.py" can be easily changed by changing the threshold.


