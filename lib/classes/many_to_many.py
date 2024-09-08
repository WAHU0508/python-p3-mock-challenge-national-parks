class NationalPark:
    all = []
    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("The name should be of string type.")
        if not len(value) >= 3:
            raise ValueError("The name should have more than 3 characters.")
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the name")
        self._name = value
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visits = {}
        for trip in Trip.all:
            if trip.national_park == self:
                if trip.visitor not in visits:
                    visits[trip.visitor] = 0
                visits[trip.visitor] += 1
        if not visits:
            return None
        return max(visits, key=visits.get)

    @classmethod
    def most_visited(cls):
        park_visits = {}
        for trip in Trip.all:
            if trip.national_park not in park_visits:
                park_visits[trip.national_park] = trip.national_park.total_visits()
        return max(park_visits, key=park_visits.get)
class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(visitor, Visitor):
            raise TypeError("visitor should be an instance of Visitor.")
        if not isinstance(national_park, NationalPark):
            raise TypeError("national_park should be an instance of NationalPark.")
        self._visitor = visitor
        self._national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str):
            raise TypeError("The start date should be a string.")
        if not len(value) >= 7:
            raise ValueError("The start date should have at least 7 characters.")
        self._start_date = value
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str):
            raise TypeError("The end date should be a string.")
        if not len(value) >= 7:
            raise ValueError("The end date should have at least 7 characters.")
        self._end_date = value
    @property
    def visitor(self):
        return self._visitor
    @property
    def national_park(self):
        return self._national_park
class Visitor:

    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("The name should be of string type.")
        if not 1 <= len(value) <= 15:
            raise ValueError("The name should have characters between 1 and 15.")
        self._name = value
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        parks_visited = list(trip.national_park for trip in self.trips())
        if park in parks_visited:
            return parks_visited.count(park)
        else:
            return 0