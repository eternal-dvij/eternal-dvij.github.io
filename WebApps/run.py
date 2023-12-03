from flask import Flask, render_template, request, jsonify,json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('WebApps/get_assessment', methods=['POST'])
def get_assessment():
    data = json.loads(request.data)
    app_type = data['app_type']
    selected_testing = data['selected_testing']

    # Define testing requirements based on the application type
    requirements = {
        "Web Applications": ["Functional Testing", "Usability Testing", "Performance Testing", "Security Testing", "Compatibility Testing", "Cross-browser Testing"],
        "Mobile Applications": ["Functional Testing", "Usability Testing", "Performance Testing", "Security Testing", "Compatibility Testing", "Mobile App Automation Testing"],
        # Add more application types and their testing requirements as needed
    }

    # Check if the selected application type is in the requirements dictionary
    if app_type in requirements:
        mandatory_testing = requirements[app_type]
        print(selected_testing)
        print(mandatory_testing)

        missing_testing = list(set(mandatory_testing) - set(selected_testing))
        print(missing_testing)
        # overdone_testing = list(set(selected_testing) - set(mandatory_testing))

        response = f"For {app_type}, mandatory testing includes: {', '.join(mandatory_testing)}\n"

        if missing_testing:
            response += f"\nYou are missing and need to focus on following: {', '.join(missing_testing)}\n"
        # if overdone_testing:
        #     response += f"You have overdone the following: {', '.join(overdone_testing)}\n"

        return jsonify({'response': response})
    else:
        return jsonify({'response': "Invalid application type. Please select a valid application type."})

if __name__ == '__main__':
    app.run(debug=True)




'''project_folder/
│
├── templates/
│   └── index.html
│
└── run.py
'''
