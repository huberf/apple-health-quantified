heart_file = open('heart_rate.csv')
raw_heart_data = heart_file.read()
first_heart_data = raw_heart_data.split("\n")
heart_data = []
for i in first_heart_data[1:len(first_heart_data)-2]:
    heart_data += [i.split(", ")]

highs = []
lows = []
low_high = []
lastDay = ""
index = -1
maxHigh = 0
maxLow = 200
for i in heart_data:
    if not i[0][0:10] == lastDay and not index == -1:
        low_high += [[lastDay, maxLow, maxHigh]]
        highs += [maxHigh]
        lows += [maxLow]
    if not i[0][0:10] == lastDay:
        index += 1
        maxHigh = 0
        maxLow = 200
    if int(i[1]) > maxHigh:
        maxHigh = i[1]
    if int(i[1]) < maxLow:
        maxLow = i[1]
    lastDay = i[0][0:10]

low_high_file = open('heart/low_high.csv', 'w')
toOutput = 'date,low,high\n'
for i in low_high:
    toOutput += str(i[0]) + ',' + str(i[1]) + ',' + str(i[2]) + '\n'
low_high_file.write(toOutput)
low_high_file.close()
