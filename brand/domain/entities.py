from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class NavLink:
    label: str
    href: str


@dataclass(frozen=True, slots=True)
class Flavor:
    name: str
    accent: str
    description: str


@dataclass(frozen=True, slots=True)
class ProductCard:
    title: str
    subtitle: str
    mood: str
    gradient: str


@dataclass(frozen=True, slots=True)
class StatHighlight:
    value: str
    label: str


@dataclass(frozen=True, slots=True)
class LandingContent:
    brand_name: str
    tagline: str
    hero_title: str
    hero_lead: str
    hero_cta_primary: str
    hero_cta_secondary: str
    nav_links: tuple[NavLink, ...]
    flavors: tuple[Flavor, ...]
    products: tuple[ProductCard, ...]
    story_title: str
    story_body: tuple[str, ...]
    stats: tuple[StatHighlight, ...]
    newsletter_heading: str
    newsletter_hint: str
    footer_note: str
    marquee_phrases: tuple[str, ...] = field(default_factory=tuple)
