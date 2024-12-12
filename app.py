from flask import Flask, request, render_template

app = Flask(__name__)

# Route untuk menampilkan form
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk memproses data POST yang dikirim dari form
@app.route('/submit', methods=['POST'])
def submit():
    # Parsing parameter dari form
    text = request.form.get('textfield')
    if text:
        return f"Data yang diterima: {text}"
    return "Error: No data provided", 400

if __name__ == '__main__':
    app.run(debug=True)
