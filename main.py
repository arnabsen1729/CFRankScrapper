import requests
from bs4 import BeautifulSoup
import json
from tabulate import tabulate

CONTEST_ID = input('CONTEST ID: ')
COUNT = 10000

URL = "https://codeforces.com/api/contest.standings?contestId=" + (CONTEST_ID) + "&from=1&count=" + str(COUNT) + "&showUnofficial=false"

print('Fetching Data...')

data = requests.get(URL).text
parsed = json.loads(data)
contestName = parsed["result"]["contest"]["name"]

print("Scanning results of " + contestName)



'''
Tables we will make:
0. All years
2. First
4. Second
6. Third
8. Fourth
 and there will be for girls only for each one of them
'''

with open('data.json') as f:
    fullResult = [[] for _ in range(10)]
    handlesTaken = []
    db = json.load(f)
    full = db["data"]
    for idx in range(COUNT):
        for user in full:
            if user["handle"] == parsed["result"]["rows"][idx]["party"]["members"][0]["handle"]:

                handlesTaken.append(user["handle"])
                

                currYear = user["year"]
                if user["gender"] == "Female":
                    if len(fullResult[1])<3:
                        fullResult[1].append([len(fullResult[1])+1, idx+1, user["name"], user["handle"]])

                    if len(fullResult[2*currYear + 1])<3:
                        fullResult[2*currYear + 1].append([len(fullResult[2*currYear + 1])+1, idx+1, user["name"], user["handle"]])

                if len(fullResult[0])<3:
                    fullResult[0].append([len(fullResult[0])+1, idx+1, user["name"], user["handle"]])
                if len(fullResult[2*currYear])<3:
                    fullResult[2*currYear].append([len(fullResult[2*currYear])+1, idx+1, user["name"], user["handle"]])




    myFile = open("results.txt",'w')
    myFile.write(contestName + " Results: \n\n")
    print(contestName + " Results: \n\n", end="")

    myFile.write('='*len(contestName + "Results: "))
    print('='*len(contestName + "Results: "), end="")

    myFile.write("\n\n\t\t-:CODE IIEST:- \n\n")
    print("\n\n\t\t-:CODE IIEST:- \n\n")
    index = 0
    myFile.write(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    print(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    index += 1
    myFile.write("\n\n\t\t-:CODE IIEST (Girls):- \n\n")
    print("\n\n\t\t-:CODE IIEST (Girls):- \n\n")

    myFile.write(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    print(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    index += 1
    myFile.write("\n\n\t\t-:FIRST YEAR:- \n\n")
    print("\n\n\t\t-:FIRST YEAR:- \n\n")

    myFile.write(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    print(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    index += 1
    myFile.write("\n\n\t\t-:FIRST YEAR (Girls):- \n\n")
    print("\n\n\t\t-:FIRST YEAR (Girls):- \n\n")

    myFile.write(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    print(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    index += 1
    myFile.write("\n\n\t\t-:SECOND YEAR:- \n\n")
    print("\n\n\t\t-:SECOND YEAR:- \n\n")

    myFile.write(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    print(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    index += 1
    myFile.write("\n\n\t\t-:SECOND YEAR (Girls):- \n\n")
    print("\n\n\t\t-:SECOND YEAR (Girls):- \n\n")

    myFile.write(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    print(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    index += 1
    myFile.write("\n\n\t\t-:THIRD YEAR:- \n\n")
    print("\n\n\t\t-:THIRD YEAR:- \n\n")

    myFile.write(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    print(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    index += 1
    myFile.write("\n\n\t\t-:THIRD YEAR (Girls):- \n\n")
    print("\n\n\t\t-:THIRD YEAR (Girls):- \n\n")

    myFile.write(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    print(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    index += 1
    myFile.write("\n\n\t\t-:FOURTH YEAR:- \n\n")
    print("\n\n\t\t-:FOURTH YEAR:- \n\n")

    myFile.write(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    print(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    index += 1
    myFile.write("\n\n\t\t-:FOURTH YEAR (Girls):- \n\n")
    print("\n\n\t\t-:FOURTH YEAR (Girls):- \n\n")

    myFile.write(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    print(tabulate(fullResult[index], headers = ["#", "RANK", "NAME", "HANDLE"]))
    index += 1




    myFile.close()
    print('DONE')
    print('Data Exported to results.txt')

# print(parsed["result"]["rows"][0]["party"]["members"][0]["handle"])
