import panel as pn
from common import Common
from rectangle import rectangle

template = pn.template.BootstrapTemplate(title="Sample")
common = Common()
t1 = rectangle(common=common)

tabs = pn.Tabs(
    ('Rectangle', pn.Column(
        t1.get_first_dashboard,
        t1.get_submit_button,
        t1.get_second_dashboard
    ))
)
sidebar = pn.Column(pn.Param(
        common,
        parameters=['number_of_shapes', 'select_button'],
        widgets={
            'number_of_shapes': {'widget_type': pn.widgets.FloatInput},
            'select_button': {'button_type': 'primary', 'margin': (0, 8, 0, 0)}
        },
        show_name=False
    ))

template.sidebar.append(sidebar)
template.main.append(tabs)
template.servable()
