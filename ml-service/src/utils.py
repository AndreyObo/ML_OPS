from pydantic import BaseModel, Field

class ModelData(BaseModel):
    LIMIT_BAL: float = Field(default=0)
    SEX: int = Field(default=0)
    EDUCATION: int = Field(default=0)
    MARRIAGE: int = Field(default=0)
    AGE: int = Field(default=0)
    PAY_0: int = Field(default=0)
    PAY_2: int = Field(default=0)
    PAY_3: int = Field(default=0)
    PAY_4: int = Field(default=0)
    PAY_5: int = Field(default=0)
    PAY_6: int = Field(default=0)
    BILL_AMT1: float = Field(default=0)
    BILL_AMT2: float = Field(default=0)
    BILL_AMT3: float = Field(default=0)
    BILL_AMT4: float = Field(default=0)
    BILL_AMT5: float = Field(default=0)
    BILL_AMT6: float = Field(default=0)
    PAY_AMT1: float = Field(default=0)
    PAY_AMT2: float = Field(default=0)
    PAY_AMT3: float = Field(default=0)
    PAY_AMT4: float = Field(default=0)
    PAY_AMT5: float = Field(default=0)
    PAY_AMT6: float = Field(default=0)


class ResponseModel(BaseModel):
    prediction:str