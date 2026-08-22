from fastapi import Header, HTTPException


def get_access_token(
    authorization: str | None = Header(default=None)
) -> str:
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Access token required"
        )

    parts = authorization.split(" ", 1)

    if (
        len(parts) != 2
        or parts[0].lower() != "bearer"
        or not parts[1].strip()
    ):
        raise HTTPException(
            status_code=401,
            detail="Access token required"
        )

    return parts[1].strip()