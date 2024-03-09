from typing import Tuple
import statistics as st
from pathlib import Path
import os



def get_salaries(salaries_file_name: str):
    try:
        path = Path(__file__)
        path = path.with_name(salaries_file_name)

        if os.stat(path.absolute()).st_size == 0:
            print(f'The file "{path.absolute()}" is empty')
            return []
            
        salaries = path.read_text('utf-8')
        return [int(line.split(',')[1]) for line in 
                [el.strip() for el in salaries.split('\n') if el.strip()]]
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
        print('Something wrong with data format, there should be - "Alex Korp,3000"')



def total_salary(path: str) -> Tuple[int, int]:
    salaries = get_salaries(path)

    if salaries:
        return sum(salaries), st.mean(salaries)
    
    return 0, 0



total, average = total_salary("salaries.txt")
print(f"Total amount of salaries: {total}\nAverage salary: {average}")
