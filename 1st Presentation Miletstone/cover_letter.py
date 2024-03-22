from transformers import GPT2LMHeadModel, GPT2Tokenizer

class CoverLetterGenerate:
    def __init__(self, applicant_name, job_title, company_name, phone_number, email, address, region, additional_experience):
        self.applicant_name = applicant_name
        self.job_title = job_title
        self.company_name = company_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.region = region
        self.additional_experience = additional_experience
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")

    def generate_cover_letter(self):
        prompt = (
            f"Dear Hiring Manager at {self.company_name},\n\n"
            f"My name is {self.applicant_name}, and I am excited to apply for the {self.job_title} position. "
            f"I believe that my experience and passion make me a perfect fit for the role. "
            f"I reside in {self.region}, and my detailed contact information is as follows:\n"
            f"Phone: {self.phone_number}"
            f"Email: {self.email}"
            f"Address: {self.address}"
            f"Throughout my career, {self.additional_experience}. "
            f"I am looking forward to the opportunity to further discuss how I can contribute to the success of {self.company_name}.\n\n"
        )

        
        encoding = self.tokenizer(prompt, return_tensors="pt")
        input_ids = encoding["input_ids"]
        attention_mask = encoding["attention_mask"]

        output = self.model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_length=800,
            pad_token_id=self.tokenizer.eos_token_id,
            num_beams=5,
            no_repeat_ngram_size=2,
            top_k=50,
            top_p=0.95,
            temperature=0.7,
            early_stopping=False
        )

        cover_letter = self.tokenizer.decode(output[0], skip_special_tokens=True)

        closing_statement = (
            "Thank you for considering my application. I look forward to the possibility of contributing to the innovative work at {company_name} and am eager to discuss how my skills and experiences align with the goals of your team.\n\n"
            "Sincerely,\n"
            "{applicant_name}\n"
            "{email}\n"
            "{phone_number}"
        ).format(company_name=self.company_name, applicant_name=self.applicant_name,email=self.email,phone_number=self.phone_number)

        complete_cover_letter = cover_letter + closing_statement
        return complete_cover_letter


# applicant_name = "John Doe"
# job_title = "Data Scientist"
# company_name = "Innovative Tech Inc"
# phone_number = "123-456-7890"
# email = "john.doe@example.com"
# address = "1234 Main Street"
# region = "Anytown"
# additional_experience = "I have five years of experience in data analysis."

# cover_letter_generator = CoverLetterGenerate(applicant_name, job_title, company_name, phone_number, email, address, region, additional_experience)
# cover_letter = cover_letter_generator.generate_cover_letter()

# print(cover_letter)
