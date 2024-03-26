# Importar
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variables que permiten calcular el consumo energético de los aparatos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# La primera página
@app.route('/')
def index():
    return render_template('index.html')
# Segunda página
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# La tercera página
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Cálculo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# El formulario
@app.route('/form')
def form():
    return render_template('form.html')

#Resultados del formulario
@app.route('/submit', methods=['POST'])
def submit_form():
    
    # Declarar variables para la recogida de datos
    name = request.form['name']
    email = request.form["email"]
    address = request.form["address"]
    date = request.form["date"]

    with open('form.txt', 'a',) as f:
        f.write(f'{name},{email},{address}, {date}\n')
    # Puedes guardar tus datos o enviarlos por correo electrónico
    return render_template('form_result.html', 
                           # Coloque aquí las variables
                           name=name,
                           email=email,
                           address=address,
                           date=date,)

app.run(debug=True)
