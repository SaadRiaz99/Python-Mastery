import httpx
import json 
import os

import asyncio


async def get_repository(username:str , repository:str):
    url = f"https://api.github.com/repos/{username}/{repository}"  # Replace with the actual repository URL




    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            data = response.json()

            print("Repository:", data["full_name"])
            print("Description:", data["description"])
            print("Stars:", data["stargazers_count"])
            print("Forks:", data["forks_count"])
            print("Issues:", data["open_issues_count"])
            print("Language:", data["language"])
            print("URL:", data["html_url"])

        elif response.status_code == 404:
            print("Repository not found!")

        else:
            print("Something went wrong!")
            print("Status:", response.status_code)


asyncio.run(
    get_repository("SaadRiaz99", "Python-Mastery"),
    # get_repository("Demolinator", "revit-mcp-server")
)