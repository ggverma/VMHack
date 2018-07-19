from flask import Flask, render_template
import json

app = Flask(__name__)

userInfo = None
with open('userdata.json') as db:
    userInfo = json.loads(db)

productInfo = None
with open('productdata.json') as db:
    productInfo = json.loads(db)

@app.route('/')
def index():
    #---------------------------------------
    # If not logged in, user must login first.
    #---------------------------------------
    # return render_template('index.html', url="http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26388-1381844103-11.gif")
    if not loggedIn():
``        return login()
    else:
        #---------------------------------------
        # Returns some products
        # If location is available, display local results first.
        #---------------------------------------
        return render_template('index.html', url="http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26388-1381844103-11.gif")

def loggedIn():
    #---------------------------------------
    # Checks if a user is logged in.
    # Returns true or false
    #---------------------------------------
    return False

@app.route('/login')
def login():
    #---------------------------------------
    # A web page showing some random products and facebook login
    #---------------------------------------
    return render_template('login.html')

@app.route('/loginform', methods = ['POST'])
def loginform():
    uname = request.form['uname']
    pwd = request.form['pwd']

    if uname in userInfo:
        if pwd == db[uname]['pwd']:
            # Sucess
            return render_template('home.html')
        else:
            # Incorrect pass
            return render_template('login.html')
    else:
        # Unregistered user
        return render_template('login.html')


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

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registerform', methods = ['POST'])
def registerform():
    newUser = {}

    uname = request.form['uname']
    pwd = request.form['pwd']
    zcode = request.form['zcode']

    newUser[uname] = {"pass": pwd, "zcode" = zcode, "products" = []}

    # Put data into DB.
    if registerUserInDB():
        # Success
        userInfo.update
        with open('userdata.json') as db:
            userInfo += newUser,

    else:
        # Failed
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

@app.route('/upload_product_form', methods = ['POST'])
def upload_product_form():
    pname = request.form['uname']
    pdesc = request.form['pdesc']
    purl = request.form['purl']
    pyear = request.form['pyear']


    # Put data into DB.
    if registerUserInDB():
        # Success
        pass
    else:
        # Failed
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

    # Fetch products from DB
    products = {}

    # Need only render--------*******************************
    pass

@app.route('/exchange')
def exchange():
    #---------------------------------------
    # Returns current products of user and selected product to exchange with.
    #---------------------------------------

    # Need only render--------*******************************
    pass

@app.route('/inbox')
def inbox():
    #---------------------------------------
    # Returns the messages with read or unread status.
    #---------------------------------------

    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)

################################################################################
# Fields in:
# Product:
#   ID (Integer)
#   Image URL (url)
#   Name (String)
#   Description (String)
#   Year Bought In (Integer)
#

# json:
# {<uname>:
#   pass: "",
#   }
