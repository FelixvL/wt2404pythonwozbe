from flask import Flask
from flask_cors import CORS
from flask import request
import unittest

import woz_data_opvragen
import bestand1
import vivianenleoni
import woz_top20
import woz_gemeentes_opvragen
import huurwoningen

import testen.test1felix as tt
import testen.testNJ 
import testen.testtllt
import testen.LVtest as lva

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
def zoekGemeente2(inputGemeente):
    return woz_gemeentes_opvragen.zoekGemeente(inputGemeente)


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_index(self):
        # Stuur een GET-verzoek naar de index route
        response = self.client.get('/')
        # Controleer of het verzoek succesvol was
        self.assertEqual(response.status_code, 200)
        # Controleer de responsedata
        self.assertEqual(response.data, b'Root Mount WOZ')

    def test_tweede(self):
        print("1")
        tt.proberen(self)

    def test_derde(self):
        print("2")
        testen.testNJ.proberen(self)

    def test_vierde(self):
        print("3")
        testen.testtllt.proberen(self)

    def test_vijfde(self):
        print("5")
        lva.MyTestCase()

if __name__ == '__main__':
    unittest.main()