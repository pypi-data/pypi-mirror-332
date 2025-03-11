# coding: UTF-8
import sys
bstack1111l1l_opy_ = sys.version_info [0] == 2
bstack1llll1l_opy_ = 2048
bstack1ll1111_opy_ = 7
def bstack11lll_opy_ (bstack11lll1_opy_):
    global bstack1lll1l_opy_
    bstack1l1l11l_opy_ = ord (bstack11lll1_opy_ [-1])
    bstack11lllll_opy_ = bstack11lll1_opy_ [:-1]
    bstack1ll1lll_opy_ = bstack1l1l11l_opy_ % len (bstack11lllll_opy_)
    bstack11l1_opy_ = bstack11lllll_opy_ [:bstack1ll1lll_opy_] + bstack11lllll_opy_ [bstack1ll1lll_opy_:]
    if bstack1111l1l_opy_:
        bstack11llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack1llll1l_opy_ - (bstack111l1l1_opy_ + bstack1l1l11l_opy_) % bstack1ll1111_opy_) for bstack111l1l1_opy_, char in enumerate (bstack11l1_opy_)])
    else:
        bstack11llll1_opy_ = str () .join ([chr (ord (char) - bstack1llll1l_opy_ - (bstack111l1l1_opy_ + bstack1l1l11l_opy_) % bstack1ll1111_opy_) for bstack111l1l1_opy_, char in enumerate (bstack11l1_opy_)])
    return eval (bstack11llll1_opy_)
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack111l11ll_opy_ import get_logger
logger = get_logger(__name__)
bstack11l111ll1ll_opy_: Dict[str, float] = {}
bstack11l11l111l1_opy_: List = []
bstack11l111lll1l_opy_ = 5
bstack11ll1111ll_opy_ = os.path.join(os.getcwd(), bstack11lll_opy_ (u"ࠫࡱࡵࡧࠨᰄ"), bstack11lll_opy_ (u"ࠬࡱࡥࡺ࠯ࡰࡩࡹࡸࡩࡤࡵ࠱࡮ࡸࡵ࡮ࠨᰅ"))
logging.getLogger(bstack11lll_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠨᰆ")).setLevel(logging.WARNING)
lock = FileLock(bstack11ll1111ll_opy_+bstack11lll_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨᰇ"))
class bstack11l11l1111l_opy_:
    duration: float
    name: str
    startTime: float
    worker: int
    status: bool
    failure: str
    details: Optional[str]
    entryType: str
    platform: Optional[int]
    command: Optional[str]
    hookType: Optional[str]
    cli: Optional[bool]
    def __init__(self, duration: float, name: str, start_time: float, bstack11l11l11111_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11l11l11111_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack11lll_opy_ (u"ࠣ࡯ࡨࡥࡸࡻࡲࡦࠤᰈ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1lll1ll1lll_opy_:
    global bstack11l111ll1ll_opy_
    @staticmethod
    def bstack1lll111l111_opy_(key: str):
        bstack1ll1lll1l1l_opy_ = bstack1lll1ll1lll_opy_.bstack1l111lll111_opy_(key)
        bstack1lll1ll1lll_opy_.mark(bstack1ll1lll1l1l_opy_+bstack11lll_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᰉ"))
        return bstack1ll1lll1l1l_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11l111ll1ll_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack11lll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᰊ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1lll1ll1lll_opy_.mark(end)
            bstack1lll1ll1lll_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack11lll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶ࠾ࠥࢁࡽࠣᰋ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11l111ll1ll_opy_ or end not in bstack11l111ll1ll_opy_:
                logger.debug(bstack11lll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡶࡤࡶࡹࠦ࡫ࡦࡻࠣࡻ࡮ࡺࡨࠡࡸࡤࡰࡺ࡫ࠠࡼࡿࠣࡳࡷࠦࡥ࡯ࡦࠣ࡯ࡪࡿࠠࡸ࡫ࡷ࡬ࠥࡼࡡ࡭ࡷࡨࠤࢀࢃࠢᰌ").format(start,end))
                return
            duration: float = bstack11l111ll1ll_opy_[end] - bstack11l111ll1ll_opy_[start]
            bstack11l111llll1_opy_ = os.environ.get(bstack11lll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤࡏࡓࡠࡔࡘࡒࡓࡏࡎࡈࠤᰍ"), bstack11lll_opy_ (u"ࠢࡧࡣ࡯ࡷࡪࠨᰎ")).lower() == bstack11lll_opy_ (u"ࠣࡶࡵࡹࡪࠨᰏ")
            bstack11l111lllll_opy_: bstack11l11l1111l_opy_ = bstack11l11l1111l_opy_(duration, label, bstack11l111ll1ll_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack11lll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠤᰐ"), 0), command, test_name, hook_type, bstack11l111llll1_opy_)
            del bstack11l111ll1ll_opy_[start]
            del bstack11l111ll1ll_opy_[end]
            bstack1lll1ll1lll_opy_.bstack11l111lll11_opy_(bstack11l111lllll_opy_)
        except Exception as e:
            logger.debug(bstack11lll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡨࡥࡸࡻࡲࡪࡰࡪࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴ࠼ࠣࡿࢂࠨᰑ").format(e))
    @staticmethod
    def bstack11l111lll11_opy_(bstack11l111lllll_opy_):
        os.makedirs(os.path.dirname(bstack11ll1111ll_opy_)) if not os.path.exists(os.path.dirname(bstack11ll1111ll_opy_)) else None
        bstack1lll1ll1lll_opy_.bstack11l111ll1l1_opy_()
        try:
            with lock:
                with open(bstack11ll1111ll_opy_, bstack11lll_opy_ (u"ࠦࡷ࠱ࠢᰒ"), encoding=bstack11lll_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᰓ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11l111lllll_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11l111ll11l_opy_:
            logger.debug(bstack11lll_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠠࡼࡿࠥᰔ").format(bstack11l111ll11l_opy_))
            with lock:
                with open(bstack11ll1111ll_opy_, bstack11lll_opy_ (u"ࠢࡸࠤᰕ"), encoding=bstack11lll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᰖ")) as file:
                    data = [bstack11l111lllll_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack11lll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴࠢࡤࡴࡵ࡫࡮ࡥࠢࡾࢁࠧᰗ").format(str(e)))
        finally:
            if os.path.exists(bstack11ll1111ll_opy_+bstack11lll_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤᰘ")):
                os.remove(bstack11ll1111ll_opy_+bstack11lll_opy_ (u"ࠦ࠳ࡲ࡯ࡤ࡭ࠥᰙ"))
    @staticmethod
    def bstack11l111ll1l1_opy_():
        attempt = 0
        while (attempt < bstack11l111lll1l_opy_):
            attempt += 1
            if os.path.exists(bstack11ll1111ll_opy_+bstack11lll_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦᰚ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack1l111lll111_opy_(label: str) -> str:
        try:
            return bstack11lll_opy_ (u"ࠨࡻࡾ࠼ࡾࢁࠧᰛ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack11lll_opy_ (u"ࠢࡆࡴࡵࡳࡷࡀࠠࡼࡿࠥᰜ").format(e))