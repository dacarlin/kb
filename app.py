import pandas
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template( 'home_page.html' )

@app.route( '/methods' )
def methods_page():
    return render_template( 'methods.html' )

@app.route( '/browse' )
def browse_page():
    df = pandas.read_csv( 'static/data_set.csv', index_col=0 )
    entry_list = [ x for x in df.iterrows() ] # returns (index, df) pairs
    return render_template( 'browse.html', entry_list=entry_list )

@app.route( '/submit' )
def submit_page():
    return render_template( 'submit.html' )
