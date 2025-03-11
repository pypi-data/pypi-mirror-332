"""
Component Registry System for OpenAgents JSON framework.

This module provides a flexible registry system for managing all components
(agents, tools, assets) with efficient lookup and metadata management.

Features:
- Component registration and discovery
- Metadata extraction and management
- Version conflict handling
- Thread-safe operations
- Registry event system
"""

import abc
import inspect
import logging
import threading
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    List,
    Optional,
    Set,
    Type,
    TypeVar,
    Union,
)

T = TypeVar("T")  # Generic type for components

logger = logging.getLogger(__name__)


@dataclass
class ComponentMetadata:
    """Metadata for a registered component."""

    name: str
    version: str = "0.1.0"
    description: str = ""
    author: str = ""
    tags: Set[str] = field(default_factory=set)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    dependencies: Dict[str, str] = field(default_factory=dict)
    extra: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_component(
        cls, component: Any, name: Optional[str] = None
    ) -> "ComponentMetadata":
        """Extract metadata from a component's docstring and annotations."""
        metadata = cls(name=name or getattr(component, "__name__", str(component)))

        # Extract description from docstring
        if component.__doc__:
            metadata.description = inspect.cleandoc(component.__doc__).split("\n\n")[0]

        # Extract version if available
        if hasattr(component, "__version__"):
            metadata.version = component.__version__

        # Extract author if available
        if hasattr(component, "__author__"):
            metadata.author = component.__author__

        # Extract tags if available
        if hasattr(component, "__tags__"):
            metadata.tags = set(component.__tags__)

        return metadata


class RegistryEvent:
    """Base class for registry events."""

    pass


class ComponentRegistered(RegistryEvent):
    """Event fired when a component is registered."""

    def __init__(self, component_id: str, component: Any, metadata: ComponentMetadata):
        self.component_id = component_id
        self.component = component
        self.metadata = metadata


class ComponentUnregistered(RegistryEvent):
    """Event fired when a component is unregistered."""

    def __init__(self, component_id: str, component: Any):
        self.component_id = component_id
        self.component = component


class ComponentLookup(RegistryEvent):
    """Event fired when a component is looked up."""

    def __init__(self, component_id: str, component: Any):
        self.component_id = component_id
        self.component = component


class BaseComponentRegistry(Generic[T], abc.ABC):
    """Abstract base class defining the interface for component registries."""

    @abc.abstractmethod
    def register(
        self,
        component_id: str,
        component: T,
        metadata: Optional[ComponentMetadata] = None,
    ) -> None:
        """Register a component with the given ID."""
        pass

    @abc.abstractmethod
    def unregister(self, component_id: str) -> bool:
        """Unregister a component with the given ID. Returns True if successful."""
        pass

    @abc.abstractmethod
    def get(self, component_id: str) -> Optional[T]:
        """Get a component by ID. Returns None if not found."""
        pass

    @abc.abstractmethod
    def list(self) -> List[str]:
        """List all registered component IDs."""
        pass

    @abc.abstractmethod
    def get_metadata(self, component_id: str) -> Optional[ComponentMetadata]:
        """Get metadata for a component. Returns None if not found."""
        pass

    @abc.abstractmethod
    def find(self, **filters) -> List[str]:
        """Find components matching the given filters."""
        pass

    @abc.abstractmethod
    def add_event_listener(
        self, event_type: Type[RegistryEvent], listener: Callable[[RegistryEvent], None]
    ) -> None:
        """Add an event listener for the given event type."""
        pass

    @abc.abstractmethod
    def remove_event_listener(
        self, event_type: Type[RegistryEvent], listener: Callable[[RegistryEvent], None]
    ) -> bool:
        """Remove an event listener. Returns True if successful."""
        pass


class InMemoryComponentRegistry(BaseComponentRegistry[T]):
    """In-memory implementation of the component registry."""

    def __init__(self):
        self._components: Dict[str, T] = {}
        self._metadata: Dict[str, ComponentMetadata] = {}
        self._event_listeners: Dict[
            Type[RegistryEvent], List[Callable[[RegistryEvent], None]]
        ] = defaultdict(list)
        self._lock = threading.RLock()  # Reentrant lock for thread safety

    def register(
        self,
        component_id: str,
        component: T,
        metadata: Optional[ComponentMetadata] = None,
    ) -> None:
        """Register a component with the given ID."""
        with self._lock:
            if component_id in self._components:
                existing_metadata = self._metadata[component_id]
                if existing_metadata.version == (
                    metadata.version if metadata else "0.1.0"
                ):
                    logger.warning(
                        f"Component {component_id} already registered with same version. Overwriting."
                    )
                else:
                    logger.warning(
                        f"Component {component_id} already registered with version {existing_metadata.version}. Overwriting with version {metadata.version if metadata else '0.1.0'}."
                    )

            self._components[component_id] = component

            # Generate metadata if not provided
            if metadata is None:
                metadata = ComponentMetadata.from_component(
                    component, name=component_id
                )

            self._metadata[component_id] = metadata

            # Fire event
            self._fire_event(ComponentRegistered(component_id, component, metadata))

    def unregister(self, component_id: str) -> bool:
        """Unregister a component with the given ID. Returns True if successful."""
        with self._lock:
            if component_id not in self._components:
                return False

            component = self._components[component_id]
            del self._components[component_id]
            del self._metadata[component_id]

            # Fire event
            self._fire_event(ComponentUnregistered(component_id, component))

            return True

    def get(self, component_id: str) -> Optional[T]:
        """Get a component by ID. Returns None if not found."""
        with self._lock:
            component = self._components.get(component_id)

            if component is not None:
                # Fire event
                self._fire_event(ComponentLookup(component_id, component))

            return component

    def list(self) -> List[str]:
        """List all registered component IDs."""
        with self._lock:
            return list(self._components.keys())

    def get_metadata(self, component_id: str) -> Optional[ComponentMetadata]:
        """Get metadata for a component. Returns None if not found."""
        with self._lock:
            return self._metadata.get(component_id)

    def find(self, **filters) -> List[str]:
        """
        Find components matching the given filters.

        Filters can include any attribute of ComponentMetadata:
        - name (str): Partial match for component name
        - version (str): Exact match for version
        - author (str): Partial match for author
        - tags (Set[str]): All tags must be present
        - etc.
        """
        with self._lock:
            results = []

            for component_id, metadata in self._metadata.items():
                match = True

                for attr, value in filters.items():
                    if not hasattr(metadata, attr):
                        match = False
                        break

                    metadata_value = getattr(metadata, attr)

                    # String partial match
                    if isinstance(metadata_value, str) and isinstance(value, str):
                        if value.lower() not in metadata_value.lower():
                            match = False
                            break

                    # Set contains all
                    elif isinstance(metadata_value, set) and isinstance(
                        value, (set, list)
                    ):
                        if not all(item in metadata_value for item in value):
                            match = False
                            break

                    # Direct equality
                    elif metadata_value != value:
                        match = False
                        break

                if match:
                    results.append(component_id)

            return results

    def add_event_listener(
        self, event_type: Type[RegistryEvent], listener: Callable[[RegistryEvent], None]
    ) -> None:
        """Add an event listener for the given event type."""
        with self._lock:
            self._event_listeners[event_type].append(listener)

    def remove_event_listener(
        self, event_type: Type[RegistryEvent], listener: Callable[[RegistryEvent], None]
    ) -> bool:
        """Remove an event listener. Returns True if successful."""
        with self._lock:
            if event_type not in self._event_listeners:
                return False

            try:
                self._event_listeners[event_type].remove(listener)
                return True
            except ValueError:
                return False

    def _fire_event(self, event: RegistryEvent) -> None:
        """Fire an event to all registered listeners."""
        event_type = type(event)

        # Make a copy of listeners to avoid modification during iteration
        listeners = list(self._event_listeners[event_type])

        for listener in listeners:
            try:
                listener(event)
            except Exception as e:
                logger.error(f"Error in event listener: {e}")


# Default registry instance
component_registry = InMemoryComponentRegistry()
