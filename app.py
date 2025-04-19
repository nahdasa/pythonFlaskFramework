from flask import Flask , render_template

app = Flask(__name__)

app_name = "My Application Name is: Nahda dan Nisa"

#1 App Route Flask "Hello World"
@app.route("/")
def home():
    return "Hei, Nahdaaa!"

#2 App Route dengan HTML
@app.route('/about')
def about():
    return render_template('about_without_bostrapp.html')

#3 App route dengan bostrapp
@app.route("/about-bostrapp")
def about_bostrapp():
    return render_template('about.html')

#4 App Route Aplikasi
@app.route("/aplikasi")
def aplikasi():
    return "<p>Ini adalah halaman nahda</p>"

#5 App route dinamis
@app.route('/alamat/<string:alamat>')
def getanama(alamat):
    return "alamat anda adalah {}".format(alamat)

#6 App route ID
@app.route('/umur/<int:umur>')  # Hanya menerima angka
def umur(umur):
    return f"Umur anda adalah: {umur}"

#7 App route Variabel Global
@app.route('/variabel-global/')
def variabel_global():
    return f"Welcome {app_name}"

#8 App route Dictionary Variabel
@app.route('/data')
def data():
    user = {"name": "Nahda", "age": 19, "city": "Makassar"}
    return render_template('data.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)