import grp
import getpass
import hashlib

# Imports for MFA
# TODO(6): Uncomment after installing the dependencies
# import pyotp
# import pyqrcode


# MFA
def check_authenticator():
    secret_key = "NeverGonnaGiveYouUpNeverGonnaLet"

    totp_auth = pyotp.totp.TOTP(secret_key).provisioning_uri(
        name='Nicolae Guta',
        issuer_name='Lab ISC'
    )

    qr_code = pyqrcode.create(totp_auth)
    # TODO(7): Display the QR code

    totp = pyotp.TOTP(secret_key)

    # TODO(8): Check the OTP code from the user


def is_user_allowed(user, allowed_group="top_10_manelisti"):
    group = grp.getgrnam(allowed_group)

    # TODO(1): Check if the user is in group

    return False


def pam_sm_authenticate(pamh, flags, argv):
    """
    Handles the authentication of the user. Part of the auth management group.

    :param (PamHandle) pamh: PamHandle object
    :param (list) flags: list of flags passed to this script
    :param (list) argv: list of arguments passed to pam_python.so module.
    :return (int): PAM return code
    """
    # TODO(2): Get username

    if not is_user_allowed(user):
        return pamh.PAM_USER_UNKNOWN

    password = getpass.getpass('Baga parola pe sistem: ')

    # TODO(3): Calculate SHA256 of the password

    # TODO(9): Add Multi-Factor Authentication
    if hex_digest == '13412ffd6149204f40e546ffa9fbd7124b410198a6ba3924f788622b929c8eb2':
        print("Ma distrez si bine fac!")
        # TODO(4): Success
    else:
        print("Ai gresit buzunarul!")

    # TODO(5): Failure


# Needed for the authentication to be successful
def pam_sm_setcred(pamh, flags, argv):
    """
    Handles the credentials change of the user. Part of the passwd management group.

    :param (PamHandle) pamh: PamHandle object
    :param (list) flags: list of flags passed to this script
    :param (list) argv: list of arguments passed to pam_python.so module.
    :return (int): PAM return code
    """
    return pamh.PAM_SUCCESS
