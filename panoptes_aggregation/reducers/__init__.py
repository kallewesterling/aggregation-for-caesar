from .point_reducer import point_reducer
from .point_reducer_hdbscan import point_reducer_hdbscan
from .rectangle_reducer import rectangle_reducer
from .question_reducer import question_reducer
from .survey_reducer import survey_reducer
from .poly_line_text_reducer import poly_line_text_reducer
from .dropdown_reducer import dropdown_reducer
from .process_kwargs import process_kwargs
from .sw_variant_reducer import sw_variant_reducer

reducers = {
    'point_reducer': point_reducer,
    'point_reducer_hdbscan': point_reducer_hdbscan,
    'rectangle_reducer': rectangle_reducer,
    'question_reducer': question_reducer,
    'survey_reducer': survey_reducer,
    'poly_line_text_reducer': poly_line_text_reducer,
    'sw_variant_reducer': sw_variant_reducer,
    'dropdown_reducer': dropdown_reducer
}
