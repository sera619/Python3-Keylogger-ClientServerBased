# Python 3 Keylogger on Server-Clientbased #

## Intructions ##

### __First off: This sample DOES NOT promote or encourage any illegal activities! The content in this document is provided solely for educational purposes and to create awareness!__ ###

Hello and welcome to a technical base concept of a Sever-Client keylogger.
For this show off i have setup a simpler JavaScript Express server. This is a very Basic server and could improve dramaticly. But just for the educaltional purposses i keep the things very easy and not Plug'n'Play useable.

Please notice:
The server will run on __127.0.0.1:8080__ (your localhost) per default.
check the files 'logger_clientside.py' and 'server/server.js' to adjust the IP-Adress and Port.

Make sure you have the followed software installed: 
###### click the software to get redirected to official softwarewebpages ######

> - [Python 3.10.x or higher](https://www.python.org/downloads/)
> - [Node.js](https://nodejs.org/en/)

#### To run the logger ####

> - Download the zip with the green downloadbutton you see above.
> - extract the zip in a directory
> - open a shell (commandlinewindow) in the created directory
> - run
>
>```bash
>    pip install -r 'requirements.txt'
>```
>
> - after all dependecies are installed open a second shell in the directory and run 
>   - the first command will start the JavaScript-server
>   - the second command start the keylogger
>
> ```bash
>   node './server/server.js'
>```
>
> ```bash
>   python3 logger_clientside.py
>```
>
> - close the shell with the running keylogger to exit them.
> - to exit the server just press CTRL+C with the shell open and focused
> - have fun with

#### DONT USE THIS FOR ILLEGAL ACTIVITIES ####
#### _Greetings S3R43o3_ ####
