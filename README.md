# Deadliner

This program will allow students of New York University to retrieve their deadlines from NYU Classes and create google calendar events for them. No data will be stored. 

1. Clone/download the git repo into a folder on your computer. 
2. Open details.py and enter your netid and password in the respective places.
3. Download a chromedriver for the version of your chrome browser (to replace the one already in the folder), extract this file and place the chromedriver in the Deadliner folder that you cloned.
4. In events.py, replace the chromedriver path (line 21) with the absolute path to the chromedriver in the folder
5. In terminal, access the folder and run "python3 setup.py install".
6. Then type "python3 quickstart.py".
7. A broswer window should open (or copy the link shown and open it in your Chrome browser) asking you to authenticate the google account you wish to use, then close after authentication flow has completed.
8. Another browser window will open (or do No.6 again) which will prompt MFA on your device. Accept it and then leave the program to run.
9. A summary of the classes should be printed on your terminal with the times and a google calendar event will be created right after. 

NOTE: If No.5 or No.6 is showing permission errors, add "sudo" in front of the commands
Enjoy using this and feel free to contact me at gdk244@nyu.edu for any issues encountered. 