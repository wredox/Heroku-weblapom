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
        """

    # Getting the data and unpacking into variables
    obi_cikkszam, cikk_neve, szallitoi_cikkszam, ean, egyseg_suly = list(cur.execute(select_sql))[0]
    
    # Returning formatted result
    return {
        "obi_cikkszam": obi_cikkszam,
        "cikk_neve": cikk_neve,
        "szallitoi_cikkszam": szallitoi_cikkszam,
        "ean": ean,
        "egyseg_suly": egyseg_suly}

# Example of usage
# based on "szallitoi_cikkszam"
# print(get_item("482237"))

# based on "obi_cikkszam"
# print(get_item("3215050"))
