from typing import Union
from fastapi import FastAPI
from g4f.client import Client

client = Client()
app = FastAPI()

@app.get("/eslestir")
def read_root(ilk: str,iki: str):
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "system", "content": """
        You are the best linguist in the world. 
        You should give a word that representing or relating to the 2 given words.

        Try to answer with a new word that have an actual meaning. 
        ONLY answer in the following format WITHOUT SPACE.
        
        [SINGLE emoji that best represent the text],[an english word that has meaning with 2 other words]
    """},
    {
     "role": "user", "content": f"{ilk} and {iki}" 
    }
    ],
    )

    sonuc = {"message":"unknown", "element":{"emoji":response.choices[0].message.content.split(",")[0],"text":response.choices[0].message.content.split(",")[1],"discovered":"true"}}
    return sonuc
