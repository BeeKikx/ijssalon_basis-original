from flask import Flask, render_template                      #11.10.1 Def.route & 11.12 render_template
app = Flask(__name__)                                         #var 'app' om website te starten

#routes definieren
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/prijzen')
def prijzen():
    items = [
        { 
            "product": "vanille-ijs 1 liter",
            "prijs": "2 euro"
        },
        {
            "product": "chocolade-ijs 1 liter",
            "prijs": "2 euro"
        }       
    ]
    return render_template("prijzen.html", items=items)
@app.route('/recepten')
def recepten():
    items = [
        {
            "recept": "Tiramisu di nona",
            "img": "tiramisu.png"
        },
        { 
            "recept": "IJstaart met chocolade",
            "img": "ijstaart.png"
        }        
    ]
    return render_template("recepten.html", items=items)


#volgende 2 regels altijd als laatst tussen 'app=Flask(__name__)'
if __name__ == '__main__':                                  #program check
    app.run(port=5000,debug=True)                           #method '.run' ; website in progress=debug=True


#10.10.2 Flask-server opstarten met default env. settings 
#set FLASK_APP=flask_app.py  en
#flask run                   werkt niet.
#Op deze wijze blijkbaar wel:
#$env:FLASK_APP = "flask_app.py"         ; env.var in Powershell
#python -m flask run                     ; 
# * Serving Flask app 'flask_app.py'
# * Debug mode: off
#WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# * Running on http://127.0.0.1:5000
#Press CTRL+C to quit

#sinds update pip uninstall flask && python -m pip install flask werkt het weer wel
#ook pip update:  [notice] A new release of pip is available: 24.2 -> 24.3.1
#[notice] To update, run: python.exe -m pip install --upgrade pip