

to run test funcitons:
  path to parent direcoty and type pytest . #execute all test funtions 
  
-V ( Verbose If u want Proper details about twst name)
pytest <path of pytest functions >
pytest /home/bhargav-wl/GitHub/pytest/test_file.py -v





#  my-pytest-course

A repository for learning pytest by building a Django web application.

The application lists companies and indicates wether they are laying off/ hiring freeze or hiring.
 
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PYTHONPATH=/{YOUR_PATH_TO_PROJECT}/my-pytest-course/:/{YOUR_PATH_TO_PROJECT}/my-pytest-course/api/coronavstech`

`DJANGO_SETTING_MODULE=api.coronavstech.coronavstech.settings`


## Run Locally

Clone the project

```bash
  git clone https://github.com/bhargavvc/pytest.git
```

Go to the project directory

```bash
  cd my-pytest-course
```

Install dependencies

```bash
  pipenv install
```

Start the Django server

```bash
  pipenv run api/coronavstech/manage.py runserver
```


## Running Tests

To run tests, run the following command

```bash
  pipenv run pytest .
```
