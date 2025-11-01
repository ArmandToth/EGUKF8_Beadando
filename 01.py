
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

class DatumTAO:
    def __init__(self, datum_str):
        self.datum = self.parseDatumTAO(datum_str)

    def parseDatumTAO(self, datum_str):
        try:
            return datetime.strptime(datum_str, "%Y.%m.%d")
        except ValueError:
            return None

    def napokSzamaTAO(self):
        if self.datum:
            mai_nap = datetime.now()
            return (mai_nap - self.datum).days
        return None

    def evNapjaTAO(self):
        if self.datum:
            return self.datum.timetuple().tm_yday
        return None

    def evKedvTAO(self):
        if self.datum:
            napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
            return napok[self.datum.weekday()]
        return None


def szamolTAO():
    datum_str = entryTAO.get()
    datumObjTAO = DatumTAO(datum_str)
    if datumObjTAO.datum:
        napok = datumObjTAO.napokSzamaTAO()
        ev_napja = datumObjTAO.evNapjaTAO()
        ev_kedv = datumObjTAO.evKedvTAO()
        eredmenyTAO.set(
            f"Megadott dátum: {datum_str}\n"
            f"Eltelt napok száma: {napok}\n"
            f"Hányadik nap az évben: {ev_napja}\n"
            f"Milyen nap: {ev_kedv}"
        )
    else:
        messagebox.showerror("Hiba!", "Hibás dátum!")

ablakTAO = tk.Tk()
ablakTAO.title("Dátum Konvertáló")
ablakTAO.geometry("320x200")

labelTAO = tk.Label(ablakTAO, text="Add meg a dátumot (ÉÉÉÉ.HH.NN):")
labelTAO.pack()

entryTAO = tk.Entry(ablakTAO)
entryTAO.pack()

gombTAO = tk.Button(ablakTAO, text=" Konvertálás ", command=szamolTAO)
gombTAO.pack()

eredmenyTAO = tk.StringVar()
eredmeny_labelTAO = tk.Label(ablakTAO, textvariable=eredmenyTAO)
eredmeny_labelTAO.pack()

ablakTAO.mainloop()
