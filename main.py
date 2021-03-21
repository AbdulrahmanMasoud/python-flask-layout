## Import Flask And Render Template[to render html pages] From Flask
from flask import Flask, render_template

## My App Name Here Is:[__main__]
app = Flask(__name__)
users = [
    ("Abdulrahman",21,"Male"),
    ("Ahmed",12,"Male"),
    ("Yasmeen",23,"Female"),
    ("Amr",8,"Male"),
    ]

## Make a New Route
@app.route('/')
def home():
    ## Render Html Page By:[render_template] And Send Some Data i Use It In html file
    return render_template('index.html',pageTitle = 'Home',custmCss = 'home',data = users)

@app.route('/about')
def about():
    return render_template('about.html',pageTitle = 'About')

@app.route('/add')
def add():
    return render_template('add.html',pageTitle = 'Add',custmCss = 'add')

## Check If __name__ == My project Name If True Run My Project On 9000 Port
if __name__ == "__main__":
    app.run(port=9000)
