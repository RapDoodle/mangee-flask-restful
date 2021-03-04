# Mangee Flask-RESTful
Mangee Flask-RESTful is a framework designed to simplify the process of building scalable Flask applications.

# Getting Started

- Clone the repository

  ```shell
  git clone https://github.com/RapDoodle/mangee-flask-restful.git
  ```

- Install python (Ubuntu)

  ```bash
  sudo add-apt-repository ppa:jonathonf/python-3.8
  ```

  For other Linux distribution or other operating system, just Google it ;)

- Install required Python packages

  ```bash
  pip3 install -r requirements.txt
  ```

  Please be noted that some dependencies may not be installed on Debian and Ubuntu. If an error occurred while installing `bcrypt`, run the following command

  ```bash
  sudo apt-get install build-essential libffi-dev python-dev
  ```

- Install MySQL (Ubuntu)

  ```bash
  sudo apt-get update
  sudo apt-get install mysql-server
  ```

- Configure MySQL (Ubuntu)

  ```bash
  sudo mysql_secure_installation utility
  ```

  For more information, please Google it

- Start MySQL

  ```bash
  sudo systemctl start mysql
  ```

# Contributors
- Bohui WU (Bowen)

# License
The project is licensed under the GNU General Public License v3. To obtain a license for commercial use, please contact bowenbhwu#gmail.com (replace # with @)

# Copyright
Copyright (c) 2021.