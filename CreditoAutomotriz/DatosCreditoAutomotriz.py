from flask import Flask, request, render_template

app = Flask(__name__)

# Simulamos un historial de crédito para los usuarios
historial_credito = {
    'usuario1': 700,
    'usuario2': 650,
    'usuario3': 600,
}

# Criterios de evaluación
CREDIT_SCORE_THRESHOLD = 650
CAPACIDAD_DE_PAGO_MINIMA = 10000


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/evaluar', methods=['POST'])
def evaluar():
    nombre = request.form['nombre']
    ingresos_mensuales = float(request.form['ingresos'])
    capacidad_de_pago = ingresos_mensuales * 0.3

    # Obtener el score de crédito del usuario
    score_credito = historial_credito.get(nombre, None)

    if score_credito is None:
        resultado = 'Usuario no encontrado.'
    elif score_credito >= CREDIT_SCORE_THRESHOLD and capacidad_de_pago >= CAPACIDAD_DE_PAGO_MINIMA:
        resultado = 'El usuario es elegible para el crédito automotriz.'
    else:
        resultado = 'El usuario no es elegible para el crédito automotriz.'

    return render_template('resultado.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
