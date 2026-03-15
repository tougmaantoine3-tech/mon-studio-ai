from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import replicate
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate")
async def generate(prompt: str, type: str):
    # On récupère le token depuis les variables d'environnement de Render
    os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")
    
    if type == "image":
        model = "stability-ai/sdxl:7762d33955883901407026e63297497ce64b1cd783857500057022ad65b5c928"
    elif type == "video":
        model = "anotherjesse/zeroscope-v2-xl:9f742d1967a4d2049e755535384666f7f63116bc987c8072049079f90f235d97"
    
    output = replicate.run(model, input={"prompt": prompt})
    return {"url": output[0]}
  
