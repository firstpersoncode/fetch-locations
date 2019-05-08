from flask import Blueprint, Response, request
import json
from src import app
# Import the database class from the main app module
from src.db import Locations

from flask_cors import CORS

CORS(app, supports_credentials=True)

# LOCATIONS

locations = Blueprint('locations', __name__, url_prefix='/locations')

def getParams(args):
    page = args.get('page', 1)
    limit = args.get('limit', 15)
    if (int(page) <= 0):
        page = 1

    if (int(limit) < 15):
        limit = 15

    return page, limit

@locations.route('/', methods=['GET'])
def getLocations():
    page, limit = getParams(request.args)

    db = Locations()
    locations = db.getAll(int(limit), int(page))

    return Response(
        json.dumps({
            'data': locations
        }, indent=4, sort_keys=True),
        status=200,
        content_type='application/json'
    )

@locations.route('/provinsi', methods=['GET'])
def getProvince():
    page, limit = getParams(request.args)

    db = Locations()
    provinsi = db.get("provinsi", int(limit), int(page))

    return Response(
        json.dumps({
            'data': provinsi
        }, indent=4, sort_keys=True),
        status=200,
        content_type='application/json'
    )

@locations.route('/kabupaten', methods=['GET'])
def getKabupaten():
    page, limit = getParams(request.args)

    db = Locations()
    kabupaten = db.get("kabupaten", int(limit), int(page))

    return Response(
        json.dumps({
            'data': kabupaten
        }, indent=4, sort_keys=True),
        status=200,
        content_type='application/json'
    )

@locations.route('/kecamatan', methods=['GET'])
def getKecamatan():
    page, limit = getParams(request.args)

    db = Locations()
    kecamatan = db.get("kecamatan", int(limit), int(page))

    return Response(
        json.dumps({
            'data': kecamatan
        }, indent=4, sort_keys=True),
        status=200,
        content_type='application/json'
    )

@locations.route('/kelurahan', methods=['GET'])
def getKelurahan():
    page, limit = getParams(request.args)

    db = Locations()
    kelurahan = db.get("kelurahan", int(limit), int(page))

    return Response(
        json.dumps({
            'data': kelurahan
        }, indent=4, sort_keys=True),
        status=200,
        content_type='application/json'
    )

@locations.route('/provinsi/set', methods=['GET'])
def setProvince():
    db = Locations()
    provinsi = db.set("provinsi")

    return Response(
        json.dumps({
            'data': provinsi
        }, indent=4, sort_keys=True),
        status=200,
        content_type='application/json'
    )

@locations.route('/kabupaten/set', methods=['GET'])
def setKabupaten():
    db = Locations()
    kabupaten = db.set("kabupaten")

    return Response(
        json.dumps({
            'data': kabupaten
        }, indent=4, sort_keys=True),
        status=200,
        content_type='application/json'
    )

@locations.route('/kecamatan/set', methods=['GET'])
def setKecamatan():
    db = Locations()
    kecamatan = db.set("kecamatan")

    return Response(
        json.dumps({
            'data': kecamatan
        }, indent=4, sort_keys=True),
        status=200,
        content_type='application/json'
    )

@locations.route('/kelurahan/set', methods=['GET'])
def setKelurahan():
    db = Locations()
    kelurahan = db.set("kelurahan")

    return Response(
        json.dumps({
            'data': kelurahan
        }, indent=4, sort_keys=True),
        status=200,
        content_type='application/json'
    )
