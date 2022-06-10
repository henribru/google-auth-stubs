from _typeshed import Incomplete

from google.auth import exceptions as exceptions

SIGN_CALLBACK_CTYPE: Incomplete

def load_offload_lib(offload_lib_path): ...
def load_signer_lib(signer_lib_path): ...
def get_sign_callback(signer_lib, config_file_path): ...
def get_cert(signer_lib, config_file_path): ...

class CustomTlsSigner:
    def __init__(self, enterprise_cert_file_path) -> None: ...
    def load_libraries(self) -> None: ...
    def set_up_custom_key(self) -> None: ...
    def attach_to_ssl_context(self, ctx) -> None: ...