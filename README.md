# Hand Cricket Simulation
This program tries to create a hand cricket simulation using python, HTML and flask. I created this program to learn flask.

## Learing References
- (Flask)[https://flask.palletsprojects.com/]
- (Jinja)[https://jinja.palletsprojects.com/]

# Flask Notes
To launch the application with debugger, run the following command:
```shell
flask run --debug
```
This launches a very simple builtin local server.

## Basic Functions
We use the `route()` decorator to tell Flask what URL should trigger our function.

Web applications use different ***HTTP request methods*** when accessing URLs. By default, a route only answers to `GET` requests. You can use the `methods` argument of the `route()` decorator to handle different HTTP methods like `POST`.

To render a template you can use the `render_template()` method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments.

To redirect a user to another endpoint, use the `redirect()` function; to abort a request early with an error code, use the `abort()` function.

# Jinja Notes
Jinja is a template engine. A Jinja template is simply a text file. Jinja can generate any text-based format (HTML, XML, CSV, LaTeX, etc). A Jinja template doesn’t need to have a specific extension. A template contains variables and/or expressions, which get replaced with values when a template is rendered; and tags, which control the logic of the template. The template syntax is heavily inspired by Django and Python.
