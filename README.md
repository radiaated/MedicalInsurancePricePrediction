## Medical Insurance Price Prediction System - Gradient Boosting Machine

A gradient boosting model built from scratch using the Pandas and NumPy libraries.

The system predicts medical insurance pricing based on various fearures and recommends various plans of different coverage features and benefits.

**Go to Notebook:**
[Open](https://github.com/radiaated/MedicalInsurancePricePrediction/blob/main/MedicalInsurancePricePrediction.ipynb)

---

The evaluation metrics of the model are shown in the table below:
| Metrics | Training Loss | Validation Loss |
|-----------|---------------|-----------------|
| MAE | 871.46 | 870.075 |
| MSE | 1182018.3792 | 1178591.5509 |
| R² Score | 0.9394 | 0.9393 |

## Web Platform Demo

![Web Platform Demo Gif](./docs/Demo.gif)

## Technologies used

- Python
- Pandas
- Numpy
- Matplotlib
- Django
- TailwindCSS

## Setup web platform

1. Git clone the repository
2. Install all dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Go to Django project directory
   ```bash
   cd web
   ```
4. Make and apply migrations to the database
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Install the database fixtures

   ```bash
   python manage.py loaddata dump.json
   ```

6. Run the django project
   ```bash
   python manage.py runserver
   ```

---

THE END
