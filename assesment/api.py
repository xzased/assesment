import re
import string

from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('string_input',
                    type=str,
                    default='',
                    help='String input for this resource')

alphabet_set = set(string.ascii_lowercase)



def get_alphabet_chars(string_input):
    """
    Removes non-alphabet characters from a string.

    :param string_input: str
    :return: str
    """
    regex = re.compile('[^a-zA-Z]')
    alphabet_chars = regex.sub('', string_input)
    return alphabet_chars


def is_pangram(string_input):
    """
    Takes a string and determines if it is a pangram.

    :param string_input: str
    :return: boolean
    """
    lower_input = string_input.lower()
    chars = get_alphabet_chars(lower_input)

    return set(chars) >= alphabet_set


class StringAPI(Resource):
    """
    Assesment API string resource
    """
    def post(self):
        """
        Receives a string as input, potentially a mixture of upper and
        lower case, numbers, special characters etc. and determines if the
        string contains at least one of each letter of the alphabet.

        Returns true if all are found and false if not.

        :return: boolean
        """
        args = parser.parse_args()
        string_input = args.get('string_input')

        # Here the response could just be a boolean as it would be a valid
        # JSON value, but a best practice would be to use an object since
        # it makes the response extendable.
        response = {
            'is_pangram': is_pangram(string_input)
        }

        return response

api.add_resource(StringAPI, '/string/')


if __name__ == '__main__':
    app.run(debug=True)
