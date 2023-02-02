# Playwright In Containers

A quick proof-of-concept showing Playwright running in one container and Chrome running in another.

## Usage

1. Build the Python container with `docker-compose build`
2. Start the Chrome container running in the background with `docker-compose up chrome`
   1. Optionally, watch the Chrome logs with `docker-compose logs -f chrome`
3. Run the example Playwright script in it's container with `docker-compose run python`
4. See the resulting screenshot in `:/screenshots` as proof of a successful execution
5. Clean-up with `docker-compose down`
