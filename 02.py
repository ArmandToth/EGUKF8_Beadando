import tkinter as tk
from tkinter import messagebox
from datum_TAO import DatumTAO

def szamol():
    datum_str = entry.get()
    datum_obj = DatumTAO(datum_str)
    global eredmeny_szoveg
    if datum_obj.datum:
        napok = datum_obj.napok_szama()
        ev_napja = datum_obj.ev_napja()
        ev_kedv = datum_obj.ev_napja_nev()
        eredmeny_szoveg = (
            f"A megadott dátum: {datum_str}\n"
            f"Eltelt napok azóta: {napok}\n"
            f"Hányadik nap az évben: {ev_napja}\n"
            f"Milyen nap: {ev_kedv}"
        )
        eredmeny_var.set(eredmeny_szoveg)
    else:
        eredmeny_szoveg = ""
        messagebox.showerror("Hiba!", "Hibás dátum!")

def ment():
    if eredmeny_szoveg:
        try:
            with open("mentett_adatok.txt", "a", encoding="utf-8") as f:
                f.write(eredmeny_szoveg + "\n---\n")
            messagebox.showinfo("Mentés", "Sikeres mentés!")
        except Exception as e:
            messagebox.showerror("Mentési hiba", str(e))
    else:
        messagebox.showwarning("Figyelmeztetés", "A mentés sikertelen!")

ablak = tk.Tk()
ablak.title("Dátum konvertáló")
ablak.geometry("340x260")

label = tk.Label(ablak, text="Add meg a dátumot (ÉÉÉÉ.HH.NN):")
label.pack()

entry = tk.Entry(ablak)
entry.pack()

gomb_szamol = tk.Button(ablak, text="Számol", command=szamol)
gomb_szamol.pack()

gomb_ment = tk.Button(ablak, text="Ment", command=ment)
gomb_ment.pack()

eredmeny_var = tk.StringVar()
eredmeny_label = tk.Label(ablak, textvariable=eredmeny_var)
eredmeny_label.pack()

eredmeny_szoveg = ""

ablak.mainloop()
