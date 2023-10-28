from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def Home_Root():
    return render_template('index.html')

@app.route("/home", methods=['GET','POST'])
def Home():
    return render_template('index.html')

@app.route("/our_work", methods=['GET','POST'])
def Projects():
    return render_template('projects.html')

@app.route("/vision", methods=['GET','POST'])
def Mission_Vission():
    return render_template('vision.html')

@app.route("/services", methods=['GET','POST'])
def Services():
    return render_template('services.html')

@app.route("/dhwani", methods=['GET','POST'])
def Dhwani():
    return render_template('about.html')

@app.route("/gallery", methods=['GET','POST'])
def Gallery():
    return render_template('gallery.html')

@app.route("/privacy_policy", methods=['GET','POST'])
def PrivacyPolicy():
    return render_template('privacy_policy.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))