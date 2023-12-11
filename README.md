# Crear entorno de trabajo
- python -m venv .venv
- venv\Scripts\activate         (Windows)
- . .venv/bin/activate          (Linux)
- . venv/bin/activate           (MacOs)
- pip install -r requirements.txt

# Crear la database
python initDatabase.py

# Ejecutar la aplicación
python run.py
