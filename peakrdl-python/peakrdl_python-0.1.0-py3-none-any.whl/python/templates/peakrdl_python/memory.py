"""
This module is intended to distributed as part of automatically generated code by the PeakRDL
Python tool. It provides a set of classes used by the autogenerated code to represent memories
"""
from array import array as Array
from typing import List

from .base import Node

from .callbacks import CallbackSet


class Memory(Node):
    """
    base class of memory wrappers

    Note:
        It is not expected that this class will be instantiated under normal
        circumstances however, it is useful for type checking
    """

    __slots__ = ['__memwidth', '__entries', '__accesswidth']

    def __init__(self,
                 callbacks: CallbackSet,
                 address: int,
                 width: int,
                 accesswidth: int,
                 entries: int,
                 logger_handle: str,
                 inst_name: str):
        """
        Initialise the class

        Args:
            callbacks: set of callback to be used for accessing the hardware or simulator
            address: address of the register
            width: width of the register in bits
            logger_handle: name to be used logging messages associate with thisobject
        """

        super().__init__(callbacks=callbacks,
                         address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name)

        self.__memwidth = width
        self.__entries = entries
        self.__accesswidth = accesswidth

    @property
    def width(self) -> int:
        """
        The width of the memory in bits, this uses the `memwidth` systemRDL property

        Returns: memory width

        """
        return self.__memwidth

    @property
    def width_in_bytes(self) -> int:
        """
        The width of the memory bytes, i.e. the width in bits divided by 8

        Returns: memory width (in bytes)

        """
        return self.width >> 3

    @property
    def entries(self) -> int:
        """
        The number of entries in the memory, this uses the `mementries` systemRDL property

        Returns: memory entries

        """
        return self.__entries

    @property
    def array_typecode(self) -> str:
        """
        the python array.array type is initialised with a typecode. This property provides the
        recommended typecode to use with this class instance (based on the memwidth)


        Returns: typecode

        """

        if self.width_in_bytes == 1:
            typecode = 'B'
        elif self.width_in_bytes == 2:
            typecode = 'I'
        elif self.width_in_bytes == 4:
            typecode = 'L'
        elif self.width_in_bytes == 8:
            typecode = 'Q'
        else:
            raise RuntimeError(f'unsupported width of {self.width_in_bytes:d} Bytes')

        return typecode

    @property
    def size_in_bytes(self) -> int:
        """
        size in bytes

        Returns: memory size
        """
        return self.entries * self.width_in_bytes

    def address_lookup(self, entry:int) -> int:
        """
        provides the address for an entry in the memory.

        Examples

        Args:
            entry: entry number to look up the address for

        Returns: Address

        """
        if not isinstance(entry, int):
            raise TypeError(f'entry must be an int but got {type(entry)}')

        if entry not in range(0, self.entries):
            raise ValueError(f'entry must be in range 0 to {self.entries-1:d} but got {entry:d}')

        return self.address + (entry * self.width_in_bytes)

    @property
    def accesswidth(self) -> int:
        """
        The access width of the register in bits, this uses the `accesswidth` systemRDL property

        Returns: register access width
        """
        return self.__accesswidth


class MemoryReadOnly(Memory):
    """
    base class of memory wrappers

    Note:
        It is not expected that this class will be instantiated under normal
        circumstances however, it is useful for type checking
    """

    __slots__ : List[str] = [ ]

    def read(self, start_entry:int, number_entries:int) -> Array:
        """
        Read from the memory

        Args:
            start_entry: index in the memory to start from, this is not the address
            number_entries: number of enries to read

        Returns: data read from memory

        """

        if not isinstance(start_entry, int):
            raise TypeError(f'start_entry should be an int got {type(start_entry)}')

        if not isinstance(number_entries, int):
            raise TypeError(f'number_entries should be an int got {type(number_entries)}')

        if start_entry not in range(0, self.entries):
            raise ValueError(f'entry must be in range 0 to {self.entries - 1:d} '
                             f'but got {start_entry:d}')

        if number_entries not in range(0, self.entries - start_entry + 1):
            raise ValueError(f'number_entries must be in range 0 to {self.entries - start_entry:d} '
                             f'but got {number_entries:d}')

        read_block_callback = self._callbacks.read_block_callback
        read_callback = self._callbacks.read_callback

        if read_block_callback is not None:

            data_read = read_block_callback(addr=self.address_lookup(entry=start_entry),
                                            width=self.width,
                                            accesswidth=self.width,
                                            length=number_entries)

            if not isinstance(data_read, Array):
                raise TypeError('The read block callback is expected to return an array')

        else:
            # there is not read_block_callback defined so we must used individual read
            data_read = Array(self.array_typecode,[0 for x in range(number_entries)])

            for entry in range(number_entries):
                entry_address = self.address_lookup(entry=start_entry+entry)
                data_entry = read_callback(addr=entry_address,
                                           width=self.width,
                                           accesswidth=self.width)

                data_read[entry] = data_entry

        return data_read


class MemoryWriteOnly(Memory):
    """
    base class of memory wrappers

    Note:
        It is not expected that this class will be instantiated under normal
        circumstances however, it is useful for type checking
    """

    __slots__ : List[str] = []

    def write(self, start_entry: int, data: Array) -> None:
        """
        Write data to memory

        Args:
            start_entry: index in the memory to start from, this is not the address
            data: data to write

        Returns: None

        """
        if not isinstance(start_entry, int):
            raise TypeError(f'start_entry should be an int got {type(start_entry)}')

        if start_entry not in range(0, self.entries):
            raise ValueError(f'entry must be in range 0 to {self.entries - 1:d} '
                             f'but got {start_entry:d}')

        if not isinstance(data, Array):
            raise TypeError(f'data should be an array.array got {type(data)}')

        if len(data) not in range(0, self.entries - start_entry + 1):
            raise ValueError(f'data length must be in range 0 to {self.entries - start_entry:d} '
                             f'but got {len(data):d}')

        write_block_callback = self._callbacks.write_block_callback
        write_callback = self._callbacks.write_callback

        if write_block_callback is not None:

            write_block_callback(addr=self.address_lookup(entry=start_entry),
                                 width=self.width,
                                 accesswidth=self.width,
                                 data=data)

        else:
            # there is not write_block_callback defined so we must used individual write
            for entry_index, entry_data in enumerate(data):
                entry_address = self.address_lookup(entry=start_entry+entry_index)
                write_callback(addr=entry_address,
                               width=self.width,
                               accesswidth=self.width,
                               data=entry_data)


class MemoryReadWrite(MemoryReadOnly, MemoryWriteOnly):
    """
    base class of memory wrappers

    Note:
        It is not expected that this class will be instantiated under normal
        circumstances however, it is useful for type checking
    """

    __slots__  : List[str] = []
