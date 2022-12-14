# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request


app = Flask(__name__)

@app.route('/test', methods =['POST'])
def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    request_data = request.get_json()

    return request_data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, port=5000)

