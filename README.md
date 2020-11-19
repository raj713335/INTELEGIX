# INTELEGIX (hack-ed-v10) Theme Intelligent Video Monitoring



A cross platform desktop application for monitoring and analyzing from a live camera feed or videos files to analyse data for

    1.  Classroom environment: How much students are participating in discussions, how is the discipline in the class etc
      
    2.  Corridor environment (outside classroom): Gents entering ladies washrooms and vice versa.
    
    3.  Hostel environment: Students outside dorms after designated timings, Unauthorized entry in campus etc

    4.  School Buses: Driver drowsy, driver talking on cellphone while driving, driver/conductor smoking in the bus etc
    
    5.  Online Exam : To monitor if the student is participating in any malpractices like using cell phones , talking,
        looking here and there etc.
    
After Videos are analysed using Machine Learning , it saves and sends data via Email,Whats App Bots,and Telegram Bots via API Tokens/keys.

This Application was created for Participating in HackerEarth Challenges hack-ed-v10 for K12 Techno Services.


## THEME Intelligent Video Monitoring

Develop a layer of analysis over video feed. It should be focussed around applications in a school or a classroom environment.

    Minimum Requirements
    
    Develop a layer of analysis over video feed. It should be focussed around applications in a school or a classroom environment.

    Some examples-
    
        1.  Classroom environment: How much students are participating in discussions, how is the discipline in the class etc
        2.  School environment (outside classroom): Discipline in corridors and open areas, Gents entering ladies washrooms and vice versa, Detecting vandalism, Detecting medical emergencies etc
        3.  Hostel environment: Students outside dorms after designated timings, Unauthorized entry in campus etc
        4.  School Buses: Driver drowsy, driver talking on cellphone while driving, driver/conductor smoking in the bus etc
    
    The analysis can be on live feed triggering alerts in real-time or on recorded feed for consolidated analysis
    
    On Front End:
    
        Build an interface to upload a video for analysis
        Display results in a presentable manner for the uploaded video
        Display results of previously uploaded videos
        Send Data to Telegram/Whats App through API
    
    On Back end:   
    
        Build the algorithm to analyze the video and identify the event(s) of your choice
        Store the clip showing the event occurrence and capture the relevant details
        The data sharing between Frontend and Backend should be in JSON format rendered over REST APIs.
        Zip all your Source Code, Screenshots, Deployment Instructions/Readme and Upload
    
    
# INTELEGIX WORKING 


# Getting Started

- Clone the repo and cd into the directory
```sh
$ git clone https://github.com/raj713335/INTELEGIX.git
$ cd INTELEGIX
```
- Delete the current Data folder inside INTELEGIX folder and then download the Data.zip from the given url and extract and copy the data folder in INTELEGIX folder

```sh
$ wget https://github.com/raj713335/INTELEGIX.git
```

- Install Python and its required Packages like tensorflow etc.

```sh
$ pip install EasyTkinter==1.1.0
$ pip install Pillow==8.0.1
$ pip install opencv-python==4.4.0.46
$ pip install requests==2.25.0
$ pip install configparser==5.0.1
$ pip install PyAutoGUI==0.9.52
$ pip install tensorflow==2.3.1
$ pip install scikit-learn==0.23.2
$ pip install wget==3.2
$ pip install pygame==2.0.0
$ pip install dlib==19.21.0
$ pip install imutils==0.5.3
$ pip install deepface==0.0.40
$ pip install keras==2.4.3
$ pip install cvlib==0.2.5
$ pip install pyinstaller 
```

- Run the app

```sh
$ python YT.py
```