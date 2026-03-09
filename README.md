## Medical Insurance Price Prediction System - Gradient Boosting Machine

A gradient boosting model built from scratch using the Pandas and NumPy libraries.

The system predicts medical insurance pricing based on various fearures and recommends various plans of different coverage features and benefits.

**Go to Notebook:**
[Open in Google Colab](https://colab.research.google.com/drive/1tc_wCYIcV5VOHDVFs0iAFLZVYilyhyn5#scrollTo=IvDk5C1yinMf)

---

The evaluation metrics of the model are shown in the table below:
| Metrics | Training Loss | Validation Loss |
|-----------|---------------|-----------------|
| MAE | - | - |
| MSE | - | - |
| R² Score | - | - |

## Platform Demo

<video width="1280" height="720" controls>
  <source src="./docs/Demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

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
5. Run the django project
   ```bash
   python manage.py runserver
   ```

---

THE END
