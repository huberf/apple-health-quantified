import xml.etree.ElementTree as ET
from operator import itemgetter

tree = ET.parse('export.xml')
root = tree.getroot()

# Hear Rate
heartRateCsv = "date, heartRate\n"
totalRecords = []
for i in root:
    if i.get("type") == "HKQuantityTypeIdentifierHeartRate" or i.get("type") == "HKQuantityTypeIdentifierHeartRate":
        totalRecords += [[i.get("endDate"), i.get("value")]]
        print i.get("endDate"), " : ", i.get("value")
totalRecords = sorted(totalRecords, key=lambda data: data[0][0:10])
for i in totalRecords:
    heartRateCsv += i[0] + ', ' + i[1] + '\n'
print "Computed Records: ", len(totalRecords)
heartFile = open("heart_rate.csv", "w")
heartFile.write(heartRateCsv)
heartFile.close()
print "Saved 'heart_rate.csv'"
