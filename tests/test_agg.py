from fuzzy_agreggate import aggregate

L = 0
M = 1
H = 2

decision_table = [[L, L, L],
                  [L, M, H],
                  [L, H, H]]

categories = [L, M, H]

values = [(0.232, 0.433),
          (0.112, 0.543),
          (0.433, 0.222)]


thresholds = [0.2, 0.4, 0.6, 0.8, 1.0]

thresholds_wf = wf(progression_factor=1.6, n_cats = 5)


def test_wf():
    assert wf(2.0) == [0.0125, 0.25, 0.5, 1]

def test_aggregation():
    assert aggregate(decision_table, categories, values, thresholds_wf) == 0.3242
