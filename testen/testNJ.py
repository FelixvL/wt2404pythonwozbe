import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import functietotestNJ

def proberen(self):
    self.assertEqual("e", functietotestNJ.naamcontrole("emma17"))
    print("SUCCES")
    return "proberen2"