# **KLGLUG-LOGBOOK** #

- Requirements that are required r

### IDE ###
     
### PYTHON ###

### MYSQL ###
     
### ARDUINO ###

    
### SERVER-SETUP ###
     
### INTEGRATION ###

## **IDE** ##
We used two various ide for the user-friendly support such as pycharm and visual studio

*WINDOWS Installation* 
follow the below instructions to install vscode in windows
- Download visual studio-code by **[clicking here](https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user)** 
- after download please install the application by simply running the *.exe* file or going to the Microsoft store and directly installing the application        

follow the below instructions to install pycharm in windows
- Download visual studio-code by **[clicking here](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)**
- after download please install the application by simply running the *.exe* file or going to the Microsoft store and directly installing the application
- or run the following command to get vscode

*UBUNTU Installation*
follow the below instructions to install vscode in Linux
- Download visual studio-code by **[clicking here](https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64)**
- run the deb file to launch the application or u can directly go to the ubuntu store and directly install the vscode code
-
update the packages before installing        
     
     sudo apt update 
installing of code
     
     sudo apt install code

follow the below instructions to install pycharm in Linux
- Download visual studio-code by **[clicking here](https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64)**
- run the deb file to launch the application or u can directly go to the ubuntu store and directly install the vscode code

## **PYTHON** ##
*UBUNTU*

verify that python is installed or not and what version is available in ur personal environment by the below command 
     
     python --version

and update the packages 

     sudo apt update

python install command 

     sudo apt install python3.8 

check the python version

     python --version

follow the steps to install pip 

     sudo apt update

     sudo apt install python3-pip

check the version of the pip that u installed

     pip3 --version

now we are going to setup opencv and i requist u to follow the instructions carefully 

*these commans r used to setup the face recognition* 

     sudo apt-get install libboost-all-dev

     sudo apt-get install libgtk-3-dev

     sudo apt-get install build-essential cmake

update the installed packages before proceeding further

     sudo apt-get update 

     sudo apt-get install scikit-image

     pip3 install scikit-learn

     pip install numpy scikit-learn cmake

     pip install dlib

     pip install face_recognition

we are done with the setup of face_recognition           

*WINDOWS*

installing the python on windows

go to the official website to download or just **[click hear to downoled](https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe)**

and run the .exe file to install python in ur local environment 
*(please make a note that where the python is installed because in further it helps to set-up the pip)* 

now u have to set up the **pip** for that follow the instructions carefully 

go to this link to set up the pip **[click here](https://bootstrap.pypa.io/get-pip.py)**

after navigating to that link copy all the text to note pad and save it as **get-pip.py** and now

now carefully follow the steps
- move that **get-pip.py** file to the python🐍 folder📂 where u previously noted where the python is installed
    
pip setup is done with the above task 

## **My SQL** ##

*UBUNTU*

SQL acts a databse fro to record all the tasks and store the data 

before installing update the packages and start setuping the database

     sudo apt update

     sudo apt install mysql-server -y

Doing so will open a prompt in your terminal for package configuration. Use the down arrow to select the **Ok** option.

Press **Enter**. This should prompt you to enter a **password:**. Your are basically setting the root password for MySQL. Don’t confuse it with root password of Ubuntu system.

Type in a password and press Tab to select **<Ok>**. Press **Enter**. You’ll now have to re-enter the password. After doing so, press Tab again to select **<Ok>**. Press **Enter**.

Some information on configuring MySQL Server will be presented. Press Tab to select **<Ok>** and **Enter** again:

noe check the sql is properly installed by the bellow command

     sudo systemctl status mysql.service

You should see Active: **active (running)** in there somewhere. If you don’t, use the following command to start the service:

create user and grant all permissions to it 

     create user 'user_name'@'localhost' identified by 'password';

     grant all privileges  on * . * to 'user_name'@'localhost';

     flush privileges; 

to login to ur personal sql user user this bellow command

     mysql -h user_name -u user -p


- *h* is used to specify a host name (if the server is located on another machine; if it isn’t, just omit it)
- *u* mentions the user
- *p* specifies that you want to input a password.

`fore reference mysql -u chinnu -p1234`


