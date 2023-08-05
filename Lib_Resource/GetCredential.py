import io
import yaml
import logging
import os

CONFIG_FILE = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "\\_Safe_\\P1-ISP_access_values.yaml"
yamlFileLocationList = {CONFIG_FILE}


def find_credential(parameter_field):
    """
    API to get the credential related details from various yaml files.

    [Input Description]
        parameter_field        : field that will be retrieved from yaml file.

    [Output Description]
        Returns : value or throws error.
    """

    try:
        for yamlFile in yamlFileLocationList:
            with io.open(yamlFile, 'r') as stream:
                data_loaded = yaml.safe_load(stream)
                # logging.error("data: {}".format(data_loaded))
            check, value = iserror(data_loaded, parameter_field)
            if check:
                # logging.error("Value: {}".format(value))
                return value
    except yaml.YAMLError as exc:
        logging.error(exc)


def iserror(data, parameter):
    """
    :param data: Dictionary database from Yaml File
    :param parameter: search filed
    :return: True / False and the Key-Value or Error message
    """
    try:
        value = data[parameter]
        return True, value
    except Exception as exc:
        return False, str(exc)
