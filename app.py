from flask import Flask, render_template, request
import json, datetime

app = Flask(__name__)

userInfo = None
with open('/usr/src/app/userdata.json', 'r') as db:
    userInfo = json.loads(db.read())

UNAME = "None"
UZIP = 0

productInfo = None
with open('/usr/src/app/productInfo.json') as db:
    productInfo = json.loads(db.read())

messages = None
with open('/usr/src/app/messages.json') as db:
    messages = json.loads(db.read())

@app.route('/')
def index():
    #---------------------------------------
    # If not logged in, user must login first.
    #---------------------------------------
    # return render_template('index.html', url="http://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26388-1381844103-11.gif")
    if not loggedIn():
        return login()
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
    global UNAME
    uname = request.form['uname']
    pwd = request.form['pwd']

    if uname in userInfo:
        if pwd == userInfo[uname]['pass']:
            # Sucess
            UNAME = uname
            zcode = userInfo[uname]['zip']
            UZIP = zcode
            products = searchInProximity(zcode)
            return render_template('home.html', uname = UNAME, products = products)
        else:
            # Incorrect pass
            return render_template('login.html')
    else:
        # Unregistered user
        return render_template('login.html')

def searchInProximity(zipcode = 0):
    #---------------------------------------
    # Searches for products in proximity of a zipcode.
    # Returns an array of products.
    #---------------------------------------
    products = []
    for key, product in productInfo.iteritems():
        product['dist'] = abs(int(zipcode) - int(userInfo[product["uname"]]['zip']))
        product['id'] = key
        products += product,
    return sorted(products, key = lambda d: d['dist'])

@app.route('/search')
def searchWithKeyword(keyword, zipcode):
    #---------------------------------------
    # Returns products related to keyword sorted by distance if possible.
    #---------------------------------------
    pass

@app.route('/home')
def home():
    products = searchInProximity(UZIP)
    return render_template('home.html', products = products , uname = UNAME)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registerform', methods = ['POST'])
def registerform():
    newUser = {}

    uname = request.form['uname']
    pwd = request.form['pwd']
    zcode = request.form['zcode']

    newUser[uname] = {"pass": pwd, "zcode": zcode, "products": []}

    # Put data into DB.
    try:
        userInfo.update(newUser)
        with open('userdata.json', 'w') as db:
            json.dump(userInfo, db)
        UNAME = uname
        products = searchInProximity(zcode)
        return render_template('home.html', uname = UNAME, products = products)
    except:
        # Failed
        return render_template('register.html')


@app.route('/product/<productID>')
def productpage(productID):
    #---------------------------------------
    # Returns a product info packet.
    #---------------------------------------
    print 'productID', productID
    product = productInfo[str(productID)]
    return render_template('productpage.html', product= product)

@app.route('/upload_product')
def upload():
    #---------------------------------------
    # Uploads user product if valid. Shows appropraite message afterwards.
    #---------------------------------------

    return render_template('upload_product.html')

@app.route('/upload_product_form', methods = ['POST'])
def upload_product_form():
    pname = request.form['pname']
    pdesc = request.form['pdesc']
    purl = request.form['purl']
    pyear = request.form['pyear']

    newProduct = {}

    newProduct[len(productInfo)+1] = {"name": pname, "desc": pdesc, "url": purl, "uname": UNAME, "year": pyear}

    # Put data into DB.
    try:
        productInfo.update(newProduct)
        with open('productInfo.json', 'w') as db:
            json.dump(productInfo, db)
        products = searchInProximity(zcode)
        return render_template('home.html', uname = UNAME, products = products)
    except Exception as e:
        # Failed
        print e
        return render_template('home.html')

def uploadStatus(message):
    #---------------------------------------
    # Shows the message on a webpage.
    #---------------------------------------
    pass

@app.route('/my_products')
def myproducts():
    #---------------------------------------
    # Shows the current products uploaded by user.
    #---------------------------------------

    # Fetch products from DB
    products = []

    for product in productInfo.values():
        if product["uname"] == UNAME:
            products += product,

    return render_template("my_products.html", products = products)

@app.route('/exchange/<productID>')
def exchange(productID):
    #---------------------------------------
    # Returns current products of user and selected product to exchange with.
    #---------------------------------------
    oproduct = productInfo[productID]
    # Need only render--------*******************************
    return render_template('exchange.html', oproduct = oproduct)

@app.route('/exchangeform', methods = ['POST'])
def exchangeform():
    #---------------------------------------
    # Returns current products of user and selected product to exchange with.
    #---------------------------------------
    pid = request.form['pid']
    msg = request.form['msg']
    mdate = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")


    newMsg =  {}
    newMsg["from"] = UNAME
    newMsg["msg"] = msg
    newMsg["date"] = mdate
    newMsg["id"] = pid
    newMsg[productInfo[pid]["uname"]] = newMsg

    messages.update(newMsg)
    with open('/usr/src/app/messages.json') as db:
        json.dump(messages, db)

    # Need only render--------*******************************
    return render_template('status.html', message = "Message sent!")


@app.route('/inbox')
def inbox():
    #---------------------------------------
    # Returns the messages with read or unread status.
    #---------------------------------------
    my_msgs = []
    print UNAME
    for uname, msg in messages.iteritems():
        if uname != UNAME:
            msgPacket = {}
            msgPacket["from"] = msg["from"]
            msgPacket["msg"] = msg["msg"]
            msgPacket["date"] = msg["date"]

            my_msgs += msgPacket,


    return render_template('inbox.html', messages = my_msgs)


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
