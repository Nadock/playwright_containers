# Playwright In Containers

A quick proof-of-concept showing [Playwright](https://playwright.dev/python/docs) running in one container and [Chrome](https://github.com/browserless/chrome) running in another.

**This repo is marked as archived as I don't intend to update it. It should work "as-is" but you use it at your own risk, etc, etc.**

## Usage

1. Build the Python container with `docker-compose build`
2. Start the Chrome container running in the background with `docker-compose up chrome`
   1. Optionally, watch the Chrome logs with `docker-compose logs -f chrome`
3. Run the example Playwright script in it's container with `docker-compose run python`
4. See the resulting screenshot in `:/screenshots` as proof of a successful execution
5. Clean-up with `docker-compose down`

## Editing Locally

Dependency management is provided via [PDM](https://github.com/pdm-project/pdm). To get a local install working run `pdm install --dev`.

Additionally, to configure VSCode to see the installed dependencies correctly, add the following to your `:/.vscode/settings.json`:

```json
{
    "python.autoComplete.extraPaths": [
        "__pypackages__/3.11/lib"
    ],
    "python.analysis.extraPaths": [
        "__pypackages__/3.11/lib"
    ]
}
```

## License

The contents of this repo are all licensed under the `MIT` license, please use it as you see fit.
