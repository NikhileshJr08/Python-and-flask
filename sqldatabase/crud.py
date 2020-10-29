from basic import db,puppy

### CREATE ###

cash = puppy('Cash',2)
db.session.add(cash)
db.session.commit()

### READ ###
#Read all puppies
all_puppies = puppy.query.all()
print(all_puppies)
#Read by ID
puppy_one = puppy.query.get(1)
print(puppy_one)
#Filters
#Read by name
puppy_cash = puppy.query.filter_by(name = 'Cash')
print(puppy_cash.all())

### UPDATE ###

first_puppy = puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

### DELETE ###

second_puppy = puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = puppy.query.all()
print(all_puppies)
