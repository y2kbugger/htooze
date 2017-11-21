===========
htooze
===========

venvs are managed by the new standard pipenv to manage virtual environments
rather than virtualenvwrapper. Read more here:

http://docs.python-guide.org/en/latest/dev/virtualenvs/
https://docs.pipenv.org/

Install pipenv using::

    pip install pipenv


Then clone the repo and install package + deps + dev-deps::

    $ git clone git@bitbucket.org:y2kbugger/htooze.git
    $ cd htooze
    $ pipenv install --dev

The pytest suite can then be ran via::

    $ pipenv run pytest

or::

    $ pipenv shell
    (htooze) $ pytest

    
