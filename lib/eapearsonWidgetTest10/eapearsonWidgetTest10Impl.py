# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
# BEGIN DS-SERVICE-WIDGET-IMPORT
# Injected by the Dynamic Service Widget Tool
#
from widget.lib.widget_support import WidgetSupport

#
# END DS-SERVICE-WIDGET-IMPORT
#END_HEADER


class eapearsonWidgetTest10:
    '''
    Module Name:
    eapearsonWidgetTest10

    Module Description:
    A KBase module: eapearsonWidgetTest10
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = "c9a275b356018c0a8152d2095d98dea5500f5367"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        # BEGIN DS-WIDGET SETUP-WIDGETS
        # Injected by the Dynamic Service Widget Tool
        #

        # We take the service packcage name from first component of the Python module path.
        service_package_name = __name__.split('.')[:1][0]

        WidgetSupport(
            service_config = config,
            service_package_name = service_package_name,
            service_instance_hash = self.GIT_COMMIT_HASH,
        ).set_global()

        # END DS-WIDGET SETUP-WIDGETS
        #END_CONSTRUCTOR
        pass


    def run_eapearsonWidgetTest10(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_eapearsonWidgetTest10
        report = KBaseReport(self.callback_url)
        report_info = report.create({'report': {'objects_created':[],
                                                'text_message': params['parameter_1']},
                                                'workspace_name': params['workspace_name']})
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }
        #END run_eapearsonWidgetTest10

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_eapearsonWidgetTest10 return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'environ': ctx.get('environ'),
                     'environ_omitted': ctx.get('environ_omitted'),
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
