class Measurement:
    def __init__(self, id, height, weight, age, waist):
        self.id = id
        self.height = height
        self.weight = weight
        self.age = age
        self.waist = waist

    def to_dict(self):
        return {
            'id': self.id,
            'height': self.height,
            'weight': self.weight,
            'age': self.age,
            'waist': self.waist
        }
