from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Any

app = FastAPI()


class InputData(BaseModel):
    data: List[Any]  


def check_special_char(ch: str) -> bool:
    return not str(ch).isalnum()


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
    try:
        if not item.data:
            raise HTTPException(status_code=400, detail="Input 'data' cannot be empty")

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        concat_string = ""

        for element in item.data:
            element = str(element).strip()  
            if element.isdigit():
                if int(element) % 2 == 0:
                    even_numbers.append(element)
                else:
                    odd_numbers.append(element)
                total_sum += int(element)

            elif element.isalpha():
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

    except HTTPException as e:
        # Pass through intentional exceptions (like empty input)
        raise e

    except Exception as e:
        # Catch unexpected errors gracefully
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )
