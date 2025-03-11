# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Bar(Component):
    """A Bar component.


Keyword arguments:

- allColOptions (optional):
    All currently available column options.

- catColOptions (optional):
    Currently available categorical options.

- config (optional):
    The config the user sets in this component.

- numColOptions (optional):
    Currently available numerical options.

- setProps (optional):
    Dash-assigned callback that should be called to report property
    changes to Dash, to make them available for callbacks."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_express_components'
    _type = 'Bar'
    @_explicitize_args
    def __init__(self, config=Component.UNDEFINED, allColOptions=Component.UNDEFINED, catColOptions=Component.UNDEFINED, numColOptions=Component.UNDEFINED, **kwargs):
        self._prop_names = ['allColOptions', 'catColOptions', 'config', 'numColOptions', 'setProps']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['allColOptions', 'catColOptions', 'config', 'numColOptions', 'setProps']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Bar, self).__init__(**args)
