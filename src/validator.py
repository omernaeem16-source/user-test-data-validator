def validate_name(name):
    errors = []

    if name == "":
        errors.append("Name is empty")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }


def validate_email(email):
    errors = []

    if "@" not in email:
        errors.append("Invalid email")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }


def validate_age(age):
    errors = []

    if age < 18 or age > 100:
        errors.append("Invalid age")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }


def validate_active(active):
    errors = []

    if not isinstance(active, bool):
        errors.append("Invalid Active")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }


def validate_id(user_id):
    errors = []

    if not isinstance(user_id, int) or user_id <= 0:
        errors.append("Invalid ID")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }


def validate_user(user):
    errors = []

    name_result = validate_name(user["name"])
    errors.extend(name_result["errors"])

    email_result = validate_email(user["email"])
    errors.extend(email_result["errors"])

    age_result = validate_age(user["age"])
    errors.extend(age_result["errors"])

    active_result = validate_active(user["active"])
    errors.extend(active_result["errors"])

    id_result = validate_id(user["id"])
    errors.extend(id_result["errors"])

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }