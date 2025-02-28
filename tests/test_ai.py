from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from transformers import pipeline
from app.utils.file_processor import generate_qr
from app.services.ml_service import text_to_speech
import base64

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/generate-qr', methods=['POST'])
@jwt_required()
def generate_qr_code():
    data = request.json.get('data')
    img = generate_qr(data)
    buffer = BytesIO()
    img.save(buffer)
    return jsonify({'qr': base64.b64encode(buffer.getvalue()).decode()})

@ai_bp.route('/text-to-speech', methods=['POST'])
@jwt_required()
def convert_text_to_speech():
    text = request.json.get('text')
    audio = text_to_speech(text)
    return jsonify({'audio': base64.b64encode(audio).decode()})
