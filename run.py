from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

# --- Ejercicio 1 ---
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    error = None
    valores = {}
    resultado = None

    if request.method == 'POST':
        try:
            n1 = float(request.form.get('nota1', ''))
            n2 = float(request.form.get('nota2', ''))
            n3 = float(request.form.get('nota3', ''))
            asistencia = float(request.form.get('asistencia', ''))

            valores = {"nota1": n1, "nota2": n2, "nota3": n3, "asistencia": asistencia}

            if not (10 <= n1 <= 70 and 10 <= n2 <= 70 and 10 <= n3 <= 70):
                error = "Las notas deben estar entre 10 y 70."
            elif not (0 <= asistencia <= 100):
                error = "La asistencia debe estar entre 0 y 100."
            else:
                prom = (n1 + n2 + n3) / 3
                estado = "Aprobado" if (prom >= 40 and asistencia >= 75) else "Reprobado"
                resultado = {"promedio": round(prom, 2), "asistencia": asistencia, "estado": estado}
        except ValueError:
            error = "Debes ingresar números válidos."

    return render_template("ejercicio1.html", error=error, valores=valores, resultado=resultado)

# --- Ejercicio 2 ---
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        nombres = [
            request.form.get('nombre1', ''),
            request.form.get('nombre2', ''),
            request.form.get('nombre3', '')
        ]
        if all(nombres):
            nombre_largo = max(nombres, key=len)
            resultado = f"El nombre más largo es '{nombre_largo}' con {len(nombre_largo)} caracteres."
    return render_template("ejercicio2.html", resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)


