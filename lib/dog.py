from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    session.query(Dog).filter(Dog.name == name).first()
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
   session.query(Dog).filter(Dog.id == id).first()
   return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()