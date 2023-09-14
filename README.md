# VRC-Name-Retriever

Get's VRChat Usernames from Last Session's Logs.

![](https://i.imgur.com/b4CVTrj.png)
## Usage

- To use this code you need to have Python 3.6 or higher installed.
- Clone this repository.
- Run `get_usernames.bat` to automatically install the required packages and run the code. (You may need to allow the batch file to run on your system)
- (Optional) Run `get_usernames.py` to run the code without installing the required packages. (You will need to install them manually)

## How it works

- This code will look for the VRChat log file in the default location. If it finds it then it will skim it for player leave/join messages. It will then print leave/join messages to the console as well as listing all the players that were in the last session.

## Issues

- If you have any issues with this code, please open an issue on this repository.
