from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class InputData(BaseModel):
    data: List[str]

def check_special_char(ch: str) -> bool:
    return not ch.isalnum()

def alternating_caps(s: str) -> str:
    s = s[::-1]  
    result = ""
    for i, ch in enumerate(s):
        if i % 2 == 0:
            result += ch.upper()
        else:
            result += ch.lower()
    return result

@app.post("/bfhl")
def bfhl(item: InputData):
    item_array = item.data
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    total_sum = 0
    concat_string = ""

    for element in item_array:
        if element.isdigit():
            if int(element) % 2 == 0:
                even_numbers.append(str(element))
            else:
                odd_numbers.append(str(element))
            total_sum += int(element)

        else:
            if element.isalpha():
                upper_elem = element.upper()
                alphabets.append(upper_elem)
                concat_string += element 
            elif check_special_char(element):
                special_characters.append(element)

    concat_string = alternating_caps(concat_string)

    response_dict = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total_sum),
        "concat_string": concat_string
    }

    return response_dict
