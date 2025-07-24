from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Example data
meals = [
    {"id": 1, "name": "Grilled Chicken Salad", "type": "healthy"},
    {"id": 2, "name": "Beef Stir Fry", "type": "high-protein"},
    {"id": 3, "name": "Vegan Tacos", "type": "vegan"},
    {"id": 4, "name": "Halal Lamb Stew", "type": "halal"}
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api/meals')
def get_meals():
    preference = request.args.get("filter")
    if preference:
        filtered = [m for m in meals if m["type"] == preference]
    else:
        filtered = meals
    return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True)
