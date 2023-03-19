# SpotiStats

Create a `secrets.json` file in root directory. Add `client_id` (str), `client_secret` (str), `redirect_uri` (str) and `scope` (list of str) in it.

## Run Application

To run the application follow following commands:
```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
gunicorn -b 0.0.0.0:9010 app:app
```
Application is now up and running on port `9010`.

For testing, send `cURL` request at `me` endpoint
```sh
curl --location 'http://0.0.0.0:9010/me'
```
