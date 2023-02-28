# -*- coding: utf-8 -*-
 
#
# Imports
#
from flask import Flask, jsonify
 
app = Flask(__name__)
 
#
# Routes
#
@app.route('/', methods=['GET'])
def test():
    return jsonify({'running': 'true'})
 
if __name__ == "__main__":
    app.run(debug=True) # remember to set debug to False
