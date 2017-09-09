#./pip install pandas

import pandas as pd
import os
import shutil

MAX_CHAR = 1+25 # 1 overall stat and 25 characters
char_order = ["Overall", "Reaper", "Tracer", "Mercy", "Hanzo", "Torbjorn", "Reinhardt", "Pharah", "Winston", "Widowmaker", "Bastion", "Symmetra", "Zenyatta", "Genji", "Roadhog", "McCree", "Junkrat", "Zarya", "Soldier" , "Lucio", "DVa", "Mei", "Sombra", "Doomfist", "Ana", "Orisa"]

def getURL():
    
    valid_platform = ["pc", "xbl", "psn"]
    valid_region = ["us", "eu", "kr", "cn"]
    
    while True:
        
        platform = input("\nWhat platform do you play on?\nComputer - pc, XBOX - xbl, Playstation - psn\nInput: ")
        
        if (platform in valid_platform):
            break;
        print("\nInvalid Input!")
            
    while True:
        
        region = input("\nWhat region do you play on\nNorth America - us, Europe - eu, Korea - kr, China - cn\nInput: ")
        
        if (region in valid_region):
            break;
        print("\nInvalid Input!")
        
    battle_tag = input("\nWhat is battletag (Ex:Toast-12702)\nInput: ")
    
    platform = "pc"
    region = "us"
    battle_tag = "Toast-12702"
    
    url = "https://playoverwatch.com/en-us/career/" + platform + "/" + region + "/" + battle_tag
    print("\nURL: " + url+"\n")
    
    return url


def getTable(url):
    
    try:
        dfs = pd.read_html(url)
    except:
        print("Error: Could not retrieve data")
    
    char_counter=-1
    sheet_counter=1
    passed = False;
    
    writer = pd.ExcelWriter('EmptyTester.xlsx')
    
    for df in dfs:
        
        char_check = list(df)[0]
        
        if (char_check == "Hero Specific" or (not passed and char_check == 'Combat')):
            char_counter+=1
            sheet_counter=1
            passed = True
            if (char_counter == MAX_CHAR):
                writer.save()
                os.remove('EmptyTester.xlsx')
                return
            writer = pd.ExcelWriter('OW_Stats_{}.xlsx'.format(char_order[char_counter]))
            
        if (passed and char_check != "Hero Specific" and char_check != "Combat"):
            passed = False
        
        df.to_excel(writer, 'Sheet{}'.format(sheet_counter))
        
        sheet_counter+=1;
        

def relocate():
    
    curr_path = os.path.dirname(os.path.abspath(__file__))
    
    if os.path.exists(curr_path+"\Stats"):
        shutil.rmtree(curr_path+"\Stats")
        os.makedirs(curr_path + "\Stats")
    else:
        os.makedirs(curr_path + "\Stats")
    
    for char in char_order:
        curr_name = curr_path + "\OW_Stats_{}.xlsx".format(char)
        next_name = curr_path + "\Stats\OW_Stats_{}.xlsx".format(char)
        os.rename(curr_name, next_name)
    

def run():
    url = getURL()
    getTable(url)
    relocate()

if __name__ == "__main__":
    run()
