import json

from widget.lib.widget_base import WidgetBase


class Widget(WidgetBase):

    def get_context(self) -> dict:
        """
        Get the object info, workspace info, and the object itself.
        """
        raw_params = self.get_param('params')

        params = json.loads(raw_params)

        print('PARAMS', params)

        output_object_ref = params['output_object_ref']
        change_log = params['change_log']

        [genome_object, workspace_info] = self.get_object(output_object_ref, ['KBaseGenomes.Genome'])

        print()
        print('GENOME OBJECT', json.dumps(genome_object, indent=4))
        print()

        return {
            'token': self.token, 
            'workspace_info': workspace_info, 
            'genome_object': genome_object,
            'change_log': change_log,
            'ui_origin': self.widget_config.get('ui_origin'),
            'base_path': self.widget_config.get('base_path'),
            'asset_url': self.get_asset_url(),
            'widget_asset_url': self.get_widget_asset_url()
        }
