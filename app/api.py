from fastapi import FastAPI, Depends
from .olx.scraping import OLX
from .database import SessionLocal

app = FastAPI()
BASE_END_POINT = "/api/v1"

def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get(f'{BASE_END_POINT}/health')
def health():
    return {"status": "ok"}


@app.get(f'{BASE_END_POINT}/olx/houses')
async def get_houses_list(page: int = 0, limit: int = 50):
    scraper = OLX()
    houses = scraper.get_parsed_data(page)
    return list(houses)[:limit]

@app.get(f'{BASE_END_POINT}/olx/houses/{{house_id}}')
async def get_house(house_id: int, page: int = 0, limit: int = 50):
    if house_id > limit:
        return {"error": "House id is greater than limit"}
    scraper = OLX()
    house = scraper.get_parsed_data(page)
    return list(house)[house_id]
