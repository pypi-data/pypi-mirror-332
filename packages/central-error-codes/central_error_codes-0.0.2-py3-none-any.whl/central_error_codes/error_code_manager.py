import json
import os

class ErrorCodeManager:
    def __init__(self, errors_dir=None):
        """Initialize the ErrorCodeManager to automatically load error codes."""
        if errors_dir:
            self.errors_dir = errors_dir  # Use the provided directory
        else:
            # Dynamically find the root directory (assuming the script runs from py_modules/src/)
            self.errors_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "errors")

        self.error_codes = self.load_all_errors()

    def load_json(self, file_path):
        """Load a JSON file from the given file path."""
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return {}

    def load_all_errors(self):
        """Load all error codes from the specified error files."""
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        errors_dir = os.path.join(repo_root, "errors")

        main_errors_path = os.path.join(errors_dir, "error-codes.json")
        main_errors = self.load_json(main_errors_path)

        error_codes = {}
        for category, file_name in main_errors.items():
            file_path = os.path.join(self.errors_dir, file_name)
            error_codes[category.lower()] = self.load_json(file_path)
        return error_codes

    def get_error_codes_by_category(self, category):
        """Return error codes for a specific category."""
        return self.error_codes.get(category.lower(), {})
    def get_llm_gateway_error(self):
        """Return LLM Gateway error codes."""
        return self.get_error_codes_by_category("LLM_GW_ERROR")
    def get_cms_error(self):
        """Return CMS error codes."""
        return self.get_error_codes_by_category("CMS_GW_ERROR")
    def get_generic_error(self):
        """Return Generic error codes."""
        return self.get_error_codes_by_category("GENERIC_ERROR")
 
    def get_review_tool_error(self):
        """Return Review tool error codes."""
        return self.get_error_codes_by_category("REVIEW_TOOL_ERROR")
    
    def get_recommendation_tool_error_codes(self):
        """Return Recommendation tool error codes."""
        return self.get_error_codes_by_category("RECOMMENDATION_TOOL_ERROR")
    def get_error_codes(self):
        """Return all error codes as a flat structure."""
        all_error_codes = {}
        for category in self.error_codes.values():
            all_error_codes.update(category) 
        return all_error_codes

def get_error_manager():
    if not hasattr(get_error_manager, "_instance"):
        get_error_manager._instance = ErrorCodeManager()
    return get_error_manager._instance

def main():
    print("Error Code Manager is running!")

    # Get the error manager instance
    manager = get_error_manager()

    # Print all error codes
    all_error_codes = manager.get_all_error_codes()
    print("All Error Codes:")
    print(json.dumps(all_error_codes, indent=4))  # Printing all error codes in a readable format

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    print("Entering the main block...")  # Debugging line
    main()