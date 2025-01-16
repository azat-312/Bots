CREATE_TABLE_registered = """
    CREATE TABLE IF NOT EXISTS registered (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    age TEXT,
    email TEXT,
    city TEXT,
    photo TEXT
    )
"""

INSERT_registered_query = """
    INSERT INTO registered (fullname, age, email, city, photo)
    VALUES (?, ?, ?, ?, ?)
"""

CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    size TEXT,
    category TEXT,
    price TEXT,
    photo TEXT
    )
"""

INSERT_store_query = """
    INSERT INTO registered (name, size, category, price, photo)
    VALUES (?, ?, ?, ?, ?)
"""