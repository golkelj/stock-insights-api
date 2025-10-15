from flask import Flask
from routes.stocks import stock_bp

app = Flask(__name__)
app.register_blueprint(stock_bp)

if __name__ == "__main__":
    app.run(debug=True)