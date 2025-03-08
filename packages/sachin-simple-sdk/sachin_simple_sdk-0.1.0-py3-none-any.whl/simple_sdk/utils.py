def validate_response(data):
    """Ensure API response contains expected fields."""
    if "id" not in data or "name" not in data:
        raise ValueError("Invalid response format")
    return data
