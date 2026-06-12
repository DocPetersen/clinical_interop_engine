Clinical Data Interoperability Engine
A modular, production-ready data pipeline designed to ingest, validate, transform, and load clinical records into a Snowflake data warehouse.

Project Evolution
This project demonstrates the transition from an exploratory proof-of-concept to a structured, scalable production system.

Initial Prototype (Jupyter Notebook): Click here to view the exploratory code

Production Implementation: Modularized architecture located in the src/ directory.

Architecture
The pipeline follows a clean, decoupled design to ensure maintainability and scalability:

main.py: Orchestrator that manages the pipeline lifecycle.

src/validator.py: Ensures data integrity and schema compliance before processing.

src/processor.py: Efficient batch transformation and automated error logging.

src/db_loader.py: Secure interface for Snowflake warehouse interactions.

Engineering Highlights
Observability: Replaced standard prints with the Python logging library for production-grade monitoring.

Data Reliability: Implemented custom validation rules and automated rejection logging for non-compliant records.

Security: Designed with environment variables to prevent hardcoding of sensitive credentials.

Maintainability: Utilized type hinting and modular design to facilitate collaborative development and unit testing.

Getting Started
Prerequisites
Python 3.10 or higher

pip

Installation
If you have a requirements.txt file, run:

Bash
pip install -r requirements.txt
Otherwise, install the dependencies manually:

Bash
pip install pandas snowflake-connector-python python-dotenv
Configuration
Create a .env file in the root directory to manage your environment variables securely:

Bash
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_WAREHOUSE=your_warehouse
SNOWFLAKE_DATABASE=your_database
SNOWFLAKE_SCHEMA=your_schema
Note: Ensure your .env file is listed in your .gitignore to prevent sensitive credentials from being committed to source control.

Execution
Run the pipeline from the root directory:

Bash
python main.py
Contributing
Contributions are welcome! Please follow these steps:

Fork the project.

Create your feature branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.
