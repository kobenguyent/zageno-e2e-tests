# Introduction

This project demostrate how to run e2e tests using python as main language.

### Tech

This e2e test is done using this framework

* seleniumbase - Reliable Browser Automation & Testing with Selenium-WebDriver and Pytest. - https://github.com/seleniumbase/SeleniumBase

### Installation

e2e test requires:

* [Python 2.7 or 3.x](https://www.python.org/downloads/) to run.

#### macOS:

Python should already come preinstalled. You can use both Python 2.7 or Python 3.6+ with SeleniumBase. If you have [Homebrew](https://brew.sh/) installed, you can use: ``brew install python3`` to install Python 3. Or you can just get everything from [https://www.python.org/downloads/](https://www.python.org/downloads/).

The official docs.python-guide.org instructions here: [Installing Python 2 on Mac OS X](https://docs.python-guide.org/starting/install/osx/) and [Installing Python 3 on Mac OS X](https://docs.python-guide.org/starting/install3/osx/#install3-osx). (NOTE: Apple has rebranded OS X as macOS but this has not been reflected in the official docs.python-guide.org instructions yet.)

#### Windows:

You can [download Python 2.7 from here](https://www.python.org/downloads/release/python-2713/) OR [download Python 3.6.6 from here](https://www.python.org/downloads/release/python-366/).

* [Pip](https://en.wikipedia.org/wiki/Pip_%28package_manager%29)

You might already have pip and setuptools installed, but if you don't:

On macOS / Windows / Linux, run the following command:
```bash
python -m ensurepip --default-pip
```

If your existing version of pip is old, upgrade to the latest version:
```bash
python -m pip install --upgrade pip setuptools
```

On CentOS 7 and some versions of Linux, you may need to install pip with ``yum``:
```bash
yum -y update
yum -y install python-pip
```

If you're having any trouble getting pip, you can [GET PIP HERE](https://pip.pypa.io/en/latest/installing/).

When done, make sure the location of pip is on your path, which is `$PATH` for macOS/Linux. (On Windows, it's the System Variables `Path` within System Environment Variables. Ex: Add "C:/Python27/Scripts/" to the end of the `Path` variable.)

You can also get pip (or fix pip) by using:
```bash
curl https://bootstrap.pypa.io/get-pip.py | python
```
* (If you get SSL errors while trying to install packages with pip, see [this Stackoverflow post](https://stackoverflow.com/questions/49768770/not-able-to-install-python-packages-ssl-tlsv1-alert-protocol-version), which tells you to run the above command.)

**Keep Pip and Setuptools up-to-date:**
```
python -m pip install -U pip setuptools
```
* (Depending on your user permissions, you may need to add ``--user`` to the command if you're not inside a [Python virtual environment](https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/virtualenv_instructions.md), or use "[sudo](https://en.wikipedia.org/wiki/Sudo)" on a UNIX-based OS if you're getting errors during installation.)

### Install project dependencies

```sh
$pip install -r requirements.txt
```

Download a web driver:

SeleniumBase can download a web driver to the [seleniumbase/drivers](https://github.com/seleniumbase/SeleniumBase/tree/master/seleniumbase/drivers) folder with the ``install`` command:
```
seleniumbase install chromedriver
```
* (You need a different web driver for each web browser you want to run automation on: ``chromedriver`` for Chrome, ``edgedriver`` for Edge, ``geckodriver`` for Firefox, ``operadriver`` for Opera, and ``iedriver`` for Internet Explorer.)

### How to trigger UI test

Run a test on Chrome:

```sh
pytest test/login_test.py --browser=chrome
```
* (Chrome is the default browser if not specified with ``--browser``)

Run a test on Chrome in headless mode:

```sh
pytest test/login_test.py --browser=chrome --headless
```

Use Demo Mode to help you see what tests are asserting.

If the example test is moving too fast for your eyes, you can run it in Demo Mode by adding --demo_mode on the command line, which pauses the browser briefly between actions, highlights page elements being acted on, and lets you know what test assertions are happening in real time:

```sh
pytest test/login_test.py --browser=chrome --headless --demo_mode
```

### Report

To generate the html report after the execution, use the following command

```sh
pytest test/shopping_test.py --browser=chrome --html=report.html
```

![enter image description here](https://i.ibb.co/N6Rsqx4/Screenshot-2019-05-09-at-10-24-53.png)