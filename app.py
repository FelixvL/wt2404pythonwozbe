from flask import Flask
from flask_cors import CORS
from flask import request

import woz_data_opvragen
import bestand1
import vivianenleoni
import woz_top20
import woz_gemeentes_opvragen
import huurwoningen

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Root Mount WOZ"

@app.route("/eigenaren/allen")
def eigenaren_allen():
  return woz_data_opvragen.toon_alle_eigenaren()


@app.route("/huizen/allen")
def huizen_allen():
  return woz_data_opvragen.toon_alle_huizen()


@app.route("/cbs/woz_per_regio_en_steden")
def woz_per_regio_en_steden():
  return woz_data_opvragen.woz_per_regio_en_steden()

@app.route("/felixenjustin")
def felixenjustin():
  return bestand1.felixenjustin()

@app.route("/pagina5/<zoekterm>")
def pagina5(zoekterm):
  return vivianenleoni.pagina5(zoekterm)

@app.route("/woz_top20")
def top20():
  return woz_top20.bestand_inlezen()

@app.route("/gemeentes")
def zoekGemeente():
  return woz_gemeentes_opvragen.zoekGemeente()

@app.route("/filter_huurwoningen/<zoekterm>/<bedragrange>")
def filter_huurwoningen(zoekterm, bedragrange):
  return huurwoningen.filter_huurwoningen(zoekterm, bedragrange)


@app.route("/felixliketest/<term>")
def flt(term):
  return woz_data_opvragen.flt(term)


@app.route("/gemeentes/<inputGemeente>")
def zoekGemeente(inputGemeente):
    return woz_gemeentes_opvragen.zoekGemeente(inputGemeente)
