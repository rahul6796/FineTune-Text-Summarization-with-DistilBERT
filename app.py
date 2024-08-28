
from fastapi import FastAPI
import uvicorn
import os
import json

from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response

from src.textsummarizationv2.pipeline.prediction import PredictionPipeline



app = FastAPI()

@app.get('/', tags=['authentication'])
async def index():
    return  RedirectResponse(url='/docs')


@app.get('/train')
async def training():
    try:
        os.system('python main.py')
        return Response("Training Successfully !!")
    except Exception as e:
        return Response(f'Error Occured ! {e}')
    
@app.get('/predict')
async def prediction(text):

    try:
        obj = PredictionPipeline()
        text  = obj.predict(text=text)
        return text
    except Exception as e:
        return Response(f'Error Occured ! {e}')


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)


