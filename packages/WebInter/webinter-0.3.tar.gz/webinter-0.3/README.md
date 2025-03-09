### **README.md**

```markdown
# WebInter

**WebInter** is a minimalist Python web framework that allows you to quickly create websites and APIs without external dependencies. It provides everything you need for building simple web applications, from routing to serving static files and templates, all in a lightweight package.

## Features

- **No external dependencies** – Everything is implemented in WebInter, so you don't need to install any third-party libraries.
- **Support for static files** – Serve CSS, JavaScript, and image files directly from your project.
- **HTML Templates** – Easily handle dynamic HTML content with simple string-based templates.
- **JSON-based APIs** – Create and manage RESTful APIs with minimal effort.
- **Request and Response Handling** – Simple and efficient ways to handle HTTP requests and responses.
- **Easy to Use** – Get your web applications up and running in no time.

## Installation

Install **WebInter** easily using `pip`:

```bash
pip install webinter
```

Once installed, you can start building your web applications without worrying about additional dependencies.

## Example Usage

Here’s a simple example that demonstrates how to create a basic web server using WebInter.

### Basic Web Server Example

```python
from webinter import WebInter

# Initialize the WebInter app with host and port
app = WebInter(host="127.0.0.1", port=8080)

# HTML Template Route - Render a simple message
@app.route("/", "<h1>This page runs with WebInter!</h1><p>Welcome to WebInter, the minimalist Python web framework.</p>")

# Static File Route - Serve static files (e.g., CSS)
app.add_static_file("style.css", "body { background-color: lightblue; font-family: Arial, sans-serif; }")
@app.route("/static/style.css", static=True)

# Start the web server
if __name__ == "__main__":
    app.run()
```

### Explanation:

- **`@app.route()`**: This is how you define a route. The first argument is the URL path, and the second argument is either a string (for static HTML) or a function (for dynamic content).
  
- **Static File Handling**: The method `add_static_file()` is used to define a static file (like a CSS file) that will be served to users when they access the corresponding route.

### Running the Application

After running the script, navigate to `http://127.0.0.1:8080/` in your browser to see the page displaying:

```
This page runs with WebInter!
Welcome to WebInter, the minimalist Python web framework.
```

## Static Files

WebInter makes it easy to serve static assets like CSS, JavaScript, and images. Just place the file in your project and use the `add_static_file()` method.

For example, you can serve a CSS file like this:

```python
app.add_static_file("style.css", "body { background-color: lightblue; }")
@app.route("/static/style.css", static=True)
```

You can then link to it in your HTML templates:

```html
<link rel="stylesheet" href="/static/style.css">
```

## Project Structure

Here’s how your project should be structured:

```
/webinter_project
    /webinter
        __init__.py
    /static
        style.css
    setup.py
    README.md
```

## Conclusion

With **WebInter**, you can easily create web applications with minimal setup. Whether you're building a simple website, API, or more complex application, WebInter provides an easy-to-use framework that’s perfect for quick projects and learning.

For more information, feel free to check the examples in the repository and explore how you can extend WebInter to suit your needs!
