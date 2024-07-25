import requests

loca_info = {
    'Location 1' : {
        'Police Station 1' : [[1231231231], [1000]],
        'Police Station 2' : [[1234567849], [5480]],
        'Police Station 3' : [[8697861695], [2450]],
        'Police Station 4' : [[9456231055], [5480]]
    },
    'Location 2' : {
        'Police Station 5' : [[9433105993], [5000]],
        'Police Station 6' : [[1357908642], [3480]]
    },
    'Location 3' : {
        'Police Station 7' : [[2468097531], [4500]],
        'Police Station 8' : [[3764987128], [3258]],
        'Police Station 9' : [[9202690123], [7480]]
    },
    'Location 4' : {
        'Police Station 10' : [[5532416627], [3733]],
        'Police Station 11' : [[1234567899], [5202]],
        'Police Station 12' : [[4439188679], [3935]],
        'Police Station 13' : [[1235233579], [4569]]
    },
    'Location 5' : {
        'Police Station 14' : [[9027444789], [2100]],
        'Police Station 15' : [[8755131256], [1589]],
        'Police Station 16' : [[6544321789], [6969]],
        'Police Station 17' : [[8980006891], [4000]]
    }
}

def get_police_station(location, loca_info):
    min_distance = float('inf')
    nearest_station = None
    output_text = ""
    if location in loca_info:
        police_station_data = loca_info[location]
        for station_name, numbers in police_station_data.items():
            output_text+='Police Station name: '+station_name+'\n'
            output_text+='Phone Number: '+ str(numbers[0][0])+'\n-----------------------------------\n'
            dist = numbers[1][0]
            int(dist)
            if(dist < min_distance):
                min_distance = dist
                nearest_station = station_name
    else:
        output_text+='No police station found for location: '+location

    output_text+='Nearest Police Station is: '+nearest_station
    #print(min_distance)
    return nearest_station, output_text

def call_station(police_station, location, loca_info):
    filename = ""
    count = 0
    if location in loca_info:
        data = loca_info[location]
        for station_name, numbers in data.items():
            if(police_station == station_name):
                num = numbers[0]
                print(numbers[1])
                import voice
                filename = voice.record()
                return filename
    else:
        print('No police Station found in this location')
    
    

# Example usage:
#location_input = input("Enter a location: ")
#nearest, text = get_police_station(location_input, loca_info)
#print(nearest)
#print(text)
#print()
#station = input('Enter police station: ')
#call_station(nearest, location_input, loca_info)