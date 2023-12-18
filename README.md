# github-actions-flask-demo
Exemple de projet : Flask + Actions GitHub. Application de salutations multilingues prenant en charge différentes langues de salutation.

#Multi-LanguageGreetingsApp

## Project description

***The Multi-Language Greetings App project is a simple application written in Python using the Flask framework. The app supports greetings in a variety of languages and was built to demonstrate Flask's core features and integration with GitHub Actions for task automation.***

## Project structure

***The project consists of the following files:***
```
- `hello_world.py`: File containing the `say_hello(name)` function with an example greeting.
- `say_hello.py`: Unit test file for the `say_hello` function.
- `multi_language.py`: The main file of the application, which contains the code that handles greetings in different languages. The application uses the Flask framework and a time delay (5 seconds) was added using `time.sleep(5)` before the application was launched.
```
## Starting the project

- python multi_language.py
- The application will be available at http://0.0.0.0:8083/. Check out the different welcome languages using your web browser.

### 1. Installing dependencies

***Run the command below in the terminal to install the necessary dependencies:***
***requirements.txt***

```
pytest==7.4.0
Flask==1.1.4
Werkzeug==1.0.1
Jinja2==2.11.3
MarkupSafe==1.1.1

```
### GitHub Actions

***The project uses GitHub Actions to automate unit tests, CI/CD and schedule cron jobs. Check the .github/workflows/.yml file for details.***
