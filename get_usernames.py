import os
import re
from colorama import Fore, init

# Get's all user joined/left events from the log (.txt) and prints them to the console (prints entire line of log)
# OnPlayerJoined / OnPlayerLeft

def find_logs():
    # return the most recently modified .txt file in the current directory (name must include log)
    logs = []
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt") and "log" in file:
            logs.append(file)
    home_dir = os.path.expanduser("~")
    local_low_folder = os.path.join(home_dir, "AppData", "LocalLow")
    path = os.path.join(local_low_folder, "VRChat", "vrchat")
    for file in os.listdir(path):
        if file.endswith(".txt") and "log" in file:
            logs.append(os.path.join(path, file))
    if logs:
        return max(logs, key=os.path.getmtime)
    else:
        return None
        
def get_usernames(players, line):
    temp_player = re.findall(r'(?<=OnPlayerJoined ).*', line)
    if temp_player == []:
        temp_player = re.findall(r'(?<=OnPlayerLeft ).*', line)
    
    if temp_player != []:
        temp_player = temp_player[0]
        if temp_player not in players:
            players.append(temp_player)
    
    return players

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