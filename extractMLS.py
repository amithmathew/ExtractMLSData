# Script              : extractMLS.py
# Pre-requisites      : BeautifulSoup, requests
# Output              : CSV File which can be filtered later.
# Assumptions         : An MLS Extract file (html) is available on disk.
# Author              : Amith Mathew
# Version             : 0.1
# License             : GPL3 - Copyright 2015, Amith Mathew
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# 


# TODO - Lots of cleanup and refactoring needed - but works as a PoC!
# TODO - Filename is hardcoded.


from bs4 import BeautifulSoup
import requests


file = r"TO_BE_CHANGED_FILENAME_OF_MLS_EXTRACT.HTML"
page = open(file)
data = page.read()

outfile = open('output.csv', 'w')
outfile.write(  "Available, ListingID, Address, Rent, Unit Type, Storeys, Level, Total Rooms, Bedrooms, Washrooms, Cross Street, Posession Date, Basement Present, Heating Type, Total Area, Laundry, AC Type, All Included?, Water, Heat, Hydro, Cable, Parking, Furnished, Parking Type, Parking Spaces, Amenities\n")

soup = BeautifulSoup(data)

for listing in soup.find_all('div', class_='formitem form viewform'):
    available = listing.find_all('span', class_='formitem formfield')[6].find_all('span', class_='value')[0].text
    if available != 'Lease' :
        continue
    addressLine = listing.find_all('span', class_='formitem formfield')[0].text
    addressUnit = listing.find_all('span', class_='formitem formfield')[1].text
    addressCity = listing.find_all('span', class_='formitem formfield')[2].text
    addressZip = listing.find_all('span', class_='formitem formfield')[4].text
    rent = listing.find_all('span', class_='formitem formfield')[5].find_all('span', class_='value')[0].text
    unitType = listing.find_all('span', class_='formitem formfield')[14].text
    unitStoreys = listing.find_all('span', class_='formitem formfield')[15].text
    unitLevel = listing.find_all('span', class_='formitem formfield')[19].find_all('span', class_='value')[0].text
    unitRooms = listing.find_all('span', class_='formitem formfield')[20].find_all('span', class_='value')[0].text
    unitBedrooms = listing.find_all('span', class_='formitem formfield')[21].find_all('span', class_='value')[0].text
    unitWashrooms = listing.find_all('span', class_='formitem formfield')[22].find_all('span', class_='value')[0].text
    crossStreet = listing.find_all('span', class_='formitem formfield')[24].find_all('span', class_='value')[0].text
    mlsListing = listing.find_all('span', class_='formitem formfield')[26].find_all('span', class_='value')[0].text
    posessionDate = listing.find_all('span', class_='formitem formfield')[28].find_all('span', class_='value')[0].text    

    basementPresent = listing.find_all('span', class_='formitem formfield')[32].find_all('span', class_='value')[0].text   
    heatType = listing.find_all('span', class_='formitem formfield')[34].find_all('span', class_='value')[0].text
    totalArea = listing.find_all('span', class_='formitem formfield')[36].find_all('span', class_='value')[0].text
    laundryType = listing.find_all('span', class_='formitem formfield')[40].find_all('span', class_='value')[0].text
    
    acType = listing.find_all('span', class_='formitem formfield')[45].find_all('span', class_='value')[0].text
    allIncluded = listing.find_all('span', class_='formitem formfield')[50].find_all('span', class_='value')[0].text
    water = listing.find_all('span', class_='formitem formfield')[51].find_all('span', class_='value')[0].text
    heat = listing.find_all('span', class_='formitem formfield')[52].find_all('span', class_='value')[0].text
    hydro = listing.find_all('span', class_='formitem formfield')[53].find_all('span', class_='value')[0].text
    cable = listing.find_all('span', class_='formitem formfield')[54].find_all('span', class_='value')[0].text
    parking = listing.find_all('span', class_='formitem formfield')[57].find_all('span', class_='value')[0].text
    furnished = listing.find_all('span', class_='formitem formfield')[63].find_all('span', class_='value')[0].text
    parkingType = listing.find_all('span', class_='formitem formfield')[66].find_all('span', class_='value')[0].text
    parkingSpaces = listing.find_all('span', class_='formitem formfield')[69].find_all('span', class_='value')[0].text
    
    amenities = listing.find_all('span', class_='formitem formfield')[72].find_all('span', class_='value')[0].text
    
#    if listing.find_all('span', class_='formitem formfield')[76].find_all('span', class_='value')[0].text == 'Living':
#        livingRoomArea = listing.find_all('span', class_='formitem formfield')[78].find_all('span', class_='value')[0].text + ' x ' + 
#                                listing.find_all('span', class_='formitem formfield')[79].find_all('span', class_='value')[0].text
                                
    
#    LivingRoomArea = 

#    MasterBedroomArea = 
#    if listing.find_all('span', class_='formitem formfield')[85].find_all('span', class_='value')[0].text == 'Living':
#        livingRoomArea = listing.find_all('span', class_='formitem formfield')[78].find_all('span', class_='value')[0].text + ' x ' + 
#                                listing.find_all('span', class_='formitem formfield')[79].find_all('span', class_='value')[0].text




#    SolariumArea = 
#    clientRemarks = 
    
    outfile.write( 
                        '"' + 
                        available + '"' + ',' + '"' +
                        mlsListing + '"' + ',' + '"' + 
                        addressLine + ',' +  
                        addressUnit + ',' + 
                        addressCity + ',' + 
                        addressZip + '"' + ',' + '"' + 
                        rent + '"' + ',' + '"' + 
                        unitType + '"' + ',' + '"' + 
                        unitStoreys + '"' + ',' + '"' + 
                        unitLevel + '"' + ',' + '"' + 
                        unitRooms + '"' + ',' + '"' + 
                        unitBedrooms + '"' + ',' + '"' + 
                        unitWashrooms + '"' + ',' + '"' + 
                        crossStreet + '"' + ',' + '"' + 
                        posessionDate + '"' + ',' + '"' + 
                        basementPresent + '"' + ',' + '"' + 
                        heatType + '"' + ',' + '"' + 
                        totalArea + '"' + ',' + '"' + 
                        laundryType + '"' + ',' + '"' + 
                        acType + '"' + ',' + '"' + 
                        allIncluded  + '"' + ',' + '"' + 
                        water  + '"' + ',' + '"' + 
                        heat  + '"' + ',' + '"' + 
                        hydro  + '"' + ',' + '"' + 
                        cable  + '"' + ',' + '"' + 
                        parking  + '"' + ',' + '"' + 
                        furnished  + '"' + ',' + '"' + 
                        parkingType  + '"' + ',' + '"' + 
                        parkingSpaces  + '"' + ',' + '"' + 
                        amenities
                        + '"' + '\n')
                    
outfile.close()
                    
#print soup