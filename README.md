# VRC-Name-Retriever

Get's VRChat Usernames from Last Session's Logs.

[![Preview](https://i.postimg.cc/508G9Dtj/image.png)](https://postimg.cc/G8hzq7G1)

Usage

- There are two scripts: `get_usernames.nu` and `get_usernames.py` (The Nushell version is the recommended version.)
- To use this code you need to have Nushell or Python ^3.6.
- Clone this repository.
- In the `get_usernames.nu` edit `LOG_DIR` and `CSV_OUTPUT_DIR` paths to match the paths you want to use
- Run `get_usernames.bat` to run the script

## How it works

- This code will look for the VRChat log file. If it finds it then it will skim it for player leave/join messages. It will then print leave/join messages to the console as well as listing all the players that were in the last session.

## Issues

- If you have any issues with this code, please open an issue on this repository.
