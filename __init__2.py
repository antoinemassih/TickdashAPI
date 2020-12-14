from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_potion import Api, ModelResource

app = Flask(__name__)
CORS(app)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Monkeyhero69@trendchart.cu0jwgiytj6k.us-east-1.rds.amazonaws.com:5432/postgres"
db = SQLAlchemy(app)


class Dashboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)

class Tickers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)


db.create_all()


class DashboardResource(ModelResource):
    class Meta:
        model = Dashboard

class TickerResource(ModelResource):
    class Meta:
        model = Tickers


api = Api(app)
api.add_resource(DashboardResource)
api.add_resource(TickerResource)

if __name__ == '__main__':
    app.run()
