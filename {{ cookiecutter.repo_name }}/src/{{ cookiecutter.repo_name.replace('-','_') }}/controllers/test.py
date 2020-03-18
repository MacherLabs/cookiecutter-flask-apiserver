import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

from {{ cookiecutter.repo_name.replace('-','_') }} import app
from eazyserver.core.utils import toJSON
from flask import request, Response


@app.route('/test_view', methods=['POST'])
def test_view():
    try:
        result = "test result from test_view"
    except Exception as e:
        return Response(str(e), 400, mimetype='application/txt')
    return Response(toJSON(result), 200, mimetype='application/json')
 

