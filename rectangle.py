import param
import panel as pn
import pandas as pd
from common import Common

class Button(param.Parameterized):
    # tab specific submit button
    submit_button = param.Action(lambda x: x.param.trigger('submit_button'), label='Submit')

class rectangle(param.Parameterized):
    length1 = param.Number(default=1, step=1, bounds=(1, 100))
    width1 = param.Number(default=1, step=1, bounds=(1, 100))
    length2 = param.Number(default=1, step=1, bounds=(1, 100))
    width2 = param.Number(default=1, step=1, bounds=(1, 100))
    button = Button()
    common = param.ClassSelector(class_=Common, default=Common())
    df = pd.DataFrame()

    def get_data(self):
        lengths = []
        widths = []
        perimeters = []
        areas = []

        for i in range(1, self.common.number_of_shapes + 1):
            lengths.append(getattr(self, f'length{i}'))
            widths.append(getattr(self, f'width{i}'))
            perimeters.append(2 * (lengths[i - 1] + widths[i - 1]))
            areas.append(lengths[i - 1] * widths[i - 1])

        self.df = pd.DataFrame({
            'Length': lengths,
            'Width': widths,
            'Perimeter': perimeters,
            'Area': areas
        })

    @param.depends('common.select_button')
    def get_first_dashboard(self):
        dimensions = pn.GridBox(ncols=self.common.number_of_shapes)
        for i in range(self.common.number_of_shapes):
            dimensions.append(
                pn.WidgetBox(
                    pn.Param(
                        self,
                        parameters=[f'length{i + 1}'],
                        widgets={
                            f'length{i + 1}': {
                                'widget_type': pn.widgets.IntInput,
                                'name': 'Length:',
                                'width': 115
                            }
                        },
                        show_name=False,
                        default_layout=pn.Column
                    ),
                    pn.Param(
                        self,
                        parameters=[f'width{i + 1}'],
                        widgets={
                            f'width{i + 1}': {
                                'widget_type': pn.widgets.FloatInput,
                                'name': 'Width:',
                                'width': 115
                            }
                        },
                        show_name=False,
                        default_layout=pn.Column
                    ),
                    margin=(4, 2, 4, 2)
                )
            )

        return dimensions

    def get_submit_button(self):
        return pn.Param(
            self.button,
            parameters=['submit_button'],
            widgets={'submit_button': {'button_type': 'primary'}},
            show_name=False
        )

    @pn.depends('common.select_button', 'button.submit_button')
    def get_second_dashboard(self):
        self.get_data()
        logging.info("Done")
        return pn.Card(pn.widgets.Tabulator(self.df))
