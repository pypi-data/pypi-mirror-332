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
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack111l11ll_opy_ import get_logger
from bstack_utils.bstack11l1lll1_opy_ import bstack1lll1ll1lll_opy_
bstack11l1lll1_opy_ = bstack1lll1ll1lll_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack11lllllll_opy_: Optional[str] = None):
    bstack11lll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡅࡧࡦࡳࡷࡧࡴࡰࡴࠣࡸࡴࠦ࡬ࡰࡩࠣࡸ࡭࡫ࠠࡴࡶࡤࡶࡹࠦࡴࡪ࡯ࡨࠤࡴ࡬ࠠࡢࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠊࠡࠢࠣࠤࡦࡲ࡯࡯ࡩࠣࡻ࡮ࡺࡨࠡࡧࡹࡩࡳࡺࠠ࡯ࡣࡰࡩࠥࡧ࡮ࡥࠢࡶࡸࡦ࡭ࡥ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᭃ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll1lll1l1l_opy_: str = bstack11l1lll1_opy_.bstack1l111lll111_opy_(label)
            start_mark: str = label + bstack11lll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴ᭄ࠣ")
            end_mark: str = label + bstack11lll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᭅ")
            result = None
            try:
                if stage.value == STAGE.bstack111ll11l_opy_.value:
                    bstack11l1lll1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack11l1lll1_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack11lllllll_opy_)
                elif stage.value == STAGE.bstack1lll1l1l11_opy_.value:
                    start_mark: str = bstack1ll1lll1l1l_opy_ + bstack11lll_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᭆ")
                    end_mark: str = bstack1ll1lll1l1l_opy_ + bstack11lll_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᭇ")
                    bstack11l1lll1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack11l1lll1_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack11lllllll_opy_)
            except Exception as e:
                bstack11l1lll1_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack11lllllll_opy_)
            return result
        return wrapper
    return decorator