## Getting up & running

See also [Installing required development tools](https://github.com/commoncode/hinoki/wiki#installing-required-development-tools)

```bash
git clone git@github.com:commoncode/hinoki.git  # Get a copy of the code
cd hinoki
virtualenv env                                  # Create our virtualenv
. env/bin/activate                              # Turn it on
pip install -r requirements.txt                 # Install our python libraries
./manage.py migrate                             # Prepare the database
./manage.py runserver                           # Start the django server
```
🚀
