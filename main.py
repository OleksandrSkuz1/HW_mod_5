# import re

# def find_all_phones(text):
#     pattern = r'\+\d{3}\(\d{2}\)\d{3}-\d{1,2}-\d{2,3}'
#     phones = re.findall(pattern, text)
#     return phones

# text = "Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787"
# phones = find_all_phones(text)
# for phone in phones:

#     print(phone)


import re

def find_all_phones(text):
    
    result = re.findall(r"\+380\(\d{2}\)\d{3}-\d{1,2}-\d{2,3}", text)
    
    return result
    
text = "Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787"

result = find_all_phones(text)

for phone in result:
    if len(phone) == 17:
        

        print(phone)


                 
                        
                        