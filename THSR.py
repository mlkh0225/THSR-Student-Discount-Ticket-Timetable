from datetime import datetime

baseDate = datetime(2015, 1, 4)
userDate = raw_input("Date (Ex: 2015,02,25): ")
userDate = datetime.strptime(userDate, "%Y,%m,%d")
weekday = int((userDate-baseDate).days)%7-1

while int((userDate-baseDate).days)>116:
	userDate = raw_input("Timetable available till 2015/4/30. Enter new date: ")
	userDate = datetime.strptime(userDate, "%Y,%m,%d")
	weekday = int((userDate-baseDate).days)%7-1

print (userDate-baseDate).days

rideTime = int(raw_input("Ride time (24 hour without minutes): "))*60

print "Station number: 1-Taipei, 2-Banqiao, 3-Taoyuan, 4-Hsinchu, 5-Taichung, 6-Chiayi, 7-Tainan, 8-Zuoying"
stationStart = int(raw_input("From station number: "))
stationEnd = int(raw_input("To station number: "))

stations = ["Taipei","Banqiao","Taoyuan","Hsinchu","Taichung","Chiayi","Tainan","Zuoying"]

t551 = [551,-1,-1,-1,-1,390,417,437,450,"50%"]
t1505 = [1505,438,446,459,471,496,-1,-1,-1,"50%"]
t1627 = [1627,558,566,579,591,619,644,663,678,"50%"]
t629 = [629,576,584,597,610,638,662,681,696,"50%"]
t1635 = [1635,618,626,639,651,679,704,723,738,"50%"]
t637 = [637,636,644,657,670,698,722,741,756,"50%"]
t139 = [139,654,662,-1,-1,706,-1,-1,750,"50%"]
t1247 = [1247,1194,1202,-1,-1,1246,-1,-1,1290,"50%"]
t749 = [749,1200,1208,1221,1233,1261,1286,1305,1320,"50%"]
t753 = [753,1236,1244,1257,1270,1298,1322,1341,1356,"50%"]
t255 = [255,1254,1262,-1,-1,1306,-1,-1,1350,"50%"]
t757 = [757,1260,1268,1281,1293,1321,1346,1365,1380,"50%"]
t259 = [259,1290,1298,-1,-1,1342,-1,-1,1386,"50%"]
t761 = [761,1296,1304,1317,1330,1358,1382,1401,1416,"50%"]
t763 = [763,1314,1322,1335,1347,1375,1400,1419,1434,"50%"]
t399 = [399,1332,-1,1351,-1,1384,1408,1426,1439,"50%"]
t541 = [541,1350,1358,1372,1383,1410,-1,-1,-1,"50%"]
t545 = [545,1380,1388,1402,1413,1439,-1,-1,-1,"50%"]

s_weekday1 = [t551,t1505,t1627,t629,t761,t763,t399,t541,t545]
s_weekday2 = [t551,t1505,t1627,t629,t255,t757,t259,t761,t763,t399,t541,t545]
s_weekday3 = [t551,t1505,t1627,t629,t763,t399,t541,t545]
s_weekday4 = [t551,t1505,t763,t399,t541,t545]
s_weekday5 = [t551,t1505]
s_weekday6 = [t551,t1247,t749,t753,t255]
s_weekday7 = [t551,t1635,t637,t139]

s_days = [s_weekday1,s_weekday2,s_weekday3,s_weekday4,s_weekday5,s_weekday6,s_weekday7]

train = [t551]

if stationEnd>stationStart:	
	for x in range(0, len(s_days[weekday])):
		if s_days[weekday][x][stationStart]>rideTime:
			if s_days[weekday][x][stationEnd]>0:
				print '{:>4}'.format(str(s_days[weekday][x][0]))+" "+'{:>8}'.format(stations[(stationStart-1)])+"("+'{:>2}'.format(str(s_days[weekday][x][stationStart]/60))+":"+'{:>2}'.format(str(s_days[weekday][x][stationStart]%60))+")  -> "+'{:>8}'.format(stations[(stationEnd-1)])+"("+'{:>2}'.format(str(s_days[weekday][x][stationEnd]/60))+":"+'{:>2}'.format(str(s_days[weekday][x][stationEnd]%60))+") Discount: "+s_days[weekday][x][9]


#print str(s_weekday1[0][5]/60)+":"+str(s_weekday1[0][5]%60)

