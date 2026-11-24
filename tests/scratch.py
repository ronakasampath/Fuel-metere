"""
from backend.app.core.modules.pricing.price import calculatePricePetrol,calculatePriceDisel

travelDisel = calculatePriceDisel(50,8,18)
assert travelDisel['CommutePriceDiesel'] < 50000
assert travelDisel['TotalLiters'] < 500


travelPetrol = calculatePricePetrol(40,8,10)
assert travelPetrol['CommutePricePetrol'] < 50000
assert travelPetrol['TotalLiters'] < 300
"""