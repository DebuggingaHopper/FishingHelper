import geocoder
from geopy.geocoders import Nominatim
import time
from pprint import pprint
from math import radians, cos, sin, asin, sqrt
import pygeoip


#This the User class, this will hold the users user name, their latitude, longitude, stat, and address.
#address refers to the addresses given to the user based on their respective state
class User:
    def __init__(self, name, user_lat, user_long, state, address = "", loc_lat=0, loc_lng=0):
        self.name = name
        self.user_lat = user_lat
        self.user_long = user_long
        self.state = state
        self.address = address
        self.loc_lat = loc_lat
        self.loc_lng = loc_lng

    #What this will display to the user is the address of fishing spots given to them
    #It shows to the user the latitude and longitude, for now it will display that but later it will just store it
    #If the address is NA, then it will say the address is unavaliable at this time. This will never fail since any address in the array that is unknown will have NA
    def showaddress(self):
        app = Nominatim(user_agent="tutorial")
        location = app.geocode("{}".format(self.address))
        print(location.address)
        self.loc_lat = location.latitude
        self.loc_lng = location.longitude
        pprint((location.latitude, location.longitude))


    #What this does is check the users state which is stores in the user class
    #It will then display the possible fishing spots in their state
    #It iterates through the array which will show all possible fishing spots, and their addresses
    def check_state(self):
        if (self.state == "Maryland"):
            print("Welcome {} to the the {} fishing spots menu: \n \n".format(self.name, self.state))
            for i in range(len(MDspots)):
                print('{} : '.format(MDspots[i]))
                if (MDadrs[i] == "NA"):
                    self.address = "{} {}".format(MDspots[i], self.state)
                    print('{} : {} km \n'.format(self.showaddress(), self.distance()))
                    for i in range(2):
                        print('\n')
                else:
                    self.address = MDadrs[i]
                    print('{} : {} km \n'.format(self.showaddress(), self.distance()))
                    for i in range(2):
                        print('\n')

    #This will calculate the distance between your current location, and the address of the fishing spot
    def distance(self):
        lon1 = radians(self.user_long)
        lon2 = radians(self.loc_lng)
        lat1 = radians(self.user_lat)
        lat2 = radians(self.loc_lat)
        dlon = lon2-lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2)*sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371
        return(c *r)




MDspots  = ["Lake Habeeb at Rocky Gap State Park" , "Town Creek Delayed Harvest" , "Liberty Reservoir", "Piney Run Reservoir", "Patapsco River", "Big Hunting Creek", "Cunningham Falls Reservoir", "Owens Creek", "Potomac River", "Broadford Lake", "Deep Creek Lake", "Savage River Tailwater Trophy Trout Fishing Area", "Casselman River", "Piney Reservoir", "North Branch Potomac River", "Blairs Valley Lake", "Gunpowder Falls", "Loch Raven Reservoir", "Prettyboy Reservoir", "Deer Creek", "Centennial Lake", "Clopper Lake", "Little Seneca Lake", "Mattawoman Creek", "Wheatley Lake", "Piscataway Creek", "Lake Artemesia", "St. Mary's Lake", "Smithville Lake", "Rising Sun Pond", "Transquaking River", "Urieville Lake", "Tuckahoe Lake", "Unicorn Lake", "Wye Mills Lake", "Adkins Mill Pond", "Johnson's Pond", "Leonard's Mill Pond"]
MDadrs =["12900 Lake Shore Dr Maryland", "28700 Headquarters Dr Maryland","5685 Oakland Rd Maryland", "30 Martz Rd Maryland", "8020 Baltimore National Pike Maryland","6916 Blacks Mill Rd Maryland","14039 Catoctin Hollow Rd Maryland", "NA", "NA","NA", "898 State Park Rd Maryland","1600 Mt Aetna Rd Maryland", "NA", "30 Martz Rd Maryland", "NA", "14022 Blairs Valley Rd Maryland","7200 Graces Quarters Rd","99 Loch Raven Dr Maryland", "NA","Walters Mill Rd Maryland", "4651 Centennial Ln Maryland", "11950 Clopper Rd Maryland", "20508 Clarksburg Rd Maryland", "NA", "La Plata Maryland","NA","8200 55th Ave Maryland", "21250 Camp Cosoma Rd Maryland", "NA","NA","NA", "NA", "NA", "110 Fishing Lake Ln Maryland", "Wye Mills Community Lake", "5168 Powellville Road Maryland", "NA", "2848 Leonards Mill Pond Dr Maryland"]

#The create function begins the whole program
def create():
    # This will be where the user will input their name, the plan is to make this an app that allows many to know all possible fishing spots and tips
    user_Name = str(input("What is your name?: "))
    # This will create a variable that will access to the users information through the ip address of their address
    # This is done to ensure that the information acquired ranging from lat, lng, and state are all from the ip address.
    g = geocoder.ip('me')
    # Here we create the user object with the information we acquired
    user = User(user_Name, g.lat, g.lng, g.state)
    # Then we run the first method to provide the possible fishing spots
    user.check_state()


if __name__ == '__main__':
    create()




