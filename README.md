# What is this?

It is a simple project where human resources specialists from different fields publish their open positions on a single platform and this is a simple project where these positions are shown to the relevant candidates.

There are 2 Different User types
- Job seeker
- Employer

The job seeker can list private postings by entering his own custom filter.

The employer can open a job posting, see the applicants and manage the posting.

## Installation

- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirement files or you can install all files
directly via requirements.txt

```bash
pip install -r requirements.txt
```

- After the project is installed, the following command should be run in order to save the relevant locations in the database.
```bash
python manage.py load_province
```

## Usage

- Install the required packages
- Download the repository
- Create an .env file and fill it in. Example .env file shared as exp.env
- Run command: ```python manage.py load_province```
- Run server


