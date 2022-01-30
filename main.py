from extractor import Extractor


res = "https://www.swiggy.com/restaurants/leon-grill-100ft-road-indiranagar-bangalore-32603"
filen= "menu1"

my_extractor = Extractor()
my_extractor.extractFrom(res,filen)