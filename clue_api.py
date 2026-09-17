from fastapi import FastAPI, Response

try:
    from alan_wake_clue_api.controller import ClueController
except ImportError:
    from controller import ClueController

clue_app = FastAPI(title="Alan Wake Clue API", description="API for managing clues in the Alan Wake game.")

@clue_app.get("/")
async def root():
    return {"message": "Welcome to the Alan Wake Clue API"}

@clue_app.get("/clues")
async def get_clues():
    return Response(content=ClueController.get_all_clues(), media_type="application/json")