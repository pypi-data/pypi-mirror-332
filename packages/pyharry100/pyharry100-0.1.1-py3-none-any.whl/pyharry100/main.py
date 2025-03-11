import argparse
import requests
import os
import json
import subprocess
def downloadDay(day):
    if(day.lower()[0:3]=="day"):
        day = day.strip(" ")
        if(len(day)==4):
            if(day[3:len(day)]=="1"):
                day = "day01"
            
            elif(day[3:len(day)]=="2"):
                day = "day02"
            
            elif(day[3:len(day)]=="3"):
                day = "day03"
            
            elif(day[3:len(day)]=="4"):
                day = "day04"
            
            elif(day[3:len(day)]=="5"):
                day = "day05"
            
            elif(day[3:len(day)]=="6"):
                day = "day06"
            
            elif(day[3:len(day)]=="7"):
                day = "day07"
            
            elif(day[3:len(day)]=="8"):
                day = "day08"
            
            elif(day[3:len(day)]=="9"):
                day = "day09"
        
        day_no = day[3:6]
        url = f'https://raw.githubusercontent.com/Zain-Zameer/100DaysPython-box/refs/heads/main/Day%20{day_no}/day{day_no}_after.md'
        r = requests.get(url, allow_redirects=True)
        if r.status_code == 200:
            with open(f'day{day_no}_after.md', 'wb') as f:
                f.write(r.content)
            # print("File downloaded successfully!")
        else:
            print(f"Failed to download file. Status Code: {r.status_code}")
        
        r = requests.get(f"https://raw.githubusercontent.com/Zain-Zameer/100DaysPython-box/refs/heads/main/Day%20{day_no}/day{day_no}_extra_practice.py", allow_redirects=True)
        if r.status_code == 200:
            with open(f'day{day_no}_extra_practice.py', 'wb') as f:
                f.write(r.content)
            # print("File downloaded successfully!")
        else:
            print(f"Failed to download file. Status Code: {r.status_code}")
        
        r = requests.get(f"https://raw.githubusercontent.com/Zain-Zameer/100DaysPython-box/refs/heads/main/Day%20{day_no}/day{day_no}_tasks.py", allow_redirects=True)
        if r.status_code == 200:
            with open(f'day{day_no}_tasks.py', 'wb') as f:
                f.write(r.content)
            # print("File downloaded successfully!")
        else:
            print(f"Failed to download file. Status Code: {r.status_code}")
        
        r = requests.get(f"https://raw.githubusercontent.com/Zain-Zameer/100DaysPython-box/refs/heads/main/Day%20{day_no}/day{day_no}_tasks_answers.py", allow_redirects=True)
        if r.status_code == 200:
            with open(f'day{day_no}_tasks_answers.py', 'wb') as f:
                f.write(r.content)
            # print("File downloaded successfully!")
        else:
            print(f"Failed to download file. Status Code: {r.status_code}")
        
        r = requests.get(f"https://raw.githubusercontent.com/Zain-Zameer/100DaysPython-box/refs/heads/main/Day%20{day_no}/progress.json", allow_redirects=True)
        if r.status_code == 200:
            with open('progress.json', 'wb') as f:
                f.write(r.content)
            # print("File downloaded successfully!")
        else:
            print(f"Failed to download file. Status Code: {r.status_code}")
        
        os.mkdir(f"Harry (Day {day_no})")
        os.mkdir("tests")
        r = requests.get(f"https://raw.githubusercontent.com/Zain-Zameer/100DaysPython-box/refs/heads/main/Day%20{day_no}/Harry%20(Day%20{day_no})/Tutorial.md", allow_redirects=True)
        if r.status_code == 200:
            with open(f'./Harry (Day {day_no})/Tutorial.md', 'wb') as f:
                f.write(r.content)
            # print("File downloaded successfully!")
        else:
            print(f"Failed to download file. Status Code: {r.status_code}")
        
        r = requests.get(f"https://raw.githubusercontent.com/Zain-Zameer/100DaysPython-box/refs/heads/main/Day%20{day_no}/tests/day{day_no}_tests.py", allow_redirects=True)
        if r.status_code == 200:
            with open(f'./tests/day{day_no}_tests.py', 'wb') as f:
                f.write(r.content)
            # print("File downloaded successfully!")
        else:
            print(f"Failed to download file. Status Code: {r.status_code}")
        
        r = requests.get(f"https://github.com/Zain-Zameer/100DaysPython-box/raw/main/Day%20{day_no}/day{day_no}_notes.pdf", allow_redirects=True)
        if r.status_code == 200:
            with open(f'day{day_no}_notes.pdf', 'wb') as f:
                f.write(r.content)
            # print("File downloaded successfully!")
        else:
            print(f"Failed to download file. Status Code: {r.status_code}")
        
    elif(day.strip(" ").lower()=="status"):
        try:
            with open("progress.json","r") as f:
                data = json.load(f)
            # print(data)
            print("=" * 40)
            print(f"{'Progress Report':^40}")
            print("=" * 40)
            for key, value in data.items():
                print(f"{key:<20}: {value}")
            print("=" * 40)
        except:
            print("No Progress found.")
    
    elif(day.strip(" ").lower()=="test"):
        l = os.listdir("./tests")
        result = subprocess.run(["python", f"tests/{l[0]}"], capture_output=True, text=True)
        print(result.stdout)
                
        
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command",help="for example:'Day6' or 'status' or 'test' ")
    args = parser.parse_args()
    if args.command:
        downloadDay(args.command)
    else:
        print("Invalid command. Use 'pyharry100 day1' or 'pyharry100 status' or 'pyharry100 test'.")
    

if __name__ == "__main__":
    main()