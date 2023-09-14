import os
import re

# Get's all user joined/left events from the log (.txt) and prints them to the console (prints entire line of log)
# OnPlayerJoined / OnPlayerLeft

def find_logs():
    # return any .txt files in the current directory (name must include log)
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt") and "log" in file:
            return file
    # try hard coded path
    home_dir = os.path.expanduser("~")
    local_low_folder = os.path.join(home_dir, "AppData", "LocalLow")
    path = os.path.join(local_low_folder, "VRChat", "vrchat")
    for file in os.listdir(path):
        if file.endswith(".txt") and "log" in file:
            return path + "\\" + file
        
def get_usernames(players, line):
    # Store the username in a list (username is anything after the OnPlayerJoined/OnPlayerLeft to the newline) (Name can have spaces)
    # If the username is already in the list, do nothing
    # If the username is not in the list, add it to the list
    
    temp_player = re.findall(r'(?<=OnPlayerJoined ).*', line)
    if temp_player == []:
        temp_player = re.findall(r'(?<=OnPlayerLeft ).*', line)
    
    if temp_player != []:
        temp_player = temp_player[0]
        if temp_player not in players:
            players.append(temp_player)
    
    return players

from colorama import Fore, init

def main():
    init()
    players = []
    log_file = find_logs()
    
    if log_file == None:
        print("No log file found")
        return
    
    print(Fore.YELLOW + "Reading log file: " + log_file)
    counter = 0
    with open(log_file, "r", encoding='UTF-8') as f:
        for line in f:
            if ("OnPlayerJoined" in line or "OnPlayerLeft" in line) and not "OnPlayerLeftRoom" in line:
                line = line.replace("\n", "")
                # Remove extra spaces from the line
                printable_line = re.sub(' +', ' ', line)
                if "OnPlayerJoined" in line:
                    print(Fore.GREEN + printable_line)
                else: 
                    print(Fore.RED + printable_line)
                players = get_usernames(players, line)
                counter += 1
                
    print(Fore.YELLOW + "\nPlayers:")
    for player in players:
        print(Fore.GREEN + " - " + player)
    print(Fore.MAGENTA + "\nTotal: " + str(len(players)))
    print("Done")

if __name__ == '__main__':
    main()