from app import app

# here we map two urls to greet function that return a string using function decorators 
# if the client request "/" or "/index" url this function will be sent to the client as response  
@app.route("/")
@app.route("/index")
def greet() -> str :
    return "hello world" 