import datetime
import json
import os
from typing import Any, Optional
from pydantic import BaseModel, Field
import requests

from llama_index.core.tools.tool_spec.base import BaseToolSpec


def _save_results_to_file(content: str) -> None:
    """Saves the search results to a file."""
    filename = f"search_results_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, "w") as file:
        file.write(content)
    print(f"Results saved to {filename}")


class SerperSearchPayload(BaseModel):
    """Payload for Serper internet search."""
    search_query: str = Field(..., description="Mandatory search query you want to use to search the internet")
    n_results: int = 10
    country: Optional[str] = ""
    location: Optional[str] = ""
    locale: Optional[str] = ""
    save_file: bool = False


class SerperToolSpec(BaseToolSpec):
    spec_functions = ["search_internet"]

    def search_internet(
        self,
        search_query: str,
        n_results: int = 10,
        country: str = "",
        location: str = "",
        locale: str = "",
        save_file: bool = False
    ) -> Any:
        """
        Perform a search on the internet using the Serper.dev API.

        :param search_query: The query to search.
        :param n_results: Number of results to return.
        :param country: Country code (e.g., 'us') for localized results.
        :param location: A location string for localized results.
        :param locale: Language code for localized results.
        :param save_file: Whether to save the results to a file.
        :return: String with formatted search results or raw response if no organic results found.
        """
        search_url = "https://google.serper.dev/search"

        payload = {"q": search_query, "num": n_results}
        if country:
            payload["gl"] = country
        if location:
            payload["location"] = location
        if locale:
            payload["hl"] = locale

        headers = {
            "X-API-KEY": os.environ["SERPER_API_KEY"],
            "content-type": "application/json",
        }

        response = requests.post(search_url, headers=headers, data=json.dumps(payload))
        results = response.json()

        if "organic" in results:
            results = results["organic"][:n_results]
            entries = []
            for result in results:
                try:
                    entries.append(
                        "\n".join(
                            [
                                f"Title: {result['title']}",
                                f"Link: {result['link']}",
                                f"Snippet: {result['snippet']}",
                                "---",
                            ]
                        )
                    )
                except KeyError:
                    continue

            content = "\n".join(entries)
            if save_file:
                _save_results_to_file(content)
            return f"\nSearch results:\n{content}\n"
        else:
            return results