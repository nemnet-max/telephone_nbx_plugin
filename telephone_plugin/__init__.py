from extras.plugins import PluginConfig


class TelephonePluginConfig(PluginConfig):
    name = 'telephone_plugin'
    verbose_name = 'Telephone NetBox Plugin'
    description = 'Telephony Management Plugin for NetBox. Based on phonebox_plugin'
    version = 'v0.0.5-beta.1'
    author = 'Nemtsev Pavel'
    author_email = 'pavel.nemtsev@gmail.com'
    base_url = 'telephone'
    min_version = "2.11.0"
    required_settings = []
    default_settings = {}
    caching_config = {
        '*': None
    }

config = TelephonePluginConfig