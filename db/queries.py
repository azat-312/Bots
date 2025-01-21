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
CREATE_TABLE_products_details = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    category TEXT ,
    infoproduct TEXT
    
    )
"""

INSERT_products_details_query = """
    INSERT INTO registered (productid, category, infoproduct)
    VALUES (?, ?, ?)
"""
CREATE_TABLE_collection = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    collection TEXT

    )
"""

INSERT_collection_query = """
    INSERT INTO registered (productid, collection)
    VALUES (?, ?)
"""