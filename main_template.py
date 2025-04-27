import librosa
from flask import Flask, request, jsonify
from flask_caching import Cache
from werkzeug.datastructures.structures import ImmutableDict, ImmutableMultiDict, TypeConversionDict

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Default value
cache.set('v', 101)

def returnbin(val):
    return bin(val)[2:]  # [2:] removes the '0b' prefix

@app.route('/', methods=['GET', 'POST'])
def process_request():
    # Check if TransmitterId cookie is set and equals 1

    # if transmitter_id or transmitter_id == '1':
    if request.method == 'GET':
        # Increment 'v' and return its binary value
        v = cache.get('v')
        return jsonify({'value': returnbin(v)})

    if request.method == 'POST':
        # Get the POST value
        value = request.form.get('value')
        # Convert binary to decimal
        decimal_value = int(value,2)
        # Set 'v' to the decimal value
        cache.set('v', decimal_value)
        return jsonify({'value': returnbin(v)})
    return jsonify({'value': returnbin(v)})
    # If TransmitterId is not set or not equal to 1, return error response
    # return jsonify({'value': '0'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
