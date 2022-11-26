from fastapi import FastAPI
from schemas import Book, Author
from fastapi import Path, Query, Body


''' uvicorn main:app --reload --port 8080 '''
app = FastAPI()

@app.get('/')
def home():
	return {"key":"Hello"}
	
	
@app.get('/{pk}')
def get_item(pk: int, q:int ):
	return {"key":pk, "q":q}
	
@app.get('/users/{name}/codes/{code_person}')
def get_user_codePersone(name: str, code_person: int):
	return {"name":name, "code_person":code_person}
	
@app.post('/book')
def post_book(item : Book):
	return item
	
@app.get("/book/{pk}")
def get_single_book(pk : int = Path(..., gt=10, le = 500), page: int = Query(None, gt=10,le = 500)):
	return {"pk":pk, "page":page}
	
@app.post("/author")
def create_author(author: Author = Body(...,embed=True)):
	return {"author":author}
	
@app.post("/book_with_author")
def create_book(item: Book, author: Author, quantity: int = Body(...)):
	return {"item": item, "author": author, "quantity":quantity}
	
@app.post("/books", response_model = Book, response_model_exclude_unset = True)
def create_books(item: Book):
	return item