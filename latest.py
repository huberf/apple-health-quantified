import xml.etree.ElementTree as ET

tree = ET.parse('export_cda.xml')
root = tree.getroot()
print root

# Hear Rate
heartRateCsv = "date, heartRate\n"
totalRecords = 0
for i in root.find('component'):
    print i.tag
    if i.get("type") == "HKQuantityTypeIdentifierHeartRate" or i.get("type") == "HKQuantityTypeIdentifierHeartRate":
        heartRateCsv += i.get("endDate") + ", " + i.get("value") + "\n"
        print i.get("endDate"), " : ", i.get("value")
        totalRecords += 1
print "Computed Records: ", totalRecords
heartFile = open("heart_rate.csv", "w")
heartFile.write(heartRateCsv)
heartFile.close()
print "Saved 'heart_rate.csv'"