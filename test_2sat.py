import TwoSATClassifier

def test_2sat_true():
    two_sat_classifier = TwoSATClassifier.TwoSATClassifier(2, 3)
    two_sat_classifier.add_clause(1, 2)
    two_sat_classifier.add_clause(2, -1)
    two_sat_classifier.add_clause(-1, -2)
    assert two_sat_classifier.is_satisfiable()

def test_2sat_false():
    two_sat_classifier = TwoSATClassifier.TwoSATClassifier(2, 4)
    two_sat_classifier.add_clause(1, 2)
    two_sat_classifier.add_clause(-1, 2)
    two_sat_classifier.add_clause(1, -2)
    two_sat_classifier.add_clause(-1, -2)
    assert not two_sat_classifier.is_satisfiable()