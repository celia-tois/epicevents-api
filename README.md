# Epic Events - API

---

Epic Events is a Customer Relationship Management (CRM) software allowing the users to perform certain or all CRUD operations depending of their role.

## How to install the project

1. Open the Terminal
2. Clone the repository:

```
$ git clone https://github.com/CeliaTois/CeliaTOIS_12_27122022.git
```

3. Go to the project folder:

```
$ cd ../path/to/the/file
```

4. Create the **virtual environment**:

```
python3 -m venv env
```

5. Activate the **virtual environment**:
   - on macOS and Linux:
     ```
     source env/bin/activate
     ```
   - on windows:
     ```
     env/Scripts/activate
     ```
6. Install the packages:

```
$ pip install -r requirements.txt
```

7. Go the app folder:

```
$ cd epicevents
```

8. Create the database:

```
$ python manage.py migrate
```

## How to run the app

1. Open the Terminal
2. Go to the project folder:

```
$ cd ../path/to/the/file
```

3. Activate the virtual environment
4. Run the command:

```
$ python manage.py runserver
```

5. Open the link written in your terminal or copy/paste it in your browser or in POSTMAN: http://127.0.0.1:8000/
