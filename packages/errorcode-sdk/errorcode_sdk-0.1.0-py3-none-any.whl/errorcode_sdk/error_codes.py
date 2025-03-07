# src/errorcode_sdk/error_codes.py

ERROR_CODES = {
    "GENERIC_ERROR": {
        "P1_DATABASE_CONNECTION": {"errorCode": "DB_CONN_FAIL", "message": "Database connection failed"},
        "P2_TIMEOUT": {"errorCode": "TIMEOUT", "message": "Request timed out"},
    },
    "AUTH_ERROR": {
        "P1_INVALID_TOKEN": {"errorCode": "INVALID_TOKEN", "message": "Token is invalid or expired"},
    }
}

def get_error_code(category: str, error_type: str):
    """
    Retrieve error code details based on category and error type.
    
    :param category: The category of the error (e.g., 'GENERIC_ERROR').
    :param error_type: The specific error type (e.g., 'P1_DATABASE_CONNECTION').
    :return: A dictionary with 'errorCode' and 'message'.
    """
    return ERROR_CODES.get(category, {}).get(error_type, {"errorCode": "UNKNOWN_ERROR", "message": "Unknown error"})
