import xml.etree.ElementTree as ET
import os   

data_folder = "Traffic signs/"
out_folder = "Trafic_OUT/"

files = [f for f in os.listdir(data_folder) if os.path.isfile(os.path.join(data_folder, f))]

for file in files:

    root = ET.parse(data_folder+file).getroot()
    iterator = root.getiterator("object")
    
    for item in iterator:

        bndbox = item.find("bndbox")
        name = item.find("name").text
        xmin = bndbox.find("xmin").text
        ymin = bndbox.find("ymin").text
        xmax = bndbox.find("xmax").text
        ymax = bndbox.find("ymax").text
        
        
        out = xmin+","+ymin+","+xmax+","+ymax+","+name        
        with open(out_folder+file.split(".")[0]+".txt", 'a') as f:
            
            f.write(out+"\n")
