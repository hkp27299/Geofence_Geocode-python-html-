import gmplot
import webbrowser
import time
import os

def tags():
    read = []
    lt =
    lg =



    return lg,lt

def plotting(lt,lg):
    latitude = [lt]
    logitude = [lg]

    gmap = gmplot.GoogleMapPlotter(21.158839, 72.809349, 15)

    gmap.scatter(latitude , longitude , '#FF0000',size = 50, marker = False )
    gmap.plot(latitude , longitude , 'cornflowerblue', edge_width = 3.0)

    #gmap.apikey = "inserting  API key here"

    gmap.draw("C:\\Users\\Harsh\\Desktop\\Programs\\Python\\geo\\geocode.html")

def server_create():

     os.system("start cmd ") #command = python -m http.server 8000

def Fencing():
    try:
        os.remove("C:\\Users\\Harsh\\Downloads\\geofence.txt")
        raise Exception
    except Exception:
        webbrowser.open("file:///C:/Users/Harsh/Desktop/Programs/Python/geo/geofence.html")
        time.sleep(15)

        with open("C:\\Users\\Harsh\\Downloads\\geofence.txt") as f:
            with open("C:\\Users\\Harsh\\Desktop\\Programs\\Python\\geo\\geofence.txt", "w") as f1:
                for line in f:
                        f1.write(line)
server_create()

Fencing()
webbrowser.open("file:///C:/Users/Harsh/Desktop/Programs/Python/geo/geofence.html")
while (True):
    lt, lg = tags()
    plotting(lt,lg)
    time.sleep(2)
