Skip to content

Sign up

Frenzy-inxide

/

Frenzy-inxide

Public

Code

Pull requests

Actions

Projects

Security

Insights

Shivamxwd/shivam.py

@shivam-xwd

Shivam - xwd Create shivam.py

 1 contributor

26 lines (14 sloc)  299 Bytes


import os, platform

try:

    import requests

except:

    os.system('pip install requests')

    os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from VIP64 import login

    login()

elif bit == '32bit':

    from prince import login

    login()

Footer

© 2023 GitHub, Inc.

Footer navigation

Terms

Privacy

Security

Status

Docs

Contact GitHub

Pricing

API

Training

Blog

About

Frenzy-inxide/Frenzy.py at main · Frenzy-inxide/Frenzy-inxide · GitHub
