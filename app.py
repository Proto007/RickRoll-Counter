from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rickroll.db'

db = SQLAlchemy(app)

class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)

@app.route('/counter', methods=['POST'])
def increment_counter():
    counter = Counter.query.filter_by(id=1).first()
    counter.count += 1
    db.session.commit()
    return render_template("home.html", count=counter.count)

@app.route('/counter', methods=['GET'])
def viewhint():
    return render_template("home.html")

@app.route('/1dc11e672faa15d56a8a6de6bb41c2ab', methods=['Get'])
def show_count():
    counter = Counter.query.filter_by(id=1).first()
    return jsonify({'count': counter.count})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.add(Counter(count=0))
        db.session.commit()
    app.run(debug=True)
