from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from models import Author,Book
from database import SessionLocal,init_db

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books")
async def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books


             
@app.post("/books")
async def create_book(title : str,author_id:int, db: Session = Depends(get_db)):
    try:
        db_book = Book(title=title,author_id=author_id)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception as e:
        print("exception occured")
        print(e)



@app.get("/authors")
async def get_authors(db: Session = Depends(get_db)):
    authors = db.query(Author).all()
    return authors

@app.post("/authors")
async def create_authors(name: str,db: Session = Depends(get_db)):
    db_author = Author(name=name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author




@app.delete("/books/{book_id}")

async def delete_book(book_id : int, db : Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return {"message": "Book deleted successfulluy"}
    
    else:
        raise HTTPException(status_code=404,detail="Book not found")


@app.delete("/authors/{author_id}")
async def delete_author(author_id : int, db :  Session = Depends(get_db)):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author:
        db.delete(db_author)
        db.commit()
        return {"message":"Author deleted successfully"}

    else:
        raise HTTPException(status_code=404,detail="Author not found") 
    




