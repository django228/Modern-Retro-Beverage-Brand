# Modern Retro Beverage Brand

Пет-проект: вымышленный бренд газировки Retro Fizz, лендинг на Django. Визуально опирался на [макет из Figma Community](https://www.figma.com/site/OwtHf9gFzeH11YEM0tDuvz/Modern-Retro-Beverage-Brand--Community-?node-id=3-561) — пиксель в пиксель через API не гонял, но общая идея (крупная типографика, «витринные» карточки, ретро-настроение) та же.

Репозиторий: [django228/Modern-Retro-Beverage-Brand](https://github.com/django228/Modern-Retro-Beverage-Brand).

## Что внутри

Код разнесён по слоям в духе DDD: доменные модели в `brand/domain`, сценарий главной в `brand/application`, отдача контента из `brand/infrastructure`, вьюха в `brand/presentation`. Шаблоны в `templates/`, стили в `static/`.

Сайт можно гонять как обычное Django-приложение, а для GitHub Pages собирается статика через [django-distill](https://github.com/meeb/django-distill): страницы выгружаются в `dist/`. Ссылки на CSS/JS относительные (`static/...`), чтобы на Pages с подпутём репозитория всё открывалось без отдельного префикса в настройках.

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
