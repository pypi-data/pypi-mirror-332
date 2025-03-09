# NanoJson library provided by Mohammed Ghanam.

![PyPI - Version](https://img.shields.io/pypi/v/NanoJson?color=blue&label=version)  
![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)  
![Status](https://img.shields.io/badge/status-active-success)  

--------
# ManageDB

**ManageDB** is a powerful and easy-to-use library for managing databases in Python projects. It simplifies database connections, query execution, and data handling with a clean and intuitive interface.

---

## 🚀 Features
- ✅ Support for multiple database types (SQLite, MySQL, PostgreSQL)  
- ✅ Simple SQL query execution  
- ✅ Automatic connection handling  
- ✅ Easy table creation and modification  
- ✅ Efficient data handling using Python  

---

## 📦 Installation
Install via `pip`:  
```bash
pip install ManageDB==0.1


---

🔥 Usage

from managedb import Database

# Connect to a SQLite database
db = Database('mydatabase.db')

# Create a Table
query = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER
)
"""
db.execute(query)

# Insert Data
db.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('John', 30))

# Fetch Data
result = db.fetch_all("SELECT * FROM users")
print(result)

# Update Data
db.execute("UPDATE users SET age = ? WHERE name = ?", (31, 'John'))

# Delete Data
db.execute("DELETE FROM users WHERE name = ?", ('John',))

# Close Connection
db.close()


---


## 🌍 Compatibility

Python: 3.8+

## Databases:

- 1) SQLite3

- 2) DB





---

##🎯 Contribution

- We welcome all contributions! Open an issue or submit a pull request on GitHub.


---

##📄 License

- ManageDB is released under the MIT License.



## For Contact:

- My telegram Account: [@midoghanam](https://t.me/midoghanam)
- My Channel: [@mido_ghanam](https://t.me/mido_ghanam)

## Best Regards ♡