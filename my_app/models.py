from my_app import db


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    first_name = db.Column(db.String(45))

    def __repr__(self):
       return "<name {}: '{} , {}'>".format(self.id, self.last_name,self.first_name,self.company_name)


print ('hello from models')

