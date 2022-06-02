import sys
from flask import Flask, render_template, request, flash

from queries import get_item, get_boxes

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

@app.route('/calc', methods=["GET", "POST"])
def calc():
    boxes_data = get_boxes()
    if request.method == "POST":  
        szamitas = ''
        item = None
        data = dict(request.form)
        # Megjönnek-e a paraméterek
        if 'cikkszam' in data and 'suly' in data:
            print('Az adatok ellenőrizve!', file = sys.stderr)
            # Súly szám-e
            suly_str =data['suly']
            if not is_int(suly_str) and not is_float(suly_str):
                data.pop("suly")
                return render_template("calc.html", boxes=boxes_data, data=data, message={"text": "Helytelen értékeket adtál meg a súlyhoz!", "category": "danger"})
                
            # Súly nem-negatív-e
            suly = float(suly_str)
            if suly < 0:
                data.pop("suly")
                return render_template("calc.html", boxes=boxes_data, data=data, message={"text": "Súly nem lehet negatív!", "category": "danger"})

            # Cikkszám létezik-e az adatbázisban

            cikkszam = int(data['cikkszam'])
            item = get_item(cikkszam)
            if not item:
                data.pop("cikkszam")
                return render_template("calc.html", boxes=boxes_data, data=data, message={"text": "Cikkszám nem található", "category":"danger"})
                
            print(cikkszam, suly, file = sys.stderr)
            print(type(cikkszam), type(suly), file = sys.stderr)
            if box_suly:=data['box_suly']:
                box_suly = float(box_suly)
                print(f"Edény súlyával korrigálva {suly} -> {suly-box_suly}")
                suly -= box_suly

            szamolas = suly / item["egyseg_suly"]
            szamitas = round(szamolas,1)
            display_txt = 'Eredmény: {} darab / méter !'.format(szamitas)
            flash(display_txt , 'info')
            print(item["egyseg_suly"], file = sys.stderr)
            print(szamolas, file=sys.stderr)          
            return render_template("calc.html", szamitas=str(szamitas), item_details=item, boxes=boxes_data)
    
    if request.method == "GET":
        return render_template("calc.html", boxes=boxes_data,)

@app.route('/rolam')
def rolam():
    return render_template("rolam.html")