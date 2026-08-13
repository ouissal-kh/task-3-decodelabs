# Task 3 — DecodLabs | Cloud Database Deployment

## 📌 Project Overview

This project demonstrates the deployment and configuration of a managed cloud relational database using **Amazon RDS with MySQL**.

The objective is to provide a reliable and scalable cloud database for storing intern records and validating data persistence through SQL and Python-based access.

---

## 🎯 Project Objectives

The project covers the following objectives:

- Provision a managed relational database using Amazon RDS.
- Configure a MySQL database instance in AWS.
- Create a database named `interns_db`.
- Create an `Interns` table with the required fields.
- Insert dummy records for testing.
- Verify data persistence using SQL queries.
- Connect to the cloud database using MySQL Workbench.
- Connect to the database programmatically using Python.

---

## ☁️ AWS RDS Configuration

| Configuration | Value |
|---|---|
| Cloud Service | Amazon RDS |
| Database Engine | MySQL Community |
| Instance Class | `db.t4g.micro` |
| AWS Region | `eu-north-1` |
| Database | `interns_db` |
| Table | `Interns` |
| Port | `3306` |

---

## 🗄️ Database Structure

The project uses the following table:

### `Interns`

| Column | Data Type | Description |
|---|---|---|
| `Name` | VARCHAR(100) | Intern name |
| `Role` | VARCHAR(100) | Intern role |
| `Email` | VARCHAR(150) | Intern email |

---

## 🧪 Data Testing

Dummy records were inserted into the `Interns` table to verify that data can be stored and retrieved successfully.

The following SQL query was used to validate the stored records:

```sql
USE interns_db;

SELECT * FROM Interns;

The query successfully returned the records stored in the RDS database.

🖥️ MySQL Workbench

The database was successfully accessed using MySQL Workbench.

The connection was configured using:

RDS endpoint
Port 3306
MySQL user admin
SSL/TLS enabled

This confirms successful connectivity between the local SQL client and the AWS RDS database.

🐍 Python Integration

As an additional integration, a Python script named test_rds.py was developed using the mysql-connector-python package.

The script:

Establishes a connection to the AWS RDS MySQL instance.
Selects the interns_db database.
Executes a query against the Interns table.
Retrieves and displays the stored records.
Closes the database connection.

Example query:

SELECT * FROM Interns;

The Python connection was successfully tested against the AWS RDS instance.

📂 Project Structure
task-3-decodelabs/
│
├── images/
│   ├── AWS RDS — Database Available
│   ├── Security Group
│   ├── MySQL Workbench — Successful Connection
│   ├── SHOW DATABASES — interns_db
│   ├── SELECT * FROM Interns — Records
│   └── Python — Connected successfully to AWS RDS
│
├── test_rds.py
├── requirements.txt
├── README.md
└── .gitignore
📸 Project Evidence

The images directory contains screenshots documenting the implementation:

AWS RDS — Database Available
Security Group Configuration
MySQL Workbench — Successful Connection
Database Verification — interns_db
Interns Table — Stored Records
Python — Successful AWS RDS Connection

These screenshots provide visual evidence of the database deployment, configuration, connectivity, and testing.

⚙️ Installation & Requirements

Install the required Python dependency with:

pip install -r requirements.txt

The project uses:

mysql-connector-python
▶️ Running the Python Test

Run the database connection script with:

python test_rds.py

The script should establish a connection to AWS RDS and display the records stored in the Interns table.

🔐 Security

Database credentials and sensitive information are not included in this repository.

The .gitignore file is configured to prevent sensitive local files and environment-specific files from being committed.

✅ Project Status

Status: Completed

The project successfully demonstrates:

☁️ Managed cloud database deployment
🗄️ MySQL database configuration
📋 Interns table creation
🧪 Data insertion and verification
🔌 MySQL Workbench connectivity
🐍 Python database integration
📸 Implementation evidence
📦 GitHub project organization