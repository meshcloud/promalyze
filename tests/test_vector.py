from promalyze.vector import Vector


class TestVector:

    @staticmethod
    def meta():
        return {
            '__name__': 'test_metric',
            'tag1': 'value1'
        }

    @staticmethod
    def value():
        return [1234, 1]

    def mock_named_vector(self):
        return {
            'metric': self.meta(),
            'value': self.value()
        }

    def mock_unnamed_vector(self):
        return {
            'metric': {},
            'value': self.value()
        }

    def setup(self):
        self.named_vector = Vector(self.mock_named_vector())
        self.unnamed_vector = Vector(self.mock_unnamed_vector())

    def teardown(self):
        self.named_vector = None
        self.unnamed_vector = None

    def test_valid_as_json(self):
        assert self.named_vector.as_json()['value'] == 1
        assert self.named_vector.as_json()['name'] == 'test_metric'

    def test_invalid_as_json(self):
        assert self.unnamed_vector.as_json()['value'] == 1
        assert self.unnamed_vector.as_json()['name'] == ''

