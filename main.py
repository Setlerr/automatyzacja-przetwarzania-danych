import json
import requests
import zipfile
from pathlib import Path
import os.path
import io
import csv

def Get_File():
    url = "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
    r = requests.get(url, stream=True)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("./")

def Check_for_json_file():
    if os.path.exists("./annotations/person_keypoints_val2017.json") is True:
        print("File is already downloaded!")
    else:
        print("Downloading File...")
        Get_File()

Check_for_json_file()
raw_data = Path("./annotations/person_keypoints_val2017.json").read_text()
data = json.loads(raw_data)
print(type(data))
data = data["images"]
with open("data.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["label","image_name","image_width","image_hight","x_min","y_min","x_max","y_max","image_url"])
    for row in data:
        temp_dict = dict(row)
        writer.writerow([row["id"],row["file_name"],row["width"],row["height"],"(0,0)","(0,0)","("+str(int(row["width"])-1)+",0)","(0,"+str(int(row["height"])-1)+")",row["coco_url"]])
    file.close()

with open("data.csv", newline='') as in_file:
    with open("data_final.csv", 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row:
                writer.writerow(row)
                
with open("data_final.csv") as file:
    reader = csv.reader(file)
    print(list(reader))