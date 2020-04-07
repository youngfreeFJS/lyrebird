from flask_restful import Resource
from lyrebird.mock import context
from flask import request
from lyrebird import application


class ImportSnapshot(Resource):
    """
    导入数据快照
    """

    def post(self):
        parent_id = request.json.get('parentId')
        import_json=context.application.data_manager.import_snapshot(parent_id)
        return context.make_ok_response(import_json=import_json, parent_id=parent_id)
