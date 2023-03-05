from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import json

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
    datas = Data.query.limit(20).all()

    # Préparer les données pour le graphique en barre Chart.js
    gestion_count = {}
    for d in datas:
        if d.gestion in gestion_count:
            gestion_count[d.gestion] += 1
        else:
            gestion_count[d.gestion] = 1

    gestion_values = list(gestion_count.values())
    gestion_labels = list(gestion_count.keys())
    bar_data = {
        'values': gestion_values,
        'labels': gestion_labels
    }

    # Préparer les données pour le graphique circulaire Chart.js
    pie_data = {
        'values': gestion_values,
        'labels': gestion_labels
    }
    return render_template('assos.html', pie_data=json.dumps(pie_data), bar_data=json.dumps(bar_data), datas=datas)

@app.route('/delete/<int:data_id>')
def delete(data_id):
    data = Data.query.get(data_id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('assos'))

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

@app.route('/dashboard')
def dashboard():
    datas = Data.query.all()

    # Préparer les données pour le graphique Chart.js
    gestion_count = {}
    for d in datas:
        if d.gestion in gestion_count:
            gestion_count[d.gestion] += 1
        else:
            gestion_count[d.gestion] = 1

    gestion_values = list(gestion_count.values())
    gestion_labels = list(gestion_count.keys())
    data = {
        'values': gestion_values,
        'labels': gestion_labels
    }
    return render_template('dashboard.html', graph_data=json.dumps(data))

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return
