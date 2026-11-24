from fastapi import FastAPI,Body
from core.modules.pricing.price import FuelPriceMesure
#from backend.app.core.modules.pricing.accept import AcceptDieselAmount,AcceptDieselPrice,AcceptPetrolAmount,AcceptPetrolPrice
from typing import Annotated
from core.modules.pricing.schemas import PriceMeasure
import core.config

app = FastAPI()


@app.get('/home')
def home() :
    return {
        "message":"Welcome to the platform!"
    }


@app.post('/price')
def CalculateFuelPrice(price:PriceMeasure):
    try:
        Cost = FuelPriceMesure(price.Consumption,price.Distance,price.FuelType)
        return {
            "cost":Cost
        }
    except ValueError as e:
        message = str(e)
        return {
                    "message":message,
        }
        
    except:
        return {
            "message":"Server Error",
        }



"""
@app.post('/Commute/Price/Disel')
def dieselPriceCalculate(DieselPrice:Annotated[float,Body(gt=0)],
                         TravelDistance:Annotated[float,Body(gt=0)],
                         VehicleConsumption:Annotated[float,Body(gt=0)],
                         LimitPrice:Annotated[float,Body(gt=0)]):
    unitPrice = DieselPrice
    distance = TravelDistance
    consumption = VehicleConsumption
    pricelimit = LimitPrice
    commute = calculatePriceDisel(unitPrice,consumption,distance)
    

    acceptance = ""


    try:
        cost = commute["CommutePriceDiesel"]
        AcceptDieselPrice(pricelimit,cost)
    except AssertionError:
        acceptance = "Disapproved"
    except:
        acceptance = "Error"
    else:
        acceptance = f"Total price : {cost}"

    return{
        "Message":acceptance
    }
        
"""   
