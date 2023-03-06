import requests

POKI_API_URL = 'https://pokeapi.co/api/v2/pokemon/454'
POKI_API_SEARCH_URL = f'{POKI_API_URL}/search'

def main():

    poki = search_poki_names('name')

    return
def search_poki_names(search_term, name=1, ability=1):
    search_term = str(search_term).strip().lower()

    quary_params= {
        'name': name,
        'ability': ability
    }
    print('Searching for pokimon names....', end='')
    resp_msg = requests.get(POKI_API_SEARCH_URL, params=quary_params)

    if resp_msg.ok:
         print('success')
         body_dict = resp_msg.json()
         name_list = body_dict['results']
         names = [j['names'] for j in name_list]


         return names
    else:
         print("failure")
         print("response code: {resp_msg.status_code} ({resp_msg.reason})")
         print("Error: {resp_msg.txt}")

         return
    
def get_random_pokimon():
     return
      
if __name__ == "__main__" :
      main()

