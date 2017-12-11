======
HTooze
======

HyperText ooze aims to be a Cell Based (read: grid) artificial life (alife).
Cell are controlled by automata as well as user input. 

Commands will be issued via a REST API hence HT or HyperText.


Installation
------------

venvs are managed by the new standard pipenv to manage virtual environments
rather than virtualenvwrapper. Read more here:

http://docs.python-guide.org/en/latest/dev/virtualenvs/
https://docs.pipenv.org/

Install pipenv using::

    $ pacman -Syyu python-pipenv

Then clone the repo and install package + deps + dev-deps::

    $ git clone git@bitbucket.org:y2kbugger/HTooze.git
    $ cd HTooze
    $ pipenv install --dev


Testing
-------

The pytest suite can then be ran via::

    $ pipenv run pytest -f

or::

    $ pipenv shell
    (HTooze)$ pytest -f
