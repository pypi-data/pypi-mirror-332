# coding: UTF-8
import sys
bstack1111ll1_opy_ = sys.version_info [0] == 2
bstack1ll11l_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11ll1l_opy_ (bstack111l1l1_opy_):
    global bstack1l111_opy_
    bstack1l1lll_opy_ = ord (bstack111l1l1_opy_ [-1])
    bstack1l1llll_opy_ = bstack111l1l1_opy_ [:-1]
    bstack1l11ll1_opy_ = bstack1l1lll_opy_ % len (bstack1l1llll_opy_)
    bstack1l11ll_opy_ = bstack1l1llll_opy_ [:bstack1l11ll1_opy_] + bstack1l1llll_opy_ [bstack1l11ll1_opy_:]
    if bstack1111ll1_opy_:
        bstack11l1111_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll11l_opy_ - (bstack111ll_opy_ + bstack1l1lll_opy_) % bstack11lllll_opy_) for bstack111ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack11l1111_opy_ = str () .join ([chr (ord (char) - bstack1ll11l_opy_ - (bstack111ll_opy_ + bstack1l1lll_opy_) % bstack11lllll_opy_) for bstack111ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack11l1111_opy_)
import atexit
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack1ll11ll111_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack11ll1l11l_opy_, bstack1111ll111_opy_, update, bstack1l111lll1l_opy_,
                                       bstack1l1ll1l11_opy_, bstack111l111l_opy_, bstack11l1l1llll_opy_, bstack11l1l111_opy_,
                                       bstack11111l1ll_opy_, bstack11lll11ll1_opy_, bstack1l1lllllll_opy_, bstack1l11l1ll11_opy_,
                                       bstack11l1lll111_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1111ll11l_opy_)
from browserstack_sdk.bstack11lllll11_opy_ import bstack1l11l1lll1_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack1l111l11ll_opy_
from bstack_utils.capture import bstack11l11llll1_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack111111111_opy_, bstack1lll1l11l1_opy_, bstack1l1l1ll11l_opy_, \
    bstack1l11l111ll_opy_
from bstack_utils.helper import bstack11l1ll1l_opy_, bstack11ll1ll1l1l_opy_, bstack11l111ll1l_opy_, bstack1ll11l1l_opy_, bstack1ll11ll111l_opy_, bstack1l1ll1111l_opy_, \
    bstack11lllll11l1_opy_, \
    bstack11ll1llllll_opy_, bstack1l11l1llll_opy_, bstack1l1111lll_opy_, bstack11lll1111l1_opy_, bstack11ll111l11_opy_, Notset, \
    bstack1l111l1ll_opy_, bstack11ll1l111ll_opy_, bstack11ll1ll111l_opy_, Result, bstack11llll1l1l1_opy_, bstack11ll1l1llll_opy_, bstack111ll1l1ll_opy_, \
    bstack1l1l1111l1_opy_, bstack1llllll1l_opy_, bstack1ll1llll11_opy_, bstack11llll111l1_opy_
from bstack_utils.bstack11ll11l1ll1_opy_ import bstack11ll11lll11_opy_
from bstack_utils.messages import bstack1l11ll111_opy_, bstack1lll11l111_opy_, bstack1ll1l111l_opy_, bstack1l111ll1_opy_, bstack11l1ll111l_opy_, \
    bstack11l1ll11l1_opy_, bstack1ll1l1111l_opy_, bstack11lllll1ll_opy_, bstack1l1lll1l_opy_, bstack1ll1lll111_opy_, \
    bstack1llllll11l_opy_, bstack1llllllll_opy_
from bstack_utils.proxy import bstack1l11ll1l1l_opy_, bstack1lllll1lll_opy_
from bstack_utils.bstack11lll1l11_opy_ import bstack11l11l1111l_opy_, bstack11l111lllll_opy_, bstack11l111ll11l_opy_, bstack11l111ll1l1_opy_, \
    bstack11l111lll1l_opy_, bstack11l111lll11_opy_, bstack11l11l11111_opy_, bstack11ll1l1l_opy_, bstack11l111l1ll1_opy_
from bstack_utils.bstack1l1ll1l111_opy_ import bstack1ll1l111_opy_
from bstack_utils.bstack1l1ll1l1ll_opy_ import bstack1ll1l11ll1_opy_, bstack11ll11ll11_opy_, bstack1l1ll11ll1_opy_, \
    bstack11lll1lll_opy_, bstack11l1llll_opy_
from bstack_utils.bstack11l11l1ll1_opy_ import bstack11l11l1l1l_opy_
from bstack_utils.bstack11l1l1111l_opy_ import bstack111111ll_opy_
import bstack_utils.accessibility as bstack1lllll11ll_opy_
from bstack_utils.bstack11l1l11lll_opy_ import bstack1ll11l1l11_opy_
from bstack_utils.bstack1111ll1l1_opy_ import bstack1111ll1l1_opy_
from browserstack_sdk.__init__ import bstack1lllll11l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1l1l_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack11ll1lllll_opy_ import bstack11ll1lllll_opy_, bstack11ll11ll1_opy_, bstack1111lll1_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1l11ll1lll1_opy_, bstack1llll1111ll_opy_, bstack1llll1lll1l_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack11ll1lllll_opy_ import bstack11ll1lllll_opy_, bstack11ll11ll1_opy_, bstack1111lll1_opy_
bstack11ll11ll_opy_ = None
bstack1l1l1l111_opy_ = None
bstack1llll11l11_opy_ = None
bstack11llll1l11_opy_ = None
bstack1lll1l11_opy_ = None
bstack1ll11l1ll1_opy_ = None
bstack1ll1lllll1_opy_ = None
bstack1l11l1111l_opy_ = None
bstack11l1llll1_opy_ = None
bstack1l11ll11_opy_ = None
bstack1l1l1l1111_opy_ = None
bstack11ll1l11_opy_ = None
bstack1ll1lll1l_opy_ = None
bstack1lll1l1ll_opy_ = bstack11ll1l_opy_ (u"ࠪࠫḗ")
CONFIG = {}
bstack1l111ll1l_opy_ = False
bstack111lllll_opy_ = bstack11ll1l_opy_ (u"ࠫࠬḘ")
bstack1lll1l11l_opy_ = bstack11ll1l_opy_ (u"ࠬ࠭ḙ")
bstack1llll11lll_opy_ = False
bstack1ll1111ll_opy_ = []
bstack1lll1ll11_opy_ = bstack111111111_opy_
bstack111ll111111_opy_ = bstack11ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭Ḛ")
bstack1l11l11l11_opy_ = {}
bstack11l1111ll_opy_ = None
bstack11l1ll1111_opy_ = False
logger = bstack1l111l11ll_opy_.get_logger(__name__, bstack1lll1ll11_opy_)
store = {
    bstack11ll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫḛ"): []
}
bstack111l1l11ll1_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_111llllll1_opy_ = {}
current_test_uuid = None
cli_context = bstack1l11ll1lll1_opy_(
    test_framework_name=bstack1l11l1l1l1_opy_[bstack11ll1l_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔ࠮ࡄࡇࡈࠬḜ")] if bstack11ll111l11_opy_() else bstack1l11l1l1l1_opy_[bstack11ll1l_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࠩḝ")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack1lll1l11ll_opy_(page, bstack1ll1l1l1l_opy_):
    try:
        page.evaluate(bstack11ll1l_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦḞ"),
                      bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨḟ") + json.dumps(
                          bstack1ll1l1l1l_opy_) + bstack11ll1l_opy_ (u"ࠧࢃࡽࠣḠ"))
    except Exception as e:
        print(bstack11ll1l_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀࠦḡ"), e)
def bstack1ll111lll1_opy_(page, message, level):
    try:
        page.evaluate(bstack11ll1l_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣḢ"), bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ḣ") + json.dumps(
            message) + bstack11ll1l_opy_ (u"ࠩ࠯ࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠬḤ") + json.dumps(level) + bstack11ll1l_opy_ (u"ࠪࢁࢂ࠭ḥ"))
    except Exception as e:
        print(bstack11ll1l_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࢀࢃࠢḦ"), e)
def pytest_configure(config):
    global bstack111lllll_opy_
    global CONFIG
    bstack1l1l11lll_opy_ = Config.bstack11l1lll11_opy_()
    config.args = bstack111111ll_opy_.bstack111ll1111ll_opy_(config.args)
    bstack1l1l11lll_opy_.bstack1llllll1ll_opy_(bstack1ll1llll11_opy_(config.getoption(bstack11ll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩḧ"))))
    try:
        bstack1l111l11ll_opy_.bstack11l1llllll1_opy_(config.inipath, config.rootpath)
    except:
        pass
    if cli.is_running():
        bstack11ll1lllll_opy_.invoke(bstack11ll11ll1_opy_.CONNECT, bstack1111lll1_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭Ḩ"), bstack11ll1l_opy_ (u"ࠧ࠱ࠩḩ")))
        config = json.loads(os.environ.get(bstack11ll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠢḪ"), bstack11ll1l_opy_ (u"ࠤࡾࢁࠧḫ")))
        cli.bstack1llllllll11_opy_(bstack1l1111lll_opy_(bstack111lllll_opy_, CONFIG), cli_context.platform_index, bstack1l111lll1l_opy_)
    if cli.bstack1llll11l11l_opy_(bstack1llll1llll1_opy_):
        cli.bstack1llll1111l1_opy_()
        logger.debug(bstack11ll1l_opy_ (u"ࠥࡇࡑࡏࠠࡪࡵࠣࡥࡨࡺࡩࡷࡧࠣࡪࡴࡸࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࠤḬ") + str(cli_context.platform_index) + bstack11ll1l_opy_ (u"ࠦࠧḭ"))
        cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.BEFORE_ALL, bstack1llll1lll1l_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack11ll1l_opy_ (u"ࠧࡽࡨࡦࡰࠥḮ"), None)
    if cli.is_running() and when == bstack11ll1l_opy_ (u"ࠨࡣࡢ࡮࡯ࠦḯ"):
        cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.LOG_REPORT, bstack1llll1lll1l_opy_.PRE, item, call)
    outcome = yield
    if cli.is_running():
        if when == bstack11ll1l_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨḰ"):
            cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.BEFORE_EACH, bstack1llll1lll1l_opy_.POST, item, call, outcome)
        elif when == bstack11ll1l_opy_ (u"ࠣࡥࡤࡰࡱࠨḱ"):
            cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.LOG_REPORT, bstack1llll1lll1l_opy_.POST, item, call, outcome)
        elif when == bstack11ll1l_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦḲ"):
            cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.AFTER_EACH, bstack1llll1lll1l_opy_.POST, item, call, outcome)
        return # skip all existing bstack111l1ll1l11_opy_
    bstack111l1lll1ll_opy_ = item.config.getoption(bstack11ll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬḳ"))
    plugins = item.config.getoption(bstack11ll1l_opy_ (u"ࠦࡵࡲࡵࡨ࡫ࡱࡷࠧḴ"))
    report = outcome.get_result()
    bstack111l1lllll1_opy_(item, call, report)
    if bstack11ll1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡴࡱࡻࡧࡪࡰࠥḵ") not in plugins or bstack11ll111l11_opy_():
        return
    summary = []
    driver = getattr(item, bstack11ll1l_opy_ (u"ࠨ࡟ࡥࡴ࡬ࡺࡪࡸࠢḶ"), None)
    page = getattr(item, bstack11ll1l_opy_ (u"ࠢࡠࡲࡤ࡫ࡪࠨḷ"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack111l1lll11l_opy_(item, report, summary, bstack111l1lll1ll_opy_)
    if (page is not None):
        bstack111l1l11lll_opy_(item, report, summary, bstack111l1lll1ll_opy_)
def bstack111l1lll11l_opy_(item, report, summary, bstack111l1lll1ll_opy_):
    if report.when == bstack11ll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧḸ") and report.skipped:
        bstack11l111l1ll1_opy_(report)
    if report.when in [bstack11ll1l_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣḹ"), bstack11ll1l_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧḺ")]:
        return
    if not bstack1ll11ll111l_opy_():
        return
    try:
        if (str(bstack111l1lll1ll_opy_).lower() != bstack11ll1l_opy_ (u"ࠫࡹࡸࡵࡦࠩḻ") and not cli.is_running()):
            item._driver.execute_script(
                bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪḼ") + json.dumps(
                    report.nodeid) + bstack11ll1l_opy_ (u"࠭ࡽࡾࠩḽ"))
        os.environ[bstack11ll1l_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪḾ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack11ll1l_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧ࠽ࠤࢀ࠶ࡽࠣḿ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11ll1l_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦṀ")))
    bstack11l1lll1_opy_ = bstack11ll1l_opy_ (u"ࠥࠦṁ")
    bstack11l111l1ll1_opy_(report)
    if not passed:
        try:
            bstack11l1lll1_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack11ll1l_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡲࡦࡣࡶࡳࡳࡀࠠࡼ࠲ࢀࠦṂ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack11l1lll1_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack11ll1l_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢṃ")))
        bstack11l1lll1_opy_ = bstack11ll1l_opy_ (u"ࠨࠢṄ")
        if not passed:
            try:
                bstack11l1lll1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11ll1l_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡵࡩࡦࡹ࡯࡯࠼ࠣࡿ࠵ࢃࠢṅ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack11l1lll1_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤ࠯ࠤࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡩࡧࡴࡢࠤ࠽ࠤࠬṆ")
                    + json.dumps(bstack11ll1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠣࠥṇ"))
                    + bstack11ll1l_opy_ (u"ࠥࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࠨṈ")
                )
            else:
                item._driver.execute_script(
                    bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡦࡤࡸࡦࠨ࠺ࠡࠩṉ")
                    + json.dumps(str(bstack11l1lll1_opy_))
                    + bstack11ll1l_opy_ (u"ࠧࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠣṊ")
                )
        except Exception as e:
            summary.append(bstack11ll1l_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡦࡴ࡮ࡰࡶࡤࡸࡪࡀࠠࡼ࠲ࢀࠦṋ").format(e))
def bstack111l1l1ll1l_opy_(test_name, error_message):
    try:
        bstack111ll11111l_opy_ = []
        bstack1l111l1l11_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧṌ"), bstack11ll1l_opy_ (u"ࠨ࠲ࠪṍ"))
        bstack111lll1ll_opy_ = {bstack11ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧṎ"): test_name, bstack11ll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩṏ"): error_message, bstack11ll1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪṐ"): bstack1l111l1l11_opy_}
        bstack111l1l1llll_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠬࡶࡷࡠࡲࡼࡸࡪࡹࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪṑ"))
        if os.path.exists(bstack111l1l1llll_opy_):
            with open(bstack111l1l1llll_opy_) as f:
                bstack111ll11111l_opy_ = json.load(f)
        bstack111ll11111l_opy_.append(bstack111lll1ll_opy_)
        with open(bstack111l1l1llll_opy_, bstack11ll1l_opy_ (u"࠭ࡷࠨṒ")) as f:
            json.dump(bstack111ll11111l_opy_, f)
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡩࡷࡹࡩࡴࡶ࡬ࡲ࡬ࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡴࡾࡺࡥࡴࡶࠣࡩࡷࡸ࡯ࡳࡵ࠽ࠤࠬṓ") + str(e))
def bstack111l1l11lll_opy_(item, report, summary, bstack111l1lll1ll_opy_):
    if report.when in [bstack11ll1l_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢṔ"), bstack11ll1l_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦṕ")]:
        return
    if (str(bstack111l1lll1ll_opy_).lower() != bstack11ll1l_opy_ (u"ࠪࡸࡷࡻࡥࠨṖ")):
        bstack1lll1l11ll_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack11ll1l_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨṗ")))
    bstack11l1lll1_opy_ = bstack11ll1l_opy_ (u"ࠧࠨṘ")
    bstack11l111l1ll1_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack11l1lll1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack11ll1l_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨṙ").format(e)
                )
        try:
            if passed:
                bstack11l1llll_opy_(getattr(item, bstack11ll1l_opy_ (u"ࠧࡠࡲࡤ࡫ࡪ࠭Ṛ"), None), bstack11ll1l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣṛ"))
            else:
                error_message = bstack11ll1l_opy_ (u"ࠩࠪṜ")
                if bstack11l1lll1_opy_:
                    bstack1ll111lll1_opy_(item._page, str(bstack11l1lll1_opy_), bstack11ll1l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤṝ"))
                    bstack11l1llll_opy_(getattr(item, bstack11ll1l_opy_ (u"ࠫࡤࡶࡡࡨࡧࠪṞ"), None), bstack11ll1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧṟ"), str(bstack11l1lll1_opy_))
                    error_message = str(bstack11l1lll1_opy_)
                else:
                    bstack11l1llll_opy_(getattr(item, bstack11ll1l_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬṠ"), None), bstack11ll1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢṡ"))
                bstack111l1l1ll1l_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack11ll1l_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡵࡱࡦࡤࡸࡪࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽ࠳ࢁࠧṢ").format(e))
def pytest_addoption(parser):
    parser.addoption(bstack11ll1l_opy_ (u"ࠤ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨṣ"), default=bstack11ll1l_opy_ (u"ࠥࡊࡦࡲࡳࡦࠤṤ"), help=bstack11ll1l_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡩࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠥṥ"))
    parser.addoption(bstack11ll1l_opy_ (u"ࠧ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦṦ"), default=bstack11ll1l_opy_ (u"ࠨࡆࡢ࡮ࡶࡩࠧṧ"), help=bstack11ll1l_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡪࡥࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠨṨ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack11ll1l_opy_ (u"ࠣ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠥṩ"), action=bstack11ll1l_opy_ (u"ࠤࡶࡸࡴࡸࡥࠣṪ"), default=bstack11ll1l_opy_ (u"ࠥࡧ࡭ࡸ࡯࡮ࡧࠥṫ"),
                         help=bstack11ll1l_opy_ (u"ࠦࡉࡸࡩࡷࡧࡵࠤࡹࡵࠠࡳࡷࡱࠤࡹ࡫ࡳࡵࡵࠥṬ"))
def bstack11l11l1lll_opy_(log):
    if not (log[bstack11ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ṭ")] and log[bstack11ll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧṮ")].strip()):
        return
    active = bstack11l1l1l111_opy_()
    log = {
        bstack11ll1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ṯ"): log[bstack11ll1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧṰ")],
        bstack11ll1l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬṱ"): bstack11l111ll1l_opy_().isoformat() + bstack11ll1l_opy_ (u"ࠪ࡞ࠬṲ"),
        bstack11ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬṳ"): log[bstack11ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭Ṵ")],
    }
    if active:
        if active[bstack11ll1l_opy_ (u"࠭ࡴࡺࡲࡨࠫṵ")] == bstack11ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࠬṶ"):
            log[bstack11ll1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨṷ")] = active[bstack11ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩṸ")]
        elif active[bstack11ll1l_opy_ (u"ࠪࡸࡾࡶࡥࠨṹ")] == bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࠩṺ"):
            log[bstack11ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬṻ")] = active[bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭Ṽ")]
    bstack1ll11l1l11_opy_.bstack1l1lllll_opy_([log])
def bstack11l1l1l111_opy_():
    if len(store[bstack11ll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫṽ")]) > 0 and store[bstack11ll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬṾ")][-1]:
        return {
            bstack11ll1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧṿ"): bstack11ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨẀ"),
            bstack11ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫẁ"): store[bstack11ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩẂ")][-1]
        }
    if store.get(bstack11ll1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪẃ"), None):
        return {
            bstack11ll1l_opy_ (u"ࠧࡵࡻࡳࡩࠬẄ"): bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹ࠭ẅ"),
            bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩẆ"): store[bstack11ll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧẇ")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.INIT_TEST, bstack1llll1lll1l_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.INIT_TEST, bstack1llll1lll1l_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.TEST, bstack1llll1lll1l_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._111l1llll11_opy_ = True
        bstack11llll1l1_opy_ = bstack1lllll11ll_opy_.bstack1lll1llll_opy_(bstack11ll1llllll_opy_(item.own_markers))
        if not cli.bstack1llll11l11l_opy_(bstack1llll1llll1_opy_):
            item._a11y_test_case = bstack11llll1l1_opy_
            if bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪẈ"), None):
                driver = getattr(item, bstack11ll1l_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ẉ"), None)
                item._a11y_started = bstack1lllll11ll_opy_.bstack1ll11ll11_opy_(driver, bstack11llll1l1_opy_)
        if not bstack1ll11l1l11_opy_.on() or bstack111ll111111_opy_ != bstack11ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭Ẋ"):
            return
        global current_test_uuid #, bstack11l1l111l1_opy_
        bstack111lll1l11_opy_ = {
            bstack11ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬẋ"): uuid4().__str__(),
            bstack11ll1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬẌ"): bstack11l111ll1l_opy_().isoformat() + bstack11ll1l_opy_ (u"ࠩ࡝ࠫẍ")
        }
        current_test_uuid = bstack111lll1l11_opy_[bstack11ll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨẎ")]
        store[bstack11ll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨẏ")] = bstack111lll1l11_opy_[bstack11ll1l_opy_ (u"ࠬࡻࡵࡪࡦࠪẐ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _111llllll1_opy_[item.nodeid] = {**_111llllll1_opy_[item.nodeid], **bstack111lll1l11_opy_}
        bstack111l1l11l11_opy_(item, _111llllll1_opy_[item.nodeid], bstack11ll1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧẑ"))
    except Exception as err:
        print(bstack11ll1l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡲࡶࡰࡷࡩࡸࡺ࡟ࡤࡣ࡯ࡰ࠿ࠦࡻࡾࠩẒ"), str(err))
def pytest_runtest_setup(item):
    store[bstack11ll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬẓ")] = item
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.BEFORE_EACH, bstack1llll1lll1l_opy_.PRE, item, bstack11ll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨẔ"))
        return # skip all existing bstack111l1ll1l11_opy_
    global bstack111l1l11ll1_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack11lll1111l1_opy_():
        atexit.register(bstack1l1ll11lll_opy_)
        if not bstack111l1l11ll1_opy_:
            try:
                bstack111l1llll1l_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack11llll111l1_opy_():
                    bstack111l1llll1l_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack111l1llll1l_opy_:
                    signal.signal(s, bstack111l1llllll_opy_)
                bstack111l1l11ll1_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack11ll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡨ࡫ࡶࡸࡪࡸࠠࡴ࡫ࡪࡲࡦࡲࠠࡩࡣࡱࡨࡱ࡫ࡲࡴ࠼ࠣࠦẕ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11l11l1111l_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack11ll1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫẖ")
    try:
        if not bstack1ll11l1l11_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack111lll1l11_opy_ = {
            bstack11ll1l_opy_ (u"ࠬࡻࡵࡪࡦࠪẗ"): uuid,
            bstack11ll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪẘ"): bstack11l111ll1l_opy_().isoformat() + bstack11ll1l_opy_ (u"࡛ࠧࠩẙ"),
            bstack11ll1l_opy_ (u"ࠨࡶࡼࡴࡪ࠭ẚ"): bstack11ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱࠧẛ"),
            bstack11ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ẜ"): bstack11ll1l_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩẝ"),
            bstack11ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨẞ"): bstack11ll1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬẟ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack11ll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫẠ")] = item
        store[bstack11ll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬạ")] = [uuid]
        if not _111llllll1_opy_.get(item.nodeid, None):
            _111llllll1_opy_[item.nodeid] = {bstack11ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨẢ"): [], bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬả"): []}
        _111llllll1_opy_[item.nodeid][bstack11ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪẤ")].append(bstack111lll1l11_opy_[bstack11ll1l_opy_ (u"ࠬࡻࡵࡪࡦࠪấ")])
        _111llllll1_opy_[item.nodeid + bstack11ll1l_opy_ (u"࠭࠭ࡴࡧࡷࡹࡵ࠭Ầ")] = bstack111lll1l11_opy_
        bstack111l1l1l11l_opy_(item, bstack111lll1l11_opy_, bstack11ll1l_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨầ"))
    except Exception as err:
        print(bstack11ll1l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡳࡷࡱࡸࡪࡹࡴࡠࡵࡨࡸࡺࡶ࠺ࠡࡽࢀࠫẨ"), str(err))
def pytest_runtest_teardown(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.TEST, bstack1llll1lll1l_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.AFTER_EACH, bstack1llll1lll1l_opy_.PRE, item, bstack11ll1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫẩ"))
        return # skip all existing bstack111l1ll1l11_opy_
    try:
        global bstack1l11l11l11_opy_
        bstack1l111l1l11_opy_ = 0
        if bstack1llll11lll_opy_ is True:
            bstack1l111l1l11_opy_ = int(os.environ.get(bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪẪ")))
        if bstack1l1l11ll11_opy_.bstack1l1l1l1l1_opy_() == bstack11ll1l_opy_ (u"ࠦࡹࡸࡵࡦࠤẫ"):
            if bstack1l1l11ll11_opy_.bstack11l11l1ll_opy_() == bstack11ll1l_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢẬ"):
                bstack111l1lll111_opy_ = bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩậ"), None)
                bstack1lllll1l11_opy_ = bstack111l1lll111_opy_ + bstack11ll1l_opy_ (u"ࠢ࠮ࡶࡨࡷࡹࡩࡡࡴࡧࠥẮ")
                driver = getattr(item, bstack11ll1l_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩắ"), None)
                bstack11111111_opy_ = getattr(item, bstack11ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧẰ"), None)
                bstack1ll1ll111l_opy_ = getattr(item, bstack11ll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨằ"), None)
                PercySDK.screenshot(driver, bstack1lllll1l11_opy_, bstack11111111_opy_=bstack11111111_opy_, bstack1ll1ll111l_opy_=bstack1ll1ll111l_opy_, bstack1ll1lllll_opy_=bstack1l111l1l11_opy_)
        if not cli.bstack1llll11l11l_opy_(bstack1llll1llll1_opy_):
            if getattr(item, bstack11ll1l_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡷࡹࡧࡲࡵࡧࡧࠫẲ"), False):
                bstack1l11l1lll1_opy_.bstack1ll1111lll_opy_(getattr(item, bstack11ll1l_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ẳ"), None), bstack1l11l11l11_opy_, logger, item)
        if not bstack1ll11l1l11_opy_.on():
            return
        bstack111lll1l11_opy_ = {
            bstack11ll1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫẴ"): uuid4().__str__(),
            bstack11ll1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫẵ"): bstack11l111ll1l_opy_().isoformat() + bstack11ll1l_opy_ (u"ࠨ࡜ࠪẶ"),
            bstack11ll1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧặ"): bstack11ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨẸ"),
            bstack11ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧẹ"): bstack11ll1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩẺ"),
            bstack11ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩẻ"): bstack11ll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩẼ")
        }
        _111llllll1_opy_[item.nodeid + bstack11ll1l_opy_ (u"ࠨ࠯ࡷࡩࡦࡸࡤࡰࡹࡱࠫẽ")] = bstack111lll1l11_opy_
        bstack111l1l1l11l_opy_(item, bstack111lll1l11_opy_, bstack11ll1l_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪẾ"))
    except Exception as err:
        print(bstack11ll1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡵࡹࡳࡺࡥࡴࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲ࠿ࠦࡻࡾࠩế"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack11l111ll1l1_opy_(fixturedef.argname):
        store[bstack11ll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡯ࡴࡦ࡯ࠪỀ")] = request.node
    elif bstack11l111lll1l_opy_(fixturedef.argname):
        store[bstack11ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡣ࡭ࡣࡶࡷࡤ࡯ࡴࡦ࡯ࠪề")] = request.node
    if not bstack1ll11l1l11_opy_.on():
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.SETUP_FIXTURE, bstack1llll1lll1l_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.SETUP_FIXTURE, bstack1llll1lll1l_opy_.POST, fixturedef, request, outcome)
        return # skip all existing bstack111l1ll1l11_opy_
    start_time = datetime.datetime.now()
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.SETUP_FIXTURE, bstack1llll1lll1l_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.SETUP_FIXTURE, bstack1llll1lll1l_opy_.POST, fixturedef, request, outcome)
        return # skip all existing bstack111l1ll1l11_opy_
    try:
        fixture = {
            bstack11ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫỂ"): fixturedef.argname,
            bstack11ll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧể"): bstack11lllll11l1_opy_(outcome),
            bstack11ll1l_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪỄ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack11ll1l_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭ễ")]
        if not _111llllll1_opy_.get(current_test_item.nodeid, None):
            _111llllll1_opy_[current_test_item.nodeid] = {bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬỆ"): []}
        _111llllll1_opy_[current_test_item.nodeid][bstack11ll1l_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭ệ")].append(fixture)
    except Exception as err:
        logger.debug(bstack11ll1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡤࡹࡥࡵࡷࡳ࠾ࠥࢁࡽࠨỈ"), str(err))
if bstack11ll111l11_opy_() and bstack1ll11l1l11_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.STEP, bstack1llll1lll1l_opy_.PRE, request, step)
            return
        try:
            _111llllll1_opy_[request.node.nodeid][bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩỉ")].bstack1lllllll1l_opy_(id(step))
        except Exception as err:
            print(bstack11ll1l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰ࠻ࠢࡾࢁࠬỊ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.STEP, bstack1llll1lll1l_opy_.POST, request, step, exception)
            return
        try:
            _111llllll1_opy_[request.node.nodeid][bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫị")].bstack11l11lllll_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack11ll1l_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤࡹࡴࡦࡲࡢࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂ࠭Ọ"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.STEP, bstack1llll1lll1l_opy_.POST, request, step)
            return
        try:
            bstack11l11l1ll1_opy_: bstack11l11l1l1l_opy_ = _111llllll1_opy_[request.node.nodeid][bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ọ")]
            bstack11l11l1ll1_opy_.bstack11l11lllll_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack11ll1l_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡴࡶࡨࡴࡤ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠨỎ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack111ll111111_opy_
        try:
            if not bstack1ll11l1l11_opy_.on() or bstack111ll111111_opy_ != bstack11ll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩỏ"):
                return
            if cli.is_running():
                cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.TEST, bstack1llll1lll1l_opy_.PRE, request, feature, scenario)
                return
            driver = bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬỐ"), None)
            if not _111llllll1_opy_.get(request.node.nodeid, None):
                _111llllll1_opy_[request.node.nodeid] = {}
            bstack11l11l1ll1_opy_ = bstack11l11l1l1l_opy_.bstack111lllll1l1_opy_(
                scenario, feature, request.node,
                name=bstack11l111lll11_opy_(request.node, scenario),
                started_at=bstack1l1ll1111l_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack11ll1l_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩố"),
                tags=bstack11l11l11111_opy_(feature, scenario),
                bstack11l11l11l1_opy_=bstack1ll11l1l11_opy_.bstack11l11ll111_opy_(driver) if driver and driver.session_id else {}
            )
            _111llllll1_opy_[request.node.nodeid][bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫỒ")] = bstack11l11l1ll1_opy_
            bstack111ll1111l1_opy_(bstack11l11l1ll1_opy_.uuid)
            bstack1ll11l1l11_opy_.bstack11l11ll1l1_opy_(bstack11ll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪồ"), bstack11l11l1ll1_opy_)
        except Exception as err:
            print(bstack11ll1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬỔ"), str(err))
def bstack111l1ll1ll1_opy_(bstack11l11l1l11_opy_):
    if bstack11l11l1l11_opy_ in store[bstack11ll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨổ")]:
        store[bstack11ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩỖ")].remove(bstack11l11l1l11_opy_)
def bstack111ll1111l1_opy_(test_uuid):
    store[bstack11ll1l_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪỗ")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack1ll11l1l11_opy_.bstack111lll111ll_opy_
def bstack111l1lllll1_opy_(item, call, report):
    logger.debug(bstack11ll1l_opy_ (u"ࠧࡩࡣࡱࡨࡱ࡫࡟ࡰ࠳࠴ࡽࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡷࡹࡧࡲࡵࠩỘ"))
    global bstack111ll111111_opy_
    bstack11lllll1_opy_ = bstack1l1ll1111l_opy_()
    if hasattr(report, bstack11ll1l_opy_ (u"ࠨࡵࡷࡳࡵ࠭ộ")):
        bstack11lllll1_opy_ = bstack11llll1l1l1_opy_(report.stop)
    elif hasattr(report, bstack11ll1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࠨỚ")):
        bstack11lllll1_opy_ = bstack11llll1l1l1_opy_(report.start)
    try:
        if getattr(report, bstack11ll1l_opy_ (u"ࠪࡻ࡭࡫࡮ࠨớ"), bstack11ll1l_opy_ (u"ࠫࠬỜ")) == bstack11ll1l_opy_ (u"ࠬࡩࡡ࡭࡮ࠪờ"):
            logger.debug(bstack11ll1l_opy_ (u"࠭ࡨࡢࡰࡧࡰࡪࡥ࡯࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴ࠻ࠢࡶࡸࡦࡺࡥࠡ࠯ࠣࡿࢂ࠲ࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠣ࠱ࠥࢁࡽࠨỞ").format(getattr(report, bstack11ll1l_opy_ (u"ࠧࡸࡪࡨࡲࠬở"), bstack11ll1l_opy_ (u"ࠨࠩỠ")).__str__(), bstack111ll111111_opy_))
            if bstack111ll111111_opy_ == bstack11ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩỡ"):
                _111llllll1_opy_[item.nodeid][bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨỢ")] = bstack11lllll1_opy_
                bstack111l1l11l11_opy_(item, _111llllll1_opy_[item.nodeid], bstack11ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ợ"), report, call)
                store[bstack11ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩỤ")] = None
            elif bstack111ll111111_opy_ == bstack11ll1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥụ"):
                bstack11l11l1ll1_opy_ = _111llllll1_opy_[item.nodeid][bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪỦ")]
                bstack11l11l1ll1_opy_.set(hooks=_111llllll1_opy_[item.nodeid].get(bstack11ll1l_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧủ"), []))
                exception, bstack11l1l1l11l_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack11l1l1l11l_opy_ = [call.excinfo.exconly(), getattr(report, bstack11ll1l_opy_ (u"ࠩ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠨỨ"), bstack11ll1l_opy_ (u"ࠪࠫứ"))]
                bstack11l11l1ll1_opy_.stop(time=bstack11lllll1_opy_, result=Result(result=getattr(report, bstack11ll1l_opy_ (u"ࠫࡴࡻࡴࡤࡱࡰࡩࠬỪ"), bstack11ll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬừ")), exception=exception, bstack11l1l1l11l_opy_=bstack11l1l1l11l_opy_))
                bstack1ll11l1l11_opy_.bstack11l11ll1l1_opy_(bstack11ll1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨỬ"), _111llllll1_opy_[item.nodeid][bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪử")])
        elif getattr(report, bstack11ll1l_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭Ữ"), bstack11ll1l_opy_ (u"ࠩࠪữ")) in [bstack11ll1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩỰ"), bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ự")]:
            logger.debug(bstack11ll1l_opy_ (u"ࠬ࡮ࡡ࡯ࡦ࡯ࡩࡤࡵ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺ࠺ࠡࡵࡷࡥࡹ࡫ࠠ࠮ࠢࡾࢁ࠱ࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠢ࠰ࠤࢀࢃࠧỲ").format(getattr(report, bstack11ll1l_opy_ (u"࠭ࡷࡩࡧࡱࠫỳ"), bstack11ll1l_opy_ (u"ࠧࠨỴ")).__str__(), bstack111ll111111_opy_))
            bstack11l11l11ll_opy_ = item.nodeid + bstack11ll1l_opy_ (u"ࠨ࠯ࠪỵ") + getattr(report, bstack11ll1l_opy_ (u"ࠩࡺ࡬ࡪࡴࠧỶ"), bstack11ll1l_opy_ (u"ࠪࠫỷ"))
            if getattr(report, bstack11ll1l_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬỸ"), False):
                hook_type = bstack11ll1l_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪỹ") if getattr(report, bstack11ll1l_opy_ (u"࠭ࡷࡩࡧࡱࠫỺ"), bstack11ll1l_opy_ (u"ࠧࠨỻ")) == bstack11ll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧỼ") else bstack11ll1l_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ỽ")
                _111llllll1_opy_[bstack11l11l11ll_opy_] = {
                    bstack11ll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨỾ"): uuid4().__str__(),
                    bstack11ll1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨỿ"): bstack11lllll1_opy_,
                    bstack11ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨἀ"): hook_type
                }
            _111llllll1_opy_[bstack11l11l11ll_opy_][bstack11ll1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫἁ")] = bstack11lllll1_opy_
            bstack111l1ll1ll1_opy_(_111llllll1_opy_[bstack11l11l11ll_opy_][bstack11ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬἂ")])
            bstack111l1l1l11l_opy_(item, _111llllll1_opy_[bstack11l11l11ll_opy_], bstack11ll1l_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪἃ"), report, call)
            if getattr(report, bstack11ll1l_opy_ (u"ࠩࡺ࡬ࡪࡴࠧἄ"), bstack11ll1l_opy_ (u"ࠪࠫἅ")) == bstack11ll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪἆ"):
                if getattr(report, bstack11ll1l_opy_ (u"ࠬࡵࡵࡵࡥࡲࡱࡪ࠭ἇ"), bstack11ll1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭Ἀ")) == bstack11ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧἉ"):
                    bstack111lll1l11_opy_ = {
                        bstack11ll1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭Ἂ"): uuid4().__str__(),
                        bstack11ll1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭Ἃ"): bstack1l1ll1111l_opy_(),
                        bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨἌ"): bstack1l1ll1111l_opy_()
                    }
                    _111llllll1_opy_[item.nodeid] = {**_111llllll1_opy_[item.nodeid], **bstack111lll1l11_opy_}
                    bstack111l1l11l11_opy_(item, _111llllll1_opy_[item.nodeid], bstack11ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬἍ"))
                    bstack111l1l11l11_opy_(item, _111llllll1_opy_[item.nodeid], bstack11ll1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧἎ"), report, call)
    except Exception as err:
        print(bstack11ll1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡤࡵ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺ࠺ࠡࡽࢀࠫἏ"), str(err))
def bstack111l1ll111l_opy_(test, bstack111lll1l11_opy_, result=None, call=None, bstack11111ll1_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack11l11l1ll1_opy_ = {
        bstack11ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬἐ"): bstack111lll1l11_opy_[bstack11ll1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ἑ")],
        bstack11ll1l_opy_ (u"ࠩࡷࡽࡵ࡫ࠧἒ"): bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࠨἓ"),
        bstack11ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩἔ"): test.name,
        bstack11ll1l_opy_ (u"ࠬࡨ࡯ࡥࡻࠪἕ"): {
            bstack11ll1l_opy_ (u"࠭࡬ࡢࡰࡪࠫ἖"): bstack11ll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ἗"),
            bstack11ll1l_opy_ (u"ࠨࡥࡲࡨࡪ࠭Ἐ"): inspect.getsource(test.obj)
        },
        bstack11ll1l_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭Ἑ"): test.name,
        bstack11ll1l_opy_ (u"ࠪࡷࡨࡵࡰࡦࠩἚ"): test.name,
        bstack11ll1l_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫἛ"): bstack111111ll_opy_.bstack111ll1111l_opy_(test),
        bstack11ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨἜ"): file_path,
        bstack11ll1l_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨἝ"): file_path,
        bstack11ll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ἞"): bstack11ll1l_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ἟"),
        bstack11ll1l_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧἠ"): file_path,
        bstack11ll1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧἡ"): bstack111lll1l11_opy_[bstack11ll1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨἢ")],
        bstack11ll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨἣ"): bstack11ll1l_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭ἤ"),
        bstack11ll1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪἥ"): {
            bstack11ll1l_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬἦ"): test.nodeid
        },
        bstack11ll1l_opy_ (u"ࠩࡷࡥ࡬ࡹࠧἧ"): bstack11ll1llllll_opy_(test.own_markers)
    }
    if bstack11111ll1_opy_ in [bstack11ll1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫἨ"), bstack11ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭Ἡ")]:
        bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠬࡳࡥࡵࡣࠪἪ")] = {
            bstack11ll1l_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨἫ"): bstack111lll1l11_opy_.get(bstack11ll1l_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩἬ"), [])
        }
    if bstack11111ll1_opy_ == bstack11ll1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩἭ"):
        bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩἮ")] = bstack11ll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫἯ")
        bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪἰ")] = bstack111lll1l11_opy_[bstack11ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫἱ")]
        bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫἲ")] = bstack111lll1l11_opy_[bstack11ll1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬἳ")]
    if result:
        bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨἴ")] = result.outcome
        bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪἵ")] = result.duration * 1000
        bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨἶ")] = bstack111lll1l11_opy_[bstack11ll1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩἷ")]
        if result.failed:
            bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫἸ")] = bstack1ll11l1l11_opy_.bstack111l11ll1l_opy_(call.excinfo.typename)
            bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧἹ")] = bstack1ll11l1l11_opy_.bstack111lll1l111_opy_(call.excinfo, result)
        bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭Ἲ")] = bstack111lll1l11_opy_[bstack11ll1l_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧἻ")]
    if outcome:
        bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩἼ")] = bstack11lllll11l1_opy_(outcome)
        bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫἽ")] = 0
        bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩἾ")] = bstack111lll1l11_opy_[bstack11ll1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪἿ")]
        if bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ὀ")] == bstack11ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧὁ"):
            bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧὂ")] = bstack11ll1l_opy_ (u"ࠩࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠪὃ")  # bstack111l1lll1l1_opy_
            bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫὄ")] = [{bstack11ll1l_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧὅ"): [bstack11ll1l_opy_ (u"ࠬࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠩ὆")]}]
        bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ὇")] = bstack111lll1l11_opy_[bstack11ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭Ὀ")]
    return bstack11l11l1ll1_opy_
def bstack111l1l1lll1_opy_(test, bstack11l1111l1l_opy_, bstack11111ll1_opy_, result, call, outcome, bstack111l1ll1lll_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack11l1111l1l_opy_[bstack11ll1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫὉ")]
    hook_name = bstack11l1111l1l_opy_[bstack11ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬὊ")]
    hook_data = {
        bstack11ll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨὋ"): bstack11l1111l1l_opy_[bstack11ll1l_opy_ (u"ࠫࡺࡻࡩࡥࠩὌ")],
        bstack11ll1l_opy_ (u"ࠬࡺࡹࡱࡧࠪὍ"): bstack11ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ὎"),
        bstack11ll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ὏"): bstack11ll1l_opy_ (u"ࠨࡽࢀࠫὐ").format(bstack11l111lllll_opy_(hook_name)),
        bstack11ll1l_opy_ (u"ࠩࡥࡳࡩࡿࠧὑ"): {
            bstack11ll1l_opy_ (u"ࠪࡰࡦࡴࡧࠨὒ"): bstack11ll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫὓ"),
            bstack11ll1l_opy_ (u"ࠬࡩ࡯ࡥࡧࠪὔ"): None
        },
        bstack11ll1l_opy_ (u"࠭ࡳࡤࡱࡳࡩࠬὕ"): test.name,
        bstack11ll1l_opy_ (u"ࠧࡴࡥࡲࡴࡪࡹࠧὖ"): bstack111111ll_opy_.bstack111ll1111l_opy_(test, hook_name),
        bstack11ll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫὗ"): file_path,
        bstack11ll1l_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫ὘"): file_path,
        bstack11ll1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪὙ"): bstack11ll1l_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ὚"),
        bstack11ll1l_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪὛ"): file_path,
        bstack11ll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ὜"): bstack11l1111l1l_opy_[bstack11ll1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫὝ")],
        bstack11ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ὞"): bstack11ll1l_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫὟ") if bstack111ll111111_opy_ == bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧὠ") else bstack11ll1l_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷࠫὡ"),
        bstack11ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨὢ"): hook_type
    }
    bstack111lllll11l_opy_ = bstack111lll11ll_opy_(_111llllll1_opy_.get(test.nodeid, None))
    if bstack111lllll11l_opy_:
        hook_data[bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠ࡫ࡧࠫὣ")] = bstack111lllll11l_opy_
    if result:
        hook_data[bstack11ll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧὤ")] = result.outcome
        hook_data[bstack11ll1l_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩὥ")] = result.duration * 1000
        hook_data[bstack11ll1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧὦ")] = bstack11l1111l1l_opy_[bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨὧ")]
        if result.failed:
            hook_data[bstack11ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪὨ")] = bstack1ll11l1l11_opy_.bstack111l11ll1l_opy_(call.excinfo.typename)
            hook_data[bstack11ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭Ὡ")] = bstack1ll11l1l11_opy_.bstack111lll1l111_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack11ll1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭Ὢ")] = bstack11lllll11l1_opy_(outcome)
        hook_data[bstack11ll1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨὫ")] = 100
        hook_data[bstack11ll1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭Ὤ")] = bstack11l1111l1l_opy_[bstack11ll1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧὭ")]
        if hook_data[bstack11ll1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪὮ")] == bstack11ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫὯ"):
            hook_data[bstack11ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫὰ")] = bstack11ll1l_opy_ (u"࠭ࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠧά")  # bstack111l1lll1l1_opy_
            hook_data[bstack11ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨὲ")] = [{bstack11ll1l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫέ"): [bstack11ll1l_opy_ (u"ࠩࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷ࠭ὴ")]}]
    if bstack111l1ll1lll_opy_:
        hook_data[bstack11ll1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪή")] = bstack111l1ll1lll_opy_.result
        hook_data[bstack11ll1l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬὶ")] = bstack11ll1l111ll_opy_(bstack11l1111l1l_opy_[bstack11ll1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩί")], bstack11l1111l1l_opy_[bstack11ll1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫὸ")])
        hook_data[bstack11ll1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬό")] = bstack11l1111l1l_opy_[bstack11ll1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ὺ")]
        if hook_data[bstack11ll1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩύ")] == bstack11ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪὼ"):
            hook_data[bstack11ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪώ")] = bstack1ll11l1l11_opy_.bstack111l11ll1l_opy_(bstack111l1ll1lll_opy_.exception_type)
            hook_data[bstack11ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭὾")] = [{bstack11ll1l_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ὿"): bstack11ll1ll111l_opy_(bstack111l1ll1lll_opy_.exception)}]
    return hook_data
def bstack111l1l11l11_opy_(test, bstack111lll1l11_opy_, bstack11111ll1_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack11ll1l_opy_ (u"ࠧࡴࡧࡱࡨࡤࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡦࡸࡨࡲࡹࡀࠠࡂࡶࡷࡩࡲࡶࡴࡪࡰࡪࠤࡹࡵࠠࡨࡧࡱࡩࡷࡧࡴࡦࠢࡷࡩࡸࡺࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࠦ࠭ࠡࡽࢀࠫᾀ").format(bstack11111ll1_opy_))
    bstack11l11l1ll1_opy_ = bstack111l1ll111l_opy_(test, bstack111lll1l11_opy_, result, call, bstack11111ll1_opy_, outcome)
    driver = getattr(test, bstack11ll1l_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩᾁ"), None)
    if bstack11111ll1_opy_ == bstack11ll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᾂ") and driver:
        bstack11l11l1ll1_opy_[bstack11ll1l_opy_ (u"ࠪ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠩᾃ")] = bstack1ll11l1l11_opy_.bstack11l11ll111_opy_(driver)
    if bstack11111ll1_opy_ == bstack11ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬᾄ"):
        bstack11111ll1_opy_ = bstack11ll1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᾅ")
    bstack11l111lll1_opy_ = {
        bstack11ll1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᾆ"): bstack11111ll1_opy_,
        bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩᾇ"): bstack11l11l1ll1_opy_
    }
    bstack1ll11l1l11_opy_.bstack1l11lll11_opy_(bstack11l111lll1_opy_)
    if bstack11111ll1_opy_ == bstack11ll1l_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᾈ"):
        threading.current_thread().bstackTestMeta = {bstack11ll1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᾉ"): bstack11ll1l_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫᾊ")}
    elif bstack11111ll1_opy_ == bstack11ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᾋ"):
        threading.current_thread().bstackTestMeta = {bstack11ll1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᾌ"): getattr(result, bstack11ll1l_opy_ (u"࠭࡯ࡶࡶࡦࡳࡲ࡫ࠧᾍ"), bstack11ll1l_opy_ (u"ࠧࠨᾎ"))}
def bstack111l1l1l11l_opy_(test, bstack111lll1l11_opy_, bstack11111ll1_opy_, result=None, call=None, outcome=None, bstack111l1ll1lll_opy_=None):
    logger.debug(bstack11ll1l_opy_ (u"ࠨࡵࡨࡲࡩࡥࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡧࡹࡩࡳࡺ࠺ࠡࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡩࡨࡲࡪࡸࡡࡵࡧࠣ࡬ࡴࡵ࡫ࠡࡦࡤࡸࡦ࠲ࠠࡦࡸࡨࡲࡹ࡚ࡹࡱࡧࠣ࠱ࠥࢁࡽࠨᾏ").format(bstack11111ll1_opy_))
    hook_data = bstack111l1l1lll1_opy_(test, bstack111lll1l11_opy_, bstack11111ll1_opy_, result, call, outcome, bstack111l1ll1lll_opy_)
    bstack11l111lll1_opy_ = {
        bstack11ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᾐ"): bstack11111ll1_opy_,
        bstack11ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࠬᾑ"): hook_data
    }
    bstack1ll11l1l11_opy_.bstack1l11lll11_opy_(bstack11l111lll1_opy_)
def bstack111lll11ll_opy_(bstack111lll1l11_opy_):
    if not bstack111lll1l11_opy_:
        return None
    if bstack111lll1l11_opy_.get(bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᾒ"), None):
        return getattr(bstack111lll1l11_opy_[bstack11ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨᾓ")], bstack11ll1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᾔ"), None)
    return bstack111lll1l11_opy_.get(bstack11ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᾕ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.LOG, bstack1llll1lll1l_opy_.PRE, request, caplog)
    yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_.LOG, bstack1llll1lll1l_opy_.POST, request, caplog)
        return # skip all existing bstack111l1ll1l11_opy_
    try:
        if not bstack1ll11l1l11_opy_.on():
            return
        places = [bstack11ll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧᾖ"), bstack11ll1l_opy_ (u"ࠩࡦࡥࡱࡲࠧᾗ"), bstack11ll1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᾘ")]
        logs = []
        for bstack111l1ll11ll_opy_ in places:
            records = caplog.get_records(bstack111l1ll11ll_opy_)
            bstack111l1l1l111_opy_ = bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᾙ") if bstack111l1ll11ll_opy_ == bstack11ll1l_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᾚ") else bstack11ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᾛ")
            bstack111l1l1l1ll_opy_ = request.node.nodeid + (bstack11ll1l_opy_ (u"ࠧࠨᾜ") if bstack111l1ll11ll_opy_ == bstack11ll1l_opy_ (u"ࠨࡥࡤࡰࡱ࠭ᾝ") else bstack11ll1l_opy_ (u"ࠩ࠰ࠫᾞ") + bstack111l1ll11ll_opy_)
            test_uuid = bstack111lll11ll_opy_(_111llllll1_opy_.get(bstack111l1l1l1ll_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack11ll1l1llll_opy_(record.message):
                    continue
                logs.append({
                    bstack11ll1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᾟ"): bstack11ll1ll1l1l_opy_(record.created).isoformat() + bstack11ll1l_opy_ (u"ࠫ࡟࠭ᾠ"),
                    bstack11ll1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᾡ"): record.levelname,
                    bstack11ll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᾢ"): record.message,
                    bstack111l1l1l111_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack1ll11l1l11_opy_.bstack1l1lllll_opy_(logs)
    except Exception as err:
        print(bstack11ll1l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡥࡲࡲࡩࡥࡦࡪࡺࡷࡹࡷ࡫࠺ࠡࡽࢀࠫᾣ"), str(err))
def bstack11l1ll11l_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack11l1ll1111_opy_
    bstack1l111lllll_opy_ = bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬᾤ"), None) and bstack11l1ll1l_opy_(
            threading.current_thread(), bstack11ll1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᾥ"), None)
    bstack11ll1l111_opy_ = getattr(driver, bstack11ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪᾦ"), None) != None and getattr(driver, bstack11ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫᾧ"), None) == True
    if sequence == bstack11ll1l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬᾨ") and driver != None:
      if not bstack11l1ll1111_opy_ and bstack1ll11ll111l_opy_() and bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᾩ") in CONFIG and CONFIG[bstack11ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᾪ")] == True and bstack1111ll1l1_opy_.bstack1ll1ll11l1_opy_(driver_command) and (bstack11ll1l111_opy_ or bstack1l111lllll_opy_) and not bstack1111ll11l_opy_(args):
        try:
          bstack11l1ll1111_opy_ = True
          logger.debug(bstack11ll1l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡼࡿࠪᾫ").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack11ll1l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡥࡳࡨࡲࡶࡲࠦࡳࡤࡣࡱࠤࢀࢃࠧᾬ").format(str(err)))
        bstack11l1ll1111_opy_ = False
    if sequence == bstack11ll1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩᾭ"):
        if driver_command == bstack11ll1l_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨᾮ"):
            bstack1ll11l1l11_opy_.bstack1111111l_opy_({
                bstack11ll1l_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫᾯ"): response[bstack11ll1l_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬᾰ")],
                bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᾱ"): store[bstack11ll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᾲ")]
            })
def bstack1l1ll11lll_opy_():
    global bstack1ll1111ll_opy_
    bstack1l111l11ll_opy_.bstack1llll1l1l_opy_()
    logging.shutdown()
    bstack1ll11l1l11_opy_.bstack111lllllll_opy_()
    for driver in bstack1ll1111ll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack111l1llllll_opy_(*args):
    global bstack1ll1111ll_opy_
    bstack1ll11l1l11_opy_.bstack111lllllll_opy_()
    for driver in bstack1ll1111ll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1l1ll11l1l_opy_, stage=STAGE.bstack1111l111_opy_, bstack1l1l11l111_opy_=bstack11l1111ll_opy_)
def bstack1l1l11111_opy_(self, *args, **kwargs):
    bstack1ll1ll11l_opy_ = bstack11ll11ll_opy_(self, *args, **kwargs)
    bstack11l11111l_opy_ = getattr(threading.current_thread(), bstack11ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡖࡨࡷࡹࡓࡥࡵࡣࠪᾳ"), None)
    if bstack11l11111l_opy_ and bstack11l11111l_opy_.get(bstack11ll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᾴ"), bstack11ll1l_opy_ (u"ࠫࠬ᾵")) == bstack11ll1l_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭ᾶ"):
        bstack1ll11l1l11_opy_.bstack1ll1l11111_opy_(self)
    return bstack1ll1ll11l_opy_
@measure(event_name=EVENTS.bstack1ll11l1l1_opy_, stage=STAGE.bstack1l11ll1l11_opy_, bstack1l1l11l111_opy_=bstack11l1111ll_opy_)
def bstack1l1111ll11_opy_(framework_name):
    from bstack_utils.config import Config
    bstack1l1l11lll_opy_ = Config.bstack11l1lll11_opy_()
    if bstack1l1l11lll_opy_.get_property(bstack11ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪᾷ")):
        return
    bstack1l1l11lll_opy_.bstack1l1111l1_opy_(bstack11ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫᾸ"), True)
    global bstack1lll1l1ll_opy_
    global bstack1l111l11_opy_
    bstack1lll1l1ll_opy_ = framework_name
    logger.info(bstack1llllllll_opy_.format(bstack1lll1l1ll_opy_.split(bstack11ll1l_opy_ (u"ࠨ࠯ࠪᾹ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1ll11ll111l_opy_():
            Service.start = bstack11l1l1llll_opy_
            Service.stop = bstack11l1l111_opy_
            webdriver.Remote.get = bstack111l1l11l_opy_
            webdriver.Remote.__init__ = bstack1ll11ll1l_opy_
            if not isinstance(os.getenv(bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡄࡖࡆࡒࡌࡆࡎࠪᾺ")), str):
                return
            WebDriver.close = bstack11111l1ll_opy_
            WebDriver.quit = bstack1lll1ll11l_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack1ll11l1l11_opy_.on():
            webdriver.Remote.__init__ = bstack1l1l11111_opy_
        bstack1l111l11_opy_ = True
    except Exception as e:
        pass
    if os.environ.get(bstack11ll1l_opy_ (u"ࠪࡗࡊࡒࡅࡏࡋࡘࡑࡤࡕࡒࡠࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡏࡎࡔࡖࡄࡐࡑࡋࡄࠨΆ")):
        bstack1l111l11_opy_ = eval(os.environ.get(bstack11ll1l_opy_ (u"ࠫࡘࡋࡌࡆࡐࡌ࡙ࡒࡥࡏࡓࡡࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡉࡏࡕࡗࡅࡑࡒࡅࡅࠩᾼ")))
    if not bstack1l111l11_opy_:
        bstack1l1lllllll_opy_(bstack11ll1l_opy_ (u"ࠧࡖࡡࡤ࡭ࡤ࡫ࡪࡹࠠ࡯ࡱࡷࠤ࡮ࡴࡳࡵࡣ࡯ࡰࡪࡪࠢ᾽"), bstack1llllll11l_opy_)
    if bstack1ll11l11ll_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._1l1111l1l1_opy_ = bstack1lll111ll1_opy_
        except Exception as e:
            logger.error(bstack11l1ll11l1_opy_.format(str(e)))
    if bstack11ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ι") in str(framework_name).lower():
        if not bstack1ll11ll111l_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1l1ll1l11_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack111l111l_opy_
            Config.getoption = bstack11ll11l1_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1l11111l_opy_
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11lll111l1_opy_, stage=STAGE.bstack1111l111_opy_, bstack1l1l11l111_opy_=bstack11l1111ll_opy_)
def bstack1lll1ll11l_opy_(self):
    global bstack1lll1l1ll_opy_
    global bstack111l11lll_opy_
    global bstack1l1l1l111_opy_
    try:
        if bstack11ll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ᾿") in bstack1lll1l1ll_opy_ and self.session_id != None and bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬ῀"), bstack11ll1l_opy_ (u"ࠩࠪ῁")) != bstack11ll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫῂ"):
            bstack1l111ll11_opy_ = bstack11ll1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫῃ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬῄ")
            bstack1llllll1l_opy_(logger, True)
            if self != None:
                bstack11lll1lll_opy_(self, bstack1l111ll11_opy_, bstack11ll1l_opy_ (u"࠭ࠬࠡࠩ῅").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1llll11l11l_opy_(bstack1llll1llll1_opy_):
            item = store.get(bstack11ll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫῆ"), None)
            if item is not None and bstack11l1ll1l_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧῇ"), None):
                bstack1l11l1lll1_opy_.bstack1ll1111lll_opy_(self, bstack1l11l11l11_opy_, logger, item)
        threading.current_thread().testStatus = bstack11ll1l_opy_ (u"ࠩࠪῈ")
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࠦΈ") + str(e))
    bstack1l1l1l111_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack1ll1ll1ll1_opy_, stage=STAGE.bstack1111l111_opy_, bstack1l1l11l111_opy_=bstack11l1111ll_opy_)
def bstack1ll11ll1l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack111l11lll_opy_
    global bstack11l1111ll_opy_
    global bstack1llll11lll_opy_
    global bstack1lll1l1ll_opy_
    global bstack11ll11ll_opy_
    global bstack1ll1111ll_opy_
    global bstack111lllll_opy_
    global bstack1lll1l11l_opy_
    global bstack1l11l11l11_opy_
    CONFIG[bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭Ὴ")] = str(bstack1lll1l1ll_opy_) + str(__version__)
    command_executor = bstack1l1111lll_opy_(bstack111lllll_opy_, CONFIG)
    logger.debug(bstack1l111ll1_opy_.format(command_executor))
    proxy = bstack11l1lll111_opy_(CONFIG, proxy)
    bstack1l111l1l11_opy_ = 0
    try:
        if bstack1llll11lll_opy_ is True:
            bstack1l111l1l11_opy_ = int(os.environ.get(bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬΉ")))
    except:
        bstack1l111l1l11_opy_ = 0
    bstack11ll1111l1_opy_ = bstack11ll1l11l_opy_(CONFIG, bstack1l111l1l11_opy_)
    logger.debug(bstack11lllll1ll_opy_.format(str(bstack11ll1111l1_opy_)))
    bstack1l11l11l11_opy_ = CONFIG.get(bstack11ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩῌ"))[bstack1l111l1l11_opy_]
    if bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ῍") in CONFIG and CONFIG[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ῎")]:
        bstack1l1ll11ll1_opy_(bstack11ll1111l1_opy_, bstack1lll1l11l_opy_)
    if bstack1lllll11ll_opy_.bstack11lllllll1_opy_(CONFIG, bstack1l111l1l11_opy_) and bstack1lllll11ll_opy_.bstack111l1l1ll_opy_(bstack11ll1111l1_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1llll11l11l_opy_(bstack1llll1llll1_opy_):
            bstack1lllll11ll_opy_.set_capabilities(bstack11ll1111l1_opy_, CONFIG)
    if desired_capabilities:
        bstack1lll1lll1l_opy_ = bstack1111ll111_opy_(desired_capabilities)
        bstack1lll1lll1l_opy_[bstack11ll1l_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩ῏")] = bstack1l111l1ll_opy_(CONFIG)
        bstack11ll11l1l_opy_ = bstack11ll1l11l_opy_(bstack1lll1lll1l_opy_)
        if bstack11ll11l1l_opy_:
            bstack11ll1111l1_opy_ = update(bstack11ll11l1l_opy_, bstack11ll1111l1_opy_)
        desired_capabilities = None
    if options:
        bstack11lll11ll1_opy_(options, bstack11ll1111l1_opy_)
    if not options:
        options = bstack1l111lll1l_opy_(bstack11ll1111l1_opy_)
    if proxy and bstack1l11l1llll_opy_() >= version.parse(bstack11ll1l_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪῐ")):
        options.proxy(proxy)
    if options and bstack1l11l1llll_opy_() >= version.parse(bstack11ll1l_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪῑ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1l11l1llll_opy_() < version.parse(bstack11ll1l_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫῒ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack11ll1111l1_opy_)
    logger.info(bstack1ll1l111l_opy_)
    bstack1ll11ll111_opy_.end(EVENTS.bstack1ll11l1l1_opy_.value, EVENTS.bstack1ll11l1l1_opy_.value + bstack11ll1l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨΐ"),
                               EVENTS.bstack1ll11l1l1_opy_.value + bstack11ll1l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ῔"), True, None)
    if bstack1l11l1llll_opy_() >= version.parse(bstack11ll1l_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨ῕")):
        bstack11ll11ll_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l11l1llll_opy_() >= version.parse(bstack11ll1l_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨῖ")):
        bstack11ll11ll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l11l1llll_opy_() >= version.parse(bstack11ll1l_opy_ (u"ࠪ࠶࠳࠻࠳࠯࠲ࠪῗ")):
        bstack11ll11ll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack11ll11ll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack11lll1llll_opy_ = bstack11ll1l_opy_ (u"ࠫࠬῘ")
        if bstack1l11l1llll_opy_() >= version.parse(bstack11ll1l_opy_ (u"ࠬ࠺࠮࠱࠰࠳ࡦ࠶࠭Ῑ")):
            bstack11lll1llll_opy_ = self.caps.get(bstack11ll1l_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨῚ"))
        else:
            bstack11lll1llll_opy_ = self.capabilities.get(bstack11ll1l_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢΊ"))
        if bstack11lll1llll_opy_:
            bstack1l1l1111l1_opy_(bstack11lll1llll_opy_)
            if bstack1l11l1llll_opy_() <= version.parse(bstack11ll1l_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨ῜")):
                self.command_executor._url = bstack11ll1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥ῝") + bstack111lllll_opy_ + bstack11ll1l_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢ῞")
            else:
                self.command_executor._url = bstack11ll1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨ῟") + bstack11lll1llll_opy_ + bstack11ll1l_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨῠ")
            logger.debug(bstack1lll11l111_opy_.format(bstack11lll1llll_opy_))
        else:
            logger.debug(bstack1l11ll111_opy_.format(bstack11ll1l_opy_ (u"ࠨࡏࡱࡶ࡬ࡱࡦࡲࠠࡉࡷࡥࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠢῡ")))
    except Exception as e:
        logger.debug(bstack1l11ll111_opy_.format(e))
    bstack111l11lll_opy_ = self.session_id
    if bstack11ll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧῢ") in bstack1lll1l1ll_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack11ll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬΰ"), None)
        if item:
            bstack111l1ll1111_opy_ = getattr(item, bstack11ll1l_opy_ (u"ࠩࡢࡸࡪࡹࡴࡠࡥࡤࡷࡪࡥࡳࡵࡣࡵࡸࡪࡪࠧῤ"), False)
            if not getattr(item, bstack11ll1l_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫῥ"), None) and bstack111l1ll1111_opy_:
                setattr(store[bstack11ll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨῦ")], bstack11ll1l_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ῧ"), self)
        bstack11l11111l_opy_ = getattr(threading.current_thread(), bstack11ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡚ࡥࡴࡶࡐࡩࡹࡧࠧῨ"), None)
        if bstack11l11111l_opy_ and bstack11l11111l_opy_.get(bstack11ll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧῩ"), bstack11ll1l_opy_ (u"ࠨࠩῪ")) == bstack11ll1l_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪΎ"):
            bstack1ll11l1l11_opy_.bstack1ll1l11111_opy_(self)
    bstack1ll1111ll_opy_.append(self)
    if bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭Ῥ") in CONFIG and bstack11ll1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ῭") in CONFIG[bstack11ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ΅")][bstack1l111l1l11_opy_]:
        bstack11l1111ll_opy_ = CONFIG[bstack11ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ`")][bstack1l111l1l11_opy_][bstack11ll1l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ῰")]
    logger.debug(bstack1ll1lll111_opy_.format(bstack111l11lll_opy_))
@measure(event_name=EVENTS.bstack1l1ll11111_opy_, stage=STAGE.bstack1111l111_opy_, bstack1l1l11l111_opy_=bstack11l1111ll_opy_)
def bstack111l1l11l_opy_(self, url):
    global bstack11l1llll1_opy_
    global CONFIG
    try:
        bstack11ll11ll11_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1l1lll1l_opy_.format(str(err)))
    try:
        bstack11l1llll1_opy_(self, url)
    except Exception as e:
        try:
            bstack1l11l11l1l_opy_ = str(e)
            if any(err_msg in bstack1l11l11l1l_opy_ for err_msg in bstack1l1l1ll11l_opy_):
                bstack11ll11ll11_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1l1lll1l_opy_.format(str(err)))
        raise e
def bstack11lll1l1ll_opy_(item, when):
    global bstack11ll1l11_opy_
    try:
        bstack11ll1l11_opy_(item, when)
    except Exception as e:
        pass
def bstack1l11111l_opy_(item, call, rep):
    global bstack1ll1lll1l_opy_
    global bstack1ll1111ll_opy_
    name = bstack11ll1l_opy_ (u"ࠨࠩ῱")
    try:
        if rep.when == bstack11ll1l_opy_ (u"ࠩࡦࡥࡱࡲࠧῲ"):
            bstack111l11lll_opy_ = threading.current_thread().bstackSessionId
            bstack111l1lll1ll_opy_ = item.config.getoption(bstack11ll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬῳ"))
            try:
                if (str(bstack111l1lll1ll_opy_).lower() != bstack11ll1l_opy_ (u"ࠫࡹࡸࡵࡦࠩῴ")):
                    name = str(rep.nodeid)
                    bstack1l11lll11l_opy_ = bstack1ll1l11ll1_opy_(bstack11ll1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭῵"), name, bstack11ll1l_opy_ (u"࠭ࠧῶ"), bstack11ll1l_opy_ (u"ࠧࠨῷ"), bstack11ll1l_opy_ (u"ࠨࠩῸ"), bstack11ll1l_opy_ (u"ࠩࠪΌ"))
                    os.environ[bstack11ll1l_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭Ὼ")] = name
                    for driver in bstack1ll1111ll_opy_:
                        if bstack111l11lll_opy_ == driver.session_id:
                            driver.execute_script(bstack1l11lll11l_opy_)
            except Exception as e:
                logger.debug(bstack11ll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫΏ").format(str(e)))
            try:
                bstack11ll1l1l_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack11ll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ῼ"):
                    status = bstack11ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭´") if rep.outcome.lower() == bstack11ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ῾") else bstack11ll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ῿")
                    reason = bstack11ll1l_opy_ (u"ࠩࠪ ")
                    if status == bstack11ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ "):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack11ll1l_opy_ (u"ࠫ࡮ࡴࡦࡰࠩ ") if status == bstack11ll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ ") else bstack11ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ ")
                    data = name + bstack11ll1l_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩ ") if status == bstack11ll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ ") else name + bstack11ll1l_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠤࠤࠬ ") + reason
                    bstack111l1l111_opy_ = bstack1ll1l11ll1_opy_(bstack11ll1l_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬ "), bstack11ll1l_opy_ (u"ࠫࠬ "), bstack11ll1l_opy_ (u"ࠬ࠭ "), bstack11ll1l_opy_ (u"࠭ࠧ​"), level, data)
                    for driver in bstack1ll1111ll_opy_:
                        if bstack111l11lll_opy_ == driver.session_id:
                            driver.execute_script(bstack111l1l111_opy_)
            except Exception as e:
                logger.debug(bstack11ll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡵ࡮ࡵࡧࡻࡸࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ‌").format(str(e)))
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾࢁࠬ‍").format(str(e)))
    bstack1ll1lll1l_opy_(item, call, rep)
notset = Notset()
def bstack11ll11l1_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1l1l1l1111_opy_
    if str(name).lower() == bstack11ll1l_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩ‎"):
        return bstack11ll1l_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤ‏")
    else:
        return bstack1l1l1l1111_opy_(self, name, default, skip)
def bstack1lll111ll1_opy_(self):
    global CONFIG
    global bstack1ll1lllll1_opy_
    try:
        proxy = bstack1l11ll1l1l_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack11ll1l_opy_ (u"ࠫ࠳ࡶࡡࡤࠩ‐")):
                proxies = bstack1lllll1lll_opy_(proxy, bstack1l1111lll_opy_())
                if len(proxies) > 0:
                    protocol, bstack1ll1ll111_opy_ = proxies.popitem()
                    if bstack11ll1l_opy_ (u"ࠧࡀ࠯࠰ࠤ‑") in bstack1ll1ll111_opy_:
                        return bstack1ll1ll111_opy_
                    else:
                        return bstack11ll1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢ‒") + bstack1ll1ll111_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack11ll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡴࡷࡵࡸࡺࠢࡸࡶࡱࠦ࠺ࠡࡽࢀࠦ–").format(str(e)))
    return bstack1ll1lllll1_opy_(self)
def bstack1ll11l11ll_opy_():
    return (bstack11ll1l_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫ—") in CONFIG or bstack11ll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭―") in CONFIG) and bstack1ll11l1l_opy_() and bstack1l11l1llll_opy_() >= version.parse(
        bstack1lll1l11l1_opy_)
def bstack1lll1111_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack11l1111ll_opy_
    global bstack1llll11lll_opy_
    global bstack1lll1l1ll_opy_
    CONFIG[bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ‖")] = str(bstack1lll1l1ll_opy_) + str(__version__)
    bstack1l111l1l11_opy_ = 0
    try:
        if bstack1llll11lll_opy_ is True:
            bstack1l111l1l11_opy_ = int(os.environ.get(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ‗")))
    except:
        bstack1l111l1l11_opy_ = 0
    CONFIG[bstack11ll1l_opy_ (u"ࠧ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ‘")] = True
    bstack11ll1111l1_opy_ = bstack11ll1l11l_opy_(CONFIG, bstack1l111l1l11_opy_)
    logger.debug(bstack11lllll1ll_opy_.format(str(bstack11ll1111l1_opy_)))
    if CONFIG.get(bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ’")):
        bstack1l1ll11ll1_opy_(bstack11ll1111l1_opy_, bstack1lll1l11l_opy_)
    if bstack11ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ‚") in CONFIG and bstack11ll1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭‛") in CONFIG[bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ“")][bstack1l111l1l11_opy_]:
        bstack11l1111ll_opy_ = CONFIG[bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭”")][bstack1l111l1l11_opy_][bstack11ll1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ„")]
    import urllib
    import json
    if bstack11ll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ‟") in CONFIG and str(CONFIG[bstack11ll1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ†")]).lower() != bstack11ll1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭‡"):
        bstack11l111111_opy_ = bstack1lllll11l_opy_()
        bstack1111l1lll_opy_ = bstack11l111111_opy_ + urllib.parse.quote(json.dumps(bstack11ll1111l1_opy_))
    else:
        bstack1111l1lll_opy_ = bstack11ll1l_opy_ (u"ࠨࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠪ•") + urllib.parse.quote(json.dumps(bstack11ll1111l1_opy_))
    browser = self.connect(bstack1111l1lll_opy_)
    return browser
def bstack11l11l11_opy_():
    global bstack1l111l11_opy_
    global bstack1lll1l1ll_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1lll1lllll_opy_
        if not bstack1ll11ll111l_opy_():
            global bstack1ll11l1ll_opy_
            if not bstack1ll11l1ll_opy_:
                from bstack_utils.helper import bstack1ll111111l_opy_, bstack1l11l11l1_opy_
                bstack1ll11l1ll_opy_ = bstack1ll111111l_opy_()
                bstack1l11l11l1_opy_(bstack1lll1l1ll_opy_)
            BrowserType.connect = bstack1lll1lllll_opy_
            return
        BrowserType.launch = bstack1lll1111_opy_
        bstack1l111l11_opy_ = True
    except Exception as e:
        pass
def bstack111l1l11l1l_opy_():
    global CONFIG
    global bstack1l111ll1l_opy_
    global bstack111lllll_opy_
    global bstack1lll1l11l_opy_
    global bstack1llll11lll_opy_
    global bstack1lll1ll11_opy_
    CONFIG = json.loads(os.environ.get(bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠨ‣")))
    bstack1l111ll1l_opy_ = eval(os.environ.get(bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ․")))
    bstack111lllll_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡌ࡚ࡈ࡟ࡖࡔࡏࠫ‥"))
    bstack1l11l1ll11_opy_(CONFIG, bstack1l111ll1l_opy_)
    bstack1lll1ll11_opy_ = bstack1l111l11ll_opy_.bstack11lll1l1l_opy_(CONFIG, bstack1lll1ll11_opy_)
    if cli.bstack11111l1l_opy_():
        bstack11ll1lllll_opy_.invoke(bstack11ll11ll1_opy_.CONNECT, bstack1111lll1_opy_())
        cli_context.platform_index = int(os.environ.get(bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ…"), bstack11ll1l_opy_ (u"࠭࠰ࠨ‧")))
        cli.bstack1llllll1l1l_opy_(cli_context.platform_index)
        cli.bstack1llllllll11_opy_(bstack1l1111lll_opy_(bstack111lllll_opy_, CONFIG), cli_context.platform_index, bstack1l111lll1l_opy_)
        cli.bstack1llll1111l1_opy_()
        logger.debug(bstack11ll1l_opy_ (u"ࠢࡄࡎࡌࠤ࡮ࡹࠠࡢࡥࡷ࡭ࡻ࡫ࠠࡧࡱࡵࠤࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࠨ ") + str(cli_context.platform_index) + bstack11ll1l_opy_ (u"ࠣࠤ "))
        return # skip all existing bstack111l1ll1l11_opy_
    global bstack11ll11ll_opy_
    global bstack1l1l1l111_opy_
    global bstack1llll11l11_opy_
    global bstack11llll1l11_opy_
    global bstack1lll1l11_opy_
    global bstack1ll11l1ll1_opy_
    global bstack1l11l1111l_opy_
    global bstack11l1llll1_opy_
    global bstack1ll1lllll1_opy_
    global bstack1l1l1l1111_opy_
    global bstack11ll1l11_opy_
    global bstack1ll1lll1l_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack11ll11ll_opy_ = webdriver.Remote.__init__
        bstack1l1l1l111_opy_ = WebDriver.quit
        bstack1l11l1111l_opy_ = WebDriver.close
        bstack11l1llll1_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack11ll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ‪") in CONFIG or bstack11ll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ‫") in CONFIG) and bstack1ll11l1l_opy_():
        if bstack1l11l1llll_opy_() < version.parse(bstack1lll1l11l1_opy_):
            logger.error(bstack1ll1l1111l_opy_.format(bstack1l11l1llll_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack1ll1lllll1_opy_ = RemoteConnection._1l1111l1l1_opy_
            except Exception as e:
                logger.error(bstack11l1ll11l1_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1l1l1l1111_opy_ = Config.getoption
        from _pytest import runner
        bstack11ll1l11_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack11l1ll111l_opy_)
    try:
        from pytest_bdd import reporting
        bstack1ll1lll1l_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬ‬"))
    bstack1lll1l11l_opy_ = CONFIG.get(bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ‭"), {}).get(bstack11ll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ‮"))
    bstack1llll11lll_opy_ = True
    bstack1l1111ll11_opy_(bstack1l11l111ll_opy_)
if (bstack11lll1111l1_opy_()):
    bstack111l1l11l1l_opy_()
@bstack111ll1l1ll_opy_(class_method=False)
def bstack111l1l1ll11_opy_(hook_name, event, bstack1l1l11lll11_opy_=None):
    if hook_name not in [bstack11ll1l_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨ "), bstack11ll1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬ‰"), bstack11ll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨ‱"), bstack11ll1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬ′"), bstack11ll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩ″"), bstack11ll1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭‴"), bstack11ll1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬ‵"), bstack11ll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩ‶")]:
        return
    node = store[bstack11ll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬ‷")]
    if hook_name in [bstack11ll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨ‸"), bstack11ll1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬ‹")]:
        node = store[bstack11ll1l_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡯ࡴࡦ࡯ࠪ›")]
    elif hook_name in [bstack11ll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠪ※"), bstack11ll1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠧ‼")]:
        node = store[bstack11ll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡥ࡯ࡥࡸࡹ࡟ࡪࡶࡨࡱࠬ‽")]
    hook_type = bstack11l111ll11l_opy_(hook_name)
    if event == bstack11ll1l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨ‾"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_[hook_type], bstack1llll1lll1l_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack11l1111l1l_opy_ = {
            bstack11ll1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ‿"): uuid,
            bstack11ll1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⁀"): bstack1l1ll1111l_opy_(),
            bstack11ll1l_opy_ (u"ࠫࡹࡿࡰࡦࠩ⁁"): bstack11ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ⁂"),
            bstack11ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩ⁃"): hook_type,
            bstack11ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪ⁄"): hook_name
        }
        store[bstack11ll1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ⁅")].append(uuid)
        bstack111l1ll1l1l_opy_ = node.nodeid
        if hook_type == bstack11ll1l_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧ⁆"):
            if not _111llllll1_opy_.get(bstack111l1ll1l1l_opy_, None):
                _111llllll1_opy_[bstack111l1ll1l1l_opy_] = {bstack11ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ⁇"): []}
            _111llllll1_opy_[bstack111l1ll1l1l_opy_][bstack11ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⁈")].append(bstack11l1111l1l_opy_[bstack11ll1l_opy_ (u"ࠬࡻࡵࡪࡦࠪ⁉")])
        _111llllll1_opy_[bstack111l1ll1l1l_opy_ + bstack11ll1l_opy_ (u"࠭࠭ࠨ⁊") + hook_name] = bstack11l1111l1l_opy_
        bstack111l1l1l11l_opy_(node, bstack11l1111l1l_opy_, bstack11ll1l_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ⁋"))
    elif event == bstack11ll1l_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧ⁌"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll1111ll_opy_[hook_type], bstack1llll1lll1l_opy_.POST, node, None, bstack1l1l11lll11_opy_)
            return
        bstack11l11l11ll_opy_ = node.nodeid + bstack11ll1l_opy_ (u"ࠩ࠰ࠫ⁍") + hook_name
        _111llllll1_opy_[bstack11l11l11ll_opy_][bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⁎")] = bstack1l1ll1111l_opy_()
        bstack111l1ll1ll1_opy_(_111llllll1_opy_[bstack11l11l11ll_opy_][bstack11ll1l_opy_ (u"ࠫࡺࡻࡩࡥࠩ⁏")])
        bstack111l1l1l11l_opy_(node, _111llllll1_opy_[bstack11l11l11ll_opy_], bstack11ll1l_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ⁐"), bstack111l1ll1lll_opy_=bstack1l1l11lll11_opy_)
def bstack111l1ll11l1_opy_():
    global bstack111ll111111_opy_
    if bstack11ll111l11_opy_():
        bstack111ll111111_opy_ = bstack11ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪ⁑")
    else:
        bstack111ll111111_opy_ = bstack11ll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ⁒")
@bstack1ll11l1l11_opy_.bstack111lll111ll_opy_
def bstack111l1l1l1l1_opy_():
    bstack111l1ll11l1_opy_()
    if cli.is_running():
        try:
            bstack11ll11lll11_opy_(bstack111l1l1ll11_opy_)
        except Exception as e:
            logger.debug(bstack11ll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࡸࠦࡰࡢࡶࡦ࡬࠿ࠦࡻࡾࠤ⁓").format(e))
        return
    if bstack1ll11l1l_opy_():
        bstack1l1l11lll_opy_ = Config.bstack11l1lll11_opy_()
        bstack11ll1l_opy_ (u"ࠩࠪࠫࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡊࡴࡸࠠࡱࡲࡳࠤࡂࠦ࠱࠭ࠢࡰࡳࡩࡥࡥࡹࡧࡦࡹࡹ࡫ࠠࡨࡧࡷࡷࠥࡻࡳࡦࡦࠣࡪࡴࡸࠠࡢ࠳࠴ࡽࠥࡩ࡯࡮࡯ࡤࡲࡩࡹ࠭ࡸࡴࡤࡴࡵ࡯࡮ࡨࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡇࡱࡵࠤࡵࡶࡰࠡࡀࠣ࠵࠱ࠦ࡭ࡰࡦࡢࡩࡽ࡫ࡣࡶࡶࡨࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡲࡶࡰࠣࡦࡪࡩࡡࡶࡵࡨࠤ࡮ࡺࠠࡪࡵࠣࡴࡦࡺࡣࡩࡧࡧࠤ࡮ࡴࠠࡢࠢࡧ࡭࡫࡬ࡥࡳࡧࡱࡸࠥࡶࡲࡰࡥࡨࡷࡸࠦࡩࡥࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡕࡪࡸࡷࠥࡽࡥࠡࡰࡨࡩࡩࠦࡴࡰࠢࡸࡷࡪࠦࡓࡦ࡮ࡨࡲ࡮ࡻ࡭ࡑࡣࡷࡧ࡭࠮ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠࡪࡤࡲࡩࡲࡥࡳࠫࠣࡪࡴࡸࠠࡱࡲࡳࠤࡃࠦ࠱ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪࠫࠬ⁔")
        if bstack1l1l11lll_opy_.get_property(bstack11ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡱࡴࡪ࡟ࡤࡣ࡯ࡰࡪࡪࠧ⁕")):
            if CONFIG.get(bstack11ll1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ⁖")) is not None and int(CONFIG[bstack11ll1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ⁗")]) > 1:
                bstack1ll1l111_opy_(bstack11l1ll11l_opy_)
            return
        bstack1ll1l111_opy_(bstack11l1ll11l_opy_)
    try:
        bstack11ll11lll11_opy_(bstack111l1l1ll11_opy_)
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࡶࠤࡵࡧࡴࡤࡪ࠽ࠤࢀࢃࠢ⁘").format(e))
bstack111l1l1l1l1_opy_()