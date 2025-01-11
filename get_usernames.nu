# Put your VRChat install folder here:
const LOG_DIR = '\\GEOFFERYS-CYBER\Users\powel\AppData\LocalLow\VRChat\vrchat'
# Put the folder you'd like to save the results to
const CSV_OUTPUT_DIR = 'N:\users\geoffery\photos\VRChat'

def process_log [file] {
    cd $LOG_DIR
    let table = open $file 
    | split row --regex '(\d{4}\.\d{2}\.\d{2})' 
    | parse " {Time} {Type}  -  [{Event}] {OnPlayer} {PlayerName} ({UserId}){extra}" 
    | reject "extra"
    | str trim
    | where OnPlayer =~ "OnPlayer"
    | reject "Type"
    | reject "Event"

    print "\n# Player Joins"
    let playerJoins = $table | where OnPlayer == "OnPlayerJoined"
    print $playerJoins

    print "\n# Player Leaves"
    let playerLeft = $table | where OnPlayer == "OnPlayerLeft"
    print $playerLeft

    print "\n# Names"
    let names = find_names $table

    # Save player joins to a text file
    $names | polars save ($CSV_OUTPUT_DIR + '\playerNameLogs.csv')
    $playerJoins | to csv | save -f ($CSV_OUTPUT_DIR + '\playerLogs.csv')
    $playerLeft | to csv | save --append ($CSV_OUTPUT_DIR + '\playerLogs.csv')
}

def find_names [table] {
    let names = $table 
    | reject "Time"
    | reject "OnPlayer"
    | sort-by "PlayerName"
    
    let names = $names 
    | polars into-df
    | polars drop-duplicates
    | polars sort-by "PlayerName" 

    print $names
    return $names
}

def find_log [] {
    cd $LOG_DIR
    let log = ls 
    | where name =~ "output"
    | sort-by modified
    | last
    print ("Found: " + $log.name)

    return $log.name
}

def main [] {
    clear
    let file = find_log
    process_log $file
}