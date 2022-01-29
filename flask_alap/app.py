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

@app.route('/calc', methods = ['GET'])
def calc():
    szamitas = ''
    item = None
    if request.method == 'GET':
        if request.args.get('beker') and request.args.get('a') != 0 or None:
            print('Az adatok ellenőrizve!', file = sys.stderr)
            beker_str = request.args.get('beker')
            a_str = request.args.get('a')
            if is_int(beker_str) and is_float(a_str):
                print('Adatok konvertálhatóságának ellenörzése!', file = sys.stderr)
                beker = int(beker_str)
                a = float(a_str)
                print(beker, a, file = sys.stderr)
                print(type(beker), type(a), file = sys.stderr)
                if beker or a > 0:
                    item = get_item(beker)
                    if item:
                        szamolas = a / item["egyseg_suly"]
                        szamitas = round(szamolas,1)
                        display_txt = 'Eredmény: {} darab / méter !'.format(szamitas)
                        flash(display_txt , 'info')
                        print(item["egyseg_suly"], file = sys.stderr)
                        print(szamolas, file=sys.stderr)
                    else:
                        return render_template("calc.html", message={"text": "Cikkszám nem található", "category":"danger"})
                else:
                    return render_template("calc.html", message={"text": "Negatív értéket nem adhatsz meg", "category":"danger"})
            else:
                return render_template("calc.html", message={"text": "Helytelen értékeket adtál meg!", "category":"danger"})
    return render_template("calc.html", szamitas=str(szamitas), item_details=item)