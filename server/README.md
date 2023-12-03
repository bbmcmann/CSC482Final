To start Flask server:

1. Create a `.venv` file if you don't have one already
   1. mac: `python3 -m venv .venv`
   2. windows: `py -3 -m venv .venv`
2. Activate virtual environment
   1. mac: `source .venv/bin/activate`
   2. windows: `.venv\Scripts\activate`
3. Install all requirements with `pip install -r requirements.txt`
4. Start the debug server with `flask --app app run --debug `
5. To stop virtual environment, run `deactivate`
