import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app import models, schemas, crud, deps

deps.create_database()
models.Base.metadata.create_all(bind=deps.engine)
app = FastAPI(docs_url="/api_docs", redoc_url="/api_redoc")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/memes", response_model=list[schemas.Meme])
def read_memes(skip: int = 0, limit: int = 15, db: Session = Depends(deps.get_db)):
    memes = crud.get_memes(db, skip=skip, limit=limit)
    return memes

@app.get("/memes/{meme_id}", response_model=schemas.Meme)
def read_meme(meme_id: int, db: Session = Depends(deps.get_db)):
    try:
        db_meme = crud.get_meme(db, meme_id=meme_id)
        if db_meme is None:
            raise HTTPException(status_code=404, detail="Meme not found")
        return db_meme
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/memes", response_model=schemas.Meme)
def create_meme(meme: schemas.MemeCreate, db: Session = Depends(deps.get_db)):
    try:
        return crud.create_meme(db=db, meme=meme)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/memes/{meme_id}", response_model=schemas.Meme)
def update_meme(meme_id: int, meme: schemas.MemeCreate, db: Session = Depends(deps.get_db)):
    try:    
        return crud.update_meme(db=db, meme_id=meme_id, meme=meme)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/memes/{meme_id}", response_model=schemas.Meme)
def delete_meme(meme_id: int, db: Session = Depends(deps.get_db)):
    try:
        return crud.delete_meme(db=db, meme_id=meme_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
