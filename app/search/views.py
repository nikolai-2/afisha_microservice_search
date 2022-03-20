from flasgger import swag_from
from flask import Blueprint, request, jsonify

from app.errors import ResponseError
from app.search.search import Searcher

search_module = Blueprint("search", __name__, url_prefix='/search/')


@search_module.route('/', methods=['GET'])
@swag_from("search.yml")
def search():
    query = request.args.get('query')
    sort_by = request.args.get('sort', 'relevant')
    if not query:
        raise ResponseError(400, 'Query not found')

    searcher = Searcher(query, sort_by)
    result = searcher.search()

    return jsonify({'events': result})
