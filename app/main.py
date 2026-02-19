# Entry point of FastAPI application.
   # Creates FastAPI instance.
   # Includes API routers.
   # Handles startup events (DB initialization).
  # DOES NOT contain business logic.
  
  
from fastapi import FastAPI
from api.routes import router
import uvicorn

app = FastAPI(title="Core Intelligence API", version="1.0")


#incluude the router 
 
app.include_router(router)


if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=8080 , reload = True)