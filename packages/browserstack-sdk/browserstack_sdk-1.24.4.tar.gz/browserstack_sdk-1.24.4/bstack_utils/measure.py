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
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1l111l11ll_opy_ import get_logger
from bstack_utils.bstack1ll11ll111_opy_ import bstack1lll11ll1l1_opy_
bstack1ll11ll111_opy_ = bstack1lll11ll1l1_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1l1l11l111_opy_: Optional[str] = None):
    bstack11ll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡊࡥࡤࡱࡵࡥࡹࡵࡲࠡࡶࡲࠤࡱࡵࡧࠡࡶ࡫ࡩࠥࡹࡴࡢࡴࡷࠤࡹ࡯࡭ࡦࠢࡲࡪࠥࡧࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠏࠦࠠࠡࠢࡤࡰࡴࡴࡧࠡࡹ࡬ࡸ࡭ࠦࡥࡷࡧࡱࡸࠥࡴࡡ࡮ࡧࠣࡥࡳࡪࠠࡴࡶࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᬐ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll1ll11l11_opy_: str = bstack1ll11ll111_opy_.bstack1l11l11llll_opy_(label)
            start_mark: str = label + bstack11ll1l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᬑ")
            end_mark: str = label + bstack11ll1l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᬒ")
            result = None
            try:
                if stage.value == STAGE.bstack1l11ll1l11_opy_.value:
                    bstack1ll11ll111_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1ll11ll111_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1l1l11l111_opy_)
                elif stage.value == STAGE.bstack1111l111_opy_.value:
                    start_mark: str = bstack1ll1ll11l11_opy_ + bstack11ll1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᬓ")
                    end_mark: str = bstack1ll1ll11l11_opy_ + bstack11ll1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᬔ")
                    bstack1ll11ll111_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1ll11ll111_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1l1l11l111_opy_)
            except Exception as e:
                bstack1ll11ll111_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1l1l11l111_opy_)
            return result
        return wrapper
    return decorator