import json

def write_json(data, filename='data.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

def takeInput():
    obj = {
        "name" : 'N/A',
        "year" : 1,
        "gender": "Male",
        "handle": "N/A"
    }
    obj["name"] = input("NAME: ")
    obj["year"] = int(input("YEAR: "))
    obj["gender"] = input("GENDER: ")
    obj["handle"] = input("HANDLE: ")
    return obj


flag = True
while flag:
    with open('data.json') as f:
        db = json.load(f)
        db["data"].append(takeInput())
        write_json(db)


    ch = input('Do you want to add more[y/n]?: ')
    if(ch=='n'):
        print("Changes Updated!")
        flag = False
