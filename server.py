import html
import sys
from os import environ
from subprocess import check_output

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

TEMPLATE = """
<ul>
    <li>
        Python runtime version: <code>{my_ver}</code>
    </li>
    <li>
        PyPy exe path: <code>{pypy_exe}</code>
    </li>
    <li>
        PyPy version: <code>{pypy_ver}</code>
    </li>
</ul>
"""


@app.get("/", response_class=HTMLResponse)
def home():
    my_ver = sys.version
    pypy_exe = environ.get("PYPY_EXECUTABLE")
    pypy_ver = (
        check_output([pypy_exe, "--version"], universal_newlines=True)
        if pypy_exe
        else "-"
    )
    d = dict(
        my_ver=my_ver,
        pypy_exe=pypy_exe or "not found",
        pypy_ver=pypy_ver,
    )

    return TEMPLATE.format(**{k: html.escape(v) for k, v in d.items()})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
