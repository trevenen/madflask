#### FLASK DASHBOARD APP WITH PLOTLY.

### Setting up python virtual environment

    pip install virtualenv

### Python 2:

    $ virtualenv env

### python3.6

    python3.6 -m venv env

### Activate the virtual environment

    source env/bin/activate

### set the environmental variable. for development variable we have "dev" production we have "prod" staging we have "stage".

    export APP_CONFIG_FILE=dev

### Terminal commands

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all

### Viewing the app

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/dashboard

### Deactivate the virtual environment when not using

    deactivate
