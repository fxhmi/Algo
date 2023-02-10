pos = {
    "KTM": 3,
    "MRT": 7,
    "LRT": 5,
    "BUS": 6,
    "CAR": 6,
    "WALK": 0
}

neg = {
    "KTM": 5,
    "MRT": 2,
    "LRT": 2,
    "BUS": 3,
    "CAR": 3,
    "WALK": 0
}

pathAttributes = {
    "path": [["UM - LRT Kerinchi", "LRT Kerinchi - Masjid Jamek", "Masjid Jamek - Dataran Merdeka"],
             # 2.699+5.477+0.443
             ["UM - Pantai Hill Park", "Pantai Hill Park - Central Market", "Central Market - Dataran Merdeka"],
             # 3.306+6.452+0.58
             ["UM - MRT Phileo", "MRT Phileo - Pasar Seni", "Pasar Seni - Dataran Merdeka"],  # 3.208+8.268+0.994
             ["UM - KTM KL Sentral", "KTM KL Sentral - KTM KL", "KTM KL - Dataran Merdeka"],  # 6.338+0.029+2.946
             ["UM - Flat PKNS Kerinchi", "Flat PKNS Kerinchi - LRT Kerinchi", "LRT Kerinchi - LRT Masjid Jamek",
              "LRT Masjid Jamek - Dataran Merdeka"],  # 2.864+1.254+5.477+0.443
             ["UM - MRT Phileo", "MRT Phileo - MRT Pasar Seni", "MRT Pasar Seni - LRT Masjid Jamek",
              "LRT Masjid Jamek - Dataran Merdeka"],  # 3.208+8.268+0.873+0.443
             ["UM - LRT Uni", "LRT Uni - LRT Masjid Jamek", "LRT Masjid Jamek - Dataran Merdeka"],  # 3.024+6.197+0.443
             ["UM - Stadium Hoki KL", "Stadium Hoki KL - Suasana Sentral Loft", "Suasana Sentral Loft - One Sentral",
              "One Sentral - Bangunan Sultan Abdul Samad", "Bangunan Sultan Abdul Samad - Dataran Merdeka"],
             # 1.5+4.381+0.517+2.998+0.059
             ["UM - KTM MidValley", "KTM MidValley - KTM Batu Caves", "KTM Batu Caves",
              "KTM Bank Negara - Dataran Merdeka"],
             # 6.976+17.487+10.846+0.792
             ["UM - LRT Uni", "LRT Uni - Taman Bukit Angkasa", "Taman Bukit Angkasa - Central Market",
              "Central Market - Dataran Merdeka"]  # 3.024+1.723+6.359+0.58
             ],
    "mode": [["CAR", "LRT", "WALK"],
             ["BUS", "BUS", "WALK"],
             ["BUS", "MRT", "WALK"],
             ["CAR", "KTM", "WALK"],
             ["BUS", "WALK", "LRT", "WALK"],
             ["BUS", "MRT", "LRT", "WALK"],
             ["BUS", "LRT", "WALK"],
             ["WALK", "BUS", "WALK", "BUS", "WALK"],
             ["CAR", "KTM", "KTM", "WALK"],
             ["WALK", "BUS", "BUS", "CAR"],
             ],
    "distance": [2.699 + 5.477 + 0.443,
                 3.306 + 6.452 + 0.58,
                 3.208 + 8.268 + 0.994,
                 6.338 + 0.029 + 2.946,
                 2.864 + 1.254 + 5.477 + 0.443,
                 3.208 + 8.268 + 0.873 + 0.443,
                 3.024 + 6.197 + 0.443,
                 1.5 + 4.381 + 0.517 + 2.998 + 0.059,
                 6.976 + 17.487 + 10.846 + 0.792,
                 3.024 + 1.723 + 6.359 + 0.58],
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
        if z == "KTM":
            total += 3;
        elif z == "MRT":
            total += 7
        elif z == "LRT":
            total += 5
        elif z == "BUS":
            total += 6
        elif z == "CAR":
            total += 6
        else:
            total += 0
    pathAttributes["positive"][i]=total;
    i += 1;
#negative counter
i = 0;
for x in pathAttributes["negative"]:
    total = 0;
    for z in pathAttributes["mode"][i]:
        if z == "KTM":
            total += 5;
        elif z == "MRT":
            total += 2
        elif z == "LRT":
            total += 2
        elif z == "BUS":
            total += 3
        elif z == "CAR":
            total += 3
        else:
            total += 0
    pathAttributes["negative"][i]=total;
    i += 1;
#score counter
i=0;
distanceWeightage = 90
negativeWeightage = 10
positiveWeightage = 10
for x in pathAttributes["score"]:
    score=(pathAttributes["distance"][i]*distanceWeightage)+(pathAttributes["negative"][i]*negativeWeightage)-(pathAttributes["positive"][i]*positiveWeightage);
    pathAttributes["score"][i]=int(score)
    i+=1;

print(pathAttributes["positive"])
print(pathAttributes["negative"])
print(pathAttributes["score"])

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
