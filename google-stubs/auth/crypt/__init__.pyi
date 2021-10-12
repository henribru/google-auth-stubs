from typing import Any

from google.auth.crypt import base, es256

Signer = base.Signer
Verifier = base.Verifier
RSASigner: Any
RSAVerifier: Any
ES256Signer = es256.ES256Signer
ES256Verifier = es256.ES256Verifier
