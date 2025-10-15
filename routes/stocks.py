from flask import Blueprint, jsonify, request
from utils.fetch_data import get_stock_data

stock_bp = Blueprint("stocks", __name__, url_prefix="/api")


@stock_bp.route("/")
def home():
    return "Flask API is live!"

@stock_bp.route("/stock/<ticker>", methods=["GET"])
def stock_info(ticker):
    try:
        data = get_stock_data(ticker.upper())
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400