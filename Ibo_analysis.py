
# Datenquelle: names.csv
# Enthält StateCode, Geschlecht, Geburtsjahr, Name und Häufigkeit
# ----------------------------------------------------------------------

cache_file = "cache.csv"

# Funktion zum Einlesen der CSV-Datei

def get_content(file):
    with open(file, "r") as data:
        lines = data.readlines()
        header = lines[0].strip().split(",")
    return header, lines


# Funktion zum Schreiben der gefilterten oder sortierten Daten in eine Datei

def generate_cache_file(header, lines, file = cache_file):
    with open(file, "w") as new_file:
        new_file.write(",".join(header) + "\n")
        for line in lines:
            new_file.write(",".join(line) + "\n")


# Formatiertes Ausgeben der Tabelle in der Konsole

def print_formatted_table(file = cache_file):
    header, lines = get_content(file)

    print("\nFormatted Table, from file:", file)
    print("With a total of " + str(len(lines)-1) +" entrys.")
    print("-" * round(23.2 * len(header)))
    print(("| {:<20} "*len(header) + "|").format( *header))
    print("-" * round(23.2 * len(header)))
    for line in lines[1:]:
        print(("| {:<20} "*len(header) + "|").format( *line.strip().split(",")))


# Filterfunktion: Zeilen mit bestimmten Werten in einer Spalte

def get_rows_by_value(column, value, file = cache_file, return_table = False):
    header, lines = get_content(file)

    if column not in header:
        print("Spalte '" + column + "' nicht gefunden.")
        return

    col_index = header.index(column)
    rows = []
    for line in lines[1:]:
        row = line.strip().split(",")
        if row[col_index] in value:
            rows.append(row)

    generate_cache_file(header, rows)
    print("\nOnly returned rows with value in column:", column)
    print("For Values:", value)
    if return_table:
        print_formatted_table()


# Sortierfunktion (Bubble Sort für Lerneffekt)

def sort_by(column, area, reverse=False, file=cache_file, return_table=False):
    header, lines = get_content(file)

    if column not in header:
        print("Spalte '" + column +"' nicht gefunden.")
        return
    if area == []:
        area = [1, len(lines)]

    rows = [line.strip().split(",") for line in lines[area[0] : area[1]]]

    col_index = header.index(column)
    for i in range(len(rows)):
        for j in range(0, len(rows) - i -1):
            a = int(rows[j][col_index])
            b = int(rows[j + 1][col_index])
            if (a > b and not reverse) or (a < b and reverse):
                rows[j], rows[j + 1] = rows[j + 1], rows[j]

    generate_cache_file(header, rows)
    print("\nSorted by column:", column)
    print("Range:", area[0], "to", area[1])
    if return_table:
        print_formatted_table()


# Zähle Gesamtanzahl der Menschen (Summe der Spalte 'Number')

def count_humans(file = cache_file):
    header, lines = get_content(file)
    col_index = header.index("Number")
    total_humans = 0
    for line in lines[1:]:
        row = line.strip().split(",")
        total_humans += int(row[col_index])
    return total_humans


# Durchschnittsalter berechnen

def average_age(file=cache_file):
    header, lines = get_content(file)
    col_index = header.index("YearOfBirth")
    current_year = 2025

    total_age = 0
    count = 0
    for line in lines[1:]:
        row = line.strip().split(",")
        age = current_year - int(row[col_index])
        total_age += age
        count += 1

    if count == 0:
        print("No data available to calculate average age.")
        return None
    avg_age = total_age / count
    return avg_age


# Beispiel: Nutzung der Funktionen

get_rows_by_value("StateCode", ["DE"], "names.csv")
get_rows_by_value("YearOfBirth", ["1990"])
get_rows_by_value("Sex", ["M"],"cache.csv", True)

print("\nTotal humans:", count_humans())
print("\nAverage age:", average_age())
