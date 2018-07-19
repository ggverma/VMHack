from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #---------------------------------------
    # If not logged in, user must login first.
    #---------------------------------------
    if not loggedIn():
        login()
    else:
        #---------------------------------------
        # Returns some products
        # If location is available, display local results first.
        #---------------------------------------
        pass

def loggedIn():
    #---------------------------------------
    # Checks if a user is logged in.
    # Returns true or false
    #---------------------------------------
    pass

@app.route('/login')
def login():
    #---------------------------------------
    # A web page showing some random products and facebook login
    #---------------------------------------
    pass

def searchInProximity(zipcode):
    #---------------------------------------
    # Searches for products in proximity of a zipcode.
    # Returns an array of products.
    #---------------------------------------
    pass

@app.route('/search')
def searchWithKeyword(keyword, zipcode):
    #---------------------------------------
    # Returns products related to keyword sorted by distance if possible.
    #---------------------------------------
    pass

@app.route('/product/<productID>')
def getProductInfo(productID):
    #---------------------------------------
    # Returns a product info packet.
    #---------------------------------------
    pass

@app.route('/upload')
def upload():
    #---------------------------------------
    # Uploads user product if valid. Shows appropraite message afterwards.
    #---------------------------------------

    pass

def uploadStatus(message):
    #---------------------------------------
    # Shows the message on a webpage.
    #---------------------------------------
    pass

@app.route('/myproducts')
def myproducts():
    #---------------------------------------
    # Shows the current products uploaded by user.
    #---------------------------------------
    pass

@app.route('/exchange')
def exchange():
    #---------------------------------------
    # Returns current products of user and selected product to exchange with.
    #---------------------------------------
    pass

@app.route('/inbox'):
def inbox():
    #---------------------------------------
    # Returns the messages with read or unread status.
    #---------------------------------------
    pass

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

################################################################################
# Fields in:
# Product:
#   ID (Integer)
#   Name (String)
#   Description (String)
#   Year Bought In (Integer)
#
