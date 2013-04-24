learnpy
=======
Stub code for teaching python

Installation
------------
1. Install `virtualenvwrapper` with apt
2. Start a new shell
3. Clone the repo: `git clone https://github.com/wearpants/learnpy.git`
4. Create a new virtualenv: `mkvirtualenv learnpy`
5. `cd learnpy`
6. Install packages: `pip install -r requirements.txt`


Editor setup
------------------
Make sure your editor is using spaces, *not* tabs. An indentation size of 4 is standard.

Running tests
-------------
`nosetests --with-coverage`

Update docs
-----------
`make -C doc/ html`
