from my_app import db


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    first_name = db.Column(db.String(45))

    def __repr__(self):
       return "<name {}: '{} , {}'>".format(self.id, self.last_name,self.first_name,self.company_name)

class Coverage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pss_name = db.Column(db.String(30))
    tsa_name = db.Column(db.String(30))
    sales_level_1 = db.Column(db.String(30))
    sales_level_2 = db.Column(db.String(30))
    sales_level_3 = db.Column(db.String(30))
    sales_level_4 = db.Column(db.String(30))
    sales_level_5 = db.Column(db.String(30))
    fiscal_year = db.Column(db.String(30))

    @staticmethod
    def newest():
        return Coverage.query.order_by(Coverage.pss_name).all()

    def get_page(page_num):
        num_of_pages = Coverage.query.paginate(per_page=10)
        return Coverage.query.order_by(Coverage.id).offset(page_num*10)

    def newest_name(num):
        return Coverage.query.order_by(Coverage.pss_name).limit(num)

print ('hello from models')

