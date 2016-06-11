class PayloadDB (object):
    def __init__ (self, db_file):
        self.db_file = db_file

    def get_payloads (self):

        payloads = list ()

        try:
            import xml.etree.cElementTree as ET
        except ImportError:
            import xml.etree.ElementTree as ET

        for i in ET.ElementTree (file=self.db_file).getroot ():
            resd = dict ()
            for j in i:
                resd [j.tag] = j.text
            payloads.append (resd)

        return payloads