from bs4 import BeautifulSoup
from get_details import GetDetails

get_details = GetDetails()

print('The readen resume:', end='\n\n')
get_details.get_summery()
get_details.get_education()
get_details.get_job_experience()
get_details.get_certificates()
get_details.get_technical_skills()
get_details.get_languages()