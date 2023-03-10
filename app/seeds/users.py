from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    admin = User(
        username='Admin', email='admin@snacc.com', password='password')
    demo = User(
        username='Demo', email='demo@aa.io', password='password')
    bobbie = User(
        username='Jeddy', email='jeddy@aa.io', password='password')

    db.session.add(admin)
    db.session.add(demo)
    db.session.add(bobbie)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
