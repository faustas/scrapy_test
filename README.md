# Scrapy Test project

Just a small test project with the  Scrap scraping framework.

## Prerequisites

You should have installed:

- python3
- venv (Virtual environment tool)
- pip

## Creating a new virtual Python environment

```shell
python3 -m venv env
```

## Activate the environment

```shell
source env/bin/activate
```

## Check which python environment is used

```shell
which python
```

## Leave the python environment

```shell
deactivate
```

## Create the requirements.txt file

```shell script
pip freeze > requirements.txt
``` 

# Install for the project

Activate the environment and install the packages.
```shell script
pip install -r requirements.txt
```

# How to create a completely new Scrapy project

See: https://docs.scrapy.org/en/latest/intro/tutorial.html


The main structure from this project was created by:
```shell script
scrapy startproject scrapy_spider
```

The test spider by:
```shell script
scrapy genspider heise_crawler heise.de
```

Executing the spider:
```shell script
scrapy runspider scrapy_spider/scrapy_spider/spiders/heise_crawler.py  -o output_filename.json -t json
```