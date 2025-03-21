import os
from dataclasses import dataclass

import requests
from colorful_print import color
from locust import FastHttpUser, task, between, events
from locust.env import Environment


@dataclass(frozen=True)
class Config:
    factorial_endpoint = os.getenv("FACTORIAL_ENDPOINT", "/factorial")
    cache_endpoint = os.getenv("CACHE_ENDPOINT", "/cache")


config = Config()


class MyLocustAppUser(FastHttpUser):
    wait_time = between(0.1, 2)

    # def on_start(self) -> None:
    #     response = self.client.get("/liveness").success()
    #     self.client.get("/readiness").raise_for_status()

    @task
    def request_factorial(self):
        if config.factorial_endpoint:
            self.client.get(config.factorial_endpoint)

    @task
    def request_cache(self):
        if config.factorial_endpoint:
            self.client.get(config.cache_endpoint)


@events.test_start.add_listener
def on_test_start(environment: Environment, **kwargs):
    color.green("Starting locust", bold=True)

    def _check(url: str):
        response = requests.get(url)
        response.raise_for_status()
        color.yellow(response.json(), bold=True)

    _check(f"{environment.host}/readiness")
    _check(f"{environment.host}/liveness")


@events.test_stop.add_listener
def on_test_stop(environment: Environment, **kwargs):
    color.green("Stopping locust", bold=True)
