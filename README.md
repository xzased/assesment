Assesment
=========

Simple web service that receive a string as input and determines if the string
contains at least one of each letter of the alphabet.

Requirements
------------

- Flask-Restful

Installation
------------

Clone this repo and cd into its root directory:

    $ git clone https://github.com/xzased/assesment.git
    $ cd assesment

You can create a virtual environment and install the required packages with the following commands:

    $ python3 -m venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

Running the API
---------------

With the virtual environment activated you can start the flask API.

    (venv) $ python assesment/api.py


In another terminal, you can test it with different data:

    $ curl -d "string_input=HI" -X POST http://localhost:5000/string/
    {
        "is_pangram": false
    }

    $ curl -d "string_input=Farmer jack realized that big yellow quilts were expensive" -X POST http://localhost:5000/string/
    {
        "is_pangram": true
    }

Testing the API
---------------

Basic unit tests are included in this project under `/tests`.

    (venv) $ python -m unittest
