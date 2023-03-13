from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/conjugate/{verb}")
async def conjugate(verb: str):
    base = verb[:-2]
    return {
        "verb": verb, 
        "forms": [
            ("je", base + "e"),
            ("tu", base + "es"),
            ("il/elle", base + "e"),
            ("nous", base + "ons"),
            ("vous", base + "ez"),
            ("ils/elles", base + "ent"),
        ]}
