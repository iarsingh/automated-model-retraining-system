class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if not body.get("drift") and int(body.get("age_days") or 0) <= 30: failed.append("no_retrain_needed")
    return {"passed": not failed, "failed": failed, "applied": False}
