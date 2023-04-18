# Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET

def loadDatabaseNames(DatabaseFile):
    # Get the root of the xml document
    mytree = ET.parse(DatabaseFile)
    myroot = mytree.getroot()

    # Define a list of names and the total for tracking
    applicationNames = []
    totalNames = 0

    # Define a list of types to search for
    searchTypes = ['bacnet.mpx.point.DigitalInput',
                   'bacnet.mpx.point.TemperatureInput',
                   'bacnet.mpx.point.VoltageOutput',
                   'bacnet.mpx.point.DigitalOutput',
                   'bacnet.mpx.value.AnalogValue',
                   'bacnet.mpx.value.DigitalValue',
                   'server.point.BV',
                   "server.point.AV"
                   ]

    # Use iter to iterate through all the "OI" Tags
    for child in myroot.iter("OI"):
        # Take the name attribute of the child
        name = child.attrib["NAME"]
        attrib = child.attrib["TYPE"]

        #If the name meets certain conditions then store it into the applicationNames list and increment totalNames count
        if(attrib in searchTypes):
            totalNames += 1
            applicationNames.append(name)

    #Write the filtered names to a csv file
    with open('data/applicationNames.csv', 'w') as f:
        for i in range(len(applicationNames)):
            f.write(f"{applicationNames[i]}\n")

    return applicationNames