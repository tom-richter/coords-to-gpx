import re
coords_file = open("coords.txt")
gpx_file = open("coords.gpx", "w+")
stage = 100

head = """<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<gpx xmlns="http://www.topografix.com/GPX/1/1" version="1.1" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
    <metadata>
        <name></name>
        <desc></desc>
        <author>
            <name></name>
        </author>
    </metadata>
"""
gpx_file.write(head)

for line in coords_file:
    coords = [int(s) for s in re.findall(r'\d+', line)]
    coords_n = coords[0] + (coords[1]+(coords[2]/1000))/60
    coords_e = coords[3] + (coords[4]+(coords[5]/1000))/60
    #print(str(coords_n), str(coords_e))
    waypoint = ('    <wpt lat="' + str(coords_n) + '" lon="' + str(coords_e) 
    + '">\n        <name>Stage' + str(stage)+ '</name>\n    </wpt>\n')
    gpx_file.write(waypoint)
    stage += 1
       
gpx_file.write('</gpx>')
gpx_file.close()
coords_file.close()