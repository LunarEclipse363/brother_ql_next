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
        """
        Returns the printer identifier (already human-readable)
        """
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
  Model('QL-1110NWB', (301, 35434), number_bytes_per_row=162, additional_offset_r=44),
  Model('QL-1115NWB', (301, 35434), number_bytes_per_row=162, additional_offset_r=44),
]


class ModelsJsonSchema():
    SCHEMA_V1 = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://brother-ql-next.lunareclipse.zone/pub/schemas/models-1.0.0",
        "title": "Models",
        "description": "List of supported label printer models",
        "type": "object",
        "properties": {
            "$schema": {
                "description": "Canonical URL of the schema used by this document",
                "type": "string",
                "format": "uri",
            },
            "$version": {
                "description": "Version number following Semver 2.0, equal to the $schema version. Major version change indicates breaking changes.",
                "type": "string",
                "pattern": r"^(?<major>0|[1-9]\d*)\.(?<minor>0|[1-9]\d*)\.(?<patch>0|[1-9]\d*)(?:-(?<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$",
            },
            "models": {
                "description": "The models dict",
                "type": "object",
                "items": {
                    "type": "object",
                    "patternProperties": {
                        "[A-Za-z_][A-Za-z0-9_]*": {
                            "title": "Model",
                            "description": "The description of the properties of a single model",
                            "type": "object",
                            "properties": {
                                "lengthDots": {
                                    "title": "Length (dots)",
                                    "description": "Minimum and maximum tape lengths, in dots, supported by this printer.",
                                    "type": "object",
                                    "properties": {
                                        "min": {
                                            "type": "integer",
                                        },
                                        "max": {
                                            "type": "integer",
                                        },
                                    },
                                    "required": ["min", "max"],
                                    "additionalProperties": False,
                                },
                                "feedDots": {
                                    "title": "Feed (dots)",
                                    "description": "Supported amounts of feed (start/end margins) in dots.",
                                    "type": "object",
                                    "properties": {
                                        "min": {
                                            "type": "integer",
                                        },
                                        "max": {
                                            "type": "integer",
                                        },
                                    },
                                    "required": ["min", "max"],
                                    "additionalProperties": False,
                                },
                                "bytesPerRow": {
                                    "title": "Bytes per row",
                                    "description": "Number of bytes per row printed. Multiply by 8 for number of dots spanning the print head's full width.",
                                    "type": "integer",
                                },
                                "additionalOffsetRight": {
                                    "title": "Additional right-offset",
                                    "type": "integer",
                                },
                                "invalidateBytes": {
                                    "description": "Number of NULL bytes sent for an invalidate command.",
                                    "type": "integer"
                                },
                                "features": {
                                    "title": "Features",
                                    "type": "object",
                                    "properties": {
                                        "modeSetting": {
                                            "description": "Support for the mode setting opcode.",
                                            "type": "boolean",
                                        },
                                        "cutting": {
                                            "description": "Printer has an automatic label cutting blade.",
                                            "type": "boolean",
                                        },
                                        "expandedMode": {
                                            "description": "Support for the expanded mode opcode.",
                                            "type": "boolean",
                                        },
                                        "compression": {
                                            "description": "Support for compressed raster data.",
                                            "type": "boolean",
                                        },
                                        "twoColor": {
                                            "description": "Support for two color printing (black/red/white), requires special labels.",
                                            "type": "boolean",
                                        },
                                    },
                                    "required": ["modeSetting", "cutting", "expandedMode", "compression", "twoColor"],
                                },
                            },
                            "required": ["lengthDots", "feedDots", "bytesPerRow", "additionalOffsetRight", "invalidateBytes", "features"],
                        },
                    },
                    "additionalProperties": False,
                },
            },
        },
        "required": ["$schema", "$version", "models"],
    }
    
    @classmethod
    def schema(cls, version=1):
        """Returns the schema in a json-able form"""

        if version != 1:
            raise Exception("Unsupported schema version")
        
        return cls.SCHEMA_V1

    @classmethod
    def all_models(cls, version=1):
        """Returns the supported models list in a json-able form"""

        if version != 1:
            raise Exception("Unsupported schema version")

        models_object = {
            "$schema": "https://brother-ql-next.lunareclipse.zone/pub/schemas/models-1.0.0",
            "$version": "1.0.0",
            "models": {},
        }

        for model in ALL_MODELS:
            model_object = {
                "lengthDots": { "min": model.min_max_length_dots[0], "max": model.min_max_length_dots[1] },
                "feedDots": { "min": model.min_max_feed[0], "max": model.min_max_feed[1] },
                "bytesPerRow": model.number_bytes_per_row,
                "additionalOffsetRight": model.additional_offset_r,
                "invalidateBytes": model.num_invalidate_bytes,
                "features": {
                    "modeSetting": model.mode_setting,
                    "cutting": model.cutting,
                    "expandedMode": model.expanded_mode,
                    "compression": model.compression,
                    "twoColor": model.two_color,
                },
            }
            models_object["models"][model.identifier] = model_object

        return models_object


class ModelsManager(ElementsManager):
    """
    Class for accessing the list of supported printer models
    """
    elements = copy.copy(ALL_MODELS) #: :meta private:
    element_name = 'model'
