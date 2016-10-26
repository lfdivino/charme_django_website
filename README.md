# CHARMÉ todo dia

Website and blog

Develop by Luiz Felipe do Divino <lf.divino@gmail.com>

Template develop by Freehtml5.co

## How to develop?

1. Clone the repository
2. create a virtualenv with python 3.5
3. Active the virtualenv
4. Install the dependencies
5. Configure the instance with .env
6. Execute the tests

```console
git clone https://github.com/lfdivino/charme_django_website.git charme
cd charme
python -m venv .charme
source .charme/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```



