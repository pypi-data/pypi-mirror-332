from typing import Optional, List, Dict, Any
from dnawave.models.base import BaseModel

class WorkflowRun(BaseModel):
    _endpoint = "workflow-run"
    _list_key = "workflowRuns"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Basic properties
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.status = kwargs.get('status')
        self.workflow_type = kwargs.get('workflowType')
        self.external_workflow_id = kwargs.get('externalWorkflowId')
        self.workflow_id = kwargs.get('workflowId')
        
        # Configuration properties
        self.priority = kwargs.get('priority')
        self.storage_capacity = kwargs.get('storageCapacity')
        self.retention_mode = kwargs.get('retentionMode')
        self.storage_type = kwargs.get('storageType')
        self.parameters = kwargs.get('parameters', {})
        
        # Dataset relationships
        self.datasets = kwargs.get('datasets', [])
        
        # Metadata
        self.tenant_id = kwargs.get('tenantId')
        self.created_at = kwargs.get('createdAt')
        self.updated_at = kwargs.get('updatedAt')
        self.created_by_membership = kwargs.get('createdByMembership')
        self.updated_by_membership = kwargs.get('updatedByMembership')
        self.workflow_run_status = kwargs.get('workflowRunStatus')

    @classmethod
    def create(cls, 
               name: str,
               workflow_id: str,
               datasets: List[Dict[str, str]],
               workflow_execution_type: str = "immediate",
               **kwargs) -> 'WorkflowRun':
        """
        Create a new workflow run.
        
        Args:
            name: Name of the workflow run
            workflow_id: ID of the workflow to run
            datasets: List of dataset objects with id and name, e.g. [{"id": "...", "name": "..."}]
            workflow_execution_type: Type of execution ("immediate" or "scheduled")
            **kwargs: Additional parameters
        
        Returns:
            WorkflowRun: The created workflow run instance
        """
        data = {
            'name': name,
            'workflowId': workflow_id,
            'datasets': datasets,
            'workflowExecutionType': workflow_execution_type,
            **kwargs
        }
        instance = cls(**data)
        return instance.save()

    def get_status(self) -> Optional[Dict[str, Any]]:
        """
        Get the detailed status of the workflow run.
        """
        return self.workflow_run_status

    def __repr__(self):
        return (f"WorkflowRun(id={self.id}, name={self.name}, "
                f"status={self.status}, workflow_id={self.workflow_id})")