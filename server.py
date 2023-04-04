from flask import Flask, request
#from this tool (from flask ) import this class (import Flask )
#This allow us (request) to make a reques in the post method

import json 

from about import me #importing my dictionary
from data import mock_data

#After create a client in config.py, we import de db
#From the file config
from  config import db

#Create an instance of Flask class -> app = Flask() 
app = Flask(__name__) #Magic variables __name__

#WEB SERVER
#To show something when the server starts
@app.get("/")
def home():
    return "Hello World from a flask server"

@app.get("/test")
def test():
    return "This is a test page"

#API SERVER, this is what we need
#An API is a program designed to be consumed for
#another program

@app.get("/api/version")
def version():
    return json.dumps("1.0") #We work with JSON

#An endpoint that retuns the infrmation of my dictionary
@app.get("/api/about")
def about():
    return json.dumps(me)

#get /api/developer/name
#return the full name of the developer plus the email
#eg. Sergio Inzunza -- sinzunza@sdgku.edu

@app.get("/api/developer/name")
def developer_name():
    name = me["name"]
    last_name = me["last_name"]
    email = me["email"]
    developer = f"{name} {last_name} -- {email}"
    return json.dumps(developer)
    # return json.dumps(f"{me["name"]} {me["last_name"]} -- {me["email"]}")

#An endpoint that retuns the infrmation of my catalog
@app.get("/api/catalog")
def get_catalog():

    #Change mock_data for the db (Class 110 - 2)
                        #A kind of filter
    cursor = db.products.find({})
    #Cursor is a object that we can only read
    #Do not parse to json or something else

    results = []
    #Add cursor to an empty list to manage data
    for prod in cursor:
        results.append(fix_id(prod))

    #return json.dumps(mock_data)
    return json.dumps(results)


#--------------A POST REQUEST----------------
@app.post("/api/catalog")
def save_product():
    #get the json payload from the request
    #we will get a dictionary, product is a dictorionary
    product = request.get_json() 

    #Save the product to DB
    #If the collection (products) does not exist, it would be created.
    db.products.insert_one(product)

    #Print something just to chek
    print("-----------MY FIRST GET REQUEST-------------")
    print(fix_id(product))

    #The endpoints always has to return somethin, if not, that 
    #will be an error
    return json.dumps(product)

@app.get("/api/products/count")
def products_count():
    return json.dumps(len(mock_data))

#class 4
#1. get /api/products/total
#return the sum of all prices in the catalog
@app.get("/api/products/total")
def products_total():
    total = 0
    for product in mock_data:
        total = total + float(product["price"])
    return json.dumps(total)

#2.  get /api/categories
#return a list of categories
@app.get("/api/products/categories")
def products_categories():
    #get all
    cursor = db.products.find({})

    #list of categories
    categories = []

    for prod in cursor:
        category = prod["category"]

        if category not in categories:
            categories.append(category)

    #we fix the id if we return all the prod
    return json.dumps(categories)

#3. Create dynamic endpoints # get /api/catalog/<variable> 
@app.get("/api/catalog/<category>")
def products_by_category(category):
    #Create a list
    #products = []
    #Travel mock_data with a for loop
    #for product in mock_data:
        #from the product, get the category
        #the_category = product["category"]
        #if category is equal to the category we received
        #if the_category == "Clutch":
        #if the_category.lower() == category.lower(): #use lower to avoid case-sensitive
            #if so, append product to the list
            #products.append(product)
    # at the end of the for loope, return the list

    #Get it from the DB
    cursor = db.products.find({"category": category})
    results = []
    for prod in cursor:
        results.append(fix_id(prod))
    
    return json.dumps(results)

#4. get /api/products/lower/<price>
# should return all the products whose price is lower than price var
@app.get("/api/products/lower/<price>")
def products_lower_price(price):
    fixed_price = float(price)
    results = []

    for prod in mock_data:
        if prod["price"] < fixed_price:
            results.append(prod)
    
    return json.dumps(results)

#5. get /api/products/greater/<price>
# prices geater OR EQUAL 

@app.get("/api/products/geater/<price>")
def producst_geater_price(price):
    fixed_price = float(price)
    results = []

    for prod in mock_data:
        if prod["price"] >= fixed_price:
            results.append(prod)
    
    return json.dumps(results)

#6. get /api/products/search/<term>
# search must be case insensitive

# create an empy list
# for to travel mock_data
# if the product title lowercase contains the term
# add the product to the list

@app.get("/api/products/search/<term>")
def products_search(term):
    result = []

    for prod in mock_data:
        if term.lower() in prod["title"].lower():
            result.append(prod)
    
    return json.dumps(result)

def fix_id(record):
    #Read the id to remove the _ of id.
    record["_id"] = str(record["_id"])
    return record



############################################################
###################### CUPON CODES #########################
############################################################

# POST /api/coupons -> Save coupons
# { "code": "qwerty", "discount": 10 }
@app.post("/api/coupons")
def save_coupon():
    coupon = request.get_json() 
    db.coupons.insert_one(coupon)
    print("----------- SAVING A COUPON-------------")
    print(fix_id(coupon))

    return json.dumps(coupon)


# GET /api/coupons  -> return all the coupons
@app.get("/api/coupons")
def get_coupon():
    cursor = db.coupons.find({})
    results = []

    for coupon in cursor:
        results.append(fix_id(coupon))

    return json.dumps(results)

#Start the server
app.run(debug=True) #debug = True get details about an error,
#but do not used in production

