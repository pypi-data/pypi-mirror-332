from typing import Optional, List, Dict, Any
from dnawave.models.base import BaseModel

class Dataset(BaseModel):
    _endpoint = "dataset"
    _list_key = "datasets"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Basic properties
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.source = kwargs.get('source')
        self.bucket_key = kwargs.get('bucket_key')
        
        # Content properties
        self.keywords = kwargs.get('keywords', [])
        self.links = kwargs.get('links', [])
        self.articles = kwargs.get('articles', [])
        self.summary = kwargs.get('summary')
        self.tags = kwargs.get('tags', [])

        # Metadata
        self.tenant_id = kwargs.get('tenantId')
        self.created_at = kwargs.get('createdAt')
        self.updated_at = kwargs.get('updatedAt')
        self.created_by_membership = kwargs.get('createdByMembership')
        self.updated_by_membership = kwargs.get('updatedByMembership')
        self.import_hash = kwargs.get('importHash')

    @classmethod
    def create(cls,
               name: str,
               bucket_key: str,
               source: str = 's3',
               description: Optional[str] = None,
               keywords: Optional[List[str]] = None,
               tags: Optional[List[Dict[str, str]]] = None,
               **kwargs) -> 'Dataset':
        """
        Create a new dataset.
        
        Args:
            name: Name of the dataset
            bucket_key: Storage bucket key
            source: Source type (default: 's3')
            description: Dataset description
            keywords: List of keywords
            tags: List of tag objects with id and name, e.g. [{"id": "...", "name": "..."}]
            **kwargs: Additional parameters
        
        Returns:
            Dataset: The created dataset instance
        """
        data = {
            'name': name,
            'bucket_key': bucket_key,
            'source': source,
            'description': description,
            'keywords': keywords or [],
            'tags': tags or [],
            **kwargs
        }
        instance = cls(**data)
        return instance.save()

    def add_article(self, title: str, authors: List[str], abstract: str, 
                   url: Optional[str] = None, doi: Optional[str] = None) -> None:
        """
        Add an article to the dataset.
        
        Args:
            title: Article title
            authors: List of author names
            abstract: Article abstract
            url: Optional URL to the article
            doi: Optional DOI of the article
        """
        article = {
            'title': title,
            'authors': authors,
            'abstract': abstract,
            'url': url,
            'doi': doi
        }
        if not self._data.get('articles'):
            self._data['articles'] = []
        self._data['articles'].append(article)

    def add_tag(self, tag_id: str, tag_name: str) -> None:
        """
        Add a tag to the dataset.
        
        Args:
            tag_id: ID of the tag
            tag_name: Name of the tag
        """
        if not self._data.get('tags'):
            self._data['tags'] = []
        self._data['tags'].append({'id': tag_id, 'name': tag_name})

    def __repr__(self):
        return f"Dataset(id={self.id}, name={self.name}, source={self.source})"