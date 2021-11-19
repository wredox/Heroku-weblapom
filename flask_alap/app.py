import sys
from flask import Flask, render_template, request, flash

from data import szam

app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.config['SESSION_PROTECTION'] = 'W_m-iN7Kow3D'


# Létrehozunk egy útvonalat
# Az útvonal megnyitásakor az alatta definiált fütvény kerül meghívásra, ha úgy
# tetszik ez a fügvény fut le akkor amikor az elérési utat a böngészöben megnyitják
#
# 2 módja van annak hogy az elérési utat és a hozzá tartozó fügvényt létrehozzuk....
#     1.
#        Ha a project kicsi ( pár oldalas ), akkor az app fájl tartalmazza az összes elérési utat.
#     2.
#        Ha a project nagyobb, optimálisabb, ha a definiciók külön fájlban vannak ( erre most nem térnék ki! )

@app.route('/', methods = ['GET'])
def hello_world():
    # Jelenleg ez az útvonal a 'Hello World!' stringel tér vissza.
    # Minden definiált függvénynek vissza kell adnia egy vagy több értéket
    # Abban az esetben ha a függvény at dolgoz fel, meg kell határoznunk az 
    # beviteli módjának a methodusát.
    # A methodus lehet:  'post', 'get', 'head', 'put', 'delete'
    # Az alábbiakban a 'post' és a 'get' methodust fogjuk használni.
    return render_template("hello.html")


# Nézzünk egy 'get' hívást
# Meghatározzun hogy mi történjen
# Az álltalad küldött mintát használom
@app.route('/calc', methods = ['GET'])  # Létre hoztuk az utvonalat
def index():
    # Mivel s web stringként küldi át az at, meg kell probálnunk 
    # konvertálni, a számunkra megfelelő adattípusra
    
    #float érték vizsgálata
    def is_float(value):
        '''
        value paraméter: str()  
        '''
        try:
            # érvényesitjük az érvelésünk.
            # Ha convertálható az érték "float" típusuvá a visszatérési érték igaz (True)! 
            float(value)
            return True
        except:
            return False
        
    def is_int(value):
        try:
            # érvényesitjük az érvelésünk.
            # Ha convertálható az érték "int" típusuvá a visszatérési érték igaz (True)! 
            int(value)
            return True
        except:
            return False
        
    # Ha get methodot használjuk meg ell szereznünk az at, amivel dolgotni szeretnénk!
    szamitas = ''
    if request.method == 'GET':
        # A print utasítás csak a conzolon jelenik meg...
        # Kötelező  ellenörzése:
            
        if request.args.get('beker') and request.args.get('a') != 0 or None:
            print('Az adatok ellenőrizve!', file = sys.stderr)
            # ha az  léteznek, tároljuk öket változóba
            # mivel a web str()-t kül át, ezért az at convertálnunk kell.
            beker_str = request.args.get('beker')
            a_str = request.args.get('a')
            if is_int(beker_str) and is_float(a_str):
                print('Adatok konvertálhatóságának ellenörzése!', file = sys.stderr) 
                # Az új változóban már konvertáljuk az értkeket, hogy dolgozni is tudjunk vele.
                beker = int(beker_str)
                a = float(a_str)
                print(beker, a, file = sys.stderr)
                print(type(beker), type(a), file = sys.stderr)
                # Vizsgáljuk, ha kissebb mint 0 ez egy negatív szám, ami nem megengedett a feldolgozás szempontjából.
                if beker or a > 0:           
                    #ha a megfelelő típusokat küldte az user,a számítás végbe megy!
                    if szam.get(beker):
                        szamolas = a / szam.get(beker)
                        szamitas = round(szamolas,1)
                        display_txt = 'Eredmény: {} méter !'.format(szamitas)
                        flash(display_txt , 'info')
                        print(szam.get(beker), file = sys.stderr)
                        print(szamolas, file=sys.stderr)
                else:         
                    #ha az értéke negatív szám, hibaüzenet:                    
                    flash('Negatív értéket nem adhatsz meg', 'danger')
            else:
                # Abban az esetben ha a "beker és aZ "a" változó nem a megfelelő 
                # számokat tartalmaza, hibaüzenet:
                flash('Helytelen értékeket adtál meg!', 'danger')

    
    return render_template("index.html", szamitas=str(szamitas))


#if __name__ == '__main__':
#     app.run()
