from __future__ import annotations

from brand.domain.entities import LandingContent
from brand.infrastructure.landing_repository import LandingRepository


class GetLandingPage:
    def __init__(self, repository: LandingRepository | None = None) -> None:
        self._repository = repository or LandingRepository()

    def execute(self) -> LandingContent:
        return self._repository.get_landing()
