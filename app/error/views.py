from flask import Blueprint, jsonify

from app.errors import ResponseError

error_module = Blueprint("error", __name__, url_prefix='/')


@error_module.app_errorhandler(Exception)
def error_handler():
    error = ResponseError(500, "Unknown error")
    return jsonify(error.to_dict())