"""
Module containing helper functions for printing information in a human-readable format
"""

import logging
from typing import Sequence

from brother_ql.labels import FormFactor, LabelsManager

logger = logging.getLogger(__name__)

def textual_label_description(label_sizes_to_include: Sequence[str]) -> str:
    """
    Returns a textual description of labels with the specified sizes
    """
    output = "Supported label sizes:\n"
    output = ""
    fmt = " {label_size:9s} {dots_printable:14s} {label_descr:26s}\n"
    output += fmt.format(label_size="Name", dots_printable="Printable px", label_descr="Description")
    #output += fmt.format(label_size="", dots_printable="width x height", label_descr="")
    for label_size in label_sizes_to_include:
        label = LabelsManager()[label_size]
        if label.form_factor in (FormFactor.DIE_CUT, FormFactor.ROUND_DIE_CUT):
            dp_fmt = "{0:4d} x {1:4d}"
        elif label.form_factor == FormFactor.ENDLESS:
            dp_fmt = "{0:4d}"
        else:
            dp_fmt = " - unknown - "
        dots_printable = dp_fmt.format(*label.dots_printable)
        label_descr = label.name
        output += fmt.format(label_size=label_size, dots_printable=dots_printable, label_descr=label_descr)
    return output

def log_discovered_devices(available_devices, level=logging.INFO):
    """
    Logs all automatically discovered devices to console.
    """
    for dev in available_devices:
        result = {'model': 'unknown'}
        result.update(dev)
        logger.log(level, "  Found a label printer: {identifier}  (model: {model})".format(**result))

def textual_description_discovered_devices(available_devices) -> str:
    # TODO: figure out what is the type of the argument and document it
    output = ""
    for dev in available_devices:
        output += dev['identifier']
    return output
