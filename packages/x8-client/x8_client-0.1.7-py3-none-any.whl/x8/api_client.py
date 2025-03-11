"""API client for interacting with the video processing service."""

import logging
from typing import Dict, List, Optional, Any, Union, TypeVar, cast

import requests
from requests.exceptions import RequestException

from .config import API_BASE_URL, SECRET_KEY, DEFAULT_TIMEOUT, DEFAULT_PAGE_SIZE
from .exceptions import APIError, VideoProcessingError, FacebookPostingError
from .models import Article, FacebookPost, Video

logger = logging.getLogger(__name__)

T = TypeVar('T')

class APIClient:
    """Client for interacting with the video processing API.
    
    This client provides methods for fetching articles, creating videos, and posting content
    to Facebook through the backend API.
    
    Attributes:
        base_url: Base URL for the API endpoints
        secret_key: Authentication secret key for API requests
    """

    def __init__(self, base_url: str = API_BASE_URL, secret_key: str = SECRET_KEY) -> None:
        """Initialize the API client.

        Args:
            base_url: Base URL for the API
            secret_key: Authentication secret key
            
        Raises:
            ValueError: If base_url or secret_key is not provided
        """
        if not base_url:
            raise ValueError("API_BASE_URL is not configured")
        if not secret_key:
            raise ValueError("SECRET_KEY is not configured")
            
        self.base_url = f'{base_url}/api'
        self.secret_key = secret_key

    def _get_headers(self) -> Dict[str, str]:
        """Get headers for API requests.

        Returns:
            Dictionary containing authorization and content-type headers
        """
        return {
            "Authorization": f"Bearer {self.secret_key}",
            "Content-Type": "application/json"
        }
    
    def _make_request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict[str, Any]] = None, 
        data: Optional[Dict[str, Any]] = None,
        error_msg: str = "API request failed"
    ) -> Dict[str, Any]:
        """Make a request to the API.
        
        Args:
            method: HTTP method to use (GET, POST, etc.)
            endpoint: API endpoint to call (without base URL)
            params: URL parameters to include
            data: JSON data to send in the request body
            error_msg: Error message to use if the request fails
            
        Returns:
            Parsed JSON response
            
        Raises:
            APIError: If the API request fails
        """
        url = f"{self.base_url}/{endpoint}"
        
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self._get_headers(),
                params=params,
                json=data,
                timeout=DEFAULT_TIMEOUT
            )
            logger.debug(f"[x8] {method} {url} - Status: {response.status_code}")
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            logger.error(f"[x8] {error_msg}: {str(e)}")
            raise APIError(f"{error_msg}: {str(e)}") from e

    def _read_articles(
        self,
        page: int = 0,
        size: int = DEFAULT_PAGE_SIZE,
        category: Optional[str] = None,
        tags: Optional[str] = None,
        src: Optional[str] = None,
        video_made: Optional[bool] = None,
        has_img: Optional[bool] = None,
        has_video: Optional[bool] = None,
        age: int = 0,
        fb_posted: Optional[bool] = None
    ) -> List[Article]:
        """Fetch articles from the API based on given filters.

        Args:
            page: Page number for pagination
            size: Number of items per page
            category: Filter by category
            tags: Filter by tags
            src: Filter by source
            video_made: Filter by video status
            has_img: Filter by image presence
            has_video: Filter by video presence
            age: Filter by age in days
            fb_posted: Filter by Facebook posted status

        Returns:
            List of Article objects

        Raises:
            APIError: If the API request fails
        """
        # Remove self from locals and filter out None values
        params = {k: v for k, v in locals().items() 
                 if k != 'self' and v is not None}
        
        response_data = self._make_request(
            method="GET",
            endpoint="articles",
            params=params,
            error_msg="Failed to fetch articles"
        )
        
        return [Article.from_dict(article) for article in response_data.get('data', [])]

    def get_articles_not_made_video(
        self,
        category: Optional[str] = None,
        tags: Optional[str] = None,
        age: int = 0
    ) -> List[Article]:
        """Get articles that haven't been processed into videos yet.

        Args:
            category: Optional category filter
            tags: Optional tags filter
            age: Maximum age of articles in days

        Returns:
            List of Article objects
        """
        return self._read_articles(
            video_made=False,
            category=category,
            tags=tags,
            has_img=True,
            age=age
        )

    def get_articles_not_fb_posted(
        self,
        category: Optional[str] = None,
        tags: Optional[str] = None,
        age: int = 1,
        fb_posted: bool = False
    ) -> List[Article]:
        """Get articles that haven't been posted to Facebook yet.

        Args:
            category: Optional category filter
            tags: Optional tags filter
            age: Maximum age of articles in days
            fb_posted: Whether the article has been posted to Facebook

        Returns:
            List of Article objects
        """
        return self._read_articles(
            fb_posted=fb_posted,
            category=category,
            tags=tags,
            age=age
        )
        
    def get_article_by_id(self, article_id: str) -> Optional[Article]:
        """Get a specific article by its ID.
        
        Args:
            article_id: Unique identifier of the article
            
        Returns:
            Article object if found, None otherwise
            
        Raises:
            APIError: If the API request fails
        """
        try:
            response_data = self._make_request(
                method="GET",
                endpoint=f"articles/{article_id}",
                error_msg=f"Failed to fetch article {article_id}"
            )
            return Article.from_dict(response_data)
        except APIError as e:
            if "404" in str(e):
                logger.warning(f"Article {article_id} not found")
                return None
            raise

    def make_video(
        self, 
        video: Video, 
        included_long_video: bool = False, 
        fmt: Optional[str] = None, 
        **kwargs
    ) -> Dict[str, Any]:
        """Process an article into a video.

        Args:
            video: Video object containing processing details
            included_long_video: Whether to include long video version
            fmt: Format of the video output
            **kwargs: Additional parameters to pass to the API

        Returns:
            Processed video data as dictionary

        Raises:
            VideoProcessingError: If video processing fails
        """
        # Build parameters dictionary with all options
        params = {}
        if included_long_video:
            params['included_long_video'] = included_long_video
        if fmt:
            params['fmt'] = fmt
        # Add any additional keyword arguments to the parameters
        params.update(kwargs)

        try:
            return self._make_request(
                method="POST",
                endpoint="video/ve8",
                params=params,
                data=video.to_dict(),
                error_msg=f"Error making video for article: {video.unique_id}"
            )
        except APIError as e:
            # Convert APIError to more specific VideoProcessingError
            raise VideoProcessingError(str(e)) from e

    def post_facebook(self, fb_post: FacebookPost) -> Dict[str, Any]:
        """Post content to Facebook.
        
        Args:
            fb_post: FacebookPost object containing post details
            
        Returns:
            Response data as dictionary
            
        Raises:
            FacebookPostingError: If posting to Facebook fails
        """
        try:
            return self._make_request(
                method="POST",
                endpoint="facebook/vf8",
                data=fb_post.to_dict(),
                error_msg=f"Error posting to Facebook for: {fb_post.unique_id}"
            )
        except APIError as e:
            # Convert APIError to more specific FacebookPostingError
            raise FacebookPostingError(str(e)) from e
            
    def update_article(self, article: Article) -> Article:
        """Update an existing article.
        
        Args:
            article: Article object with updated fields
            
        Returns:
            Updated Article object
            
        Raises:
            APIError: If the API request fails
        """
        response_data = self._make_request(
            method="PUT",
            endpoint=f"articles/{article.unique_id}",
            data=article.to_dict(),
            error_msg=f"Error updating article: {article.unique_id}"
        )
        
        return Article.from_dict(response_data)