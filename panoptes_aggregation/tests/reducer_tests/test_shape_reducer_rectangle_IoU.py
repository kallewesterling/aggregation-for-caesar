from panoptes_aggregation.reducers.shape_reducer_dbscan import process_data as process_data_dbscan, shape_reducer_dbscan
from .base_test_class import ReducerTest


extracted_data = [
    {
        'frame0': {
            'T0_tool0_x': [1.0],
            'T0_tool0_y': [0.0],
            'T0_tool0_width': [2.0],
            'T0_tool0_height': [2.0]
        }
    },
    {
        'frame0': {
            'T0_tool0_x': [0.0],
            'T0_tool0_y': [1.0],
            'T0_tool0_width': [2.0],
            'T0_tool0_height': [2.0]
        }
    },
    {
        'frame0': {
            'T0_tool0_x': [2.0],
            'T0_tool0_y': [1.0],
            'T0_tool0_width': [2.0],
            'T0_tool0_height': [2.0]
        }
    },
    {
        'frame0': {
            'T0_tool0_x': [1.0],
            'T0_tool0_y': [2.0],
            'T0_tool0_width': [2.0],
            'T0_tool0_height': [2.0]
        }
    },
    {}
]

kwargs_extra_data = {
    'user_id': [
        1,
        2,
        3,
        4,
        5
    ]
}

processed_data = {
    'shape': 'rectangle',
    'symmetric': False,
    'frame0': {
        'T0_tool0': [
            (1.0, 0.0, 2.0, 2.0),
            (0.0, 1.0, 2.0, 2.0),
            (2.0, 1.0, 2.0, 2.0),
            (1.0, 2.0, 2.0, 2.0)
        ],
    }
}

reduced_data = {
    'frame0': {
        'T0_tool0_rectangle_x': [1.0, 0.0, 2.0, 1.0],
        'T0_tool0_rectangle_y': [0.0, 1.0, 1.0, 2.0],
        'T0_tool0_rectangle_width': [2.0, 2.0, 2.0, 2.0],
        'T0_tool0_rectangle_height': [2.0, 2.0, 2.0, 2.0],
        'T0_tool0_cluster_labels': [0, 0, 0, 0],
        'T0_tool0_clusters_count': [4],
        'T0_tool0_clusters_x': [1.0],
        'T0_tool0_clusters_y': [1.0],
        'T0_tool0_clusters_width': [2.0],
        'T0_tool0_clusters_height': [2.0],
        'T0_tool0_clusters_sigma': [0.77],
    }
}

TestShapeReducerRectangle = ReducerTest(
    shape_reducer_dbscan,
    process_data_dbscan,
    extracted_data,
    processed_data,
    reduced_data,
    'Test shape rectangle reducer with DBSCAN and IoU metric',
    network_kwargs=kwargs_extra_data,
    pkwargs={'shape': 'rectangle'},
    kwargs={
        'eps': 0.9,
        'min_samples': 2,
        'metric_type': 'IoU'
    },
    test_name='TestShapeReducerRectangleIoU',
    round=3
)
