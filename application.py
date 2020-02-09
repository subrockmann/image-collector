from app import app
from app import s3

@app.route('/')
def home():
    return "Hello World - Index"





if __name__ == "__main__":
    app.debug = True
    app.run()