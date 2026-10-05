# Попроси ChatGPT настроить GitHub Pages

Сам сайт ещё не означает, что он опубликован. Следующий шаг — связать репозиторий с GitHub Pages.

## Запрос

> Настрой публикацию этого репозитория через GitHub Pages и GitHub Actions.
>
> Используй стандартный workflow:
> checkout → configure-pages → build Jekyll → upload artifact → deploy-pages.
>
> Проверь права workflow и зависимости между build и deploy.
>
> После изменения дождись завершения workflow и проверь его результат.

Если инструмент ChatGPT не имеет доступа к настройкам Pages, пользователь один раз выбирает Settings → Pages → Build and deployment → Source → GitHub Actions. После этого дальнейшие публикации выполняются workflow.