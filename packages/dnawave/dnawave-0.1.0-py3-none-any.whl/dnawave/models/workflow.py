from typing import Optional, List, Dict, Any
from dnawave.models.base import BaseModel

class Workflow(BaseModel):
    _endpoint = "workflow"
    _list_key = "workflows"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Basic properties
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.external_id = kwargs.get('externalId')
        
        # Configuration properties
        self.engine = kwargs.get('engine')
        self.main = kwargs.get('main')
        self.parameter_template = kwargs.get('parameterTemplate')
        self.accelerators = kwargs.get('accelerators')
        self.definition_uri = kwargs.get('definitionUri')
        self.storage_capacity = kwargs.get('storageCapacity')
        self.configs = kwargs.get('configs')
        
        # Content properties
        self.keywords = kwargs.get('keywords', [])
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
               engine: str,
               parameter_template: Dict[str, Any],
               description: Optional[str] = None,
               main: Optional[str] = None,
               accelerators: Optional[str] = None,
               definition_uri: Optional[str] = None,
               tags: Optional[List[Dict[str, str]]] = None,
               **kwargs) -> 'Workflow':
        """
        Create a new workflow.
        
        Args:
            name: Name of the workflow
            engine: Workflow engine (e.g., 'nextflow')
            parameter_template: Template for workflow parameters
            description: Workflow description
            main: Main entry point
            accelerators: Compute accelerators configuration
            definition_uri: URI to workflow definition
            tags: List of tag objects with id and name, e.g. [{"id": "...", "name": "..."}]
            **kwargs: Additional parameters
        
        Returns:
            Workflow: The created workflow instance
        """
        data = {
            'name': name,
            'engine': engine,
            'parameterTemplate': parameter_template,
            'description': description,
            'main': main,
            'accelerators': accelerators,
            'definitionUri': definition_uri,
            'tags': tags or [],
            **kwargs
        }
        instance = cls(**data)
        return instance.save()

    def update_parameter_template(self, parameter_template: Dict[str, Any]) -> None:
        """
        Update the workflow's parameter template.
        
        Args:
            parameter_template: New parameter template
        """
        self._data['parameterTemplate'] = parameter_template

    def add_tag(self, tag_id: str, tag_name: str) -> None:
        """
        Add a tag to the workflow.
        
        Args:
            tag_id: ID of the tag
            tag_name: Name of the tag
        """
        if not self._data.get('tags'):
            self._data['tags'] = []
        self._data['tags'].append({'id': tag_id, 'name': tag_name})

    def __repr__(self):
        return f"Workflow(id={self.id}, name={self.name}, engine={self.engine})"