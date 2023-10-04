# PhyEx Recorder PyQT-Based Python Program for Synchronized Camera Recording
Created by Jindrich 27.3.2023

This program is a Python-based application that enables synchronized recording from four different cameras. It uses the ffmpeg library to handle the synchronization of video feeds from the cameras. The program also features a user-friendly GUI that enables the user to select an exercise and add user data to a database.

## Getting Started
To use this program, you will need to have Python 3.x installed on your machine, along with several additional libraries. These libraries can be installed using the pip package manager by running the following command:

`pip install -r requirements.txt`
You will also need to install the ffmpeg library. Instructions for installing this library can be found on the ffmpeg website.

##Running the Program
To run the program, navigate to the project directory in your terminal and run the following command:

`python main.py`
This will launch the main window of the application.

Set the second network adapter for the cameras:
IPv4: 192.168.1.100
MASK: 255.255.255.0
Gateway: 192.168.1.1
Default DNS: 8.8.8.8
Alternative DNS: 8.8.4.4

## How to Use the Program
Exercise Selection
The main window of the application contains two tabs: "Exercise Selection" and "User Data".

In the "Exercise Selection" tab, you can select an exercise from a dropdown list. Once you select an exercise, the program will display a live feed from each of the four cameras. The video feeds are synchronized using the ffmpeg library, so they will all start and stop at the same time.



## User Data
In the "User Data" tab, you can enter data about the user performing the exercise. You can enter the following information:
g
Name
Age
Gender
Height
Weight
Once you enter this data, you can click the "Add User" button to add the user to the database.

# Database
The program uses an SQLite3 database to store user data. The database contains a single table called "users" with the following columns:

id
name
age
gender
height
weight
When you click the "Add User" button, the program will insert a new row into the "users" table with the user's information.




