from typing import List, Dict
from pathlib import Path
import os



def parse_cat_info(cat_str: str) -> Dict:
    cat_id, name, age = cat_str.split(',')
    return {
        'id': cat_id,
        'name': name,
        'age': age
    }



def get_cats(cats_file_name: str):
    try:
        path = Path(__file__)
        path = path.with_name(cats_file_name)

        if os.stat(path.absolute()).st_size == 0:
            print(f'The file "{path.absolute()}" is empty')
            return []
            
        cats = path.read_text('utf-8')
        return [parse_cat_info(line) for line in 
                [el.strip() for el in cats.split('\n') if el.strip()]]
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
        print('Something wrong with data format, there should be - "60b90c3b13067a15887e1ae4,Simon,12"')



def get_cats_info(path: str) -> List[Dict]:
    cats = get_cats(path)
    return cats if cats else []



cats_info = get_cats_info('cats.txt')
print(cats_info)
