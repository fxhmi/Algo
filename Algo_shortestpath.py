# from geopy.distance import geodesic
# from geopy.geocoders import Nominatim
import googlemaps  # use "pip install googlemaps" on terminal
# import sys
# import heapq
from collections import defaultdict, deque
import gmplot  # for plotting lines on map, use "pip install gmplot" on terminal

# import functools
# import operator
# import requests, json
# from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyDfSFnGD830NV6q_BaRcOb7TQcoUyec06Y')

# geolocator = Nominatim(user_agent="Algo Assignment")

# yang gmaps.geocode is basically cam pointer to that location
# starting location
um = gmaps.geocode('University of Malaya')

# middle points
lrtUni = gmaps.geocode('LRT Universiti')
lrtKerinchi = gmaps.geocode('LRT Kerinchi')
lrtPS = gmaps.geocode('Pasar Seni Station')
lrtMJ = gmaps.geocode('Masjid Jamek Station')
mrtPhileo = gmaps.geocode('MRT Phileo Damansara')
pantaiHP = gmaps.geocode('Hub Pantai Hillpark')
centralMarket = gmaps.geocode('Central Market, Kuala Lumpur')
ktmKLS = gmaps.geocode('KTM KL Sentral')
ktmMV = gmaps.geocode('KTM Mid Valley, Kuala Lumpur')
ktmBC = gmaps.geocode('KTM Batu Caves')
ktmBN = gmaps.geocode('KTM Bank Negara')
pknsKerinchi = gmaps.geocode('Flat PKNS Kerinchi')
klSentral = gmaps.geocode('Kuala Lumpur Sentral Station')
kl1077 = gmaps.geocode('KL1077 KL Sentral')
stadiumKL = gmaps.geocode('Stadium Hoki KL')
sentralLoft = gmaps.geocode('Suasana Sentral Loft')
oneSentral = gmaps.geocode('Go KL Bus KL Sentral Bus Stop (Red Line)')
abdulSamad = gmaps.geocode('Sultan Abdul Samad Building')
bukitAngkasa = gmaps.geocode('Taman Bukit Angkasa')

# api key
# apiKey = 'AIzaSyDfSFnGD830NV6q_BaRcOb7TQcoUyec06Y'

# url
# url ='https://maps.googleapis.com/maps/api/distancematrix/json?'

merdekaSq = gmaps.geocode('Dataran Merdeka, Kuala Lumpur')
coordinates = [merdekaSq[0]['geometry']['location']['lat'],
               merdekaSq[0]['geometry']['location']['lng']]  # latitude, longitude
vertices = ['University of Malaya', 'LRT Kerinchi', 'Kuala Lumpur Sentral Station', 'Flat PKNS Kerinchi',
            'LRT Universiti', 'KL1077 KL Sentral', 'Taman Bukit Angkasa',
            'Stadium Hoki KL', 'Suasana Sentral Loft', 'KTM Mid Valley, Kuala Lumpur', 'KTM Batu Caves',
            'KTM Bank Negara', 'Go KL Bus KL Sentral Bus Stop (Red Line)',
            'Masjid Jamek Station', 'Hub Pantai Hillpark', 'Central Market, Kuala Lumpur', 'MRT Phileo Damansara',
            'Pasar Seni Station', 'Sultan Abdul Samad Building', 'Dataran Merdeka, Kuala Lumpur']

edges = [['University of Malaya', 'LRT Kerinchi'], ['University of Malaya', 'Hub Pantai Hillpark'],
         ['University of Malaya', 'Kuala Lumpur Sentral Station'], ['University of Malaya', 'MRT Phileo Damansara'],
         ['University of Malaya', 'Flat PKNS Kerinchi'], ['University of Malaya', 'LRT Universiti'],
         ['University of Malaya', 'Stadium Hoki KL'],
         ['University of Malaya', 'LRT Universiti'], ['LRT Universiti', 'Taman Bukit Angkasa'],
         ['University of Malaya', 'KTM Mid Valley, Kuala Lumpur'], ['KTM Mid Valley, Kuala Lumpur', 'KTM Batu Caves'],
         ['Stadium Hoki KL', 'Suasana Sentral Loft'], ['Flat PKNS Kerinchi', 'LRT Kerinchi'],
         ['Kuala Lumpur Sentral Station', 'KL1077 KL Sentral'], ['LRT Universiti', 'Masjid Jamek Station'],
         ['LRT Kerinchi', 'Masjid Jamek Station'], ['Suasana Sentral Loft', 'Go KL Bus KL Sentral Bus Stop (Red Line)'],
         ['Go KL Bus KL Sentral Bus Stop (Red Line)', 'Sultan Abdul Samad Building'],
         ['Taman Bukit Angkasa', 'Central Market, Kuala Lumpur'],
         ['Hub Pantai Hillpark', 'Central Market, Kuala Lumpur'], ['MRT Phileo Damansara', 'Pasar Seni Station'],
         ['KTM Batu Caves', 'KTM Bank Negara'],
         ['Pasar Seni Station', 'Masjid Jamek Station'],
         ['Central Market, Kuala Lumpur', 'Dataran Merdeka, Kuala Lumpur'],
         ['Masjid Jamek Station', 'Dataran Merdeka, Kuala Lumpur'],
         ['Sultan Abdul Samad Building', 'Dataran Merdeka, Kuala Lumpur'],
         ['KL1077 KL Sentral', 'Dataran Merdeka, Kuala Lumpur'], ['KTM Bank Negara', 'Dataran Merdeka, Kuala Lumpur'],
         ['Central Market, Kuala Lumpur', 'Dataran Merdeka, Kuala Lumpur'],
         ['Pasar Seni Station', 'Dataran Merdeka, Kuala Lumpur']]

points = [[um, lrtKerinchi], [um, pantaiHP],
          [um, klSentral], [um, mrtPhileo],
          [um, pknsKerinchi], [um, lrtUni], [um, stadiumKL],
          [um, lrtUni], [lrtUni, bukitAngkasa],
          [um, ktmMV], [ktmMV, ktmBC],
          [stadiumKL, sentralLoft], [pknsKerinchi, lrtKerinchi],
          [klSentral, kl1077], [lrtUni, lrtMJ],
          [lrtKerinchi, lrtMJ], [sentralLoft, oneSentral],
          [oneSentral, abdulSamad], [bukitAngkasa, centralMarket],
          [pantaiHP, centralMarket], [mrtPhileo, lrtPS],
          [ktmBC, ktmBN],
          [lrtPS, lrtMJ],
          [centralMarket, merdekaSq],
          [lrtMJ, merdekaSq], [abdulSamad, merdekaSq],
          [kl1077, merdekaSq], [ktmBN, merdekaSq],
          [centralMarket, merdekaSq], [lrtPS, merdekaSq]]

modes = ['driving', 'transit, transit_mode=bus',
         'driving', 'transit, transit_mode=bus',
         'driving', 'transit, transit_mode=bus', 'walking',
         'walking', 'transit, transit_mode=bus',
         'driving', 'transit, transit_mode=train',
         'transit, transit_mode=bus', 'walking',
         'walking', 'transit, transit_mode=train',
         'transit, transit_mode=train', 'walking',
         'transit, transit_mode=bus', 'transit, transit_mode=bus',
         'transit, transit_mode=bus', 'transit, transit_mode=train',
         'transit, transit_mode=train',
         'transit, transit_mode=train',
         'driving',
         'walking', 'walking',
         'transit, transit_mode=bus', 'walking',
         'walking', 'walking']
distance = []  # save distance of all stops
edgeGraph = {}  # for edge and distance
g = {}  # for edges, nested dictionary -> use for weighted graph


def setDistance():
    for i, item in enumerate(points):
        originStr = str((points[i][0])[0]['geometry']['location']['lat']) + ', ' + str(
            (points[i][0])[0]['geometry']['location']['lng'])
        destStr = str((points[i][1])[0]['geometry']['location']['lat']) + ', ' + str(
            (points[i][1])[0]['geometry']['location']['lng'])

        if modes[i].find('transit') != -1:
            if modes[i].find('transit_mode=train'):
                directions = gmaps.directions(originStr, destStr, mode='transit', transit_mode='train')
                # print(directions[0]['legs'][0]['distance']['value'])

            elif modes[i].find('transit_mode=bus'):
                directions = gmaps.directions(originStr, destStr, mode='transit', transit_mode='bus')
                # print(directions[0]['legs'][0]['distance']['value'])

        elif modes[i] == 'walking':
            directions = gmaps.directions(originStr, destStr, mode='walking')
            # print(directions[0]['legs'][0]['distance']['value'])

        else:
            directions = gmaps.directions(originStr, destStr, mode='driving')
            # print(directions[0]['legs'][0]['distance']['value'])

        distance.append(directions[0]['legs'][0]['distance']['value'] / 1000)


def setGraph():
    for i, item in enumerate(vertices):
        edgeGraph = {}
        for j, item in enumerate(edges):
            if (edges[j][0] == vertices[i]):
                edgeGraph.update({edges[j][1]: distance[j]})
                print(edgeGraph)

        g.update({vertices[i]: edgeGraph})

    print(" ")
    for key in g:
        print(key, '-> ', g[key])

    graph1 = Graph1()
    for vertex in g:
        for values in g[vertex]:
            graph1.add_node(vertex)
            graph1.add_edge(vertex, values, g[vertex][values])

    print(" ")
    shortest_path(graph1, 'University of Malaya', 'Dataran Merdeka, Kuala Lumpur')

class Graph1(object):
    def __init__(self):
        self.dist = {}
        self.node = set()  # create empty list using set
        self.edges = defaultdict(list)  # return dictionary object

    def add_node(self, value):
        self.node.add(value)

    def add_edge(self, node_from, node_to, dist):
        self.edges[node_from].append(node_to)  # use method append to add adjacent to the graph
        self.edges[node_to].append(node_from)
        self.dist[(node_from, node_to)] = dist


def dijks_algo(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.node)
    # print(nodes)

    while nodes:
        min_node = None
        for n in nodes:
            if n in visited:  # traverse the visied node to find the min value
                if min_node is None:
                    min_node = n
                elif visited[n] < visited[min_node]:
                    min_node = n
        if min_node is None:
            break

        # print(min_node)

        nodes.remove(min_node)  # remove the first matching element/delete element doesn't exist
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.dist[(min_node, edge)]
            except:  # solve the key error of the last node, exp : 'North Court Mid Valley, Kuala Lumpur'
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijks_algo(graph, origin)
    full_route = deque()
    # print(destination)
    temp = paths[
        destination]  # hold the destination to be add to the full route, starting from the back(destination to origin)

    while temp != origin:
        full_route.appendleft(temp)  # add element to the left side of deque object till meet the source
        temp = paths[temp]

    full_route.appendleft(origin)  # add the origin
    full_route.append(destination)  # add the destination

    print(F'Shortest distance : %.3f km ' % visited[destination])
    print(F'Path : ', list(full_route))
    plot_map(list(full_route))
    return visited[destination], list(full_route)


# GoogleMapPlotter to return Map object

def plot_map(ShortestPath):
    # to get latitude and longitude of every item in shortest path
    lat_list = []
    lon_list = []
    for x in ShortestPath:
        lat_list.append(gmaps.geocode(x)[0]["geometry"]["location"]["lat"])
        lon_list.append(gmaps.geocode(x)[0]["geometry"]["location"]["lng"])

    # Pass the center latitude and center longitude (Set center as McD Bangsar, zoom range : 14)

    gmap1 = gmplot.GoogleMapPlotter(3.1345249, 101.6656899, 14)
    gmap1.apikey = "AIzaSyBaVdPnbR_hU0vWb57zl8bUzDX7GAj_wGA"

    # scatter points on the google map
    gmap1.scatter(lat_list, lon_list, '# FF0000', size=40, marker=False)
    # draw line in between coordinates
    gmap1.plot(lat_list, lon_list, 'cornflowerblue', edge_width=2.5)
    # Pass absolute path
    gmap1.draw("testMap1.html")
    print("Plotted map can be found in root folder.")


setDistance()
setGraph()
