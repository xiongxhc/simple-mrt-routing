from collections import defaultdict
from main import MRT_GRAPH
from utils import (
    location_per_station,
    stations_per_location,
    translate_route_to_sentence
)

def test_location_per_station():
    assert location_per_station() == {
   "NS1":"Jurong East",
   "NS2":"Bukit Batok",
   "NS3":"Bukit Gombak",
   "NS4":"Choa Chu Kang",
   "NS5":"Yew Tee",
   "NS7":"Kranji",
   "NS8":"Marsiling",
   "NS9":"Woodlands",
   "NS10":"Admiralty",
   "NS11":"Sembawang",
   "NS12":"Canberra",
   "NS13":"Yishun",
   "NS14":"Khatib",
   "NS15":"Yio Chu Kang",
   "NS16":"Ang Mo Kio",
   "NS17":"Bishan",
   "NS18":"Braddell",
   "NS19":"Toa Payoh",
   "NS20":"Novena",
   "NS21":"Newton",
   "NS22":"Orchard",
   "NS23":"Somerset",
   "NS24":"Dhoby Ghaut",
   "NS25":"City Hall",
   "NS26":"Raffles Place",
   "NS27":"Marina Bay",
   "NS28":"Marina South Pier",
   "EW1":"Pasir Ris",
   "EW2":"Tampines",
   "EW3":"Simei",
   "EW4":"Tanah Merah",
   "EW5":"Bedok",
   "EW6":"Kembangan",
   "EW7":"Eunos",
   "EW8":"Paya Lebar",
   "EW9":"Aljunied",
   "EW10":"Kallang",
   "EW11":"Lavender",
   "EW12":"Bugis",
   "EW13":"City Hall",
   "EW14":"Raffles Place",
   "EW15":"Tanjong Pagar",
   "EW16":"Outram Park",
   "EW17":"Tiong Bahru",
   "EW18":"Redhill",
   "EW19":"Queenstown",
   "EW20":"Commonwealth",
   "EW21":"Buona Vista",
   "EW22":"Dover",
   "EW23":"Clementi",
   "EW24":"Jurong East",
   "EW25":"Chinese Garden",
   "EW26":"Lakeside",
   "EW27":"Boon Lay",
   "EW28":"Pioneer",
   "EW29":"Joo Koon",
   "EW30":"Gul Circle",
   "EW31":"Tuas Crescent",
   "EW32":"Tuas West Road",
   "EW33":"Tuas Link",
   "CG0":"Tanah Merah",
   "CG1":"Expo",
   "CG2":"Changi Airport",
   "NE1":"HarbourFront",
   "NE3":"Outram Park",
   "NE4":"Chinatown",
   "NE5":"Clarke Quay",
   "NE6":"Dhoby Ghaut",
   "NE7":"Little India",
   "NE8":"Farrer Park",
   "NE9":"Boon Keng",
   "NE10":"Potong Pasir",
   "NE11":"Woodleigh",
   "NE12":"Serangoon",
   "NE13":"Kovan",
   "NE14":"Hougang",
   "NE15":"Buangkok",
   "NE16":"Sengkang",
   "NE17":"Punggol",
   "CC1":"Dhoby Ghaut",
   "CC2":"Bras Basah",
   "CC3":"Esplanade",
   "CC4":"Promenade",
   "CC5":"Nicoll Highway",
   "CC6":"Stadium",
   "CC7":"Mountbatten",
   "CC8":"Dakota",
   "CC9":"Paya Lebar",
   "CC10":"MacPherson",
   "CC11":"Tai Seng",
   "CC12":"Bartley",
   "CC13":"Serangoon",
   "CC14":"Lorong Chuan",
   "CC15":"Bishan",
   "CC16":"Marymount",
   "CC17":"Caldecott",
   "CC19":"Botanic Gardens",
   "CC20":"Farrer Road",
   "CC21":"Holland Village",
   "CC22":"Buona Vista",
   "CC23":"one-north",
   "CC24":"Kent Ridge",
   "CC25":"Haw Par Villa",
   "CC26":"Pasir Panjang",
   "CC27":"Labrador Park",
   "CC28":"Telok Blangah",
   "CC29":"HarbourFront",
   "CE0":"Promenade",
   "CE1":"Bayfront",
   "CE2":"Marina Bay",
   "DT1":"Bukit Panjang",
   "DT2":"Cashew",
   "DT3":"Hillview",
   "DT5":"Beauty World",
   "DT6":"King Albert Park",
   "DT7":"Sixth Avenue",
   "DT8":"Tan Kah Kee",
   "DT9":"Botanic Gardens",
   "DT10":"Stevens",
   "DT11":"Newton",
   "DT12":"Little India",
   "DT13":"Rochor",
   "DT14":"Bugis",
   "DT15":"Promenade",
   "DT16":"Bayfront",
   "DT17":"Downtown",
   "DT18":"Telok Ayer",
   "DT19":"Chinatown",
   "DT20":"Fort Canning",
   "DT21":"Bencoolen",
   "DT22":"Jalan Besar",
   "DT23":"Bendemeer",
   "DT24":"Geylang Bahru",
   "DT25":"Mattar",
   "DT26":"MacPherson",
   "DT27":"Ubi",
   "DT28":"Kaki Bukit",
   "DT29":"Bedok North",
   "DT30":"Bedok Reservoir",
   "DT31":"Tampines West",
   "DT32":"Tampines",
   "DT33":"Tampines East",
   "DT34":"Upper Changi",
   "DT35":"Expo",
   "TE1":"Woodlands North",
   "TE2":"Woodlands",
   "TE3":"Woodlands South",
   "TE4":"Springleaf",
   "TE5":"Lentor",
   "TE6":"Mayflower",
   "TE7":"Bright Hill",
   "TE8":"Upper Thomson",
   "TE9":"Caldecott",
   "TE10":"Mount Pleasant",
   "TE11":"Stevens",
   "TE12":"Napier",
   "TE13":"Orchard Boulevard",
   "TE14":"Orchard",
   "TE15":"Great World",
   "TE16":"Havelock",
   "TE17":"Outram Park",
   "TE18":"Maxwell",
   "TE19":"Shenton Way",
   "TE20":"Marina Bay",
   "TE21":"Marina South",
   "TE22":"Gardens by the Bay"
}, "Test location_per_station" 

def test_stations_per_location():
    assert stations_per_location() == {
   "Jurong East":[
      "NS1",
      "EW24"
   ],
   "Bukit Batok":[
      "NS2"
   ],
   "Bukit Gombak":[
      "NS3"
   ],
   "Choa Chu Kang":[
      "NS4"
   ],
   "Yew Tee":[
      "NS5"
   ],
   "Kranji":[
      "NS7"
   ],
   "Marsiling":[
      "NS8"
   ],
   "Woodlands":[
      "NS9",
      "TE2"
   ],
   "Admiralty":[
      "NS10"
   ],
   "Sembawang":[
      "NS11"
   ],
   "Canberra":[
      "NS12"
   ],
   "Yishun":[
      "NS13"
   ],
   "Khatib":[
      "NS14"
   ],
   "Yio Chu Kang":[
      "NS15"
   ],
   "Ang Mo Kio":[
      "NS16"
   ],
   "Bishan":[
      "NS17",
      "CC15"
   ],
   "Braddell":[
      "NS18"
   ],
   "Toa Payoh":[
      "NS19"
   ],
   "Novena":[
      "NS20"
   ],
   "Newton":[
      "NS21",
      "DT11"
   ],
   "Orchard":[
      "NS22",
      "TE14"
   ],
   "Somerset":[
      "NS23"
   ],
   "Dhoby Ghaut":[
      "NS24",
      "NE6",
      "CC1"
   ],
   "City Hall":[
      "NS25",
      "EW13"
   ],
   "Raffles Place":[
      "NS26",
      "EW14"
   ],
   "Marina Bay":[
      "NS27",
      "CE2",
      "TE20"
   ],
   "Marina South Pier":[
      "NS28"
   ],
   "Pasir Ris":[
      "EW1"
   ],
   "Tampines":[
      "EW2",
      "DT32"
   ],
   "Simei":[
      "EW3"
   ],
   "Tanah Merah":[
      "EW4",
      "CG0"
   ],
   "Bedok":[
      "EW5"
   ],
   "Kembangan":[
      "EW6"
   ],
   "Eunos":[
      "EW7"
   ],
   "Paya Lebar":[
      "EW8",
      "CC9"
   ],
   "Aljunied":[
      "EW9"
   ],
   "Kallang":[
      "EW10"
   ],
   "Lavender":[
      "EW11"
   ],
   "Bugis":[
      "EW12",
      "DT14"
   ],
   "Tanjong Pagar":[
      "EW15"
   ],
   "Outram Park":[
      "EW16",
      "NE3",
      "TE17"
   ],
   "Tiong Bahru":[
      "EW17"
   ],
   "Redhill":[
      "EW18"
   ],
   "Queenstown":[
      "EW19"
   ],
   "Commonwealth":[
      "EW20"
   ],
   "Buona Vista":[
      "EW21",
      "CC22"
   ],
   "Dover":[
      "EW22"
   ],
   "Clementi":[
      "EW23"
   ],
   "Chinese Garden":[
      "EW25"
   ],
   "Lakeside":[
      "EW26"
   ],
   "Boon Lay":[
      "EW27"
   ],
   "Pioneer":[
      "EW28"
   ],
   "Joo Koon":[
      "EW29"
   ],
   "Gul Circle":[
      "EW30"
   ],
   "Tuas Crescent":[
      "EW31"
   ],
   "Tuas West Road":[
      "EW32"
   ],
   "Tuas Link":[
      "EW33"
   ],
   "Expo":[
      "CG1",
      "DT35"
   ],
   "Changi Airport":[
      "CG2"
   ],
   "HarbourFront":[
      "NE1",
      "CC29"
   ],
   "Chinatown":[
      "NE4",
      "DT19"
   ],
   "Clarke Quay":[
      "NE5"
   ],
   "Little India":[
      "NE7",
      "DT12"
   ],
   "Farrer Park":[
      "NE8"
   ],
   "Boon Keng":[
      "NE9"
   ],
   "Potong Pasir":[
      "NE10"
   ],
   "Woodleigh":[
      "NE11"
   ],
   "Serangoon":[
      "NE12",
      "CC13"
   ],
   "Kovan":[
      "NE13"
   ],
   "Hougang":[
      "NE14"
   ],
   "Buangkok":[
      "NE15"
   ],
   "Sengkang":[
      "NE16"
   ],
   "Punggol":[
      "NE17"
   ],
   "Bras Basah":[
      "CC2"
   ],
   "Esplanade":[
      "CC3"
   ],
   "Promenade":[
      "CC4",
      "CE0",
      "DT15"
   ],
   "Nicoll Highway":[
      "CC5"
   ],
   "Stadium":[
      "CC6"
   ],
   "Mountbatten":[
      "CC7"
   ],
   "Dakota":[
      "CC8"
   ],
   "MacPherson":[
      "CC10",
      "DT26"
   ],
   "Tai Seng":[
      "CC11"
   ],
   "Bartley":[
      "CC12"
   ],
   "Lorong Chuan":[
      "CC14"
   ],
   "Marymount":[
      "CC16"
   ],
   "Caldecott":[
      "CC17",
      "TE9"
   ],
   "Botanic Gardens":[
      "CC19",
      "DT9"
   ],
   "Farrer Road":[
      "CC20"
   ],
   "Holland Village":[
      "CC21"
   ],
   "one-north":[
      "CC23"
   ],
   "Kent Ridge":[
      "CC24"
   ],
   "Haw Par Villa":[
      "CC25"
   ],
   "Pasir Panjang":[
      "CC26"
   ],
   "Labrador Park":[
      "CC27"
   ],
   "Telok Blangah":[
      "CC28"
   ],
   "Bayfront":[
      "CE1",
      "DT16"
   ],
   "Bukit Panjang":[
      "DT1"
   ],
   "Cashew":[
      "DT2"
   ],
   "Hillview":[
      "DT3"
   ],
   "Beauty World":[
      "DT5"
   ],
   "King Albert Park":[
      "DT6"
   ],
   "Sixth Avenue":[
      "DT7"
   ],
   "Tan Kah Kee":[
      "DT8"
   ],
   "Stevens":[
      "DT10",
      "TE11"
   ],
   "Rochor":[
      "DT13"
   ],
   "Downtown":[
      "DT17"
   ],
   "Telok Ayer":[
      "DT18"
   ],
   "Fort Canning":[
      "DT20"
   ],
   "Bencoolen":[
      "DT21"
   ],
   "Jalan Besar":[
      "DT22"
   ],
   "Bendemeer":[
      "DT23"
   ],
   "Geylang Bahru":[
      "DT24"
   ],
   "Mattar":[
      "DT25"
   ],
   "Ubi":[
      "DT27"
   ],
   "Kaki Bukit":[
      "DT28"
   ],
   "Bedok North":[
      "DT29"
   ],
   "Bedok Reservoir":[
      "DT30"
   ],
   "Tampines West":[
      "DT31"
   ],
   "Tampines East":[
      "DT33"
   ],
   "Upper Changi":[
      "DT34"
   ],
   "Woodlands North":[
      "TE1"
   ],
   "Woodlands South":[
      "TE3"
   ],
   "Springleaf":[
      "TE4"
   ],
   "Lentor":[
      "TE5"
   ],
   "Mayflower":[
      "TE6"
   ],
   "Bright Hill":[
      "TE7"
   ],
   "Upper Thomson":[
      "TE8"
   ],
   "Mount Pleasant":[
      "TE10"
   ],
   "Napier":[
      "TE12"
   ],
   "Orchard Boulevard":[
      "TE13"
   ],
   "Great World":[
      "TE15"
   ],
   "Havelock":[
      "TE16"
   ],
   "Maxwell":[
      "TE18"
   ],
   "Shenton Way":[
      "TE19"
   ],
   "Marina South":[
      "TE21"
   ],
   "Gardens by the Bay":[
      "TE22"
   ]
}, "Test stations_per_location"

def test_create_mrt_single_line_adjacency_list():
    stations = location_per_station()
    graph = MRT_GRAPH(len(stations))
    graph.create_mrt_single_line_adjacency_list(stations)
    # graph.print_mrt_adjacency_list()

def test_create_mrt_connected_station_adjacency_list():
    locations = stations_per_location()
    graph = MRT_GRAPH(len(locations))
    graph.create_mrt_connected_station_adjacency_list(locations)
    # graph.print_mrt_adjacency_list()

def test_translate_route_to_sentence():
    routes = ["DT28","DT27","DT26","CC10","CC9","EW8","EW9","EW10","EW11","EW12","EW13","NS25","NS24","NS23"]
    assert translate_route_to_sentence(routes) == [
        'Take DT line from Kaki Bukit to Ubi', 
        'Take DT line from Ubi to MacPherson', 
        'Change from DT line to CC line', 
        'Take CC line from MacPherson to Paya Lebar', 
        'Change from CC line to EW line', 
        'Take EW line from Paya Lebar to Aljunied', 
        'Take EW line from Aljunied to Kallang', 
        'Take EW line from Kallang to Lavender', 
        'Take EW line from Lavender to Bugis', 
        'Take EW line from Bugis to City Hall', 
        'Change from EW line to NS line', 
        'Take NS line from City Hall to Dhoby Ghaut', 
        'Take NS line from Dhoby Ghaut to Somerset'
        ], "Test translate_route_to_sentence"

def test_create_mrt_map():
    stations = location_per_station()
    locations = stations_per_location()
    graph = MRT_GRAPH(len(stations))
    graph.create_mrt_single_line_adjacency_list(stations)
    graph.create_mrt_connected_station_adjacency_list(locations)
    graph.BFS_SP("NS1", "CC2")


if __name__ == "__main__":
    test_location_per_station()
    test_stations_per_location()
    test_create_mrt_single_line_adjacency_list()
    test_create_mrt_connected_station_adjacency_list()
    test_translate_route_to_sentence()
    test_create_mrt_map()

    print("\n-----ALL TEST CASE PASSED-----\n")