from moresmart import User, Subject
    
def populate_db(db):
    db.drop_all()
    db.create_all()
    guest = User('gooid','guest','guesterson','contact','stats' ,'subjs',0,'email','pwd')
    db.session.add(guest)
    db.session.commit()	

    subjs = [['McGill','COMPUTERs','COMP250'],['McGill','The Badger Hole','COMP250']]
    for s in subjs:
        sub = Subject(s[0],s[1],s[2])
        db.session.add(sub)
    db.session.commit()

if __name__ == '__main__':
	from moresmart import db
	populate_db(db)
