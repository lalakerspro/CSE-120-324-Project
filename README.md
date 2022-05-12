This app lets you scan a spring using a detachable webcam camera, and outputs whether the logo is legible or not.

EQUIPMENT:
You will need the following:
A windows PC
A detachable webcam

DEPENDENCIES:
You need the following libraries installed:

python
opencv2
PIL
imutils
numpy
mySQL database

The SQL Server:
https://dev.mysql.com/downloads/installer/

TO RUN THE APP:

1. open a terminal and run "main.py"
2. A window should pop up, labeled "SpringScan". This is where the webcam is fed
3. Move the webcam as close as you can to the spring logo, and press SPACEBAR to capture the spring shown on the feed
4. An image of the captured spring will pop up, as well as a message on if it is legible or not.
5. The captured springs will be shown in the "images" folder.
6. A tet file called "results.txt" will store the time of the captures and the results

FIXING SMALL ISSUES:
1. If the wrong camera is being read, the number after "Video.Capture() can be changed in line 23 of "main.py".
2. If the legibility scanning is being deemed inaccurate, line 53 of "main.py" can be easily changed by changing the threshold. 

