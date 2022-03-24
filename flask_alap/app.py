import sys
from flask import Flask, render_template, request, flash

from queries import get_item

app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.config['SESSION_PROTECTION'] = 'W_m-iN7Kow3D'

def is_float(value):
    '''
    value paraméter: str()  
    '''
    try:
        float(value)
        return True
    except:
        return False
    
def is_int(value):
    try:
        int(value)
        return True
    except:
        return False

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calc')
def calc():
    szamitas = ''
    item = None
    # Megjönnek-e a paraméterek
    if not request.args.get('cikkszam') and not request.args.get('suly'):
            return render_template("calc.html")
        
    print('Az adatok ellenőrizve!', file = sys.stderr)

    # Súly szám-e
    suly_str = request.args.get('suly')
    if not is_int(suly_str) or not is_float(suly_str):
        return render_template("calc.html", message={"text": "Helytelen értékeket adtál meg a súlyhoz!", "category": "danger"})
        
    # Súly nem-negatív-e
    suly = float(suly_str)
    if suly < 0:
        return render_template("calc.html", message={"text": "Súly nem lehet negatív!", "category": "danger"})

    # Cikkszám létezik-e az adatbázisban
    cikkszam = int(request.args.get('cikkszam'))
    item = get_item(cikkszam)
    if not item:
        return render_template("calc.html", message={"text": "Cikkszám nem található", "category":"danger"})
        
    print(cikkszam, suly, file = sys.stderr)
    print(type(cikkszam), type(suly), file = sys.stderr)
    szamolas = suly / item["egyseg_suly"]
    szamitas = round(szamolas,1)
    display_txt = 'Eredmény: {} darab / méter !'.format(szamitas)
    flash(display_txt , 'info')
    print(item["egyseg_suly"], file = sys.stderr)
    print(szamolas, file=sys.stderr)          
    return render_template("calc.html", szamitas=str(szamitas), item_details=item)

@app.route('/rolam')
def rolam():
    return render_template("rolam.html")