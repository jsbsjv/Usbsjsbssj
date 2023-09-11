from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome To 𝑠𝑜𝑢𝑛𝑑𝑤𝑎𝑣𝑒 Source'

# تحياتي عبودي سكيبه
if __name__ == "__main__":
    app.run()
