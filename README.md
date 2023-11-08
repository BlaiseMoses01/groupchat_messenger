# Groupchat Messenger

Ths is a groupchat client/server messenger app developed in Python using socket programming

## Description

This program was developed during my CSCE416: Introduction to Computer Networks Course. The purpose of the assignment was to demonstrate how TCP servers manage multiple client sockets and how this can be manipulated to relay messages and data between multiple clients on a shared server. I was tasked with creating a groupchat client/server architecture in which a message from one client was relayed through the server to all other clients connected at that time. I achieved this using socket programming in Python.

## Getting Started

### Dependencies
* Python, any version should work but I recommend the latest

### Installing

* clone the repo using the command: 
```
git clone  https://github.com/BlaiseMoses01/groupchat_messenger.git
```
Alternatively you can download the repo as a zip from the link in the above command, and extract the files locally.

### Executing program

* Running the Program

* Step 1: Open the cloned repo in a console window or your IDE of choice

* Step 2: Launch the server using the below command 
```
python GroupChatServer.py <PORTNUMBER>
```
replace <PORTNUMBER> with a value, any should work . In my demo, I use "111", just remember the value you choose as you will need it later when launching the client(s). 

If you completed this step correctly , the console should display "waiting for a clients..."

* Step 3: In a separate terminal window , launch the client with the below command

```
python GroupChatClient.py <SERVERNAME> <SERVERPORT>
```
<SERVERNAME> should be "localhost" unless you renamed, and <SERVERPORT> is whatver value you used for <PORTNUMBER> while completing step 2

If done correctly , the client window should display "Connected to Server at ( <SERVERNAME>, <SERVERPORT>).

* Step 4: Repeat step 3 for as many clients as you wish to connect to the server, each will need its own terminal window.

* Step 5: send messages between the clients as much as needed, and one completed use CNTRL^D on Mac or CNTRL^Z + # on Windows in any client terminal to disconenct that client, or use the same command in the server window which will disconnect all the sockets. 

## Help
If you are having trouble getting the terminals to connnect , remember that you MUST launch the server first and you must use the same portnumber in both commands, otherwise the clients will fail to connect.

## Authors
Blaise Moses (blaisemoses2001@gmail.com)

## License
This project is licensed under the Apache License

## Acknowledgments
I would like to acknowledge my CSCE416 professor , Nelakuditi Srihari, for the written and coded examples in class that allowed me to understand the structure and syntax enough to complete this project.