import openai
import json

class ResumeGenerate:
    def __init__(self, fullname, phoneNumber, emailAddress, address, city, state, zipCode, objective, education, experience, technicalSkills, softSkills, certifications, projects, languages, additionalInformation, linkdinprofile, professionalSummary):
        self.fullname = fullname
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.objective = objective
        self.education = education
        self.experience = experience
        self.technicalSkills = technicalSkills
        self.softSkills = softSkills
        self.certifications = certifications
        self.projects = projects
        self.languages = languages
        self.additionalInformation = additionalInformation
        self.linkdinprofile = linkdinprofile
        self.professionalSummary = professionalSummary
        
        # Load API key from a config file
        with open('config.json', 'r') as f:
            self.config = json.load(f)
        openai.api_key = self.config['api-key']

    def generate_resume(self):
        """
        Generates a detailed and formatted resume based on the provided information using GPT-3.5 Turbo.
        """
        content = (
            "Generate a Europass CV Pattter for this given info"
            "Generate a detailed and professional resume based on the following given information.Please make good detailed, extensive and professional resume.Based on this information, generate a detailed and professional resume starts with name and ends with linkdin profile link:\n\n"
            f"Full Name: {self.fullname}\n"
            f"Contact Information: Phone: {self.phoneNumber}, Email: {self.emailAddress}, "
            f"Address: {self.address}, City: {self.city}, State: {self.state}, Zip Code: {self.zipCode}\n\n"
            f"Objective: {self.objective}\n\n"
            f"Education: {self.education}\n\n"
            f"Experience: {self.experience}\n\n"
            f"Professional Summary: {self.professionalSummary}\n\n"
            f"Skills: Technical Skills: {self.technicalSkills}, Soft Skills: {self.softSkills}\n\n"
            f"Certifications with name,issuign organization and year obrtained so set it according to it: {self.certifications}\n\n"
            f"LinkedIn Profile: {self.linkdinprofile}\n\n"
            f"Projects: {self.projects}\n\n"
            f"Languages and Profcieny: {self.languages}\n\n"
            f"Additional Information: {self.additionalInformation}\n\n"
            "Education have degree name , major , university name, gradudation year,courses all togther so adjust it accordign to it "
            "Experience have position title,company name,location,startdate,enddate responsibilties so set it according to it,"
            "Certifications have certificationa name, issuing organization and year obtained so set it according to it."
            "Please generate a detailed and professional resume, highlighting the key attributes and accomplishments of the applicant."
            "Dont add anything in start or end just start it with name and end it with lindin profile name "
            f"Please generate a detailed and explained resume with more detailed jsut add anything relevant to make it more impactfull and dont add summary or anything in the end of resume just add linkdinprofile link in the end and in start after perosnal info add objectives and related info that will be needed in resume"
        )

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": content}]
        )
        return completion.choices[0].message.content
