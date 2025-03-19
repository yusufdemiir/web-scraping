from bs4 import BeautifulSoup

class GetDetails:

    def get_summery(self):
        with open('index.html', 'r') as html_file:
            content = html_file.read()
            soup = BeautifulSoup(content, 'lxml')
            summery = soup.find_all('div', id = 'summery')
            for sum in summery:
                sum_name = sum.p.text  
                print('Summery:')
                print(sum_name)          


    def get_education(self):
        with open('index.html', 'r') as html_file:
            content = html_file.read()
            soup = BeautifulSoup(content, 'lxml')

            education = soup.find_all('div', id = 'education')
            for edu in education:
                education_name = edu.ul.text
                print('Education:')
                print(education_name)

    def get_job_experience(self):
        with open('index.html', 'r') as html_file:
            content = html_file.read()
            soup = BeautifulSoup(content, 'lxml')

            experiences = soup.find_all('div', id = 'job-experince')
            for experience in experiences:
                experince_name = experience.ul.text
                print('Job Experience:')
                print(experince_name)
    
    def get_certificates(self):
        with open('index.html', 'r') as html_file:
            content = html_file.read()
            soup = BeautifulSoup(content, 'lxml')

            certificates = soup.find_all('div', id = 'certificates')
            for certificate in certificates:
                certificate_name = certificate.ul.text
                print('Certificates:')
                print(certificate_name)

    def get_technical_skills(self):
        with open('index.html', 'r') as html_file:
            content = html_file.read()

            soup = BeautifulSoup(content, 'lxml')

            technical_skills = soup.find_all('div', id = 'technical-skills')
            for skill in technical_skills:
                skill_name = skill.ul.text
                print('Technical Skills:')
                print(skill_name)
        
    def get_languages(self):
        with open('index.html', 'r') as html_file:
            content = html_file.read()
            soup = BeautifulSoup(content, 'lxml')

            languages = soup.find_all('div', id = 'languages')
            for language in languages:
                language_name = language.ul.text
                print('Languages:')
                print(language_name)