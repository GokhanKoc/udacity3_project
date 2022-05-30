# Put the code for your API here.

import pickle as pkl
import pandas as pd
import uvicorn
from fastapi.responses import JSONResponse
from fastapi import FastAPI

from .data_model import BasicInputData


import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)


from ml.data import process_data
from ml.model import inference
import config as config


if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")


app = FastAPI(
    title="API for Salary Model",
    description="Return prediction for salary",
    version="0.0.1",
)
with open(config.MODEL_PATH, 'rb') as f:
    encoder, lb, model = pkl.load(f)


@app.get("/")
async def welcome():
    """
    Example function for returning home directory.
    Args:
    Returns:
        example_message (Dict) : Example message response for home directory
        GET request.
    """
    return {'message': 'Welcome to the salary predictor!!'}

@app.post("/predictions")
async def prediction(input_data: BasicInputData):
    """
    Example function for returning model output from POST request.
    The function take in a single web form entry and converts it to a single
    row of input data conforming to the constraints of the features used in the model.
    Args:
        input_data (BasicInputData) : Instance of a BasicInputData object. Collected data from
        web form submission.
    Returns:
        json_res (JSONResponse) : A JSON serialized response dictionary containing
        model classification of input data.
    """
    # Read the trained model and the encoder
    with open(config.MODEL_PATH, 'rb') as f:
        encoder, lb, model = pkl.load(f)

    # Formatting input_data
    input_df = pd.DataFrame(
        {k: v for k, v in input_data.dict(by_alias=True).items()}, index=[0]
    )

    x_data, _, _, _ = process_data(
        X=input_df,
        categorical_features=config.cat_features,
        label=None,
        training=False,
        encoder=encoder,
        lb=lb
    )

    # get predictions and return
    pred = inference(model, x_data)

    y = lb.inverse_transform(pred)[0]

    print(y)

    return {"predicted salary": y}