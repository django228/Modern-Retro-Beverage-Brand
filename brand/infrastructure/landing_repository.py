from __future__ import annotations

from brand.domain.entities import (
    Flavor,
    LandingContent,
    NavLink,
    ProductCard,
    StatHighlight,
)


class LandingRepository:
    def get_landing(self) -> LandingContent:
        return LandingContent(
            brand_name="Retro Fizz",
            tagline="Modern Retro Beverage",
            hero_title="Вкус, который помнит семидесятые",
            hero_lead=(
                "Газировка с характером: меньше сахара, больше яркости. "
                "Холодная банка, тёплый вайб — как в лучших витринах старых супермаркетов."
            ),
            hero_cta_primary="Найти рядом",
            hero_cta_secondary="Состав",
            nav_links=(
                NavLink("Вкусы", "#flavors"),
                NavLink("Линейка", "#lineup"),
                NavLink("История", "#story"),
                NavLink("Контакты", "#footer"),
            ),
            marquee_phrases=(
                "LOW SUGAR",
                "BOLD FLAVOR",
                "ICE COLD",
                "RETRO LABEL",
                "REAL BUBBLES",
                "MADE WITH CARE",
            ),
            flavors=(
                Flavor(
                    name="Ruby Citrus",
                    accent="#e85d4c",
                    description="Грейпфрут, красный апельсин и щепотка морской соли.",
                ),
                Flavor(
                    name="Velvet Cola",
                    accent="#5c3d2e",
                    description="Тёмная карамель, ваниль бобов и мягкая кислинка.",
                ),
                Flavor(
                    name="Neon Berry",
                    accent="#7b5cff",
                    description="Лесные ягоды, лайм и лёгкая мятная свежесть.",
                ),
            ),
            products=(
                ProductCard(
                    title="Sunset Pop",
                    subtitle="Limited",
                    mood="Тёплый закат, хрустящий лёд",
                    gradient="linear-gradient(145deg, #ff6b4a 0%, #ffb347 55%, #fff3e0 100%)",
                ),
                ProductCard(
                    title="Midnight Fizz",
                    subtitle="Classic",
                    mood="Глубокий колор, тонкая искра цитруса",
                    gradient="linear-gradient(145deg, #1a1a2e 0%, #3d2c4d 45%, #6b4e71 100%)",
                ),
                ProductCard(
                    title="Coastal Lime",
                    subtitle="Fresh",
                    mood="Солёный бриз и зелёный лайм",
                    gradient="linear-gradient(145deg, #0f766e 0%, #5eead4 50%, #ecfdf5 100%)",
                ),
            ),
            story_title="Почему мы не играем в «ещё одну газировку»",
            story_body=(
                (
                    "Мы собрали визуальный код ретро-этикеток и современную рецептуру "
                    "без лишнего сиропа. Каждая банка — это маленький постер: крупный шрифт, "
                    "смелые полосы, честный состав."
                ),
                (
                    "Производство небольшими партиями, чтобы держать вкус стабильным, "
                    "а этикетку — живой."
                ),
            ),
            stats=(
                StatHighlight(value="4.2g", label="сахара на 100 мл"),
                StatHighlight(value="0", label="искусственных красителей"),
                StatHighlight(value="12", label="натуральных ароматов"),
            ),
            newsletter_heading="Первыми узнавайте о лимитках",
            newsletter_hint="Почта только для новостей бренда, без лишнего шума.",
            footer_note=(
                "© Retro Fizz — fan-made landing для портфолио. "
                "Дизайн вдохновлён community-макетом."
            ),
        )
