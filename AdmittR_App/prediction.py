import pandas as pd
import pickle


# Load the pre-trained model
with open('model.pkl', 'rb') as file:
    hybrid_loaded = pickle.load(file)

def predict(student):
    # Mapping of course names to numerical values
    course_data = {
        'Accounting': 0,
        'Agriculture': 1,
        'Banking and Finance': 2,
        'Business Administration': 3,
        'Chemistry': 4,
        'Computer Science': 5,
        'Economics': 6,
        'Electrical and Electronics Engineering': 7,
        'English': 8,
        'French': 9,
        'Human Kinetics': 10,
        'Law': 11,
        'Linguistics and Nigerian Languages': 12,
        'Mass Communication': 13,
        'Mathematics': 14,
        'Mechanical Engineering': 15,
        'Medicine and Surgery': 16,
        'Microbiology': 17,
        'Petroleum Engineering': 18,
        'Psychology': 19,
        'Science Education': 20,
        'Sociology': 21
    }
    
    # Map the course name to its corresponding numerical value
    if student['Course'][0] in course_data.keys():
        student['Course'][0] = course_data[student['Course'][0]]
    
    # Convert 'First_Choice' to 1 for 'Yes' and 0 for 'No'
    if student['First_Choice'][0] == 'Yes':
        student['First_Choice'][0] = 1
    elif student['First_Choice'][0] == 'No':
        student['First_Choice'][0] = 0
    
    # Extract the subject combo and remove it from the student data
    subject_combo = student['Subject_Combo']
    del student['Subject_Combo']
    
    # Create a DataFrame from the student data
    student_df = pd.DataFrame(student)
    
    # Make predictions using the pre-trained model
    pred = hybrid_loaded.predict_proba(student_df)
    result = [round(pred[0][1] * 100, 2), hybrid_loaded.predict(student_df)[0]]
    
    # Create a list of subjects and their criteria
    subjects = [
                    {'course': 'Accounting', 'cat': 2, 'main': ['MTH', 'ACC'], 'main2': ['ECO', 'COM', 'GOV']},
                    {'course': 'Agriculture', 'cat': 2, 'main': ['CHM'], 'main2': ['PHY', 'MTH', 'AGR', 'BIO']},
                    {'course': 'Banking and Finance', 'cat': 2, 'main': ['ECO', 'GOV'], 'main2': ['COM', 'ACC']},
                    {'course': 'Business Administration', 'cat': 2, 'main': ['ECO', 'GOV'], 'main2': ['COM', 'ACC']},
                    {'course': 'Chemistry', 'cat': 2, 'main': ['MTH', 'CHM'], 'main2': ['PHY', 'BIO']},
                    {'course': 'Computer Science', 'cat': 1, 'main': ['MTH', 'PHY', 'CHM']},
                    {'course': 'Economics', 'cat': 2, 'main': ['MTH', 'ECO'], 'main2': ['COM', 'ACC']},
                    {'course': 'Electrical and Electronics Engineering', 'cat': 1, 'main': ['MTH', 'PHY', 'CHM']},
                    {'course': 'English', 'cat': 2, 'main': ['LIT', 'GOV'], 'main2': ['ECO', 'CRS', 'IRS']},
                    {'course': 'French', 'cat': 2, 'main': ['FRE', 'LIT'], 'main2': ['GOV', 'CRS', 'IRS']},
                    {'course': 'Human Kinetics', 'cat': 1, 'main': ['PHY', 'CHM', 'BIO']},
                    {'course': 'Law', 'cat': 2, 'main': ['LIT', 'GOV'], 'main2': ['IRS', 'CRS']},
                    {'course': 'Lingustics and Nigerian Languages', 'cat': 3, 'main': ['LIT'], 'main2': ['CRS', 'IRS'], 'main3': ['YOR', 'IGB', 'HAU']},
                    {'course': 'Mass Communication', 'cat': 2, 'main': ['GOV', 'LIT'], 'main2': ['ECO', 'CRS', 'IRS']},
                    {'course': 'Mathematics', 'cat': 2, 'main': ['MTH', 'PHY'], 'main2': ['CHM', 'BIO']},
                    {'course': 'Mechanical Engineering', 'cat': 1, 'main': ['MTH', 'PHY', 'CHM']},
                    {'course': 'Medicine and Surgery', 'cat': 1, 'main': ['PHY', 'CHM', 'BIO']},
                    {'course': 'Microbiology', 'cat': 1, 'main': ['PHY', 'CHM', 'BIO']},
                    {'course': 'Petroleum Engineering', 'cat': 1, 'main': ['MTH', 'PHY', 'CHM']},
                    {'course': 'Psychology', 'cat': 2, 'main': ['GOV'], 'main2': ['CRS', 'IRS', 'ECO']},
                    {'course': 'Science Education', 'cat': 1, 'main': ['PHY', 'CHM', 'BIO']},
                    {'course': 'Sociology', 'cat': 2, 'main': ['GOV', 'LIT'], 'main2': ['CRS', 'IRS']}
    ]
    
    # Initialize a list to store admission details
    admission_details = []
    
    # Check admission criteria for each course
    for subject in subjects:
        if subject['cat'] == 1:
            if sorted(subject['main']) == sorted(subject_combo):
                student_df.loc[0, 'Course'] = course_data[subject['course']]
                if hybrid_loaded.predict(student_df)[0] == 'Yes':
                    admission_details.append({
                        'Course': subject['course'],
                        'Admission': 'Yes',
                        'Probability': round(hybrid_loaded.predict_proba(student_df)[0][1] * 100, 2)
                    })
        
        elif subject['cat'] == 2:
            temp_list = [val for val in subject_combo if val not in subject['main']]
            if len(subject['main']) == 2:
                if len(temp_list) == 1:
                    if temp_list[0] in subject['main2']:
                        student_df.loc[0, 'Course'] = course_data[subject['course']]
                        if hybrid_loaded.predict(student_df)[0] == 'Yes':
                            admission_details.append({
                                'Course': subject['course'],
                                'Admission': 'Yes',
                                'Probability': round(hybrid_loaded.predict_proba(student_df)[0][1] * 100, 2)
                            })
        
            elif len(subject['main']) == 1:
                if len(temp_list) == 2:
                    if temp_list[0] and temp_list[1] in subject['main2']:
                        student_df.loc[0, 'Course'] = course_data[subject['course']]
                        if hybrid_loaded.predict(student_df)[0] == 'Yes':
                            admission_details.append({
                                'Course': subject['course'],
                                'Admission': 'Yes',
                                'Probability': round(hybrid_loaded.predict_proba(student_df)[0][1] * 100, 2)
                            })
    
    # Create a dictionary containing the main admission result, probability, and admission details
    results = {
        'Admission': result[1],
        'Probability': result[0],
        'AdmissionDetails': admission_details
    }
    
    return results
