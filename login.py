@app.route("/login', methods ['GET', 'POST' ]")
def login() :
    msg=''
    if request.method == 'POST' and 'username' in request. form and 'password' in request. form:
        username = request. form["username" ]
        password = request. form[ "password"]
        mydb = mysql. connector.connect(
        host="remotemysql.com",
        user= "Rz8hqn1dk4",
        password="ndewx03xe0",
        database="Rz8hqn1dk4")
        mycursor - mydb. cursor()
        mycursor.execute( "SELECT * FROM LoginDetails WHERE Name = %s AND Passwrd - %s", (username, password))
        account = mycursor.fetchone()
    if account:
        print('login success')
        name - account [1]
        id = account [0]
        msg = 'Logged in Successfully"
        print('login successfull')
        return render_template(' index.html" , msg-msg, name=name, id=id)
        else:
        msg - 'incorrect Credentials. Kindly check"
        return render_template( 'login.html' ,msg_msg)
    else:
return render_template( 'login.html")
