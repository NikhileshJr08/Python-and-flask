#Create enteries into the table
from models import db,puppy,toy,owner

rufus = puppy('Rufus')
fido = puppy('Fido')

db.session.add_all([rufus,fido])
db.session.commit()

print(puppy.query.all())

#Searching for a puppy by it's name
rufus = puppy.query.filter_by(name='Rufus').first()
print(rufus)

##Creating a owner
nikhi = owner('nikhi',rufus.id)

#Giving toys to dogs
toy1 = toy('Blue ball',rufus.id)
toy2 = toy('Red ball',rufus.id)

db.session.add_all([nikhi,toy1,toy2])
db.session.commit()

rufus = puppy.query.filter_by(name = 'Rufus').first()
print(rufus)
rufus.report_toys()
