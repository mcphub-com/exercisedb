import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/justin-WFnsXH_t6/api/exercisedb'

mcp = FastMCP('exercisedb')

@mcp.tool()
def body_part_body_part(limit: Annotated[Union[int, float, None], Field(description='Default: 10')] = None,
                        offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Return list of exercises based on body part'''
    url = 'https://exercisedb.p.rapidapi.com/exercises/bodyPart/back'
    headers = {'x-rapidapi-host': 'exercisedb.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def exercises_body_part_list() -> dict: 
    '''Return list body parts'''
    url = 'https://exercisedb.p.rapidapi.com/exercises/bodyPartList'
    headers = {'x-rapidapi-host': 'exercisedb.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def exercises_equipment_list() -> dict: 
    '''Return list of equipment'''
    url = 'https://exercisedb.p.rapidapi.com/exercises/equipmentList'
    headers = {'x-rapidapi-host': 'exercisedb.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def exercises_target_list() -> dict: 
    '''Return list of target muscles'''
    url = 'https://exercisedb.p.rapidapi.com/exercises/targetList'
    headers = {'x-rapidapi-host': 'exercisedb.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def equipment_type(limit: Annotated[Union[int, float, None], Field(description='Default: 10')] = None,
                   offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Return list of exercises based on equipment type'''
    url = 'https://exercisedb.p.rapidapi.com/exercises/equipment/assisted'
    headers = {'x-rapidapi-host': 'exercisedb.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def target_target(limit: Annotated[Union[int, float, None], Field(description='Default: 10')] = None,
                  offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Return list of exercises by target muscle'''
    url = 'https://exercisedb.p.rapidapi.com/exercises/target/abductors'
    headers = {'x-rapidapi-host': 'exercisedb.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def exercise_id(id: Annotated[str, Field(description='')]) -> dict: 
    '''Return an exercise by it's id'''
    url = 'https://exercisedb.p.rapidapi.com/exercises/exercise/%7Bid%7D'
    headers = {'x-rapidapi-host': 'exercisedb.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def name_name(offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              limit: Annotated[Union[int, float, None], Field(description='Default: 10')] = None) -> dict: 
    '''Return list of exercises by name'''
    url = 'https://exercisedb.p.rapidapi.com/exercises/name/%7Bname%7D'
    headers = {'x-rapidapi-host': 'exercisedb.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'offset': offset,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def exercises(limit: Annotated[Union[int, float, None], Field(description='Default: 10')] = None,
              offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Return list of all exercises'''
    url = 'https://exercisedb.p.rapidapi.com/exercises'
    headers = {'x-rapidapi-host': 'exercisedb.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
