"""Automated tests for the Student Task Manager.

Run with:
    python -m unittest discover -s tests -v
"""

import os
import sys
import unittest

# Allow importing task_manager from the project root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Complete DevOps assignment")
        self.assertIsNotNone(task)
        self.assertEqual(task["title"], "Complete DevOps assignment")
        self.assertEqual(len(self.manager.list_tasks()), 1)
        # Empty title must be rejected
        self.assertIsNone(self.manager.add_task(""))
        self.assertIsNone(self.manager.add_task("   "))

    def test_complete_task(self):
        task = self.manager.add_task("Study for viva")
        result = self.manager.complete_task(task["id"])
        self.assertTrue(result)
        self.assertTrue(self.manager.list_tasks()[0]["completed"])
        # Invalid ID must return False
        self.assertFalse(self.manager.complete_task(999))

    def test_delete_task(self):
        task = self.manager.add_task("Task to delete")
        result = self.manager.delete_task(task["id"])
        self.assertTrue(result)
        self.assertEqual(len(self.manager.list_tasks()), 0)
        # Invalid ID must return False
        self.assertFalse(self.manager.delete_task(999))


if __name__ == "__main__":
    unittest.main()
