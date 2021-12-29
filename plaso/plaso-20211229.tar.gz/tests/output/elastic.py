#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the Elasticsearch output module."""

import unittest

from unittest.mock import MagicMock

from plaso.output import elastic
from plaso.output import shared_elastic

from tests.output import test_lib


class TestElasticsearchOutputModule(elastic.ElasticsearchOutputModule):
  """Elasticsearch output module for testing."""

  def _Connect(self):
    """Connects to an Elasticsearch server."""
    self._client = MagicMock()


@unittest.skipIf(shared_elastic.elasticsearch is None, 'missing elasticsearch')
class ElasticsearchOutputModuleTest(test_lib.OutputModuleTestCase):
  """Tests for the Elasticsearch output module."""

  # pylint: disable=protected-access

  def testWriteHeader(self):
    """Tests the WriteHeader function."""
    output_mediator = self._CreateOutputMediator()
    output_module = TestElasticsearchOutputModule(output_mediator)

    self.assertIsNone(output_module._client)

    output_module.WriteHeader()

    self.assertIsNotNone(output_module._client)


if __name__ == '__main__':
  unittest.main()
