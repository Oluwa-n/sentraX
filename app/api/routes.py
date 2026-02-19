 # Defines HTTP endpoints:
     # - POST /ask
      # - GET /models
      # - GET /health
      # - GET /user/{id}
      # ONLY handles request/response.
       # Calls service layer.
      # NO AI logic.
      # NO DB raw queries.
      
from fastapi import APIRouter

router = APIRouter()

@router.get('/home')
def index():
    return {'message': 'Welcome to the Core Intelligence API!'}
      