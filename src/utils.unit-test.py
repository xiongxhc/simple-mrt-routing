from utils import translate_route_to_sentence

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

if __name__ == "__main__":
    test_translate_route_to_sentence()
    print("Everything passed")