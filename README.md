# **PokeBerryStatsAPI**

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-3918/)
[![Django 4.2](https://img.shields.io/badge/Django-4.2-blue.svg)](https://www.djangoproject.com/download/4.2.7/tarball/)
[![Requirements Status](https://img.shields.io/badge/requirements-blue.svg)](https://github.com/valchuferr13/PokeBerryStatsAPI/blob/main/requirements.txt)

## Introduction

A Django-based REST API for aggregating and analyzing statistics of Berries from the Pokémon universe. Utilizes external Pokémon data sources to provide detailed stats including growth times, frequency, and more. Features Docker containerization, caching for enhanced performance, and a histogram visualization endpoint using Matplotlib. Developed with Python and tested with pytest for reliability and efficiency. Open for contributions and further development.

## Getting Started

### Prerequisites
Before you jump in, make sure you've got:
- A virtual environment (recommended, but not mandatory) to keep the project's dependencies in check.
- Docker installed. Grab it from the [official Docker website.](https://www.docker.com/products/docker-desktop)

#### Step 1: Set Up Your Environment
1. Clone or download the API repository from [here](https://github.com/valchuferr13/PokeBerryStatsAPI).

    ```bash
    git clone [URL_DEL_REPOSITORIO]
    cd [NOMBRE_DEL_DIRECTORIO]
    ```

2. Head to the project's root folder in your terminal.

3. In the root directory of the project, create a .env file. This file should be structured according to the guidelines provided in the .env.example file. Ensure all necessary environment variables are properly set as the example.

4. Optional: Create and activate a virtual environment for the project:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

#### Step 2: Build and Run Docker
1. In the project root, execute the following command:
   ```bash
   docker-compose build --no-cache
   ```

2. Get the container up and running:
   ```bash
   docker-compose up
   ```
3. Confirm the application is running properly by visiting http://localhost:8000 in your web browser.


#### Step 3: Unit Testing
Basic unit tests are included to verify the correct functionality of the API. Execute these tests using:
```bash
pytest tests.py
```

The tests will run and display results in the terminal. Ensure that all tests pass successfully.
