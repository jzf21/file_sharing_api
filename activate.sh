#shell script to start fastapi server from installing venv to downloading dependencies

# create virtual environment

py -m venv venv

# activate virtual environment
source venv/Scripts/activate

# install dependencies
pip install -r requirements.txt

# start fastapi server
uvicorn main:app --reload
```
