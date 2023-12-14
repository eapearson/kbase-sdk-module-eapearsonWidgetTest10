from installed_clients.WorkspaceClient import Workspace

from widget.lib.widget_base import WidgetBase
from widget.lib.widget_error import WidgetError
from widget.lib.widget_utils import object_info_to_dict, workspace_info_to_dict


class Widget(WidgetBase):

    def get_context(self) -> dict:
        """
        Get the object info, workspace info, and the object itself.
        """
        ref = self.get_param('ref')

        # get workspace and object infos.
        # workspace = Workspace(
        #     url = self.config.get('workspace-url'),
        #     token = self.token
        # )
        # params = {
        #     'includeMetadata': 1,
        #     'objects': [{'ref': ref}]
        # }
        # try:
        #     object_info = object_info_to_dict(workspace.get_object_info3(params)['infos'][0])
        # except Exception as ex:
        #     raise WidgetError(
        #         title="Error",
        #         code="error-fetching-object",
        #         message=str(ex)) from ex

        # if object_info['size'] > 1_000_000:
        #     raise WidgetError(
        #         title="Error",
        #         code="file-too-big",
        #         message=f"Object too big: {object_info['size']}")

        # workspace_id = object_info['workspace_id']

        # workspace_info = workspace_info_to_dict(workspace.get_workspace_info({"id": workspace_id}))

        # params = {
        #     'objects': [{'ref': ref}],
        #     'infostruct': 1
        # }
        # media_object = workspace.get_objects2(params)['data'][0]

        [media_object, workspace_info] = self.get_object(ref, ['KBaseBiochem.Media'])

        print('MEDIA OBJECT', media_object)

        # for compound in media_object['data']['mediacompounds']:
        #     if 'id' not in compound:
        #         if 'compound_ref' in compound:
        #             if compound['compound_ref'].startswith('kbase/default/compounds/id/'):
        #                 _, _, _, _, compound_id = compound['compound_ref'].split('/')
        #                 compound['id'] = compound_id

        return {
            'token': self.token, 
            # 'object_info': object_info, 
            'workspace_info': workspace_info, 
            'media_object': media_object,
            'ui_origin': self.widget_config.get('ui_origin'),
            'base_path': self.widget_config.get('base_path'),
            'asset_url': self.get_asset_url(),
            'widget_asset_url': self.get_widget_asset_url()
        }
