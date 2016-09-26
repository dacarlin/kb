import pandas
from flask import Flask, render_template
app = Flask(__name__)

# URLs

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

# custom display filters

@app.template_filter( 'fmt_kinetic' )
def fmt_kinetic( x ):
    '''Returns a color string based on the value of a kinetic constant'''
    my_color = ( 1, 0, 0, 0.7 )
    return 'rgba( {}, {}, {}, {} )'.format( *my_color )

# old custom filters code

import math
import numpy as np

bglb_color = {
  -4: "rgb( 47, 79, 79 )", #same as -3 for now
  -3: "rgb( 47, 79, 79 )",
  -2: "rgb( 102, 139, 139 )",
  -1: "rgb( 150, 205, 205 )",
   0: "rgb( 224, 224, 224 )", #neutral
   1: "rgb( 238, 233, 191 )",
   2: "rgb( 238, 220, 130 )",
   3: "rgb( 238, 220, 130 )", #same as -2 for now
   4: "rgb( 238, 220, 130 )",
}

@app.template_filter( 'colorize' )
def colorize( value, arg ): # value, value to compare to
    if value == None: # it's missing
        return 'rgba( 0,0,0,0 )'
    else:
        result = math.floor( np.log( value / arg ) )
        if result <= -4:
            return "rgba( 47, 79, 79, 1 )"
        elif result >= 4:
            return "rgb( 238, 220, 130 )"
        elif -4 <= result <= 4:
            return bglb_color[ result ]
        else:
            return 'rgba( 255, 0, 0, 0.2 )' #outside dyanamic range!
