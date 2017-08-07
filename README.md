Multi-layered tests framework
=========
This is a multi-layered tests framework for **[Comments](http://commentssprintone.azurewebsites.net/)** website. It is using pytest 
and selenium libraties to run automated tests.

### How to install?

1. Create separate virtual environment with Python 3.5.x.
2. Run `pip install -r requirements.txt` to install required Python's dependencies.

### How to run automated tests?

1. You need to download the latest version of webdriver executable to run tests.
Check **[selenium official website](http://docs.seleniumhq.org/download/)** 
`Third Party Browser Drivers` for latest versions of browser that you need.
2. Then launch it and run command `pytest comments` from terminal within your 
virtual environment.


### Tests samples
There are 4 samples of tests in `comments/tests/` folder(one of them will fail because of bug). You can run it for 
demo.