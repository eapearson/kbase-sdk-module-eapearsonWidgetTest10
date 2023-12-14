import json

from widget.lib.widget_base import WidgetBase
from widget.lib.widget_error import WidgetError


class Widget(WidgetBase):
    def get_context(self) -> dict:
        """
        Get the object info, workspace info, and the object itself.
        """
        ref = self.get_param('ref')

        # workspace = GenericClient(
        #     module_name='Workspace',
        #     url = self.config.get('workspace-url'),
        #     token = self.token,
        #     timeout=10000
        # )
        # params = {
        #     'includeMetadata': 1,
        #     'objects': [{'ref': ref}]
        # }
        # try:
        #     object_info = object_info_to_dict(workspace.call_func('get_object_info3', [params])[0]['infos'][0])
        # except WidgetError as werr:
        #     raise werr
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

        # type_module, type_name, _type_version_major, _type_version_minor = re.split(r'[.-]', object_info['type_id'])

        # if type_module != "KBaseStructure" and type_name != "ProteinStructures":
        #     raise WidgetError(
        #         title="Error",
        #         code="incorrect-type",
        #         message=f"Expected an object of type KBaseStructure.ProteinStructures, but got {object_info['type_id']}"
        #     )

        # workspace_id = object_info['workspace_id']

        # workspace_info = workspace_info_to_dict(workspace.call_func('get_workspace_info', [{"id": workspace_id}])[0])

        # params = {
        #     'objects': [{'ref': ref}],
        #     'infostruct': 1
        # }
        # protein_structures_object = workspace.call_func('get_objects2', [params])[0]['data'][0]


        [protein_structures_object, workspace_info] = self.get_object(ref, ["KBaseStructure.ProteinStructures"])

        if 'pdb_infos' not in protein_structures_object["data"]:
            raise WidgetError(
                title='Error',
                code='no-pdb-infos',
                message="No 'pdb_infos' found in the object"
            )

        pdb_infos_json = json.dumps(protein_structures_object["data"]["pdb_infos"])

        return {
            'token': self.token, 
            # 'object_info': object_info, 
            'workspace_info': workspace_info, 
            'ui_origin': self.widget_config.get('ui_origin'),
            'base_path': self.widget_config.get('base_path'),
            'asset_url': self.get_asset_url(),
            'widget_asset_url': self.get_widget_asset_url(),
            'protein_structures_object': protein_structures_object,
            'pdb_infos_json': pdb_infos_json
        }
