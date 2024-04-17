import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import functietotestNJ

def proberen(self):
    foutmelding = "dit is geen geldige naam"
    foutmelding2 = "voer een naam in"
    # self.assertEqual("emma", functietotestNJ.naamcontrole("emma"))
    # self.assertEqual(foutmelding, functietotestNJ.naamcontrole(""))
    self.assertEqual("e", functietotestNJ.naamcontrole("emma17"))
    # self.assertEqual(foutmelding, functietotestNJ.naamcontrole("emma17"))
    # self.assertEqual(foutmelding, functietotestNJ.naamcontrole("emma18"))
    # self.assertEqual(foutmelding, functietotestNJ.naamcontrole("''emma18'!@#'"))
    # self.assertEqual(foutmelding2, functietotestNJ.naamcontrole(None))
    print("SUCCES")
    return "proberen2"