"""Main Tester Script"""
#  Copyright (c) 2023. Asger Jon Vistisen - MIT License
from __future__ import annotations

from typing import Union, Never, NoReturn, Any

Data = list[list[Union[int, float]]]


class Matrix:
  """Look at me getting all transposed!"""

  def __init__(self, data: Data) -> None:
    self._data = [*data, ]
    _rowLengths = [len(row) for row in self._data]
    if min(_rowLengths) - max(_rowLengths):
      raise ValueError("All rows must have the same length!")
    self._rowCount = _rowLengths[0]
    self._colCount = len(self._data)
    self._transposed = 0

  def _getT(self) -> bool:
    """Getter-function for transposed flag"""
    return True if self._transposed else False

  def _setT(self, value: Any) -> NoReturn:
    """Setter-function for transposed flag"""
    self._transposed = 1 if value else 0

  def _toggleT(self, ) -> NoReturn:
    """Toggle-function for transposed flag"""
    self._setT(not self._getT())

  def _getDataH(self) -> Data:
    """Getter-function for rows"""
    return self._data

  def _getDataV(self) -> Data:
    """Getter-function for cols"""
    cols = [[] for _ in range(self._colCount)]
    for (i, row) in enumerate(self._getDataH()):
      for val in row:
        cols[i].append(val)
    return cols

  def _getRows(self) -> Data:
    """Getter-function for rows"""
    return self._getDataV() if self.T else self._getDataH()

  def _getCols(self) -> Data:
    """Getter-function for rows"""
    return self._getDataH() if self.T else self._getDataV()

  def _noSet(self, *_) -> Never:
    """Illegal setter"""
    raise TypeError('read-only property')

  def _noDel(self) -> Never:
    """Illegal deleter"""
    raise TypeError('read-only property')

  rows = property(_getRows, _noSet, _noDel)
  cols = property(_getCols, _noSet, _noDel)
  T = property(_getT, _setT, _noDel)


class OP:
  """I can transpose all the matrices!"""

  def __rpow__(self, other: Matrix) -> Matrix:
    """Transposes the matrix if self is T"""
    other.T = not other.T
    return other
