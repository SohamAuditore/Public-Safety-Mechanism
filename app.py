import PySimpleGUI as sg
import location
import voice
import routes
import sound
import policestation
import fakecall

locations = ['Location 1','Location 2','Location 3','Location 4','Location 5']
layout = [
    [sg.Text('Silent Siren', font=16, text_color='black')],
    [sg.Text('Access Location', font=12)],
    [sg.Combo(locations, key='-location-', size=(40,4), enable_events=True)],
    [sg.Button('Ok', key='-ok-', enable_events=True)],
    [sg.Button('Get Help Now', size=(10,2), key='-help-')],
    [sg.Multiline('Details', font=12, size=(40,8), key='-OUTPUT-', justification='center', autoscroll=True)],
    [sg.Button('Generate Fake Call', key='-Fake-', size=(20,3))]
]

layout2 = [
    [sg.Button('Enable', key='-enable-', size=(10,3))],
    [sg.Text('', key='-station_number-', font=14, text_color='red')],
    [sg.Text('', key='-call_location-', font=14, text_color='black')],
    [sg.Multiline('', key='-routes-',font=8, size=(50,8))],
    [sg.Button('Answer', key='-answer-', size=(10,2)), sg.Button('Decline', key='-decline-', size=(10,2))],
    [sg.Text('Note: On Answering the call, the audio file will be played')]
]

window = sg.Window('Valhalla', layout, size=(600,500), element_justification='center')

police_station = ""
user_location = ""
audio_filename = ""

while True:
    event, values = window.read()
    if event==sg.WIN_CLOSED:
        break
    elif event=='-ok-':
        loc = values['-location-']
        user_location = loc
        nearest, text = location.get_police_station(loc, location.loca_info)
        police_station = nearest
        window['-OUTPUT-'].update('Your current location is: '+loc+'\nThe police stations are:\n'+text)
    elif event=='-help-':
        window['-OUTPUT-'].update('Calling '+nearest)
        window['-OUTPUT-'].update('Sending recording to '+nearest)
        filename = location.call_station(nearest, loc, location.loca_info)
        audio_filename = filename
        #print(filename)
    elif event=='-Fake-':
        fakecall.fake_call()

window.close()
print(user_location, police_station, audio_filename)
index = 0
window2 = sg.Window('Police Station', layout2, size=(600,600), element_justification='center')

while True:
    event2, values2 = window2.read()
    if event2==sg.WIN_CLOSED:
        break
    elif event2=='-enable-':
        window2['-station_number-'].update('Station: '+police_station)
        window2['-call_location-'].update('Call from: '+user_location)
        shortest_routes = routes.print_routes_for_location(user_location, routes.routes)
        window2['-routes-'].update(shortest_routes)
    
    elif event2=='-answer-':
        policestation.play_audio(audio_filename)
        break
    elif event2=='-decline-':
        if user_location:
            stations = location.loca_info[user_location]
            station_names = list(stations.keys())
            if index < len(station_names)-1:
                index+=1
            else:
                index=0
            window2['-station_number-'].update(f'{station_names[index]}')
                    
window2.close()    
