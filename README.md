# CHOPS
This project [chops](https://chops-fee5c95170e3.herokuapp.com/) is a minimalistic eccormmerce site for the sales of different kinds of meals
<!-- ![home](/assets/images/finterface.png) -->
# User Experience (UX)
Key information for the app
this section provides insight into the UX process, focusing on who the app is for, the main aims of the project and how the app can help users meet their needs
<!-- 
![exit](/assets/images/exit.png) -->

# Project goals:<br>
 User able to login

 integrated alluth

 able to search for meal based on names
<!-- ![input](/assets/images/inputinterface.png)  -->
<br>

able to add to cart even without logging in

sychronizing your cart after loggin in
<!-- ![option](/assets/images/priceoption.png) -->

making purchase for more a meal multiple time
<!-- ![option](/assets/images/priceoption.png) -->
<br>



# Features:<br>
Login
![input](assets/1708385128580.png) <br>

Signup
![input](assets/1708385173248.png) <br>

products
![input](assets/1708385207327.png) <br>




# Project workflow:<br>

Auth <br>

The Project implement  django alluth for authentication<br>
AllAuth Takes care of all neccsary authentication template, authenication funtionalities


Product <br>
The project conatined already test data as a dictionary located in the settings.py file

<br>

The project use The browser localstorage to keep track of the cart and checkout system







# Responsiveness<br>

screen w-1700
![input](assets/1708384794067.png) <br>



screen w-1500
![input](assets/1708384825394.png) <br>

screen w-600
![input](assets/1708384851620.png) <br>

screen w-350
![input](assets/1708384874442.png) <br>



# WIREFRAME<br>




# ADMIN CREDENTIALS<br>
username dussy@gmail.com<br>
password Admin@123<br>




# TEST.........<br>

Model Testing:<br>

Implementing Django testing for models involves creating a structured approach to ensure that the database interactions and business logic encapsulated in your models function as expected. Here is a detailed note on how I implemented Django testing for models in a recent project:

### 1. Setting Up the Testing Environment

**Objective**: Configure the environment for writing and running tests.

- **Installed Dependencies**: Ensured `pytest-django` and `django` were included in the project's `requirements.txt` to facilitate testing.
- **Configured Settings**: Modified `settings.py` to include a separate database for testing to prevent interference with the development and production databases.

### 2. Writing Test Cases

**Objective**: Develop test cases to validate model behavior.

- **Test Suite Structure**: Created a `tests` directory within the Django app directory and added `__init__.py` to recognize it as a module.
- **Test Class**: Created test classes for each model, inheriting from `TestCase` in `django.test`.

```python
from django.test import TestCase
from eccommerce.base.models import OTP
from .models import MyModel


class TestCartModel(TestCase):
    """
    Things to test:
    - Can be create a cart with the bare minimum of fields? (name, image and userid)
    - Does the __str__ method behave as expected?
    
    - Do two carts with the same title and user same id?
    """

    @classmethod
    def setUpTestData(cls):
        cls.user = USER_MODEL.objects.create_user(
            email='janedoe@test.com',
            first_name='Jane',
            last_name='Doe',
            username='user123',
            password='password456'
        )

        cls.cart = CART.objects.create(
            name='rice',
            image='rice.jpg',
            price="20",
            productid="2",
            
            user_id=cls.user.username,
        )



```

### 3. Testing Model Methods

**Objective**: Ensure that custom methods on the models behave correctly.

- **Method Testing**: For models with  methods as str, wrote test cases to verify their output and side effects.

```python


class TestReservationModel(TestCase):
    """
    Things to test:
    - Can be create a cart with the bare minimum of fields? (name, image and userid)
    - Does the __str__ method behave as expected?
    
    - Do two carts with the same title and user same id?
    """

   @classmethod
   def test_cart_str(self):
        """ Tests the __str__ of the cart model"""

        self.assertEqual(str(self.cart), 'usercart')


```

### 4. Testing Model Validations

**Objective**: Ensure that model validations are working as expected.

- **Validation Testing**: Tested the model's field validations by creating instances with invalid data and asserting that errors are raised.

```python
from django.core.exceptions import ValidationError

class MyModelValidationTestCase(TestCase):
   def test_invalid_data(self):
        obj = CART(name="")  # Name is required
        with self.assertRaises(ValidationError):
        
            obj.full_clean()  # This method triggers model validation
```

### 5. Testing Database object are unique

**Objective**: Validate that database constraints (e.g., unique constraints) are enforced.

- **Constraint Testing**: Checked for the enforcement of unique constraints and other database-level validations.

```python
 def test_id_are_unique(self):
        """ Tests two carts with identical titles from the same author receive different slugs """

        second_title = CART.objects.create(
            name='beans',
            price='10',
            image='beans.jpg',
            productid="3",
            user_id=self.user.username,
        )

        self.assertNotEqual(self.cart.productid, second_title.productid)

```

### 6. Running the Tests

**Objective**: Execute the tests to verify model functionality.

- **Command**: Used Django’s built-in test runner to run the test suite.

```bash
python manage.py test
```

- **Pytest**: Alternatively, used `pytest` for running tests to leverage its advanced features and more readable output.

```bash
pytest
```

### Conclusion

By implementing these structured steps for testing Django models, I ensured robust validation of model behaviors, including data integrity, business logic, and database constraints. This process not only helped in catching bugs early but also maintained a high standard of code reliability and quality throughout the development lifecycle.

# TEST.........<br>

 Tests that a GET request works and renders the correct template   

 ![input](assets/Screenshot2024-02-22122014.png) <br>

 ![input](assets/Screenshot2024-02-22120524.png) <br>

 Test Model
 The cart model

 ![input](assets/Screenshot2024-02-22122102.png) <br>

 ![input](assets/Screenshot2024-02-22120524.png) <br>




# Deployment<br>
``` make a new file name Procfile and do not put any extension in it. It is a file required by Heroku

. For our app we can write the following command "web: gunicorn name_of_your_app.wsgi -log-file -" in the procfile

. pip install gunicorn

. login into heroku in the browser

. Make a new heroku app

. update settings.py file ALLOWED_HOSTS = ["your_app_name.herokuapp.com"]

. With a couple of lines of config WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service

so run pip install whitenoise


Add it in MIDDLEWARE in settings.py file

MIDDLEWARE = [
   'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
   ...
]

.Make a new Github Repo and add all of your code in it.

.Using Heroku Postgres
Go to your app dashboard and in the Resources section search for Postgres and click add.


. Now paste the following code below DATABASES in settings file

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)


.Currently, your database is empty and you might want to fill it.

Open terminal
type → heroku login
After the login run the following commands
heroku run python manage.py makemigrations
heroku run python manage.py migrate ...

# Credits<br>
Full credit goes to code institute for the template provided to make this project a possiblityl


