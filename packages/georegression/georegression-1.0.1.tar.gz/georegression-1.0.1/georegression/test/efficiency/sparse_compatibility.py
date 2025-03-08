from scipy.sparse import csr_array
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.metrics import r2_score

from georegression.stacking_model import StackingWeightModel
from georegression.test.data import load_HP
from georegression.weight_matrix import weight_matrix_from_points
from georegression.weight_model import WeightModel

from time import time as t

X, y_true, xy_vector, time = load_HP()


def test_compatibility():
    weight_matrix = weight_matrix_from_points(
        [xy_vector, time], [xy_vector, time], "euclidean", "bisquare", None, None, 0.1, None
    )

    # Normal case
    t1 = t()
    estimator = WeightModel(
        ExtraTreeRegressor(max_depth=1, splitter="random"),
        "euclidean",
        "bisquare",
        neighbour_count=0.1
    )
    estimator.fit(X, y_true, [xy_vector, time], weight_matrix=weight_matrix)
    t2 = t()
    print(t2 - t1)
    print(estimator.llocv_score_)

    # Sparse case
    weight_matrix = csr_array(weight_matrix)

    t1 = t()
    estimator = WeightModel(
        ExtraTreeRegressor(max_depth=1, splitter="random"),
        "euclidean",
        "bisquare",
        neighbour_count=0.1
    )
    estimator.fit(X, y_true, [xy_vector, time], weight_matrix=weight_matrix)
    t2 = t()
    print(t2 - t1)
    print(estimator.llocv_score_)


def test_stacking_compatibility():
    weight_matrix = weight_matrix_from_points(
        [xy_vector, time],
        [xy_vector, time],
        "euclidean",
        "bisquare", None, None,
        0.1, None
    )

    # Normal case
    estimator = StackingWeightModel(
        ExtraTreeRegressor(max_depth=1, splitter="random"),
        neighbour_leave_out_rate=0.1,
        use_numba=False
    )
    # estimator.fit(X, y_true, [xy_vector, time], weight_matrix=weight_matrix)
    print(estimator.llocv_score_)
    print(estimator.llocv_stacking_)

    # Sparse case
    weight_matrix = csr_array(weight_matrix)

    estimator = StackingWeightModel(
        ExtraTreeRegressor(max_depth=1, splitter="random"),
        neighbour_leave_out_rate=0.1,
        use_numba=False
    )
    estimator.fit(X, y_true, [xy_vector, time], weight_matrix=weight_matrix)
    print(estimator.llocv_score_)
    print(estimator.llocv_stacking_)

    print()

if __name__ == '__main__':
    # test_compatibility()
    test_stacking_compatibility()
