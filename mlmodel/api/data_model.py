"""
Schema for the input data using pydantic.
NOTE: pydantic is primarily a parsing library: not a validation library.
Pydantic guarantees the types and constrains of the output model: not the input data.
"""

from pydantic import BaseModel, Field


class BasicInputData(BaseModel):
    """
    Schema for the input data on the POST method.
    All inputs are indices from dropdown lists within a web form.

    """

    # access the data from form
    age: int
    workclass: str
    fnlgt: int
    education: str
    education_num: int = Field(alias='education_num')
    marital_status: str = Field(alias='marital_status')
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: int = Field(alias='capital_gain')
    capital_loss: int = Field(alias='capital_loss')
    hours_per_week: int = Field(alias='hours_per_week')
    native_country: str = Field(alias='native_country')

    class Config:
        """
        FastAPI autogenerates documentation for the data model/API etc.
        schema_extra is just used as an example for documentation purposes.
        Go to http://172.0.0.1:8000/docs to view the docs.
        """
        schema_extra = {
            "example": {
                    "age": 55,
                    "workclass": "Private",
                    "fnlgt": 77516,
                    "education": "Masters",
                    "education_num": 13,
                    "marital_status": "Never-married",
                    "occupation": "Adm-clerical",
                    "relationship": "Not-in-family",
                    "race": "White",
                    "sex": "Female",
                    "capital_gain": 2174,
                    "capital_loss": 0,
                    "hours_per_week": 40,
                    "native_country": "United-States",
            }
        }