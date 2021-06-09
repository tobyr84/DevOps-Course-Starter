# DevOps Apprenticeship: Project Exercise

## Setup
 

Setup.sh has been designed to automate the boring stuff for you :smile: 

Updates your resources, installs the pre-requisites, installs the latest version of python, installs poetry, clones the required GIT respository for the App and establishes your dependences.  

All you need to do is input your Trello credentials into the .env file
 
## Documention 
Schematic overviews of the appliation seperated into 3 level views; 
* Level 1 - Context
* Level 2 - Container 
* Level 3 - Component

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). 

Pip install Arrow for an easier setup with the testing of the application.  Arrow is a Python library that offers a sensible and human-friendly approach to creating, manipulating, formatting and converting dates, times and timestamps.

```bash
$ pip install -U arrow

$ poetry add arrow 
```

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
=======
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

### Notes

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like developement mode (which also enables features like hot reloading when you make a file change).

You'll need a trello account and fill in your trello credentials in the .env file.

Please ensure that you populate the `.env` file with the details of names and IDs of your respective lists within Trello. 

### ** Testing **

The application has been built with some standard tests to ensure that the everything is fully working.  In order to use these, you need to run the following python test files 

``` 
$ python test_view_model.py
```
This is the main file that contains all of the tests.  Running this python file will run all tests on the application.  

The following tests will also ensure the application is fully working prior to use.  They will test the functionality around the tasks within the application.  
```
* test_to_do
```
Tests and confirms the status of all tasks not yet started.  

```
* test_doing
```
Tests and confirms the status of all tasks that are currently In Progress.
```
* test_done
```
Tests and confirms the status of all tasks that are competed.  
```
* test_show_all_done_items_returns_for_small_numbers_of_items
```
This tests the functionality about returning a shortened list of either 5 or less completed items.  This will support the different view options within the application.  
```
* test_show_all_done_items_returns_false_for_large_numbers_of_items
```
This test will confirm the function of returning results for completed tasks whereby the quantity if greater than 5.  This will also support differnt view options within the application.  

 
### Docker

Use the following command to pass the key variables into the container.  
```
docker run --env-file .env -p 5000:5000 todo-app 
```

