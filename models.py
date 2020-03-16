from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()




class Family(db.Model):
    __tablename__ = 'Family_Doe'
    member_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    last_name = db.Column(db.String(20), nullable=False, unique=True)
    age= db.Column(db.Integer, nullable=False)
    lucky_number = db.Column(db.String(400), nullable=False)

""" def serialize(self):
        return {
            "id": self.id,
            "Name": self.name,
            "Last_name": self.Last_name,
            "Age": self.Age,
            "Lucky_Number": self.Lucky_number       
        }"""





def add_member(self, member):
        member ["id"] = self._generateId()
        self._members.append(member)
        return self._members

def delete_member(self, id):
        self._members = list(filter(lambda member: member['id']!=id, self._members))
        return self._members

def update_member(self, id, member):
        self._members = list(filter(lambda member: member['id']!=id,self._members))
        return None

def get_member(self, id):
        member= next(filter(lambda member: member['id']==id,self._members),None)
        return member

def get_all_members(self):
        return self._members




