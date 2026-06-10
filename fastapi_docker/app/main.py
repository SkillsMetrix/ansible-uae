# import package
from fastapi import FastAPI
# create the object
app= FastAPI()
# created user data as array
users=[{'id':101,'username':'Admin','email':'admin@mail.com'}]

@app.get('/')
def welcomeMsg():
    return {'message': 'Welcome to FastAPI'}

@app.get('/loadusers')
def welcomeMsg():
    return {'userdata': users}