
import logging

logger = logging.getLogger(__name__)

class ElementsManager(object):
    """
    A class managing a collection of 'elements'.
    Those elements are expected to be objects that
    * can be compared for equality against each other
    * have the attribute .identifier
    """
    elements = []
    element_name = "element"

    def iter_identifiers(self):
        for element in self.elements:
            yield element.identifier

    def iter_elements(self):
        for element in self.elements:
            yield element

    def identifiers(self):
        return list(map(lambda e : e.identifier, self.elements))

    def get(self, identifier, default=None):
        return next(filter(lambda l : l.identifier == identifier, self.elements), default)

    def __getitem__(self, key):
        value = next(filter(lambda l : l.identifier == key, self.elements), None)
        if value is not None:
            return value
        else:
            raise KeyError()
