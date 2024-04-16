import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import bestand1

def proberen(self):
    self.assertEqual(201, 201)
    self.assertEqual(25, bestand1.optellen(20, 5))
    print("proberen")
    return "proberen2"