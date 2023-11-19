from attr import attrs, attrib
from typing import Tuple

import copy

from brother_ql.helpers import ElementsManager

@attrs
class Model(object):
    """
    This class represents a printer model. All specifics of a certain model
    and the opcodes it supports should be contained in this class.
    """
    #: A string identifier given to each model implemented. Eg. 'QL-500'.
    identifier: str = attrib()
    #: Minimum and maximum number of rows or 'dots' that can be printed.
    #: Together with the dpi this gives the minimum and maximum length
    #: for continuous tape printing.
    min_max_length_dots: Tuple[int, int] = attrib()
    #: The minimum and maximum amount of feeding a label
    min_max_feed: Tuple[int, int] = attrib(default=(35, 1500))
    number_bytes_per_row: int = attrib(default=90)
    #: The required additional offset from the right side
    additional_offset_r: int = attrib(default=0)
    #: Support for the 'mode setting' opcode
    mode_setting: bool = attrib(default=True)
    #: Model has a cutting blade to automatically cut labels
    cutting: bool = attrib(default=True)
    #: Model has support for the 'expanded mode' opcode.
    #: (So far, all models that have cutting support do).
    expanded_mode: bool = attrib(default=True)
    #: Model has support for compressing the transmitted raster data.
    #: Some models with only USB connectivity don't support compression.
    compression: bool = attrib(default=True)
    #: Support for two color printing (black/red/white)
    #: available only on some newer models.
    two_color: bool = attrib(default=False)
    #: Number of NULL bytes needed for the invalidate command.
    num_invalidate_bytes: int = attrib(default=200)

    @property
    def name(self) -> str:
        return self.identifier

ALL_MODELS = [
  Model('QL-500',     (295, 11811), compression=False, mode_setting=False, expanded_mode=False, cutting=False),
  Model('QL-550',     (295, 11811), compression=False, mode_setting=False),
  Model('QL-560',     (295, 11811), compression=False, mode_setting=False),
  Model('QL-570',     (150, 11811), compression=False, mode_setting=False),
  Model('QL-580N',    (150, 11811)),
  Model('QL-600',     (150, 11811)),
  Model('QL-650TD',   (295, 11811)),
  Model('QL-700',     (150, 11811), compression=False, mode_setting=False),
  Model('QL-710W',    (150, 11811)),
  Model('QL-720NW',   (150, 11811)),
  Model('QL-800',     (150, 11811), two_color=True, compression=False, num_invalidate_bytes=400),
  Model('QL-810W',    (150, 11811), two_color=True, num_invalidate_bytes=400),
  Model('QL-820NWB',  (150, 11811), two_color=True, num_invalidate_bytes=400),
  Model('QL-1050',    (295, 35433), number_bytes_per_row=162, additional_offset_r=44),
  Model('QL-1060N',   (295, 35433), number_bytes_per_row=162, additional_offset_r=44),
  Model('QL-1100',    (301, 35434), number_bytes_per_row=162, additional_offset_r=44),
  Model('QL-1100NWB', (301, 35434), number_bytes_per_row=162, additional_offset_r=44),
  Model('QL-1115NWB', (301, 35434), number_bytes_per_row=162, additional_offset_r=44),
]

class ModelsManager(ElementsManager):
    elements = copy.copy(ALL_MODELS)
    element_name = 'model'
