import os
import sys
import time
import unittest

sys.path.insert(0, sys.path[0]+"/..")

import harvest

class TestHarvest(unittest.TestCase):
    def setUp(self):
        self.harvest = harvest.Harvest("https://goretoytest.harvestapp.com", "tester@goretoy.com", "tester account")

    def tearDown(self):
        pass

    def test_status_up(self):
        self.assertEqual('none', harvest.status().get('indicator', None), 'System Outage')

    def test_status_down(self):
        self.assertNotEqual('none', harvest.status().get('indicator', None), 'All Systems Operational')

    def test_today(self):
        today = self.harvest.today
        self.assertTrue(set(['for_day', 'projects', 'day_entries']).issubset(set(today.keys())))
        self.assertEqual(today.get('for_day', None), time.strftime('%y-%d-%m'))

    def test_add(self):
        today = self.harvest.today
        start = time.time()
        project = today.get('projects', [{}])[0].get('id', None)
        task    = today.get('projects', [{}])[0].get('tasks', [{}])[0].get('id', None)
        self.assertTrue(self.harvest.add({
            "notes": "%s" % start,
            "hours": "1.5",
            "project_id": project,
            "task_id": task
        }))
        exists = self.harvest.today

        #test that the entry got added
        self.assertTrue(len(exists.get('day_entries', [])) > len(today.get('day_entries', [])))

        if len(exists.get('day_entries', [])) > len(today.get('day_entries', [])):
            for entry in exists.get('day_entries', []):
                if entry.get('notes', None) == start:
                    self.assertEqual("1.5", entry.get('hours', None), "Hours are not equal")
                    self.assertEqual(project, entry.get('project_id', None), "Project Id not equal")
                    self.assertEqual(task, entry.get('task_id', None), "Task Id not equal")

if __name__ == '__main__':
    unittest.main()
