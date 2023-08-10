from flask import Flask, render_template, redirect, request, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, default_image
from forms import AddPetForm, EditPetForm


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "abc123"
app.config['SECRET_KEY'] = 'ihaveasecret'

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    """shows list of pets"""
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets, default_image=default_image)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """add pet form"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data if form.photo_url.data else default_image
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species,
                      photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f'Added new pet: {name} ({species})')
        return redirect('/')

    else:
        return render_template("add_pet_form.html", form=form, default_image=default_image)


@app.route('/<int:id>', methods=['GET', 'POST'])
def pet_details(id):
    pet = Pet.query.get_or_404(id)
    is_default_image = True if pet.photo_url == default_image else False
    form = EditPetForm()  # Initialize the form without obj=pet

    if form.validate_on_submit():
        # Only update if data is present
        if form.photo_url.data and form.photo_url.data.strip():
            pet.photo_url = form.photo_url.data

        if form.notes.data and form.notes.data.strip():
            pet.notes = form.notes.data

        # Assuming the 'available' field is a boolean or 'True'/'False' string
        if form.available.data is not None:
            is_available = form.available.data == 'True'
            pet.available = is_available

        db.session.commit()
        return redirect(url_for('pet_details', id=id))

    return render_template('pet_detail.html', pet=pet, form=form, is_default_image=is_default_image)
