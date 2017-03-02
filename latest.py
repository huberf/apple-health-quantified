import xml.etree.ElementTree as ET
import os

tree = ET.parse('export_cda.xml')
root = tree.getroot()

##############
# Heart Rate #
##############

# Scout section
data = None
for i in root:
    if i.tag == "{urn:hl7-org:v3}component":
        print "1: Found component"
        data = i

if len(data) > 1:
    print "2: New data popped up"
data = data[0]
print "2: Found component"

allEntries = []
for i in data:
    if i.tag == "{urn:hl7-org:v3}entry":
        print "3: Adding one of series"
        allEntries += [i]
print allEntries

allComponents = []
for a in allEntries:
    for i in a:
        for e in i:
            if e.tag == "{urn:hl7-org:v3}component":
                allComponents += [e]
print "4: Added all components"

allMinute = []
for i in allComponents:
    for a in i:
        allMinute += [a]
print "5: Added all minuetia"

# 1: date, 2: heartRate
records = []
for i in allComponents:
    if i[0][2].get("displayName") == "Heart rate":
        print "Hit vital"
        print i[0][6].get("value")
        records += [[i[0][5][0].get("value"), i[0][6].get("value")]]

heartRateCsv = "date, heartRate\n"
totalRecords = 0
for i in records:
    heartRateCsv += i[0] + ", " + i[1] + "\n"
    totalRecords += 1
print "Computed Records: ", totalRecords
heartFile = open("heart_rate.csv", "w")
heartFile.write(heartRateCsv)
heartFile.close()
print "Saved 'heart_rate.csv'"

os.system("say Finished")
