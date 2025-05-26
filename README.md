# My APP Python API Backend

## Installation steps

1. Create the Python virtual environment

```bash
python3 -m venv ./venv
```

2. Activate virtual environment

```bash
source venv/bin/activate
```

3. Install the dependencies

```bash
pip3 install -r requirements.txt
```

4. Run the server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 3401
```

### One line command

```bash
python3 -m venv ./venv;
source venv/bin/activate;
pip3 install -r requirements.txt;
uvicorn main:app --reload --host 0.0.0.0 --port 3401;
```