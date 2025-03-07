"""YouTube-related utilities and functions."""

import re
import time
from typing import Dict, List, Union
from youtube_transcript_api import YouTubeTranscriptApi
from psykickai_tools.utils import logger

def fetch_transcript(
    url: Union[str, List[str]], 
    with_timestamp: bool = False
) -> Union[str, List[Dict[str, Union[str, float]]], List[Union[str, List[Dict[str, Union[str, float]]]]]]:
    """Fetches the transcript of one or multiple YouTube videos.

    This function extracts the transcript from either a single YouTube video URL or a list
    of URLs. It can return either the plain text transcript(s) or detailed version(s) with
    timestamps. When processing multiple URLs, it includes a 3-second delay between fetches
    to avoid rate limiting.

    Args:
        url: Either a single YouTube video URL string or a list of URL strings.
        with_timestamp: If True, returns the transcript(s) with timestamps. Defaults to False.

    Returns:
        For a single URL:
            If with_timestamp is False: a single string with the transcript text.
            If with_timestamp is True: a list of dictionaries containing:
                - text (str): The text segment
                - start (float): Start time in seconds
                - duration (float): Duration of the segment in seconds
        For a list of URLs:
            A list containing the corresponding transcript results for each URL.

    Raises:
        ValueError: If the video ID cannot be extracted from any URL or if any transcript
            could not be fetched.

    Examples:
        >>> # Single URL
        >>> url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        >>> transcript = fetch_transcript(url)
        >>> 
        >>> # Multiple URLs
        >>> urls = [
        ...     "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        ...     "https://www.youtube.com/watch?v=another_video_id"
        ... ]
        >>> transcripts = fetch_transcript(urls, with_timestamp=True)
    """
    def _extract_and_fetch_single(video_url: str) -> Union[str, List[Dict[str, Union[str, float]]]]:
        """Helper function to process a single URL."""
        try:
            # Extract video ID from URL
            match = re.search(r'v=([a-zA-Z0-9_-]+)', video_url)
            if not match:
                raise ValueError(f"Could not extract video ID from URL: {video_url}")
            
            video_id = match.group(1)
            logger.debug(f"Extracting transcript for video ID: {video_id}")
            
            # Fetch transcript
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            
            if with_timestamp:
                logger.debug("Returning transcript with timestamps")
                return transcript
            else:
                logger.debug("Returning plain text transcript")
                return ' '.join(line['text'] for line in transcript)
                
        except Exception as e:
            logger.error(f"Failed to fetch transcript for {video_url}: {str(e)}")
            raise ValueError(f"Could not fetch transcript for {video_url}: {str(e)}")

    # Handle single URL case
    if isinstance(url, str):
        return _extract_and_fetch_single(url)
    
    # Handle list of URLs
    if not url:  # Empty list check
        return []
    
    results = []
    for i, single_url in enumerate(url):
        if i > 0:  # Add delay between fetches, except for the first one
            logger.debug("Pausing for 3 seconds before next fetch")
            time.sleep(3)
        
        results.append(_extract_and_fetch_single(single_url))
    
    return results 