from pastebin_api import post_new_paste
from poke_api import search_poki_names
import sys

def main():
    search_term = get_search_term()
    name_list = search_poki_names(search_term)
    if name_list:
        title, body_text = get_paste_content()
        paste_url = post_new_paste (title, body_text)
        print(f'URL of  poki names paste: {paste_url}')

def get_search_term():
    num_params = len(sys.argv) - 1
    if num_params > 0:
        search_term = sys.argv[1]
        return search_term
    else:
        print('Error: Missing search term')
        sys.exit(1)

def get_paste_content(name_list, search_term):

    title = f'Pokimon Containing the Term "{search_term}"'

    divider = '=' *20
    body_text = ''

    for name in name_list:
        body_text += name + '\n'
        body_text += divider + '\n'

    return title, body_text

if __name__ == "__main__":
    main()        
         