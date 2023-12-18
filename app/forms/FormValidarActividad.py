from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeLocalField
from wtforms.validators import DataRequired, Length, Regexp, ValidationError

class FormValidarActividad(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=5, max=100, message="La longitud debe estar entre 5 y 100 caracteres."),
                        Regexp('^[a-zA-Z0-9.,\-_ áéíóúÁÉÍÓÚ]*$', message="Solo se permiten caracteres alfanuméricos, coma, punto, guión, subguión y tildes.")])

    fechaInicio = DateTimeLocalField('Fecha de inicio', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])

    fechaFin = DateTimeLocalField('Fecha de fin', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])

    tipo = StringField('Tipo de actividad', validators=[Length(min=1, max=20, message="La longitud debe estar entre 1 y 20 caracteres."),
                        Regexp('^[a-zA-Z0-9.,\-_ áéíóúÁÉÍÓÚ]*$', message="Solo se permiten caracteres alfanuméricos, coma, punto, guión, subguión y tildes.")])

    descripcion = TextAreaField('Descripción', validators=[Length(min=20, max=200, message="La longitud debe estar entre 20 y 200 caracteres."),
                        Regexp('^[a-zA-Z0-9.,\-_ áéíóúÁÉÍÓÚ]*$', message="Solo se permiten caracteres alfanuméricos, coma, punto, guión, subguión y tildes.")])

    evento = StringField('Evento', validators=[
        Length(min=1, max=40, message="La longitud debe estar entre 1 y 20 caracteres."),
        Regexp('^[a-zA-Z0-9.,\-_ áéíóúÁÉÍÓÚ]*$', message="Solo se permiten caracteres alfanuméricos, coma, punto, guión, subguión y tildes.")
    ])

    ambiente= StringField('Ambiente', validators=[
        Length(min=1, max=20, message="La longitud debe estar entre 1 y 20 caracteres."),
        Regexp('^[a-zA-Z0-9.,\-_ áéíóúÁÉÍÓÚ]*$', message="Solo se permiten caracteres alfanuméricos, coma, punto, guión, subguión y tildes.")
    ])

    def validate(self):
        if not super(FormValidarActividad, self).validate():
            return False

        if self.fechaInicio.data and self.fechaFin.data and self.fechaInicio.data > self.fechaFin.data:
            self.fechaFin.errors.append('La fecha de fin debe ser posterior o igual a la fecha de inicio.')
            return False

        return True
