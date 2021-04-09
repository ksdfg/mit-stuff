# Assignment 1 - Selenium

## Fetch articles from Google Scholars

The following vars need to be set in your .env/settings.ini file, or set/passed as env variables

- `ass1_headless` - whether selenium is to be run headless or not (defaults to false)

To fetch links, run

```commandline
python -m assignment1
```

(considering your pwd is the repo root)

## Test Github Login

The following vars need to be set in your .env/settings.ini file, or set/passed as env variables

- `ass1_email` - email used to log in to github

- `ass1_password` - password used to log in to github

- `ass1_username` - your github username

- `ass1_headless` - whether selenium is to be run headless or not (defaults to false)

To run the tests, run

```commandline
pytest assignment1
```

(considering your pwd is the repo root)