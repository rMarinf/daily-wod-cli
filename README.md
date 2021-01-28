# Daily WOD CLI (WIP)
The idea is to get the daily WOD from Crossfit page and publish it in a communication channel like Telegram, Slack..etc


## Run

```shell
Usage: daily-wod [OPTIONS]

  Get the WOD from Crossfit Web

Options:
  -d, --day TEXT            Select the day of WOD (format:yyyy/mm/dd)
  -sc, --show-content TEXT  Show info in tty or telegram channel (default:
                            tty)

  --help                    Show this message and exit.
```

## Tests

Execute this command to launch the tests

```shell
py.test
```

### Coverage

```shell
pytest --cov=src --cov-report=html --cov-report term-missing test/
```