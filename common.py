import param
import panel as pn

class Common(param.Parameterized):
    number_of_shapes = param.Number(default=1,step=1.0,bounds=(1,2))
    select_button =  param.Action(lambda x: x.param.trigger('select_button'), label='Select')
