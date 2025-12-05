import unittest
from gitgrind import main
import pygit2
import logging


class TestGitGrind(unittest.TestCase):
    def test_epoch(self):
        repo = pygit2.Repository('.')
        grind = main.GitGrind(repo)
        found = grind.grind("author == 'kurt godwin'", "logic")
        print("Found: ", found)
        epoch = str(found['normal'][0].id)
        print("Epoch: ", epoch)
        self.assertTrue(epoch == "9342134002bca2bef1ec8e9d63a6ec5690558d62") 

    def test_initial_message(self):
        repo = pygit2.Repository('.')
        grind = main.GitGrind(repo,logger=logging)
        found = grind.grind("message == 'workflow updates'", "logic")
        print("Found: ", found)
        epoch = str(found['normal'][0].id)
        print("Epoch: ", epoch)
        print("Message: ", found['normal'][0].messege)
        self.assertTrue(epoch == "939dd6bd244d6e37b397b40b36af2b1a7faac5db")
        
