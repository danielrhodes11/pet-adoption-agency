from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    app.app_context().push()


default_image = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQMAAADCCAMAAAB6zFdcAAAAS1BMVEXMzMx/f3/Q0NB5eXnIyMiVlZWEhITAwMCLi4vR0dF8fHy0tLSjo6OysrLDw8Obm5t1dXWsrKyWlpampqa6urqtra2Ojo6fn59vb28EtcIDAAAFL0lEQVR4nO2bCZejKhBGpRAVUNxQ3///pa9wSUdjejJ9Mp1ovnvOTBYpZriylAajCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnAqK0+cQ06ub8lOolM+iPKgEGqQwz0HI4ZgSSAqhnoMQ8pgOYikyTc9AZ0LGr27OjwgOnnP2CA4+ycHU8fcOfIoDits+yZpix8KnOKBc8hoojBT+JuhDHJDilXRCdtuoz3DAvUBckOkm7DMcxFcKxE3YRzig1lw7kOnm8Ec46FcOzGZG+AwHiVg5yOHAtKd3cJsNklrPB8XZHZBXWeNWR6hbzwebBp/OgR6k4XRwkw2uFGzvGp3NwZIQrhMh8tcJwk3MyRxkS683awmdnA8Y4U6dK5NLvga+WbWV0p4vmow05W1NZ3JAqVjNfWsJlHZtW+zdRj+RA7IrA0IkmwbfuYVyIgdUy7UCYZLHWnYaB6vL47+TcBYH1NwqYAnZIzWdxUFvdhTcl0BaX/k7gwOKk30FLKHfWwicMrxILkfO4IDXxPvsSOAFJNxeTZa18wQOyN/rBJOEZptJLbOnsbPDwzvgNPg7BVsJFH9NHXK6kXB4B3tr4obrX9bXuaRsxu8O7oDKPyrgpuZ6DtomUibjXPLYDvS9NfGehJsswghPx3YQ3V0TtxJaHZbEbKe4qQ+9/yB5VAFLqPW0JO51kiM7+BtMfXfyZDOf4UDsd4KZD3HwLXAAB3AAB3AAB3AAB3AAB3AABydzQA/fO3gAc8znWG5/Y/05sj6mg4iKLHkOWXFQBWE/wbtVBAAAAIBfJXZ/WTL90yWAc9eVLsXTO6XfACrkoyXtWFJX9vvMh8pG55eNOlT58dX999P/4b+HrOC/wlbTaN5tOu86Hb/5+jiXZAfS0uXL6XV6e/kYx5QrmmrgKzA/vrpqrvMNCS2jNm1VR7Vqw+/og2o8t9Kq0uVhR874MVo58NbzUf7QqRDTpuFKy8+hZG1wQL5Ug2MHduC6Rwf8L5S3T8O+ntAyLZK2ln1ZiJxc1fq88tSZoksq7tiZLcR49fflQOdCFT27U5m1idJlOOtVuoSWpc6VLmTnleS6TWuTgeuNqO89V/t+EkYHSa5102tdZ9rzW53UJCxRUUWpIa2dXEpGs4NEUyxdVMZaF0KnkrtLEkKJQ/UwOqgLrSOZajNocjJ2FXnBVac3T3q8nqkfcIObnKjOeMAWrTJ1HG4A8bmrk6EsyyqNVmMhDzvSTBppXw8J+0gKnbUcakPo5IC06/I+OAi9X3h2kE91PbwO/RobB3xO+9wndVwtDmxRFHZc37wZA6QfHcQmpV6UXSs05T2Xpzl07gedbFo7O6DJQc91Wfva9u6xdtBrxV2XDI+FMLlV3O4wl9dj0bgKU7zn1k4OXFpx528FT3iy5R40horFgfA8iCp2UBOPmzAWeNRc6noryJrJgRrGfjAkLlWy5SmtKASP86x3rk+mhaGRrW1lSTTwJBhLngSLuDMibMKrCv52Dp3mxKyMfSa9Nsa7rBnnRNG4NNvb5/xqfMOTv+f1seMTP1BUiswXOWnflD6s6Tzgh7koO0oyXiOoC/tQlSPLx2LlwkIajs+hdU1FS04J5XKrG9snOXcVLhFzXfnrWvoNtOQ3y58x01GO53BJ6wd16JI/zXFfidTlcEigloqmt7QUv/vQz3tCTdLV5qh3hZ8EFcPwjjndr3KobgsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCv8T8P0EKx6h83/QAAAABJRU5ErkJggg=="


class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=default_image)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)


# # Pet
# pet_urls
# Pet:
#    pet_urls = db.Column(ARRAY(db.Text))
