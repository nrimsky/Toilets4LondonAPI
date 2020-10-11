# Toilets4LondonAPI

- This is a REST API built with Django Rest Framework
- Intended to be serve as a simple way to manage London toilet data
- Currently deployed at https://toilets4london.herokuapp.com/
- View simple map of data at https://toilets4london.herokuapp.com/toilets/view_map/

# Running Locally

1. Clone the repo `git clone https://github.com/toilets4london/Toilets4LondonAPI.git`
2. cd into the project directory `cd Toilets4LondonAPI`
3. (Optional but recommended) Create a virtual environment to download all the packages - `python3 -m venv env` and activate it `source env/bin/activate`
4. Install the requirements `pip install -r requirements.txt`
5. Go into `settings.py` and set `DEBUG = True` *(remember to set back to False in production)*
6. Run `python manage.py migrate` to set up the database
7. Run `python manage.py createsuperuser` to set up an admin account, following the instructions to add your email address and a password (for testing purposes these can be fake)
8. Run `python manage.py runserver` to run the development server on localhost
9. Navigate to http://127.0.0.1:8000/ or click the link generated by Django to see the browsable API
    
# Endpoints used by [mobile app](https://github.com/toilets4london/ToiletApp/)

- GET all toilets `/toilets/?page_size=1000` (increase `page_size` if there are > 1000 toilets in the database)
- POST sign up { 'email' : *your email* , 'password' : *your password* } `/auth/users/`
- POST obtain api token { 'email' : *your email* , 'password' : *your password* } `/auth/token/login/`
- POST star rating { 'toilet' : *valid toilet id* , 'rating': *1-5 star rating* } HEADERS { 'Authorization' : *token [valid api token]* } `/ratings/`
- POST report a toilet { 'toilet' : *valid toilet id* , 'reason' : *valid reason code, see below* , 'other_description' : *text describing problem* } HEADERS { 'Authorization' : *token [valid api token]* } `/reports/`
- POST forgot password { 'email' : *your email* } `/reset-password/`
- POST reset password with token received by email { 'token' : *token in email* , 'password' : *your new password* } `/reset-password/confirm/`

| Problem                   | Report reason code |
| ------------------------- | ------------------ |
| Does not exist            | "DNE"              |
| No toilet paper           | "NTP"              |
| Long queue                | "LQ"               |
| No handwashing facilities | "NH"               |
| Blocked or broken         | "BOB"              |
| Not clean                 | "NC"               |
| Other                     | "O"                |