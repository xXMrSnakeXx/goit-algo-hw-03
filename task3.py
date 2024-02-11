import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11    ",
]

def normalize_phone(phone_number):
    listNumbers = []
    for number in phone_number:
      patern = r"\+{0,1}[\d]"
      formatedPhone =''.join(re.findall(patern, number))
      if len(formatedPhone) == 12:
        listNumbers.append('+' + formatedPhone)
      elif len(formatedPhone) == 10:
         listNumbers.append('+38' + formatedPhone)
      elif 10 < len(formatedPhone) > 13:
         print("The number format is not valid")  
      else:
          listNumbers.append(formatedPhone)    
    print(listNumbers) 


normalize_phone(raw_numbers)    