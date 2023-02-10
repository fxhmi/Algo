import googlemaps
from collections import defaultdict, deque
import gmplot  # for plotting lines on map, use "pip install gmplot" on terminal
import plotly.graph_objects as go
import string as s
import numpy
import numpy as np

gmaps = googlemaps.Client(key='AIzaSyDfSFnGD830NV6q_BaRcOb7TQcoUyec06Y')

# starting location
um = gmaps.geocode('University of Malaya')

# middle points
lrtUni = gmaps.geocode('LRT Universiti')
lrtKerinchi = gmaps.geocode('LRT Kerinchi, Kuala Lumpur')
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

#PROBLEM 1
merdekaSq = gmaps.geocode('Dataran Merdeka, Kuala Lumpur') #destination
coordinates = [merdekaSq[0]['geometry']['location']['lat'], merdekaSq[0]['geometry']['location']['lng']] #latitude, longitude

vertices = ['University of Malaya', 'LRT Kerinchi, Kuala Lumpur', 'Kuala Lumpur Sentral Station', 'Flat PKNS Kerinchi', 'LRT Universiti', 'KL1077 KL Sentral', 'Taman Bukit Angkasa',
            'Stadium Hoki KL', 'Suasana Sentral Loft', 'KTM Mid Valley, Kuala Lumpur', 'KTM Batu Caves', 'KTM Bank Negara', 'Go KL Bus KL Sentral Bus Stop (Red Line)',
            'Masjid Jamek Station', 'Hub Pantai Hillpark', 'Central Market, Kuala Lumpur', 'MRT Phileo Damansara',
            'Pasar Seni Station', 'Sultan Abdul Samad Building', 'Dataran Merdeka, Kuala Lumpur']

edges = [['University of Malaya', 'LRT Kerinchi, Kuala Lumpur'], ['University of Malaya', 'Hub Pantai Hillpark'],
         ['University of Malaya', 'Kuala Lumpur Sentral Station'], ['University of Malaya', 'MRT Phileo Damansara'],
         ['University of Malaya', 'Flat PKNS Kerinchi'], ['University of Malaya', 'LRT Universiti'], ['University of Malaya', 'Stadium Hoki KL'],
         ['University of Malaya', 'LRT Universiti'], ['LRT Universiti', 'Taman Bukit Angkasa'],
         ['University of Malaya', 'KTM Mid Valley, Kuala Lumpur'], ['KTM Mid Valley, Kuala Lumpur', 'KTM Batu Caves'],
         ['Stadium Hoki KL', 'Suasana Sentral Loft'], ['Flat PKNS Kerinchi', 'LRT Kerinchi, Kuala Lumpur'],
         ['Kuala Lumpur Sentral Station', 'KL1077 KL Sentral'], ['LRT Universiti', 'Masjid Jamek Station'],
         ['LRT Kerinchi, Kuala Lumpur', 'Masjid Jamek Station'], ['Suasana Sentral Loft', 'Go KL Bus KL Sentral Bus Stop (Red Line)'],
         ['Go KL Bus KL Sentral Bus Stop (Red Line)', 'Sultan Abdul Samad Building'], ['Taman Bukit Angkasa', 'Central Market, Kuala Lumpur'],
         ['Hub Pantai Hillpark', 'Central Market, Kuala Lumpur'], ['MRT Phileo Damansara', 'Pasar Seni Station'],
         ['KTM Batu Caves', 'KTM Bank Negara'], ['Pasar Seni Station', 'Masjid Jamek Station'],
         ['Central Market, Kuala Lumpur', 'Dataran Merdeka, Kuala Lumpur'],
         ['Masjid Jamek Station', 'Dataran Merdeka, Kuala Lumpur'], ['Sultan Abdul Samad Building', 'Dataran Merdeka, Kuala Lumpur'],
         ['KL1077 KL Sentral', 'Dataran Merdeka, Kuala Lumpur'], ['KTM Bank Negara', 'Dataran Merdeka, Kuala Lumpur'],
         ['Central Market, Kuala Lumpur', 'Dataran Merdeka, Kuala Lumpur'], ['Pasar Seni Station', 'Dataran Merdeka, Kuala Lumpur']]


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
          [ktmBC, ktmBN], [lrtPS, lrtMJ],
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
         'transit, transit_mode=train', 'transit, transit_mode=train',
         'driving',
         'walking', 'walking',
         'transit, transit_mode=bus', 'walking',
         'walking', 'walking']

transport = ['CAR', 'BUS',
             'CAR', 'BUS',
             'CAR', 'BUS', 'WALK',
             'WALK', 'BUS',
             'CAR', 'KTM',
             'BUS', 'WALK',
             'WALK', 'LRT',
             'LRT', 'WALK',
             'BUS', 'BUS',
             'BUS', 'MRT',
             'KTM', 'LRT',
             'CAR',
             'WALK', 'WALK',
             'BUS', 'WALK',
             'WALK', 'WALK']

distance = [] #save distance of all stops
edgeGraph = {} #for edge and distance
g = {} #for edges, nested dictionary -> use for weighted graph


def setDistance():
    for i, item in enumerate(points):
        originStr = str((points[i][0])[0]['geometry']['location']['lat']) + ', ' + str(
            (points[i][0])[0]['geometry']['location']['lng'])
        destStr = str((points[i][1])[0]['geometry']['location']['lat']) + ', ' + str(
            (points[i][1])[0]['geometry']['location']['lng'])

        if modes[i].find('transit') != -1:
            if modes[i].find('transit_mode=train'):
                directions = gmaps.directions(originStr, destStr, mode='transit', transit_mode='train')

            elif modes[i].find('transit_mode=bus'):
                directions = gmaps.directions(originStr, destStr, mode='transit', transit_mode='bus')

        elif modes[i] == 'walking':
            directions = gmaps.directions(originStr, destStr, mode='walking')

        else:
            directions = gmaps.directions(originStr, destStr, mode='driving')
            #print(directions[0]['legs'][0]['distance']['value'])

        distance.append(directions[0]['legs'][0]['distance']['value'] / 1000)

def setGraph():
    for i, item in enumerate(vertices):
        edgeGraph = {}
        for j, item in enumerate(edges):
            if (edges[j][0] == vertices[i]):
                edgeGraph.update({edges[j][1]: distance[j]})
                #print(edgeGraph)

        g.update({vertices[i]: edgeGraph})

    #print(g)

    graph = Graph(len(vertices))
    for vertex in g:
        for values in g[vertex]:
            graph.add_node(vertex)
            graph.add_edge(vertex, values, g[vertex][values])

    return graph

class Graph(object):
    def __init__(self, length):
        self.vertex = length #to find routes
        self.graph = defaultdict(list) #to find routes
        self.dist = {}
        self.node = set()      #create empty list using set
        self.edges = defaultdict(list)  #return dictionary object
        self.path = [] #save routes
        self.mode = [] #save travel modes
        self.distance = [] #save distances between stops

    def add_node(self, value):
        self.node.add(value)

    def add_edge(self, node_from, node_to, dist):
        self.edges[node_from].append(node_to)   #use method append to add adjacent to the graph
        self.edges[node_to].append(node_from)
        self.dist[(node_from, node_to)] = dist
        self.graph[node_from].append(node_to)

    def getPathAttributes(self, start, dest):
        visited = [False] * (self.vertex)
        route = []
        self.getPaths(start, dest, visited, route)
        self.getDistances()

    #DFS
    def getPaths(self, start, dest, visited, route):
        i = vertices.index(start)
        visited[i] = True
        route.append(start)

        if start == dest: #found path from UM -> Dataran Merdeka
            copyRoute = list(route)
            self.path.append(copyRoute) #do not refer to route, to avoid popping route in path array as well

        else:
            for s in self.graph[start]: #refers to where the starting location branches off to
                j = vertices.index(s) #get that location's index from vertices list
                if visited[j] == False: #if that node has not been visited
                    self.getPaths(s, dest, visited, route)

        route.pop()
        visited[i] = False

    def getDistances(self):
        self.distance = [0] * len(self.path)
        for i in range(len(self.path)):
            self.getAllDistances(self.path[i], i)

    def getAllDistances(self, route, index):
        tempMode = []
        for i in range(len(route)-1):
            tempRoute = [route[i], route[i+1]] #get the edge
            if tempRoute in edges: #check if the edge is in the edges list
                i = edges.index(tempRoute) #get index of the edge in the edges list
                self.distance[index] += distance[i] #add distance
                tempMode.append(transport[i]) #add mode
        self.mode.append(tempMode)


def dijks_algo(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.node)
    # print(nodes)

    while nodes:
        min_node = None
        for n in nodes:
            if n in visited:    #traverse the visied node to find the min value
                if min_node is None:
                    min_node = n
                elif visited[n] < visited[min_node]:
                    min_node = n
        if min_node is None:
            break

        # print(min_node)

        nodes.remove(min_node)       #remove the first matching element/delete element doesn't exist
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.dist[(min_node, edge)]
            except:             #solve the key error of the last node, exp : 'North Court Mid Valley, Kuala Lumpur'
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

def shortest_path(graph, origin, destination):
    visited, paths = dijks_algo(graph, origin)
    full_route = deque()
    # print(destination)
    temp = paths[destination] #hold the destination to be add to the full route, starting from the back(destination to origin)

    while temp != origin:
        full_route.appendleft(temp)      #add element to the left side of deque object till meet the source
        temp = paths[temp]

    full_route.appendleft(origin)        #add the origin
    full_route.append(destination)       #add the destination

    print("The path with the shortest distance is: ")
    print(F'Shortest distance : %.3f km ' % visited[destination])
    print(F'Path : ', list(full_route))

    if list(full_route) in graph.path:
        index = graph.path.index(list(full_route))
        print("Travel Modes: ", graph.mode[index])

    plot_map(list(full_route))
    return graph


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


#PROBLEM 2
def rawFile(readFile, writeFile):  #append text without punctuation to a new file
    file1 = open(readFile, "r",encoding="utf-8")
    file2 = open(writeFile, "w", encoding="utf-8")
    text = file1.read()

    for i in s.punctuation:
        text = text.replace(i, " ")

    file2.write(text)
    file1.close()
    file2.close()

def countWords(readFile):  #count num of words from text file
    f = open(readFile, "r",encoding="utf8")
    text = f.read()
    word = text.lower().split()
    f.close()
    return len(word)

def stopword():
    file = open("stopword.txt", "r",encoding="utf8")
    text = file.read().lower().split()
    file.close()
    return text

def StopWordCount(readFile):
    file1 = open(readFile, "r", encoding="utf8")
    pattern = file1.read().lower().split()

    text = stopword()

    sw = []
    for i in pattern:
        for j in text:
            found = boyer_goodSuffix(i, j)
            if found == True:
                sw.append(i)
    file1.close()
    return sw.__len__()

def removeStopWord(readFile):  #return the list of words without stopwords from car text file
    text = stopword()
    file = open(readFile, "r",encoding="utf8")
    pattern = file.read().lower().split()

    new = []
    for i in pattern:
        for j in text:
            found = boyer_goodSuffix(i, j)
            if found == True:
                break
        if not found:
            new.append(i)
    file.close()
    return new

def countAfterRemove(newFile, removeSWFile):
    #new file
    file2 = open(newFile, "w+", encoding="utf8")

    # write to new file
    newfile = removeStopWord(removeSWFile)

    for m in newfile:
        file2.write(m + " ")
    file2.close()

    # read from new file
    readfile = open(newFile, "r", encoding="utf8")
    text = readfile.read().split()
    readfile.close()
    return len(text)

def preprocess1(shift, bpos, pat, m):
    # m is the length of pattern
    i = m
    j = m + 1
    bpos[i] = j

    while i > 0:
        while j <= m and pat[i - 1] != pat[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i

            j = bpos[j]  # if mismatch, update the next border

        i -= 1  # if pat[i-1]==pat[j-1], bpos[i-1]=j-1
        j -= 1
        bpos[i] = j

def preprocess2(shift, bpos, m):
    j = bpos[0]
    for i in range(m + 1):

        if shift[i] == 0:
            shift[i] = j  # shift pattern from i to j

        if i == j:
            j = bpos[j]

def boyer_goodSuffix(pat, text):
    # s is shift of the pattern with respect to text
    s = 0
    m = len(pat)
    n = len(text)

    bpos = [0] * (m + 1)

    # initialize all occurrence of shift to 0
    shift = [0] * (m + 1)

    # do preprocessing
    preprocess1(shift, bpos, pat, m)
    preprocess2(shift, bpos, m)

    while s <= n - m:
        j = m - 1

        while j >= 0 and pat[j] == text[s + j]:  # match
            j -= 1

        if j < 0 and n == m and s == 0:
            s += shift[0]  # reset shift position
            return True
        else:
            # mismatch, shift the pattern shift[j+1]
            s += shift[j + 1]

    return False

def naive(pattern, text):  # compare pos and neg words
    p = len(pattern)
    t = len(text)

    for i in range(t - p + 1):
        j = 0
        while j < p:
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == p:
            if i == 0:
                if p == t:
                    return True

    return False

def positive():  #list of positive words
    f = open("PositiveWords.txt", "r",encoding="utf8")
    text = f.read().lower().split()
    f.close()
    return text

def getPositiveCount(readFile):
    file1 = open(readFile, "r", encoding="utf8")
    pattern = file1.read().lower().split()

    # read +veword textfile
    text = positive()

    pos = []
    for i in pattern:
        for j in text:
            found = naive(i, j)
            if found == True:
                pos.append(i)
                break
    file1.close()
    return pos.__len__()

def negative():  # list of negative words
    f = open("NegativeWords.txt", "r",encoding="utf8")
    text = f.read().lower().split()
    f.close()
    return text

def getNegativeCount(readFile):
    file1 = open(readFile, "r", encoding="utf8")
    pattern = file1.read().lower().split()

    # read -veword textfile
    text = negative()

    neg = []
    for i in pattern:
        for j in text:
            found = naive(i, j)
            if found == True:
                neg.append(i)
                break
    file1.close()
    return neg.__len__()

def conclusion(positiveWords, negativeWords, readFile):
    f = open(readFile, "r",encoding="utf8")
    text = f.read()
    word = text.lower().split()

    numofWords = len(word)

    numofPos = round((positiveWords / numofWords) * 100)
    numofNeg = round((negativeWords / numofWords) * 100)
    print("numOfPos: ", numofPos)
    print("numofNeg: ", numofNeg)

    print("Positive :", "{}".format(numofPos) + "% Negative : ", "{}".format(numofNeg) + "%")
    print()
    f.close()
    if numofPos > numofNeg:
        print("The article is giving positive statements")
        return 1, numofPos, numofNeg
    elif numofPos < numofNeg:
        print("The article is giving negative statements")
        return -1, numofPos, numofNeg
    else:
        print("The article is giving an equal positive and negative statements")
        return 0, numofPos, numofNeg


print("****************************************************************************************")
print("                                     Problem 1")
print("****************************************************************************************")

setDistance()
graph = setGraph()
graph.getPathAttributes("University of Malaya", "Dataran Merdeka, Kuala Lumpur")
print("Possible routes to Dataran Merdeka: ")
for path in graph.path:
    print(path)
print()
shortest_path(graph, 'University of Malaya', 'Dataran Merdeka, Kuala Lumpur')

print()


print("****************************************************************************************")
print("                                     Problem 2")
print("****************************************************************************************")

rawFile("rawKTM.txt", "KTM.txt")
rawFile("rawMRT.txt", "MRT.txt")
rawFile("rawLRT.txt", "LRT.txt")
rawFile("rawBUS.txt", "BUS.txt")
rawFile("rawCAR.txt", "CAR.txt")
rawFile("rawWALKING.txt","WALK.txt")

print()
print("Total number of words for KTM : ")
ktmWords = countWords("KTM.txt")
print(ktmWords)
print()
print("Total number of words for MRT : ")
mrtWords = countWords("MRT.txt")
print(mrtWords)
print()
print("Total number of words for LRT : ")
lrtWords = countWords("LRT.txt")
print(lrtWords)
print()
print("Total number of words for BUS : ")
busWords = countWords("BUS.txt")
print(busWords)
print()
print("Total number of words for CAR : ")
carWords = countWords("CAR.txt")
print(carWords)
print()
print("Total number of words for WALK : ")
walkWords = countWords("WALK.txt")
print(walkWords)

# KTM
print("****************************************************************************************")
print("KTM")
ktmStopWords = StopWordCount("KTM.txt")
print("Total word counts for stopwords : ", ktmStopWords)
ktmWordsAfterRemove = countAfterRemove("newKTM.txt", "KTM.txt")
print("Total number of words after removing stopwords :", ktmWordsAfterRemove)
print()

ktmPositiveWords = getPositiveCount("newKTM.txt")
print("Total word counts for positive words : ", ktmPositiveWords)
print()
ktmNegativeWords = getNegativeCount("newKTM.txt")
print("Total word counts for negative words :", ktmNegativeWords)
print()
value, ktmNumOfPos, ktmNumOfNeg = conclusion(ktmPositiveWords, ktmNegativeWords, "newKTM.txt")

print("The article on KTM has a total of {} words. ".format(ktmWords) + "After removing {} stopwords, only ".format(ktmStopWords) +
      "{} remain.\n".format(ktmWordsAfterRemove) + "From the total words remaining, there are {} words giving a positive sentiment ".format(ktmPositiveWords)
      + " while {} words give a negative sentiment.".format(ktmNegativeWords))

if value == -1:
    print ("It shows that the users are unsatisfied with the service quality provided and other issues such as the delay of arrival times,\n"
           "punctuality issues, ticketing issues, train frequency and also lack of focus and coordination which has ultimately resulted in bad implementation.")

elif value == 0:
    print("It shows that the users were neutral with the service quality provided.")

elif value == 1:
    print("It shows that the users were satisfied with the service quality provided in aspects namely,\n"
          "punctuality and also the focus and coordination.")



# MRT
print("****************************************************************************************")
print("MRT")
mrtStopWords = StopWordCount("MRT.txt")
print("Total word counts for stopwords : ", mrtStopWords)
mrtWordsAfterRemove = countAfterRemove("newMRT.txt", "MRT.txt")
print("Total number of words after removing stopwords :", mrtWordsAfterRemove)
print()

mrtPositiveWords = getPositiveCount("newMRT.txt")
print("Total word counts for positive words : ", mrtPositiveWords)
print()
mrtNegativeWords = getNegativeCount("newMRT.txt")
print("Total word counts for negative words :", mrtNegativeWords)
print()
value, mrtNumOfPos, mrtNumOfNeg = conclusion(mrtPositiveWords, mrtNegativeWords, "newMRT.txt")

print("The article on MRT has a total of {} words. ".format(mrtWords) + "After removing {} stopwords, only ".format(mrtStopWords) +
      "{} remain.\n".format(mrtWordsAfterRemove) + "From the total words remaining, there are {} words give a positive sentiment "
       .format(mrtPositiveWords) + " while {} words give a negative sentiment.".format(mrtNegativeWords))

if value == -1:
    print(
        "It shows that technology transfer has failed. This puts the MRT at a lower ranking in the market. Users will be unsatisfied with the quality\n"
        " of service. ")

elif value == 0:
    print("It shows that the users were neutral with the service quality provided.")

elif value == 1:
    print("If we compare between the MRT and the KTM, the article about MRT has a more positive sentiment than KTM. The application of technology transfer\n"
          "in the public transportation industry can be observed in the MRT. Benefits of technology transfer in MRT project include\n"
          "additional skillsets for the organization, improving quality and productivity of construction work, allows\n"
          "employees to learn new knowledge and with the additional skill sets of employees, a safer and more efficient MRT project\n"
          "can be achieved and the organization will have a better position in the market. This will ultimately result in better services, making\n"
          "it a conducive option when needing to travel by public transportation.")


# LRT
print("****************************************************************************************")
print("LRT")
lrtStopWords = StopWordCount("LRT.txt")
print("Total word counts for stopwords : ", lrtStopWords)
lrtWordsAfterRemove = countAfterRemove("newLRT.txt", "LRT.txt")
print("Total number of words after removing stopwords :", lrtWordsAfterRemove)
print()

lrtPositiveWords = getPositiveCount("newLRT.txt")
print("Total word counts for positive words : ", lrtPositiveWords)
print()
lrtNegativeWords = getNegativeCount("newLRT.txt")
print("Total word counts for negative words :", lrtNegativeWords)
print()
value, lrtNumOfPos, lrtNumOfNeg = conclusion(lrtPositiveWords, lrtNegativeWords, "newLRT.txt")

print("The article on LRT has a total of {} words. ".format(lrtWords) + "After removing {} stopwords, only ".format(lrtStopWords) +
      "{} remain.\n".format(lrtWordsAfterRemove) + "From the total words remaining, there are {} words give a positive sentiment "
       .format(lrtPositiveWords) + " while {} words give a negative sentiment.".format(lrtNegativeWords))

if value == -1:
    print("The LRT services are not flexible. The low quality of services makes the LRT an unsuitable choice for users.")

elif value == 0:
    print("It shows that the users were neutral with the service quality provided.")

elif value == 1:
    print("The LRT is an efficient and conducive form of public transportation especially with the efforts to reduce energy consumption without \n"
          "sacrificing customer satisfaction. The LRT allows room for more flexible scheduling and services.")


# BUS
print("****************************************************************************************")
print("BUS")
busStopWords = StopWordCount("BUS.txt")
print("Total word counts for stopwords : ", busStopWords)
busWordsAfterRemove = countAfterRemove("newBUS.txt", "BUS.txt")
print("Total number of words after removing stopwords :", busWordsAfterRemove)
print()

busPositiveWords = getPositiveCount("newBUS.txt")
print("Total word counts for positive words : ", busPositiveWords)
print()
busNegativeWords = getNegativeCount("newBUS.txt")
print("Total word counts for negative words :", busNegativeWords)
print()
value, busNumOfPos, busNumOfNeg = conclusion(busPositiveWords, busNegativeWords, "newBUS.txt")

print("The article on BUS has a total of {} words. ".format(busWords) + "After removing {} stopwords, only ".format(busStopWords) +
      "{} remain.\n".format(busWordsAfterRemove) + "From the total words remaining, there are {} words give a positive sentiment "
       .format(busPositiveWords) + " while {} words give a negative sentiment.".format(busNegativeWords))

if value == -1:
    print("It shows that the users were unsatisfied with the service quality provided and other issues namely safety.")

elif value == 0:
    print("It shows that the users were neutral with the service quality provided.")

elif value == 1:
    print("It shows that the users are satisfied with the bus service due to easy access to the bus stop, cheap fares, bus schedule \n"
          "availability and good bus conditions. Despite issues of overcrowded buses and feeling unsafe during the night, customer \n"
          "satisfaction overall is high.")



# CAR
print("****************************************************************************************")
print("CAR")
carStopWords = StopWordCount("CAR.txt")
print("Total word counts for stopwords : ", carStopWords)
carWordsAfterRemove = countAfterRemove("newCAR.txt", "CAR.txt")
print("Total number of words after removing stopwords :", carWordsAfterRemove)
print()

carPositiveWords = getPositiveCount("newCAR.txt")
print("Total word counts for positive words : ", carPositiveWords)
print()
carNegativeWords = getNegativeCount("newCAR.txt")
print("Total word counts for negative words :", carNegativeWords)
print()
value, carNumOfPos, carNumOfNeg = conclusion(carPositiveWords, carNegativeWords, "newCAR.txt")

print("The article on CAR has a total of {} words. ".format(carWords) + "After removing {} stopwords, only ".format(carStopWords) +
      "{} remain.\n".format(carWordsAfterRemove) + "From the total words remaining, there are {} words give a positive sentiment "
       .format(carPositiveWords) + " while {} words give a negative sentiment.".format(carNegativeWords))

if value == -1:
    print("Car use threatens the urban quality of life because it is noisy, causes odour annoyance, local air pollution and yields traffic accidents.\n"
          "Some people may choose to travel via public transport due to those factors.")

elif value == 0:
    print("The users are neutral.")

elif value == 1:
    print("It shows that car has become a popular choice of transportation for the public. Private car use has grown rapidly\n"
          "in the last few decades. The number of motorised vehicles in the world grew from about 75 million to about 675 million between years 1950 and 1990.\n"
          "The factor of comfort, convenience, freedom, not stressful, control, status, pleasure, security, travel speed,\n"
          "various experiences and flexibility makes the public choose the car as their go-to mode of transportation.")

#WALKING
print("****************************************************************************************")
print("WALKING")
walkStopWords = StopWordCount("WALK.txt")
print("Total word counts for stopwords : ", walkStopWords)
walkWordsAfterRemove = countAfterRemove("newWALK.txt", "WALK.txt")
print("Total number of words after removing stopwords :", walkWordsAfterRemove)
print()

walkPositiveWords = getPositiveCount("newWALK.txt")
print("Total word counts for positive words : ", walkPositiveWords)
print()
walkNegativeWords = getNegativeCount("newWALK.txt")
print("Total word counts for negative words :", walkNegativeWords)
print()
value, walkNumOfPos, walkNumOfNeg = conclusion(walkPositiveWords, walkNegativeWords, "newWALK.txt")

print("The article on WALKING has a total of {} words. ".format(walkWords) + "After removing {} stopwords, only ".format(walkWordsAfterRemove) +
      "{} remain.\n".format(walkWordsAfterRemove) + "From the total words remaining, there are {} words give a positive sentiment "
       .format(walkPositiveWords) + " while {} words give a negative sentiment.".format(walkNegativeWords))

if value == -1:
    print("Users would not voluntarily choose walking to get to their destination due to certain factors, mainly road accidents.\n"
          "Furthermore, the routes are not pedestrian-friendly.")

elif value == 0:
    print("The users are neutral.")

elif value == 1:
    print("Walking is a major transport mode, of crucial importance to several large groups in the community and a contributor to reducing\n"
          "motor vehicle emissions. In certain situations, walking is a better alternative as opposed to public transporation in terms of\n"
          "accessibility and mobility.")

#graph for positive and  negative words

transport = ['KTM','MRT','LRT','BUS','CAR','WALKING']
positive=[ktmPositiveWords, mrtPositiveWords, lrtPositiveWords, busPositiveWords, carPositiveWords,walkPositiveWords]
negative=[ktmNegativeWords, mrtNegativeWords, lrtNegativeWords, busNegativeWords, carNegativeWords,walkNegativeWords]
fig = go.Figure(data=[go.Bar(name='Positive', x=transport, y=positive,text=positive,textposition='auto',marker_color='green'),
                              go.Bar(name='Negative', x=transport, y=negative, text=negative, textposition='auto')])
fig.update_layout(title_text='Positive and Negative words',yaxis_title='Count')

fig.show()


# graph for word frequency and stopwords

transport = ['KTM', 'MRT','LRT','BUS','CAR','WALKING']
count = [ktmWords, mrtWords, lrtWords, busWords, carWords,walkWords]
word = [ktmStopWords, mrtStopWords, lrtStopWords, busStopWords, carStopWords,walkStopWords]

fig = go.Figure(
    data=[go.Bar(name='Word Frequency', x=transport, y=count, text=count, textposition='auto'),
          go.Bar(name='StopWords', x=transport, y=word, text=word, textposition='auto')])

fig.update_layout(title_text='Word Frequency and Stopwords', yaxis_title='Count')

fig.show()

print()


print("****************************************************************************************")
print("                                     Problem 3")
print("****************************************************************************************")

pos = {
    "KTM": ktmNumOfPos,
    "MRT": mrtNumOfPos,
    "LRT": lrtNumOfPos,
    "BUS": busNumOfPos,
    "CAR": carNumOfPos,
    "WALK": walkNumOfPos
}

neg = {
    "KTM": ktmNumOfNeg,
    "MRT": mrtNumOfNeg,
    "LRT": lrtNumOfNeg,
    "BUS": busNumOfNeg,
    "CAR": carNumOfNeg,
    "WALK": walkNumOfNeg
}

pathAttributes = {
    "path": graph.path,
    "mode": graph.mode,
    "distance": graph.distance,
    "positive": [0,
                 0,
                 0,
                 0,
                 0,
                 0,
                 0,
                 0,
                 0,
                 0],
    "negative": [0,
                 0,
                 0,
                 0,
                 0,
                 0,
                 0,
                 0,
                 0,
                 0],
    "score": [0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0],
}

# positive counter
i = 0;
for x in pathAttributes["positive"]:
    total = 0;
    for z in pathAttributes["mode"][i]:
        total += pos[z]
    pathAttributes["positive"][i]=total
    i += 1
#negative counter
i = 0;
for x in pathAttributes["negative"]:
    total = 0;
    for z in pathAttributes["mode"][i]:
        total += neg[z]
    pathAttributes["negative"][i]=total
    i += 1
#score counter
i=0;
distanceWeightage = 50
negativeWeightage = 50
positiveWeightage = 50
for x in pathAttributes["score"]:
    score=(pathAttributes["distance"][i]*distanceWeightage)+(pathAttributes["negative"][i]*negativeWeightage)-(pathAttributes["positive"][i]*positiveWeightage)
    pathAttributes["score"][i]=int(score)
    i+=1

for i in range (len(pathAttributes["path"])):
    print("Route: ", pathAttributes["path"][i])
    print("Travel modes: ", pathAttributes["mode"][i])
    print("Positive: ", pathAttributes["positive"][i])
    print("Negative: ", pathAttributes["negative"][i])
    print("Score: ", pathAttributes["score"][i])
    print()

#sorting
pathTemp = pathAttributes["path"]
scoreTemp = pathAttributes["score"]

import numpy
pathTemp = numpy.array(pathTemp)
scoreTemp = numpy.array(scoreTemp)
inds = scoreTemp.argsort()
pathSorted = pathTemp[inds]

#printing
print()
print("Recommended paths (1=Most recommended, 10=Least recommended)")
i = 1
for x in pathSorted:
    print(i, end = ": ")
    i+=1
    print(x)
