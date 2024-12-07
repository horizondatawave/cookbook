from typing import List, Optional, Any
import requests
from bs4 import BeautifulSoup
from llama_index.core.schema import Document
from llama_index.core.tools.tool_spec.base import BaseToolSpec


class ScrapeWebsiteTool(BaseToolSpec):
    """Tool spec for reading and parsing web content by URL"""

    spec_functions = [
        "fetch_content",
    ]

    headers: Optional[dict] = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com/',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    def __init__(self,  cookies: Optional[dict] = None) -> None:
        """Initialize with optional URL and cookies."""
        super().__init__()  
        self.cookies = cookies or {}

    def fetch_content(self, url: str) -> str:
        """
        Read the content of a web page by URL.
        Use it for get and parsing web content by URL..

        Args:
            url: The URL of the web page to fetch. If not provided, the instance's website_url is used.

        Returns:
            result: A string containing the parsed textual content of the web page.
        """
        website_url = url
        if not website_url:
            raise ValueError("A URL must be provided to fetch content.")

        response = requests.get(
            website_url,
            timeout=15,
            headers=self.headers,
            cookies=self.cookies
        )
        response.encoding = response.apparent_encoding

        # Парсинг страницы с использованием BeautifulSoup
        parsed = BeautifulSoup(response.text, "html.parser")

        # Извлечение и форматирование текста
        text = parsed.get_text()
        # Удаление пустых строк и лишних пробелов
        text = '\n'.join([line for line in text.split('\n') if line.strip() != ''])
        text = ' '.join([word for word in text.split(' ') if word.strip() != ''])

        return text


# tool = ScrapeWebsiteTool()
# text = tool.fetch_content("https://www.statista.com/statistics/242477/global-revenue-of-market-research-companies/")
# print(text)