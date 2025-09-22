### Hexlet tests and linter status:
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Viacheslav161_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Viacheslav161_python-project-50)
[![Actions Status](https://github.com/Viacheslav161/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Viacheslav161/python-project-83/actions)
# Page Analyzer
****

## Project Description

Page Analyzer is a website that analyzes specified pages for SEO readiness, similar to PageSpeed Insights.
****


## Installation

### Clone the repository:

```
git clone git@github.com:lyovaparsyan94/python-project-83.git
```

```
cd python-project-83
```

### To use this application, you need to configure the .env file.

After cloning the repository, rename the .env_example file to .env. Inside the file, you will find the SECRET_KEY and
DATABASE_URL variables. Replace their values with your own.
****

### Next, use the command below to install the required dependencies and generate the database tables.

```
make build
```

### Start the application with the following command:

```
make start
```
