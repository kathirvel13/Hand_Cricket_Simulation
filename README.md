# Hand Cricket Simulation
This program tries to create a hand cricket simulation using Python, HTML, Jinja and Flask. I created this program to learn flask.

## Learing References
- [Flask](https://flask.palletsprojects.com/)
- [Jinja](https://jinja.palletsprojects.com/)

# Jinja Notes
Jinja is a template engine. A [Jinja template](https://jinja.palletsprojects.com/en/3.1.x/templates/) is simply a text file. Jinja can generate any text-based format (HTML, XML, CSV, LaTeX, etc). A Jinja template doesn’t need to have a specific extension. A template contains variables and/or expressions, which get replaced with values when a template is rendered; and tags, which control the logic of the template. The template syntax is heavily inspired by Django and Python.

There are a few kinds of delimiters. The default Jinja delimiters are configured as follows:
- {% ... %} for Statements
- {{ ... }} for Expressions to print to the template output
- {# ... #} for Comments not included in the template output

## Important Topics
- [Literals](https://jinja.palletsprojects.com/en/3.1.x/templates/#literals)
- [Arithmetic Operators](https://jinja.palletsprojects.com/en/3.1.x/templates/#math)
- [Comparison Operators](https://jinja.palletsprojects.com/en/3.1.x/templates/#comparisons)
- [Logical Operators](https://jinja.palletsprojects.com/en/3.1.x/templates/#logic)
- [Python Methods](https://jinja.palletsprojects.com/en/3.1.x/templates/#python-methods)

### If Conditions
```html
{% if kenny.sick %}
    Kenny is sick.
{% elif kenny.dead %}
    You killed Kenny!  You bastard!!!
{% else %}
    Kenny looks okay --- so far
{% endif %}
```

### For Loop
```html
<h1>Members</h1>
<ul>
{% for user in users %}
  <li>{{ user.username|e }}</li>
{% endfor %}
</ul>
```

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