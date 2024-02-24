"""Current institution dependency."""

from fastapi import HTTPException

from db.models import Institution


async def current_institution(institution_name: str = '') -> Institution:
    """Return the current institution"""
    institution = await Institution.find_one(
        Institution.InstitutionName == institution_name
    )
    if institution is None:
        raise HTTPException(404, "Institution not found")
    return institution

