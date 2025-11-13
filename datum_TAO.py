from datetime import datetime

class DatumTAO:
    def __init__(self, datum_str):
        self.datum = self.parse_datum(datum_str)

    def parse_datum(self, datum_str):
        try:
            return datetime.strptime(datum_str, "%Y.%m.%d")
        except ValueError:
            return None

    def napok_szama(self):
        if self.datum:
            mai_nap = datetime.now()
            return (mai_nap - self.datum).days
        return None

    def ev_napja(self):
        if self.datum:
            return self.datum.timetuple().tm_yday
        return None

    def ev_napja_nev(self):
        if self.datum:
            napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
            return napok[self.datum.weekday()]
        return None