from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# A list to store items
items = []


# Define the structure of the item using Pydantic
class Item(BaseModel):
    text: str = None
    is_done: bool = False


@app.get('/')
def root():
    return {"Hello": "World"}


@app.post('/items')
def create_item(item: Item):
    items.append(item)
    return {"message": "Item added successfully", "items": items}


@app.get('/items', response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]


@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id: int) -> Item:
    # Simulate finding the item by ID (for this example, we use index-based lookup)
    if 0 <= item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
