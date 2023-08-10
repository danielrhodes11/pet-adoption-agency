from models import db, Pet
from app import app

db.drop_all()
db.create_all()

pets = [
    Pet(name="Whiskers",
        species="cat",
        photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ18Fyea6Gj0U4KocLCV6XkYQA2qX6F0jDljw&usqp=CAU",
        age=5,
        notes="Loves to be scratched behind the ears.", available=True),

    Pet(name="Fido",
        species="dog",
        photo_url="https://img.freepik.com/free-photo/puppy-that-is-walking-snow_1340-37228.jpg",
        age=None,
        notes="Very playful and loves to go on walks.",
        available=False),

    Pet(name="Buddy", species="porcupine", age=1, available=True)
]

db.session.add_all(pets)
db.session.commit()
