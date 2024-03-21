from flask import Flask, request, render_template, redirect, url_for, session
from cover_letter import CoverLetterGenerate

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set to a unique secret value for session management

@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/service.html')
def service():
    return render_template('service.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/login-form.html')
def login():
    return render_template('login-form.html')

@app.route('/Register-form.html')
def Register():
    return render_template('Register-form.html')

@app.route('/project.html')
def project():
    return render_template('project.html')

@app.route('/resume-form.html')
def resume_form():
    return render_template('resume-form.html')

@app.route('/coverletter-form.html')
def coverletter_form():
    return render_template('coverletter-form.html')

@app.route('/blog-single.html')
def blog_single():
    return render_template('blog-single.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/cover_letter', methods=['GET', 'POST'])
def cover_letter():
    if request.method == 'POST':
        # Extract form data
        applicant_name = f"{request.form['firstName']} {request.form['lastName']}"
        job_title = request.form['jobTitle']
        company_name = request.form['companyName']
        phone_number = request.form['phoneNumber']
        email_address = request.form['emailAddress']
        house_address = request.form['houseAddress']
        region = request.form['region']
        additional_experience = request.form['additionalExperience']
        
        print(f"Received form data: {request.form}")  # Print the form data to the console

        # Create an instance of your cover letter generator
        generator = CoverLetterGenerate(applicant_name, job_title, company_name, phone_number, email_address, house_address, region, additional_experience)
        cover_letter = generator.generate_cover_letter()

        # Store the cover letter in the session
        session['cover_letter'] = cover_letter

        # Redirect to the cover_letter_output route
        return redirect(url_for('cover_letter_output'))

    else:
        # If the method is GET, show the form to the user
        return render_template('coverletter-form.html')

@app.route('/cover_letter_output', methods=['GET'])
def cover_letter_output():
    # Retrieve the generated cover letter from the session
    cover_letter = session.get('cover_letter', None)
    return render_template('coverletter-output.html', cover_letter=cover_letter)

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
