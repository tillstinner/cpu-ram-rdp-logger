import csv
from datetime import datetime

csv_datei = "cpu-logs.csv"
schwelle = 10  # CPU-Auslastung in %

zeit_ueber_schwelle = 0
gesamt_zeit = 0
letzte_zeit = None

with open(csv_datei, newline='', encoding='utf-8') as f:
    # Ändere delimiter auf ';' falls nötig
    reader = csv.DictReader(f, delimiter=',', quotechar='"')  # Versuche erst Komma
    print("Spalten in der CSV:", reader.fieldnames)  # DEBUG: zeigt, welche Keys erkannt werden
    
    for row in reader:
        # Hier musst du die Keys aus fieldnames nutzen
        date_key = reader.fieldnames[0]
        time_key = reader.fieldnames[1]
        cpu_key = reader.fieldnames[2]

        dt_str = row[date_key] + ' ' + row[time_key]
        dt = datetime.strptime(dt_str, '%d.%m.%Y %H:%M:%S.%f')

        if letzte_zeit is not None:
            delta = (dt - letzte_zeit).total_seconds()
            gesamt_zeit += delta

            cpu_auslastung = float(row[cpu_key])
            if cpu_auslastung > schwelle:
                zeit_ueber_schwelle += delta

        letzte_zeit = dt

prozent = (zeit_ueber_schwelle / gesamt_zeit * 100) if gesamt_zeit > 0 else 0

print(f"Gesamtzeit: {gesamt_zeit:.2f} Sekunden ({gesamt_zeit/60:.2f} Minuten)")
print(f"Zeit über {schwelle}% CPU: {zeit_ueber_schwelle:.2f} Sekunden ({zeit_ueber_schwelle/60:.2f} Minuten)")
print(f"Anteil: {prozent:.2f}%")
