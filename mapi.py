from flask import Flask, jsonify
import random
from flask_cors import CORS
import logging

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
app = Flask(__name__)

# Allow requests from a specific origin (http://localhost:3001 in this case)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# comment
# List of motivational quotes
quotes = [
    """Believe you can and you're halfway there. - Theodore Roosevelt""",
    """Success is not final, failure is not fatal:
    It is the courage to continue that counts. - Winston Churchill""",
    """The only way to do great work is to love what you do. - Steve Jobs""",
    """Don't watch the clock; do what it does. Keep going. - Sam Levenson""",
    """Believe in yourself and all that you are.
    Know that there is something inside you that is greater than any obstacle.
    - Christian D. Larson""",
    """Success is walking from failure to failure with no loss of enthusiasm.
    - Winston Churchill""",
]


# comments
@app.route("/mapi-health")
def healthy():
    logging.info("Mapi is healthy and running")
    return "health endpoint says application is healthy."


@app.route("/", methods=["GET"])
def get_quote():
    logging.info("Mapi is generating the quote")
    random_quote = random.choice(quotes)
    logging.info("Mapi generated quote : " f"{random_quote}")
    return jsonify({"Quote": random_quote})


if __name__ == "__main__":
    logging.info("Mapi is up and running")
    app.run(host="0.0.0.0", port=5000)
