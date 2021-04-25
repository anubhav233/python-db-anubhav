import json

from flask import jsonify, request

from . import api_v1 as api_v1
from . import config
from project.models import DeviceMatrix, db


@api_v1.route('/')
def index():
    return jsonify({"message": "index page"})

@api_v1.route('/device-category')
def device_category():
    device_category = [device.category for device in DeviceMatrix.query.all()]
    return jsonify({
        "device_category": list(set(device_category))
    }), 200

