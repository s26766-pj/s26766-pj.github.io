from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            a_raw = request.form.get("a", "").strip()
            b_raw = request.form.get("b", "").strip()
            op = request.form.get("op", "+")

            a = float(a_raw.replace(",", ".")) if a_raw else 0.0
            b = float(b_raw.replace(",", ".")) if b_raw else 0.0

            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                if b == 0:
                    error = "Division by zero is not allowed."
                else:
                    result = a / b
            else:
                error = "Unknown operation."
        except ValueError:
            error = "Please enter valid numbers."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
