"""
Tests for the state manager implementations.

This module contains tests for the state manager implementations used by the
state management system.
"""

import os
import shutil
import tempfile
import unittest
from typing import Dict, List, Optional, Set, Any

from openagents_json.core.state.base import StateManager
from openagents_json.core.state.managers.memory import MemoryStateManager
from openagents_json.core.state.managers.file import FileStateManager


class BaseStateManagerTest:
    """Base class for state manager tests."""
    
    def test_get_set_state(self):
        """Test getting and setting state."""
        # Set state
        self.manager.set_state("agent1", "key1", "value1")
        
        # Get state
        value = self.manager.get_state("agent1", "key1")
        self.assertEqual(value, "value1")
        
        # Get non-existent state
        value = self.manager.get_state("agent1", "key2", "default")
        self.assertEqual(value, "default")
        
    def test_delete_state(self):
        """Test deleting state."""
        # Set state
        self.manager.set_state("agent1", "key1", "value1")
        
        # Delete state
        self.manager.delete_state("agent1", "key1")
        
        # Get deleted state
        value = self.manager.get_state("agent1", "key1", "default")
        self.assertEqual(value, "default")
        
    def test_clear_state(self):
        """Test clearing all state for an agent."""
        # Set multiple state keys
        self.manager.set_state("agent1", "key1", "value1")
        self.manager.set_state("agent1", "key2", "value2")
        
        # Clear state
        self.manager.clear_state("agent1")
        
        # Get cleared state
        value1 = self.manager.get_state("agent1", "key1", "default")
        value2 = self.manager.get_state("agent1", "key2", "default")
        self.assertEqual(value1, "default")
        self.assertEqual(value2, "default")
        
    def test_exists(self):
        """Test checking if state exists."""
        # Set state
        self.manager.set_state("agent1", "key1", "value1")
        
        # Check if state exists
        self.assertTrue(self.manager.exists("agent1", "key1"))
        self.assertFalse(self.manager.exists("agent1", "key2"))
        
    def test_keys(self):
        """Test listing keys for an agent."""
        # Set multiple state keys
        self.manager.set_state("agent1", "key1", "value1")
        self.manager.set_state("agent1", "key2", "value2")
        
        # Get keys
        keys = self.manager.keys("agent1")
        self.assertCountEqual(keys, ["key1", "key2"])
        
    def test_bulk_operations(self):
        """Test bulk state operations."""
        # Set bulk state
        self.manager.set_bulk_state("agent1", {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
        })
        
        # Get bulk state
        values = self.manager.get_bulk_state("agent1", ["key1", "key2"])
        self.assertEqual(values, {
            "key1": "value1",
            "key2": "value2",
        })
        
    def test_transaction(self):
        """Test transaction support."""
        # Begin transaction
        self.manager.begin_transaction()
        
        # Set state in transaction
        self.manager.set_state("agent1", "key1", "value1")
        self.manager.set_state("agent1", "key2", "value2")
        
        # Check state is visible within transaction
        self.assertEqual(self.manager.get_state("agent1", "key1"), "value1")
        
        # Commit transaction
        self.manager.commit_transaction()
        
        # Check state is persisted after commit
        self.assertEqual(self.manager.get_state("agent1", "key1"), "value1")
        self.assertEqual(self.manager.get_state("agent1", "key2"), "value2")
        
    def test_transaction_rollback(self):
        """Test transaction rollback."""
        # Set initial state
        self.manager.set_state("agent1", "key1", "initial")
        
        # Begin transaction
        self.manager.begin_transaction()
        
        # Set state in transaction
        self.manager.set_state("agent1", "key1", "changed")
        self.manager.set_state("agent1", "key2", "new")
        
        # Check state is changed within transaction
        self.assertEqual(self.manager.get_state("agent1", "key1"), "changed")
        
        # Rollback transaction
        self.manager.rollback_transaction()
        
        # Check state is reverted after rollback
        self.assertEqual(self.manager.get_state("agent1", "key1"), "initial")
        self.assertFalse(self.manager.exists("agent1", "key2"))
        
    def test_transaction_context_manager(self):
        """Test transaction context manager."""
        # Set initial state
        self.manager.set_state("agent1", "key1", "initial")
        
        # Use transaction context manager
        try:
            with self.manager.transaction():
                self.manager.set_state("agent1", "key1", "changed")
                self.manager.set_state("agent1", "key2", "new")
                raise ValueError("Test error")
        except ValueError:
            pass
        
        # Check state is reverted after exception
        self.assertEqual(self.manager.get_state("agent1", "key1"), "initial")
        self.assertFalse(self.manager.exists("agent1", "key2"))
        
        # Use transaction context manager successfully
        with self.manager.transaction():
            self.manager.set_state("agent1", "key1", "changed")
            self.manager.set_state("agent1", "key2", "new")
        
        # Check state is persisted after successful transaction
        self.assertEqual(self.manager.get_state("agent1", "key1"), "changed")
        self.assertEqual(self.manager.get_state("agent1", "key2"), "new")
        
    def test_backup_restore(self):
        """Test backup and restore functionality."""
        # Set initial state
        self.manager.set_state("agent1", "key1", "value1")
        self.manager.set_state("agent1", "key2", "value2")
        
        # Create backup
        backup_id = self.manager.create_backup("agent1")
        
        # Change state
        self.manager.set_state("agent1", "key1", "changed")
        self.manager.delete_state("agent1", "key2")
        
        # Restore backup
        result = self.manager.restore_backup("agent1", backup_id)
        self.assertTrue(result)
        
        # Check state is restored
        self.assertEqual(self.manager.get_state("agent1", "key1"), "value1")
        self.assertEqual(self.manager.get_state("agent1", "key2"), "value2")


class TestMemoryStateManager(unittest.TestCase, BaseStateManagerTest):
    """Tests for the MemoryStateManager class."""
    
    def setUp(self):
        """Set up the test case."""
        self.manager = MemoryStateManager()
        
    def tearDown(self):
        """Clean up after the test case."""
        pass


class TestFileStateManager(unittest.TestCase, BaseStateManagerTest):
    """Tests for the FileStateManager class."""
    
    def setUp(self):
        """Set up the test case."""
        self.temp_dir = tempfile.mkdtemp()
        self.manager = FileStateManager(self.temp_dir)
        
    def tearDown(self):
        """Clean up after the test case."""
        shutil.rmtree(self.temp_dir)
        
    def test_file_persistence(self):
        """Test that state is persisted to disk."""
        # Set state
        self.manager.set_state("agent1", "key1", "value1")
        
        # Create a new manager with the same directory
        new_manager = FileStateManager(self.temp_dir)
        
        # Check state is loaded from disk
        self.assertEqual(new_manager.get_state("agent1", "key1"), "value1")


if __name__ == "__main__":
    unittest.main() 