from typing import Optional, Union, List
import requests
from bs4 import BeautifulSoup
from ..utils.pydantic_models import WebpageContent, WebpageMetadata
from ..utils import logger


class WebpageLoader:
    """A class to load and parse webpage content with various extraction methods."""

    def __init__(self, urls: Union[str, List[str]], parser_type: str = "html.parser"):
        """
        Initialize the WebpageLoader with URLs to process.

        Args:
            urls: Single URL as string or multiple URLs as list of strings
            parser_type: The type of parser to use ('xml' or 'html.parser'). Defaults to 'html.parser'
        """
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         'Chrome/91.0.4472.124 Safari/537.36'
        }
        self.urls = [urls] if isinstance(urls, str) else urls
        self.parser_type = parser_type
        self.loaded_pages: List[WebpageContent] = []
        logger.debug(f"Initialized WebpageLoader with {len(self.urls)} URLs and parser type: {parser_type}")

    def load(self) -> None:
        """
        Load all URLs provided during initialization and store the results in loaded_pages.
        Each URL is processed sequentially and its content is stored regardless of success or failure.
        """
        logger.info(f"Starting to load {len(self.urls)} webpages")
        self.loaded_pages = []
        for url in self.urls:
            logger.debug(f"Processing URL: {url}")
            webpage_content = self._load_webpage(url)
            self.loaded_pages.append(webpage_content)
        logger.info(f"Completed loading {len(self.urls)} webpages")

    def get_documents(self, as_string: bool = True) -> Union[List[str], List[WebpageContent]]:
        """
        Retrieve the loaded documents either as structured objects or formatted strings.

        Args:
            as_string: If True, returns documents as formatted strings, otherwise as WebpageContent objects. Defaults to True.

        Returns:
            List of either formatted strings or WebpageContent objects depending on as_string parameter
        """
        logger.debug(f"Retrieving documents with as_string={as_string}")
        if not self.loaded_pages:
            logger.warning("No pages have been loaded yet")
            return []

        if as_string:
            return [self.get_formatted_content(page) for page in self.loaded_pages]
        return self.loaded_pages

    def _load_webpage(self, url: str) -> WebpageContent:
        """
        Load and parse a single webpage, extracting its metadata and content.

        Args:
            url: The URL of the webpage to load

        Returns:
            WebpageContent: A structured object containing the webpage's metadata and content
        """
        try:
            logger.debug(f"Attempting to fetch URL: {url}")
            response = requests.get(url, headers=self.headers)
            
            webpage_content = WebpageContent(
                url=url,
                status_code=response.status_code,
                metadata=WebpageMetadata(),
            )

            if response.status_code != 200:
                error_msg = f"Failed to retrieve the page. Status code: {response.status_code}"
                logger.error(f"{error_msg} for URL: {url}")
                webpage_content.error_message = error_msg
                return webpage_content

            logger.debug(f"Successfully fetched URL: {url}. Parsing content...")
            soup = BeautifulSoup(response.text, self.parser_type)
            
            metadata = WebpageMetadata(
                browser_title=self._extract_title(soup),
                section_number=self._extract_section_number(soup),
                subject=self._extract_subject(soup),
                language=self._extract_language(soup),
                meta_tags=self._extract_meta_tags(soup)
            )
            
            content_lines = self._extract_content_lines(soup)
            logger.debug(f"Extracted {len(content_lines)} content lines from {url}")
            
            return WebpageContent(
                url=url,
                status_code=response.status_code,
                metadata=metadata,
                content_lines=content_lines
            )

        except requests.RequestException as e:
            error_msg = f"Request failed for URL {url}: {str(e)}"
            logger.error(error_msg)
            return WebpageContent(
                url=url,
                status_code=0,
                metadata=WebpageMetadata(),
                error_message=str(e)
            )

    def get_formatted_content(self, webpage_content: WebpageContent) -> str:
        """
        Convert the structured webpage content into a formatted string containing
        browser title, subject, and content lines.

        Args:
            webpage_content: The WebpageContent object to format

        Returns:
            str: A formatted string containing the requested information
        """
        if webpage_content.error_message:
            logger.warning(f"Formatting content with error: {webpage_content.error_message}")
            return f"Error: {webpage_content.error_message}"
        
        logger.debug(f"Formatting content for URL: {webpage_content.url}")
        return "\n".join(webpage_content.content_lines)

    def _extract_title(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract the title from the webpage."""
        title_tag = soup.find('title')
        return title_tag.text.strip() if title_tag else None

    def _extract_section_number(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract the section number from the webpage."""
        section_title = soup.find('SECTNO')
        return section_title.text.strip() if section_title else None

    def _extract_subject(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract the subject from the webpage."""
        subject = soup.find('SUBJECT')
        return subject.text.strip() if subject else None

    def _extract_language(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract the language from the webpage."""
        html_tag = soup.find('html')
        return html_tag.get('lang') if html_tag else None

    def _extract_meta_tags(self, soup: BeautifulSoup) -> dict[str, str]:
        """Extract metadata from meta tags."""
        meta_tags = {}
        for tag in soup.find_all('meta'):
            if tag.get('name'):
                meta_tags[tag['name']] = tag.get('content', '')
            elif tag.get('property'):
                meta_tags[tag['property']] = tag.get('content', '')
        return meta_tags

    def _extract_content_lines(self, soup: BeautifulSoup) -> list[str]:
        """Extract content lines from the webpage."""
        for script in soup(["script", "style"]):
            script.decompose()
        
        text = soup.get_text()
        return [line.strip() for line in text.splitlines() if line.strip()]