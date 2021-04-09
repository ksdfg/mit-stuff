# Assignment 1 - Selenium

## Fetch articles from Google Scholars

The following vars need to be set in your .env/settings.ini file, or set/passed as env variables

- `ass1_headless` - whether selenium is to be run headless or not (defaults to false)

To fetch articles, run
```commandline
python -m assignment1
```

If you want to fetch articles for a specific query, run
```commandline
python -m assignment1 -q/--query QUERY
```
You can check out the help text for this by running
```commandline
python -m assignment1 -h/--help
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