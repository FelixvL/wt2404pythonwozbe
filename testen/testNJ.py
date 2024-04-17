import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import functietotestNJ

def proberen(self):
    self.assertEqual("dit is geen geldige naam", functietotestNJ.naamcontrole("emma17"))
    print("SUCCES")
    return "proberen2"