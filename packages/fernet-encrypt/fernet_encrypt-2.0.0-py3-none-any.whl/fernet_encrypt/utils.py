import json
from base64 import b64encode
from collections.abc import Generator
from glob import glob
from pathlib import Path
from time import time

import requests
import socketio
import typer
from requests import PreparedRequest, Response, Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from fernet_encrypt import logger
from fernet_encrypt.__version__ import version

APP_PATH = Path(__file__).parent
KEY_PATH = APP_PATH / "keys"
TOKEN_PATH = APP_PATH / ".fernet-encrypt"


def key_getter() -> Generator[bytes, None, None]:
    keyfiles = sorted(glob(str(KEY_PATH / "*.key")), reverse=True)

    if len(keyfiles) == 0:
        raise Exception("No keyfiles found. Create a key first.")

    for keyfile in keyfiles:
        with open(keyfile, "rb") as f:
            yield f.read()


def key_setter(key: bytes):
    keyfile = KEY_PATH / f"{int(time())}.key"

    with open(keyfile, "wb") as f:
        f.write(key)

    logger.debug(f"Created keyfile: {keyfile}")


class API:
    REMOTE_API = "https://fernet-encrypt.tysonholub.com"

    def __init__(self):
        self.token = self._set_token()
        self.session = Session()
        self.session.headers = {
            "Authorization": f"Bearer {self.token['access_token'] if self.token else ''}",
            "User-Agent": f"fernet-encrypt/v{version}",
        }
        retries = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount(self.REMOTE_API, adapter)

        self.sio = socketio.Client()
        self.sio.on("logged_in", self._handle_logged_in)
        self.sio.on("login", self._handle_login)

    def _set_token(self) -> dict | None:
        try:
            with open(TOKEN_PATH) as f:
                token = json.load(f)
        except FileNotFoundError:
            token = None

        return token

    def _prepare_request(self, method, url, **kwargs) -> PreparedRequest:
        req = requests.Request(method, url, **kwargs)
        prepared_req = self.session.prepare_request(req)

        return prepared_req

    def _make_request(self, prepared_req: PreparedRequest) -> Response:
        if not self.token:
            self.login()
            self.token = self._set_token()
            self._refresh_token(prepared_req=prepared_req)

        response = self.session.send(prepared_req, timeout=5)

        if response.status_code == 401:
            self._refresh_token(prepared_req=prepared_req)
            response = self.session.send(prepared_req, timeout=5)

        try:
            response.raise_for_status()
        except Exception:
            typer.echo(response.text, nl=False)
            raise typer.Exit(1) from None

        return response

    def _refresh_token(self, prepared_req: PreparedRequest | None = None):
        if not self.token:
            raise Exception("No token to refresh. Have you logged in?")

        refresh_token = self.token["refresh_token"]
        response = self.session.post(
            f"{self.REMOTE_API}/cli/refresh_token",
            json={"token": refresh_token},
            headers={"Content-Type": "application/json"},
            timeout=5,
        )

        try:
            response.raise_for_status()
        except Exception:
            typer.echo(response.text, nl=False)
            raise typer.Exit(1) from None

        self.token = response.json()
        self.token.update({
            "refresh_token": refresh_token,
        })

        self.session.headers.update({"Authorization": f"Bearer {self.token['access_token']}"})
        if prepared_req:
            prepared_req.headers.update({"Authorization": f"Bearer {self.token['access_token']}"})

        with open(TOKEN_PATH, "w+") as f:
            json.dump(self.token, f)

    def _handle_login(self, data):
        typer.echo(f"Login in here: {data['login_url']}")

    def _handle_logged_in(self, data):
        with open(TOKEN_PATH, "w+") as f:
            json.dump(data["token"], f)

        self.sio.disconnect()

    def login(self, refresh_token: str | None = None):
        if refresh_token is not None:
            self.token = {
                "refresh_token": refresh_token,
            }
            self._refresh_token()
        else:
            self.sio.connect(self.REMOTE_API)
            self.sio.emit("login")
            self.sio.wait()

    def encrypt(self, input: bytes, name: str) -> bytes:
        prepared_req = self._prepare_request(
            method="POST",
            url=f"{self.REMOTE_API}/api/encrypt",
            json={
                "data": b64encode(input).decode("utf-8"),
                "name": name,
            },
        )
        return self._make_request(prepared_req).content

    def decrypt(self, input: bytes) -> bytes:
        prepared_req = self._prepare_request(
            method="POST",
            url=f"{self.REMOTE_API}/api/decrypt",
            json={
                "data": b64encode(input).decode("utf-8"),
            },
        )

        return self._make_request(prepared_req).content

    def get_keys(self) -> dict:
        prepared_req = self._prepare_request(
            method="GET",
            url=f"{self.REMOTE_API}/api/keys",
        )

        return self._make_request(prepared_req).json()


api = API()
