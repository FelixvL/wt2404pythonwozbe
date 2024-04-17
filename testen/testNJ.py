import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import functietotestNJ

def proberen(self):
    self.assertEqual(201, 201)
    self.assertEqual("justin", functietotestNJ.naamcontrole("Justin"))
    print("noursjustin")
    return "proberen2"