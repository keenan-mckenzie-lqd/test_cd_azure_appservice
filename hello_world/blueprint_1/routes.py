from flask import Blueprint, request

mod = Blueprint('bp_1', __name__)

@mod.route('/bp1')
def bp():
    return 'Hello, Blueprint 1'