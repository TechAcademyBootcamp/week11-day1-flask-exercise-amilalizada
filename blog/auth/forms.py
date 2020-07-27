from blog.auth.models import User
from blog import db

class LogInForm(FlaskForm):
    username = StringField('Istifadeci adi', validators=[Length(5, 40), DataRequired()])
    password = PasswordField('Sifre', validators=[Length(min=8, max=40), DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Istifadeci adi', validators=[Length(5, 50), DataRequired()])
    email = StringField('E pocht', validators=[Email(), Length(max=40), DataRequired()])
    first_name = StringField('Ad', validators=[Length(max=40), DataRequired()])
    surname = StringField('Soyad', validators=[Length(max=40), DataRequired()])
    password = PasswordField('Sifre', validators=[Length(min=8, max=40), DataRequired()])

    def validate_username(self, field):
        exists = db.session.query(db.exists().where(User.username == field.data)).scalar()
        if exists:
            raise ValidationError('Username already taken')
        return field

    def validate_email(self, field):
        exists = db.session.query(db.exists().where(User.email == field.data)).scalar()
        if exists:
            raise ValidationError('Email already taken')
        return field
    
    def validate_password(self, field):
        data = field.data
        cap_letter = [letter for letter in data if 65 <= ord(letter) <= 90]
        if data.isdigit():
            raise ValidationError('Herif yaz')
        elif not cap_letter:



