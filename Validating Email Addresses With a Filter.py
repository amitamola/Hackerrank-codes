'''
https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
'''

def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, second = s.split('@')
        website, extension = second.split('.')
        
        username = username.replace('_', '')
        username = username.replace('-', '')
        
        if len(extension)>3:
            return False
        
        elif not website.isalnum():
            return False
        
        elif not username.isalnum():
            return False
        
        else:
            return True
           
    except:
        return False
        
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
