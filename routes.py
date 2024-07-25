routes = {
    'Location 1': {
        'Shortest route 1': ['Via Road A(1000m)', 'Via Temple x(1540m)'],
        'Shortest route 2': ['Via Tailor Shop(900m)', 'Via RoundABOUT AJX(1200m)'],
    },
    'Location 2': {
        'Shortest route 1': ['Via Highway B(800m)', 'Via Park Y(1300m)'],
        'Shortest route 2': ['Via Bridge C(1200m)', 'Via School Z(950m)'],
        'Shortest route 3': ['Via Plaza D(700m)', 'Via Cinema E(1100m)'],
    },
    'Location 3': {
        'Shortest route 1': ['Via River D(600m)', 'Via Mall Q(1100m)'],
        'Shortest route 2': ['Via Market E(750m)', 'Via Stadium R(1400m)'],
        'Shortest route 3': ['Via Alley J(900m)', 'Via Café K(1000m)'],
    },
    'Location 4': {
        'Shortest route 1': ['Via Street F(1200m)', 'Via Café S(800m)'],
        'Shortest route 2': ['Via Library G(950m)', 'Via Gym T(1300m)'],
    },
    'Location 5': {
        'Shortest route 1': ['Via Alley H(1100m)', 'Via Hospital U(700m)'],
        'Shortest route 2': ['Via Garden I(800m)', 'Via Office V(1000m)'],
        'Shortest route 3': ['Via Garden P(1100m)', 'Via Office Q(700m)'],
    },
}

def print_routes_for_location(location, routes):
    output_text = ""
    if location in routes:
        output_text+=f"\nRoutes for {location}:\n"
        routes_info = routes[location]
        for route_name, route_details in routes_info.items():
            output_text+=f"\n{route_name}: {', '.join(route_details)}"
    else:
        output_text=f"\nNo routes found for {location}"

    return output_text

#location = input('Enter a location: ')
#result = print_routes_for_location(location)
#print(result)