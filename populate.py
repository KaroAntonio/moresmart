from moresmart import User, Subject
    
def populate_db(db):
    db.drop_all()
    db.create_all()
    guest = User('gooid','guest','guesterson','contact','stats' ,'[]',0,'email','pwd')
    guest = User('gooidi','guesto','mcguesterson','contacted','statsy' ,'{"subjects":[1,2,3,4,5]}',0,'email@email.email','pwd')
    db.session.add(guest)
    db.session.commit()	

    subjs = [['McGill','COMPUTERs','COMP250'],['McGill','The Badger Hole','COMP253'],['McGill','The Badger Hop','COMP251'],['McGill','The Badger Holp','COMP252'],['McGill','The Badger Hale','COMP254']]
    for s in subjs:
        sub = Subject(s[0],s[1],s[2])
        db.session.add(sub)
    db.session.commit()

if __name__ == '__main__':
	from moresmart import db
	populate_db(db)
