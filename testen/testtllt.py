import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def delenDoorVijf (getal):
    if (not isinstance(getal, int)):
        return "het moet een getal zijn"
    if(getal <= 0):
        return "het getal moet hoger zijn dan 0"

    return getal%5 == 0

def proberen(self):
    self.assertEqual(True, delenDoorVijf(10))
    self.assertEqual(True, delenDoorVijf(5))
    self.assertEqual(True, delenDoorVijf(125))
    self.assertEqual(True, delenDoorVijf(60))
    #self.assertEqual(True, delenDoorVijf(-5))

    self.assertEqual("het getal moet hoger zijn dan 0",delenDoorVijf(-5))
    self.assertEqual("het getal moet hoger zijn dan 0",delenDoorVijf(0))
    self.assertEqual("het moet een getal zijn",delenDoorVijf("f"))
    self.assertEqual("het moet een getal zijn",delenDoorVijf("z"))

    print("proberen6")
    return "proberen2"

