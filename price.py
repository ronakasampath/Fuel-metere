import config


def PriceMesure(Consumption,Distance,FuelType):
    if FuelType.lower() == "petrol92":
        return Consumption*Distance*config.petrol92Price
    elif FuelType.lower() == "petrol95":
        return Consumption*Distance*config.petrol95Price
    elif FuelType.lower() == "supersiesel":
        return Consumption*Distance*config.SuperDieselPrice
    elif FuelType.lower() == "autodiesel":
        return Consumption*Distance*config.AutoDieselPrice
    else:
        raise ValueError("Invalid fuel type")







"""

def calculatePricePetrol(petrolLiterPrice,fuelConsumption,totalDistance):
    totalPrice = petrolLiterPrice*fuelConsumption*totalDistance
    totalLiters = fuelConsumption*totalDistance
    return {
        "CommutePricePetrol" : totalPrice,
        "TotalLiters": totalLiters
    }

def calculatePriceDisel(diselLiterPrice,fuelConsumption,totalDistance):
    totalPrice = diselLiterPrice*fuelConsumption*totalDistance
    totalLiters = fuelConsumption*totalDistance
    return {
        "CommutePriceDiesel" : totalPrice,
        "TotalLiters": totalLiters
    }
    """