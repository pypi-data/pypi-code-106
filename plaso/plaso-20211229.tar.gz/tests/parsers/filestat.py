#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for filestat parser."""

import os

import unittest

from dfvfs.lib import definitions as dfvfs_definitions
from dfvfs.path import factory as path_spec_factory

from plaso.lib import definitions
from plaso.parsers import filestat

from tests import test_lib as shared_test_lib
from tests.parsers import test_lib


class FileStatTest(test_lib.ParserTestCase):
  """Tests for filestat parser."""

  def testExt4File(self):
    """Test a file in an ext4 file system."""
    test_file_path = self._GetTestFilePath(['ext4.raw'])
    self._SkipIfPathNotExists(test_file_path)

    os_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    ext_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_EXT, inode=14,
        location='/passwords.txt', parent=os_path_spec)

    parser = filestat.FileStatParser()
    storage_writer = self._ParseFileByPathSpec(ext_path_spec, parser)

    number_of_events = storage_writer.GetNumberOfAttributeContainers('event')
    self.assertEqual(number_of_events, 4)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'extraction_warning')
    self.assertEqual(number_of_warnings, 0)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'recovery_warning')
    self.assertEqual(number_of_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'attribute_names': ['security.selinux'],
        'data_type': 'fs:stat',
        'date_time': '2021-07-22 14:07:32.842610820',
        'display_name': 'EXT:/passwords.txt',
        'file_entry_type': 'file',
        'file_size': 116,
        'file_system_type': 'EXT',
        'group_identifier': 1000,
        'inode': 14,
        'mode': 0o664,
        'number_of_links': 1,
        'owner_identifier': 1000,
        'timestamp_desc': definitions.TIME_DESCRIPTION_LAST_ACCESS}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

  def testExt2FileWithTSK(self):
    """Test a file in an ext2 file system with TSK."""
    test_file_path = self._GetTestFilePath(['ímynd.dd'])
    self._SkipIfPathNotExists(test_file_path)

    os_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    tsk_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_TSK, inode=15,
        location='/passwords.txt', parent=os_path_spec)

    parser = filestat.FileStatParser()
    storage_writer = self._ParseFileByPathSpec(tsk_path_spec, parser)

    number_of_events = storage_writer.GetNumberOfAttributeContainers('event')
    self.assertEqual(number_of_events, 3)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'extraction_warning')
    self.assertEqual(number_of_warnings, 0)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'recovery_warning')
    self.assertEqual(number_of_warnings, 0)

    events = list(storage_writer.GetEvents())

    # Note that attribute support in pytsk/libtsk is currently broken
    # also see: https://github.com/py4n6/pytsk/issues/79
    expected_event_values = {
        'attribute_names': None,
        'data_type': 'fs:stat',
        'date_time': '2012-05-25 16:00:53',
        'display_name': 'TSK:/passwords.txt',
        'file_entry_type': 'file',
        'file_size': 116,
        'file_system_type': 'EXT2',
        'group_identifier': 5000,
        'inode': 15,
        'mode': 0o400,
        'number_of_links': 1,
        'owner_identifier': 151107,
        'timestamp_desc': definitions.TIME_DESCRIPTION_LAST_ACCESS}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

  def testNtfsFile(self):
    """Test a file in a NTFS file system."""
    test_file_path = self._GetTestFilePath(['vsstest.qcow2'])
    self._SkipIfPathNotExists(test_file_path)

    os_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    qcow_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_QCOW, parent=os_path_spec)
    ext_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_NTFS,
        location='\\$Extend\\$RmMetadata\\$TxfLog\\$TxfLog.blf',
        parent=qcow_path_spec)

    parser = filestat.FileStatParser()
    storage_writer = self._ParseFileByPathSpec(ext_path_spec, parser)

    number_of_events = storage_writer.GetNumberOfAttributeContainers('event')
    self.assertEqual(number_of_events, 4)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'extraction_warning')
    self.assertEqual(number_of_warnings, 0)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'recovery_warning')
    self.assertEqual(number_of_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'attribute_names': None,
        'data_type': 'fs:stat',
        'date_time': '2013-12-03 06:30:42.9779097',
        'display_name': 'NTFS:\\$Extend\\$RmMetadata\\$TxfLog\\$TxfLog.blf',
        'file_entry_type': 'file',
        'file_size': 65536,
        'file_system_type': 'NTFS',
        'timestamp_desc': definitions.TIME_DESCRIPTION_LAST_ACCESS}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

  def testZipFile(self):
    """Test a ZIP file."""
    test_file_path = self._GetTestFilePath(['syslog.zip'])
    self._SkipIfPathNotExists(test_file_path)

    os_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    zip_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_ZIP, location='/syslog',
        parent=os_path_spec)

    parser = filestat.FileStatParser()
    storage_writer = self._ParseFileByPathSpec(zip_path_spec, parser)

    number_of_events = storage_writer.GetNumberOfAttributeContainers('event')
    self.assertEqual(number_of_events, 1)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'extraction_warning')
    self.assertEqual(number_of_warnings, 0)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'recovery_warning')
    self.assertEqual(number_of_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'data_type': 'fs:stat',
        'date_time': '2012-07-24 14:45:24',
        'display_name': 'ZIP:/syslog',
        'file_entry_type': 'file',
        'file_size': 1247,
        'file_system_type': 'ZIP',
        'inode': None,
        'timestamp_desc': definitions.TIME_DESCRIPTION_MODIFICATION}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

  def testGzipFile(self):
    """Test a GZIP file."""
    test_file_path = self._GetTestFilePath(['syslog.gz'])
    self._SkipIfPathNotExists(test_file_path)

    os_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    gzip_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_GZIP, parent=os_path_spec)

    parser = filestat.FileStatParser()
    storage_writer = self._ParseFileByPathSpec(gzip_path_spec, parser)

    number_of_events = storage_writer.GetNumberOfAttributeContainers('event')
    self.assertEqual(number_of_events, 1)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'extraction_warning')
    self.assertEqual(number_of_warnings, 0)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'recovery_warning')
    self.assertEqual(number_of_warnings, 0)

    events = list(storage_writer.GetEvents())

    test_path = os.path.join(shared_test_lib.TEST_DATA_PATH, 'syslog.gz')

    expected_event_values = {
        'data_type': 'fs:stat',
        'date_time': '2012-07-28 16:44:07',
        'display_name': 'GZIP:{0:s}'.format(test_path),
        'file_entry_type': 'file',
        'file_size': 1247,
        'file_system_type': 'GZIP',
        'inode': None,
        'timestamp_desc': definitions.TIME_DESCRIPTION_MODIFICATION}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

  def testTarFile(self):
    """Test a TAR file."""
    test_file_path = self._GetTestFilePath(['syslog.tar'])
    self._SkipIfPathNotExists(test_file_path)

    os_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    tar_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_TAR, location='/syslog',
        parent=os_path_spec)

    parser = filestat.FileStatParser()
    storage_writer = self._ParseFileByPathSpec(tar_path_spec, parser)

    number_of_events = storage_writer.GetNumberOfAttributeContainers('event')
    self.assertEqual(number_of_events, 1)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'extraction_warning')
    self.assertEqual(number_of_warnings, 0)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'recovery_warning')
    self.assertEqual(number_of_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'data_type': 'fs:stat',
        'date_time': '2012-07-24 21:45:24',
        'display_name': 'TAR:/syslog',
        'file_entry_type': 'file',
        'file_size': 1247,
        'file_system_type': 'TAR',
        'inode': None,
        'timestamp_desc': definitions.TIME_DESCRIPTION_MODIFICATION}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

  def testNestedFile(self):
    """Test a nested file."""
    test_file_path = self._GetTestFilePath(['syslog.tgz'])
    self._SkipIfPathNotExists(test_file_path)

    os_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    gzip_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_GZIP, parent=os_path_spec)
    tar_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_TAR, location='/syslog',
        parent=gzip_path_spec)

    parser = filestat.FileStatParser()
    storage_writer = self._ParseFileByPathSpec(tar_path_spec, parser)

    number_of_events = storage_writer.GetNumberOfAttributeContainers('event')
    self.assertEqual(number_of_events, 1)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'extraction_warning')
    self.assertEqual(number_of_warnings, 0)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'recovery_warning')
    self.assertEqual(number_of_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'data_type': 'fs:stat',
        'date_time': '2012-07-24 21:45:24',
        'display_name': 'TAR:/syslog',
        'file_entry_type': 'file',
        'file_size': 1247,
        'file_system_type': 'TAR',
        'inode': None,
        'timestamp_desc': definitions.TIME_DESCRIPTION_MODIFICATION}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

    test_file_path = self._GetTestFilePath(['syslog.tgz'])
    self._SkipIfPathNotExists(test_file_path)

    os_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    gzip_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_GZIP, parent=os_path_spec)

    storage_writer = self._ParseFileByPathSpec(gzip_path_spec, parser)

    number_of_events = storage_writer.GetNumberOfAttributeContainers('event')
    self.assertEqual(number_of_events, 1)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'extraction_warning')
    self.assertEqual(number_of_warnings, 0)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'recovery_warning')
    self.assertEqual(number_of_warnings, 0)

    events = list(storage_writer.GetEvents())

    test_path = os.path.join(shared_test_lib.TEST_DATA_PATH, 'syslog.tgz')

    expected_event_values = {
        'data_type': 'fs:stat',
        'date_time': '2012-07-28 16:44:43',
        'display_name': 'GZIP:{0:s}'.format(test_path),
        'file_entry_type': 'file',
        'file_size': 10240,
        'file_system_type': 'GZIP',
        'inode': None,
        'timestamp_desc': definitions.TIME_DESCRIPTION_MODIFICATION}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

  def testNestedTSK(self):
    """Test a nested TSK file."""
    test_file_path = self._GetTestFilePath(['syslog_image.dd'])
    self._SkipIfPathNotExists(test_file_path)

    os_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_OS, location=test_file_path)
    tsk_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_TSK, inode=11,
        location='/logs/hidden.zip', parent=os_path_spec)
    zip_path_spec = path_spec_factory.Factory.NewPathSpec(
        dfvfs_definitions.TYPE_INDICATOR_ZIP, location='/syslog',
        parent=tsk_path_spec)

    parser = filestat.FileStatParser()
    storage_writer = self._ParseFileByPathSpec(zip_path_spec, parser)

    number_of_events = storage_writer.GetNumberOfAttributeContainers('event')
    self.assertEqual(number_of_events, 1)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'extraction_warning')
    self.assertEqual(number_of_warnings, 0)

    number_of_warnings = storage_writer.GetNumberOfAttributeContainers(
        'recovery_warning')
    self.assertEqual(number_of_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'data_type': 'fs:stat',
        'date_time': '2012-07-20 15:44:14',
        'display_name': 'ZIP:/syslog',
        'file_entry_type': 'file',
        'file_size': 1247,
        'file_system_type': 'ZIP',
        'inode': None,
        'timestamp_desc': definitions.TIME_DESCRIPTION_MODIFICATION}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)


if __name__ == '__main__':
  unittest.main()
