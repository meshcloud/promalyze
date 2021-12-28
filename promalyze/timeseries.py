"""
Time Series handling
"""

class TimeSeries(object):
    """
    TimeSeries object handles matrix objects from Prometheus
    """

    def __init__(self, meta, ts):
        self.ts = ts

        if '__name__' in meta:
            self.name = meta['__name__']
            del meta['__name__']
        else:
            self.name = ''

        self.metadata = meta

    def timestamps(self):
        """
        returns all the timestamps as a list
        :return: list
        """
        return [x[0] for x in self.ts]

    def values(self):
        """
        returns all the values as a list
        :return: list
        """
        return [x[1] for x in self.ts]

    def as_json(self):
        """
        transforms the data for this object into a dict
        :return: dict
        """
        return {
            'name': self.name,
            'metadata': self.metadata,
            'values': self.ts
        }