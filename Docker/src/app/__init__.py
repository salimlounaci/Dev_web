from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True)
    rna_id = db.Column(db.String(30), nullable=True) 
    rna_id_ex = db.Column(db.String(30), nullable=True)
    gestion = db.Column(db.String(20), nullable=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/assos')
def assos():
    datas = Data.query.limit(30).all()
    return render_template('assos.html', datas=datas)

@app.route('/delete/<int:data_id>')
def delete(data_id):
    data = Data.query.get(data_id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('assos'))

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        rna_id = request.form['rna_id']
        rna_id_ex = request.form['rna_id_ex']
        gestion = request.form['gestion']
        new_data = Data(rna_id=rna_id, rna_id_ex=rna_id_ex, gestion=gestion)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('assos'))
    return render_template('ajouter.html')

@app.route('/modifier/<int:data_id>', methods=['GET', 'POST'])
def modifier(data_id):
    data = Data.query.get(data_id)

    if request.method == 'POST':
        data.rna_id = request.form['rna_id']
        data.rna_id_ex = request.form['rna_id_ex']
        data.gestion = request.form['gestion']
        db.session.commit()
        return redirect(url_for('assos'))
    return render_template('modifier.html', data=data)

import json
from flask import jsonify

@app.route('/dashboard')
def dashboard():
    # récupère les données de la base de données
    datas = Data.query.limit(30).all()

    # traite les données pour les préparer pour le graphe
    labels = []
    data_gestion = []

    for data in datas:
        labels.append(data.rna_id)
        data_gestion.append(data.gestion)

    # génère les données pour le graphe
    graph_data = {
        "labels": labels,
        "datasets": [{
            "label": "Gestion des données",
            "data": data_gestion,
            "backgroundColor": "rgba(255, 99, 132, 0.2)",
            "borderColor": "rgba(255, 99, 132, 1)",
            "borderWidth": 1
        }]
    }

    # convertit les données en JSON pour pouvoir les transmettre à la page HTML
    json_data = json.dumps(graph_data)

    # renvoie la page HTML avec les données pour le graphe
    return render_template('dashboard.html', data=json_data)


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
