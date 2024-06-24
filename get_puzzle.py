import requests

def fetch(difficulty : str) -> dict:
    '''
    This will pull a sudoku puzzle from https://www.youdosudoku.com/api
    @ pram:
        difficulty: "Easy, Meduim, Hard" This will be the diffulculty of the puzzle
    @ return:
        Dict{
            'difficulty' : [easy, medium, hard], 
            'puzzle' : 81 length string for puzzle, 
            'solution': solution to said puzzle}
    '''

    difficulty = difficulty.lower()
    if difficulty not in ["easy", "medium","hard"]:
        difficulty = "easy"

    body = {
    "difficulty": difficulty, # "easy", "medium", or "hard" (defaults to "easy")
    "solution": True, # True or False (defaults to True)
    "array": False # True or False (defaults to False)
    }

    headers =  {"Content-Type":"application/json"}

    try:
        response = requests.post("https://www.youdosudoku.com/api/", json=body, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return {}
