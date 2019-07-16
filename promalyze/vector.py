"""
Handles Promtheus vectors
"""

class Vector(object):
    """
    Vector object to work with Vector datatypes
    """

    def __init__(self, v):
        metric = v['metric']
        if metric is not None and '__name__' in metric:
            self.name = v['metric']['__name__']
            del v['metric']['__name__']
        else:
            self.name = ''

        self.metadata = metric
        self.timestamp = v['value'][0]
        self.value = v['value'][1]

    def as_json(self):
        """
        returns the data in the object as a dict
        :return: dict
        """
        return {
            'name': self.name,
            'metadata': self.metadata,
            'value': self.value
        }