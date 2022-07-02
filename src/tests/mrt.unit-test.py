from ..utils.utils import stationsPerLocation, locationPerStation, previousCurrentNext

def test_sum():
    assert stationsPerLocation() == {}, "Test stationsPerLocation"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")