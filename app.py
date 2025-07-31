# backend APIs
# This file contains the Flask application for the FAQ API.
# It includes endpoints to get, add, update, and delete FAQs.

# meet the requirements: Finalize backend APIs needed to support your capstone solution.

from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config
from models import db, FAQ
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# initialize the database
db.init_app(app)
with app.app_context():
    db.create_all()

# get all FAQs
@app.route('/api/faqs', methods=['GET'])
def get_faqs():
    faqs = FAQ.query.all()
    return jsonify([faq.to_dict() for faq in faqs]), 200


# get specific FAQ by ID
@app.route('/api/faqs/<int:faq_id>', methods=['GET'])
def get_faq(faq_id):
    faq = FAQ.query.get(faq_id)
    if faq:
        return jsonify(faq.to_dict()), 200
    return jsonify({"error": "FAQ not found"}), 404


# add a new FAQ
@app.route('/api/faqs', methods=['POST'])
def add_faq():
    data = request.get_json()
    
    # Check if the data is a list for batch insert
    if isinstance(data, list):
        new_faqs = []
        for item in data:
            new_faq = FAQ(question=item["question"], answer=item["answer"])
            db.session.add(new_faq)
            new_faqs.append(new_faq.to_dict())
        db.session.commit()
        return jsonify(new_faqs), 201
    else:
        new_faq = FAQ(question=data["question"], answer=data["answer"])
        db.session.add(new_faq)
        db.session.commit()
        return jsonify(new_faq.to_dict()), 201

# update an existing FAQ
@app.route('/api/faqs/<int:faq_id>', methods=['PUT'])
def update_faq(faq_id):
    faq = FAQ.query.get(faq_id)
    if not faq:
        return jsonify({"error": "FAQ not found"}), 404

    data = request.get_json()
    if "question" in data:
        faq.question = data["question"]
    if "answer" in data:
        faq.answer = data["answer"]

    db.session.commit()
    return jsonify(faq.to_dict()), 200


# delete an FAQ
@app.route('/api/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    faq = FAQ.query.get(faq_id)
    if faq:
        db.session.delete(faq)
        db.session.commit()
        return jsonify({"message": "FAQ deleted successfully"}), 200
    return jsonify({"error": "FAQ not found"}), 404

# check if the server is running
@app.route('/')
def index():
    return jsonify({"message": "FAQ API is running"}), 200

if __name__ == '__main__':
    app.run(debug=True)