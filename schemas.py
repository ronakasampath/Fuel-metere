from pydantic import BaseModel,ConfigDict,Field

class PriceMeasure(BaseModel):
    Distance:float = Field(gt=0)
    FuelType:str = Field(pattern="(?i)^(AutoDiesel|SuperDiesel|petrol95|petrol92)$")
    Consumption:float = Field(gt=0)
    

