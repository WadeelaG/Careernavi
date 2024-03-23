import os
import openai
import json

class CoverLetterGenerate:
    def __init__(self, applicant_name, job_title, company_name, phone_number, email, experience):
        self.applicant_name = applicant_name
        self.job_title = job_title
        self.company_name = company_name
        self.phone_number = phone_number
        self.email = email
        self.experience = experience
        
        # Read the API key from the config file
        with open('config.json', 'r') as f:
            self.config = json.load(f)
        openai.api_key = self.config['api-key']

    def generate_cover_letter(self):
        job_ad = f"{self.job_title} at {self.company_name}"
        additional_prompt_options = self.config['additional_prompt_options']
        content = (
            f"This is the content of my resume: {self.experience}\n"
            f"Write a cover letter for the following job advert: {job_ad}\n"
            f"{additional_prompt_options}\n\n"
            f"This is name and phone number: {self.applicant_name} {self.phone_number}\n"
            f"This is email: {self.email}"
        )
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": content}]
        )
        return completion.choices[0].message.content

# # Example usage
# applicant_name = "John Doe"
# job_title = "Data Scientist"
# company_name = "Innovative Tech Inc"
# phone_number = "123-456-7890"
# email = "john.doe@example.com"
# experience = "I have five years of experience in data analysis."

# cover_letter_generator = CoverLetterGenerate1(applicant_name, job_title, company_name, phone_number, email, experience)
# cover_letter = cover_letter_generator.generate_cover_letter()
# print(cover_letter)
