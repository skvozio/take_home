## Job applications tracker API
API to help with job applications tracking: to what position,
where, when, what is expected salary there. This is an idea for
personal project that came to my mind some time ago, after I realized I need to track my
applications not in Excel sheet :)

## Dependencies
  1. Install Python 3.7.5 or later
  2. Install Postgres and Postgis

## Launching Backend Locally Using Django Server
1. Create Postgres DB, enable PostGis in it by running:
   `psql [db_name]` and then
   `CREATE EXTENSION postgis;`
2. make sure you have `.env` file in the project root, sample `.env` file
   is located in repo as `.sample_env`
3. Edit `.env` file with your database info
4. run `python3 -m venv venv`
5. run `source venv/bin/activate`
6. run `pip install -r requirements.txt`
7. run `python manage.py migrate`
8. to run tests `python manage.py tests`   
9. to start server `python manage.py runserver`

## Swagger UI documentation
Swagger documentation is available at `http://127.0.0.1:8000/api/swagger/`
## Postman tests
Collection of Postman tests is in `job_application_requests_collection.json` file in root directory