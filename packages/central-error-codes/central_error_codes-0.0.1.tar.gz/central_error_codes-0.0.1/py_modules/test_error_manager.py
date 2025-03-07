from central_error_codes.error_code_manager import ErrorCodeManager

def test_error_manager():
    # Initialize ErrorCodeManager with the default path to the errors folder
    error_manager = ErrorCodeManager()

    # Print out all error codes or any specific category
    print("All error codes:", error_manager.get_error_codes())

    # You can test specific categories as well
    print("LLM Gateway Error Codes:", error_manager.get_llm_gateway_error())

if __name__ == "__main__":
    test_error_manager()
