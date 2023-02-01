from flask import Flask,render_template  # Import Flask to allow us to create our app
from user import User
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/login')    #  The "@" decorator associates this route with the function immediately following
def login():
    users = User.get_all()
    print (users)
    return render_template('index.html', users =users)  # renders the html of the index.html file

@app.route('/profile_page')
def home():
    return render_template('user_profile_page.html')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.