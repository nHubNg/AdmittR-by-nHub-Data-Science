# AdmittR Web Application

AdmittR is a Django-based web application that allows users to fill out an admission form and view the admission result based on selected course, scores, age, and first choice.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Admin Panel](#admin-panel)
- [License](#license)

## Features

- Fill out an admission form with the following fields:

  - Course selection from a list of available courses.
  - Subject selection (Choose subjects based on the selected course).
  - JAMB (Joint Admissions and Matriculations Board) score input.
  - WAEC (West African Examinations Council) aggregate score input.
  - Post UTME (Unified Tertiary Matriculation Examination) score input.
  - Age selection.
  - First choice (Yes or No) selection.
- Dynamically update subject choices based on the selected course.
- Submit the form and view the admission result.

## Installation

1. Clone this repository to your local machine:

   ```git
   git clone https://github.com/yourusername/AdmittR.git
   ```
2. Navigate to the project directory:

   ```git
   cd AdmittR_Project
   ```
3. Create a virtual environment (optional but recommended):

   ```git
   python -m venv venv
   ```
4. Activate the virtual environment:

- On Windows:

  ```git
  venv\Scripts\activate
  ```
- On macOS and Linux:

  ```git
  source venv/bin/activate
  ```

5. Install the required dependencies:
   ```git
   pip install -r requirements.txt
   ```


## Usage

1. Start the Django development server:

   ```bash
   python manage.py runserver
   ```
2. Access the application in your web browser at `http://localhost:8000/admission-form/`.
3. Fill out the admission form by selecting a course, subjects, entering scores, age, and first choice.
4. Submit the form to view the admission result.

## Admin Panel

- You can access the Django admin panel at `http://localhost:8000/admin/`.
- Use the superuser account created during the setup process to log in.
- In the admin panel, you can manage courses and subjects available for selection in the admission form.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
