
import unittest

import hashiterator as hashiterator
import mapcreator as mapcreator
import pathfinding as pathfinding
import integration as integration

class HashIteratorTests(unittest.TestCase):

    def test_codequality_3(self):
        expected_hash_collision = '09e97089ae'

        self.failUnless(hashiterator.find_zero_collision_from_salt('code-quality',3) == expected_hash_collision)

    def test_machinelearning_4(self):
        expected_hash_collision = 'f320e001d1'

        self.failUnless(hashiterator.find_zero_collision_from_salt('machine-learning',4) == expected_hash_collision)

    def test_artificialintelligence_5(self):
        expected_hash_collision = '610d370320'

        self.failUnless(hashiterator.find_zero_collision_from_salt('artificial-intelligence',5) == expected_hash_collision)

class MapCreatorTests(unittest.TestCase):

  def test_parse_and_create_map(self):
    expected_map = '......\n....x.\n.x...x\n'
    test_mapcreate_directory = './test_files/mapcreator_test_files'
    map_output = mapcreator.parse_and_create_map(test_mapcreate_directory)

    self.failUnless(map_output == expected_map)

class PathFindingTests(unittest.TestCase):

  def test_path_between_points(self):
    expected_path = 'OOOOx\nOxxOO\nSxxxE\n..x..\n..x..\n'
    test_mapcreate_file = './test_files/pathfinding_test_files/pathFindingTestMap.txt'
    path_output = pathfinding.path_between_points(0, 2, 4, 2, test_mapcreate_file)

    self.failUnless(path_output == expected_path)

class IntegrationTests(unittest.TestCase):

  def test_simple_integration(self):

    expected_integration_result = '8e956058e0'

    test_integration_directory = './test_files/integration_test_files'
    integration_output = integration.all_together(0, 2, 5, 2, test_integration_directory, 4)
    self.failUnless(expected_integration_result == integration_output)
