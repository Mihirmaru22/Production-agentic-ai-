from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def instance():
    return """Mount Everest ain't got shit on me \n
              Mount Everest ain't got shit on me \n
              'Cause I'm on top of the world \n
              I'm on top of the world, yeah"""