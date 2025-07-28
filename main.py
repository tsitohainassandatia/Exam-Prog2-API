from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def lire_racine():
    return {"message": "Bienvenue sur mon API"}

@app.get("/salut/{nom}")
def saluer(nom: str):
    return {"message": f"salut, {nom}!"}