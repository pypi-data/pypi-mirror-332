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

def test_neighbour_leave_out_shrink_rate():
    weight_matrix = weight_matrix_from_points(
        [xy_vector, time], [xy_vector, time], "euclidean", "bisquare", None, None, 0.1, None
    )

    estimator = StackingWeightModel(
        ExtraTreeRegressor(max_depth=1, splitter="random"),
        neighbour_leave_out_rate=0.1,
        use_numba=False,
        neighbour_leave_out_shrink_rate=0.3,
    )
    estimator.fit(X, y_true, [xy_vector, time], weight_matrix=weight_matrix)
    print(estimator.llocv_score_)
    print(estimator.llocv_stacking_)

    weight_matrix = csr_array(weight_matrix)
    estimator.use_numba = True
    estimator.fit(X, y_true, [xy_vector, time], weight_matrix=weight_matrix)
    print(estimator.llocv_score_)
    print(estimator.llocv_stacking_)


def test_meta_fitting_shrink_rate():
    weight_matrix = weight_matrix_from_points(
        [xy_vector, time], [xy_vector, time], "euclidean", "bisquare", None, None, 0.1, None
    )
    
    estimator = StackingWeightModel(
        ExtraTreeRegressor(max_depth=1, splitter="random"),
        neighbour_leave_out_rate=0.1,
        use_numba=False,
        meta_fitting_shrink_rate=0.9,
    )
    estimator.fit(X, y_true, [xy_vector, time], weight_matrix=weight_matrix)
    print(estimator.llocv_score_)
    print(estimator.llocv_stacking_)
    
    weight_matrix = csr_array(weight_matrix)
    estimator.use_numba = True
    estimator.fit(X, y_true, [xy_vector, time], weight_matrix=weight_matrix)
    print(estimator.llocv_score_)
    print(estimator.llocv_stacking_)



if __name__ == '__main__':
    # test_neighbour_leave_out_shrink_rate()
    test_meta_fitting_shrink_rate()