from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db=SQLAlchemy(app)
#db.init_app(app)

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
    #stmt = select(Data)
    #datas = Data.query.limit(10).all()
    datas = Data.query.limit(30).all()
    #rna_ids = [data.rna_id for data in datas]
    return render_template('assos.html', datas=datas)
    #result = db.session.execute(stmt)a
    #for data in datas:
     #   print(f"{data.rna_id}")
    #return render_template('assos.html')

@app.route('/assos', methods=['POST'])
def delete_data():
    data_id = request.form['data.id']
    data = Data.query.filter_by(id=data_id).first()
    db.session.delete(data)
    db.session.commit()
    return render_template('assos.html')

#@app.route('/ajouter', methods=['POST'])
#def ajouter():
 #   rna_id = request.form['rna_id']
  #  rna_id_ex = request.form['rna_id_ex']
   # gestion = request.form['gestion']
   # data = Data(rna_id=rna_id, rna_id_ex=rna_id_ex, gestion=gestion)
    #db.session.add(data)
 #   db.session.commit()
  #  flash('Les données ont été ajoutées avec succès', 'success')
   # return redirect(url_for('assos'))


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
if __name__ == '__main__':
    app.run()  

