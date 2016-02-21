from moresmart import User, Subject
    
def populate_db(db):
    db.drop_all()
    db.create_all()
    guest = User('gooid','guest','guesterson', 'guest@example.com','subjs','email','pwd')
    db.session.add(guest)
    db.session.commit()	

    subjs = [['McGill','COMP250','Big O Notation'],['McGill','COMP250','Semicolon Verbosity']]
    for s in subjs:
        sub = Subject(s[0],s[1],s[2])
        db.session.add(sub)
    db.session.commit()

        