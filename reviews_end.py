from flask import Flask, request, jsonify
from models import reviews

app = Flask(__name__)

@app.route('/reviews', methods=['POST'])
def create_review():
    try:
        data = request.get_json()
        review = Review.create_review(data)
        return jsonify(review.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.get_all_reviews()
    return jsonify([review.to_dict() for review in reviews]), 200

@app.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    try:
        review = Review.get_review(review_id)
        return jsonify(review.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    try:
        data = request.get_json()
        review = Review.update_review(review_id, data)
        return jsonify(review.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    try:
        Review.delete_review(review_id)
        return '', 204
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
