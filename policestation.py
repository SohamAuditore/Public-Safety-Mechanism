import sound
import routes

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

def play_audio(filename):
    #print(f'Calling from {location}')
    #call = receive_call(location)
    #if(call==True and filename):
    #print('Audio received')
    sound.play_wave(filename)


def receive_call(location, filename, loca_info, choice):
    pickup = False
    if(location):
        if location in loca_info.keys():
            print('Calling from '+location)
            #routes.print_routes_for_location(location, routes.routes)
            #print()
            #print()
            station_data = loca_info[location]
            for police_station, number in station_data.items():
                print(police_station, number)
                if choice==1:
                    pickup = True
                    filename = filename
                    play_audio(filename)
                    break
                else:
                    continue


    #return pickup



#receive_call_and_audio('Location 5', 'myrecording262.wav')

#receive_call('Location 5', loca_info)