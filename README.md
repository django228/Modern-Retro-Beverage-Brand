# Modern Retro Beverage Brand

Пет-проект: вымышленный бренд газировки Retro Fizz, лендинг на Django. Визуально опирался на [макет из Figma Community](https://www.figma.com/site/OwtHf9gFzeH11YEM0tDuvz/Modern-Retro-Beverage-Brand--Community-?node-id=3-561) — пиксель в пиксель через API не гонял, но общая идея (крупная типографика, «витринные» карточки, ретро-настроение) та же.

Репозиторий: [django228/Modern-Retro-Beverage-Brand](https://github.com/django228/Modern-Retro-Beverage-Brand).

## Что внутри

Код разнесён по слоям в духе DDD: доменные модели в `brand/domain`, сценарий главной в `brand/application`, отдача контента из `brand/infrastructure`, вьюха в `brand/presentation`. Шаблоны в `templates/`, стили в `static/`.

Сайт можно гонять как обычное Django-приложение, а для GitHub Pages собирается статика через [django-distill](https://github.com/meeb/django-distill): страницы выгружаются в `dist/`.

Для деплоя в CI задаётся `SITE_BASE_PATH` (имя репозитория), чтобы в HTML попали пути вида `/имя-репоз/static/...` — иначе GitHub Pages отдаёт страницу без стилей (относительный `static/` уезжает на `github.io/static/...`). Локально переменная не нужна.

Картинки из Figma в репозиторий не экспортировались (нет доступа к API файла); вместо них лежат свои SVG в `static/img/` — банка в hero, мини-банки вкусов, иллюстрации линейки, постер в блоке истории.

## Запуск у себя

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
python manage.py runserver
```

Статическая сборка:

```bash
python manage.py distill-local dist --collectstatic --force
```

## CI

В `.github/workflows/ci.yml` — ruff, black, `manage.py check`, pytest, и на `main` после успеха — деплой на GitHub Pages. В настройках репозитория для Pages нужно выбрать источник **GitHub Actions**.
