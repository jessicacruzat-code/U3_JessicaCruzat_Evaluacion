from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    # Menú con los 2 ejercicios (el 2 puede quedar como “próximamente”)
    return render_template("index.html")

# -------- Ejercicio 1 --------
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        # 1) Tomar datos del formulario
        try:
            n1 = int(request.form.get("nota1", ""))
            n2 = int(request.form.get("nota2", ""))
            n3 = int(request.form.get("nota3", ""))
            asistencia = int(request.form.get("asistencia", ""))
        except ValueError:
            # Algún valor no era entero
            return render_template(
                "ejercicio1.html",
                error="Todos los campos deben ser números enteros."
            )

        # 2) Validaciones de rango
        errores = []
        for i, n in enumerate([n1, n2, n3], start=1):
            if not (10 <= n <= 70):
                errores.append(f"La nota {i} debe estar entre 10 y 70.")
        if not (0 <= asistencia <= 100):
            errores.append("La asistencia debe estar entre 0 y 100.")
        if errores:
            return render_template("ejercicio1.html", error="<br>".join(errores),
                                   valores={"nota1": n1, "nota2": n2, "nota3": n3, "asistencia": asistencia})

        # 3) Cálculo
        promedio = round((n1 + n2 + n3) / 3, 2)
        aprobado = (promedio >= 40) and (asistencia >= 75)
        estado = "APROBADO" if aprobado else "REPROBADO"

        # 4) Mostrar resultado
        return render_template(
            "ejercicio1_resultado.html",
            n1=n1, n2=n2, n3=n3, asistencia=asistencia,
            promedio=promedio, estado=estado
        )

    # GET: mostrar formulario
    return render_template("ejercicio1.html")

# (Opcional) placeholder para el Ejercicio 2
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        n1 = (request.form.get("nombre1") or "").strip()
        n2 = (request.form.get("nombre2") or "").strip()
        n3 = (request.form.get("nombre3") or "").strip()

        if not (n1 and n2 and n3):
            return render_template(
                "ejercicio2.html",
                error="Completa los tres nombres.",
                valores={"nombre1": n1, "nombre2": n2, "nombre3": n3}
            )

        nombres = [n1, n2, n3]
        longitudes = [len(x) for x in nombres]
        maxlen = max(longitudes)
        mas_largos = [n for n in nombres if len(n) == maxlen]   # maneja empates

        return render_template(
            "ejercicio2_resultado.html",
            nombres=nombres, mas_largos=mas_largos, maxlen=maxlen
        )

    # GET
    return render_template("ejercicio2.html")


if __name__ == "__main__":
    app.run(debug=True)
