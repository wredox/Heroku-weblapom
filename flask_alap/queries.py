import sqlite3

# Database connection defitintion
con = sqlite3.connect("database.db", check_same_thread=False)

def get_item(item_id):

    # Database3 cursor, this will execute the sql queries
    cur = con.cursor()

    # Query for getting the data
    select_sql = f"""
        SELECT * FROM 'cikkszam'
        WHERE obi_cikkszam = '{item_id}'
        OR szallitoi_cikkszam =  '{item_id}'
        OR ean = '{item_id}'
        """

    # Getting the data and unpacking into variables
    try:
        obi_cikkszam, cikk_neve, szallitoi_cikkszam, ean, egyseg_suly, unit, picture = list(cur.execute(select_sql))[0]
        
        # Returning formatted result
        return {
            "obi_cikkszam": obi_cikkszam,
            "cikk_neve": cikk_neve,
            "szallitoi_cikkszam": szallitoi_cikkszam,
            "ean": ean,
            "egyseg_suly": egyseg_suly,
            "unit": unit,
            "kep": picture
        }
    except IndexError:
        return None

# Example of usage
# based on "szallitoi_cikkszam"
# print(get_item("4821237"))

# based on "obi_cikkszam"
# print(get_item("3215050"))

def get_boxes():

    # Database3 cursor, this will execute the sql queries
    cur = con.cursor()

    # Query for getting the data
    select_sql = f"""
        SELECT * FROM 'edenyek'
        """

    results = []

    # Getting the data
    for box in cur.execute(select_sql):
        id, nev, suly = box
        results.append({
        "id": id,
        "nev": nev,
        "suly": suly,
    })

    # Returning results
    return results