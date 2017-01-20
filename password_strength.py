import re
import string
import getpass

# prohibition of words found in a password blacklist
blacklist = [
    'secret',
    'password'
]
# prohibition of words found in the user's personal information
first_name = "Opanas"
last_name = "Kukuev"
# prohibition of use of company name or an abbreviation
company = "Company"
# prohibition of passwords that match the format of calendar dates, license plate numbers, telephone numbers, or other common numbers
good_password_length = 8
great_password_length = 12

def look_special_numbers(password):
    counts = 0
    re_phone_number = re.search(".?\d.?.?\d{3}.?.?\d{3}.?\d{2}.?\d{2}", password)
    re_date = re.search("[0-3]\d.?[0-1]\d.?(\d{4}|\d{2})", password)
    re_car_number = re.search("[а-я]\d{3}[а-я]{2}(\d{2,3})?", password)
    if re_phone_number.group(0):
        counts += 1
    if re_date.group(0):
        counts += 1
    if re_car_number.group(0):
        counts += 1
    return counts
    
def check_in_blacklist(password):
    """Check password in blacklist
    """
    password_in_blacklist = False
    if password in blacklist:
        password_in_blacklist = True
        
    # if blacklist in file
    '''
    blacklist_file_way = 'password_blacklist'
    password_in_blacklist = False
    with open(blacklist_file_way) as blacklist_file:
        if password in blacklist_file.read().split('\n'):
            password_in_blacklist = True
    '''
    return password_in_blacklist


def get_password_strength(password):
    strength = 1
    try:
        intpass = int(password)
        if str(intpass) == password:
            return 1
    except:
        pass
    if any([ch.isupper() for ch in password]):
        strength += 1 # 2
    if any([ch.islower() for ch in password]):
        strength += 1 # 3
    if any([ch.isdigit() for ch in password]):
        strength += 1 # 4
    if any([ch for ch in password if ch in string.punctuation]):
        strength += 1 # 5
        
    if len(password) > good_password_length:
        strength += 1 # 6
        if len(password) > great_password_length:
            strength += 1 # 7
    if not check_in_blacklist(password):
        strength += 1 # 8
        
    if re.search("[1-9]", password).group(0):
        strength += 2 - look_special_numbers(password) # 7 - 10
        
    if first_name.lower() in password.lower() or last_name.lower() in password.lower() or company.lower() in password.lower():
        strength = int(strength / 3)
        
    
    return strength
        


if __name__ == '__main__':
    password = getpass.getpass()
    strength = get_password_strength(password)
    print(strength)
