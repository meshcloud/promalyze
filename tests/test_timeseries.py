from promalyze.timeseries import TimeSeries


class TestTimeSeries:

    @staticmethod
    def named_meta():
        return {
            '__name__': 'test_metric',
            'tag1': 'value1'
        }

    @staticmethod
    def unnamed_meta():
        return {
            'tag1': 'value1'
        }

    @staticmethod
    def ts_data():
        return [
            [1234, 1],
            [5678, 2]
        ]


    def setup(self):
        self.named_timeseries = TimeSeries(self.named_meta(), self.ts_data())
        self.unnamed_timeseries = TimeSeries(self.unnamed_meta(), self.ts_data())

    def teardown(self):
        self.named_timeseries = None
        self.unnamed_timeseries = None

    def test_timestamps(self):
        assert self.named_timeseries.timestamps() == [1234, 5678]
        assert self.unnamed_timeseries.timestamps() == [1234, 5678]

    def test_values(self):
        assert self.named_timeseries.values() == [1, 2]
        assert self.unnamed_timeseries.values() == [1, 2]

    def test_named_as_json(self):
        assert self.named_timeseries.as_json()['values'] == self.ts_data()
        assert self.named_timeseries.as_json()['name'] == 'test_metric'

    def test_unnamed_as_json(self):
        assert self.unnamed_timeseries.as_json()['values'] == self.ts_data()
        assert self.unnamed_timeseries.as_json()['name'] == ''