import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def delenDoorVijf (getal):
    return getal%5 == 0

def proberen(self):
    self.assertEqual(True, delenDoorVijf(10))
    print("proberen6")
    return "proberen2"

