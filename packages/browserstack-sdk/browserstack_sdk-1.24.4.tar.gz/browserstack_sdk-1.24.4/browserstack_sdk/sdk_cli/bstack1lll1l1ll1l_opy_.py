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
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1111llll11_opy_ import (
    bstack1111ll1lll_opy_,
    bstack11111ll11l_opy_,
    bstack111l1111ll_opy_,
    bstack1111ll11l1_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack11111111l1_opy_(bstack1111ll1lll_opy_):
    bstack1l1l1l1ll11_opy_ = bstack11ll1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠤዮ")
    bstack1l1lll1ll1l_opy_ = bstack11ll1l_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥዯ")
    bstack1l1llll11l1_opy_ = bstack11ll1l_opy_ (u"ࠦ࡭ࡻࡢࡠࡷࡵࡰࠧደ")
    bstack1l1llll11ll_opy_ = bstack11ll1l_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦዱ")
    bstack1l1l1l1l111_opy_ = bstack11ll1l_opy_ (u"ࠨࡷ࠴ࡥࡨࡼࡪࡩࡵࡵࡧࡶࡧࡷ࡯ࡰࡵࠤዲ")
    bstack1l1l1l1l11l_opy_ = bstack11ll1l_opy_ (u"ࠢࡸ࠵ࡦࡩࡽ࡫ࡣࡶࡶࡨࡷࡨࡸࡩࡱࡶࡤࡷࡾࡴࡣࠣዳ")
    NAME = bstack11ll1l_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧዴ")
    bstack1l1l1l1ll1l_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lll1lll1l1_opy_: Any
    bstack1l1l1l1l1l1_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack11ll1l_opy_ (u"ࠤ࡯ࡥࡺࡴࡣࡩࠤድ"), bstack11ll1l_opy_ (u"ࠥࡧࡴࡴ࡮ࡦࡥࡷࠦዶ"), bstack11ll1l_opy_ (u"ࠦࡳ࡫ࡷࡠࡲࡤ࡫ࡪࠨዷ"), bstack11ll1l_opy_ (u"ࠧࡩ࡬ࡰࡵࡨࠦዸ"), bstack11ll1l_opy_ (u"ࠨࡤࡪࡵࡳࡥࡹࡩࡨࠣዹ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack11111lll1l_opy_(methods)
    def bstack1111l1ll11_opy_(self, instance: bstack11111ll11l_opy_, method_name: str, bstack111l1111l1_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1111lll1ll_opy_(
        self,
        target: object,
        exec: Tuple[bstack11111ll11l_opy_, str],
        bstack11111ll111_opy_: Tuple[bstack111l1111ll_opy_, bstack1111ll11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1111ll1ll1_opy_, bstack1l1l1l1lll1_opy_ = bstack11111ll111_opy_
        bstack1l1l1l11lll_opy_ = bstack11111111l1_opy_.bstack1l1l1l1l1ll_opy_(bstack11111ll111_opy_)
        if bstack1l1l1l11lll_opy_ in bstack11111111l1_opy_.bstack1l1l1l1ll1l_opy_:
            bstack1l1l1l11ll1_opy_ = None
            for callback in bstack11111111l1_opy_.bstack1l1l1l1ll1l_opy_[bstack1l1l1l11lll_opy_]:
                try:
                    bstack1l1l1l1llll_opy_ = callback(self, target, exec, bstack11111ll111_opy_, result, *args, **kwargs)
                    if bstack1l1l1l11ll1_opy_ == None:
                        bstack1l1l1l11ll1_opy_ = bstack1l1l1l1llll_opy_
                except Exception as e:
                    self.logger.error(bstack11ll1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠦࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡥࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࠧዺ") + str(e) + bstack11ll1l_opy_ (u"ࠣࠤዻ"))
                    traceback.print_exc()
            if bstack1l1l1l1lll1_opy_ == bstack1111ll11l1_opy_.PRE and callable(bstack1l1l1l11ll1_opy_):
                return bstack1l1l1l11ll1_opy_
            elif bstack1l1l1l1lll1_opy_ == bstack1111ll11l1_opy_.POST and bstack1l1l1l11ll1_opy_:
                return bstack1l1l1l11ll1_opy_
    def bstack1111l1lll1_opy_(
        self, method_name, previous_state: bstack111l1111ll_opy_, *args, **kwargs
    ) -> bstack111l1111ll_opy_:
        if method_name == bstack11ll1l_opy_ (u"ࠩ࡯ࡥࡺࡴࡣࡩࠩዼ") or method_name == bstack11ll1l_opy_ (u"ࠪࡧࡴࡴ࡮ࡦࡥࡷࠫዽ") or method_name == bstack11ll1l_opy_ (u"ࠫࡳ࡫ࡷࡠࡲࡤ࡫ࡪ࠭ዾ"):
            return bstack111l1111ll_opy_.bstack11111lll11_opy_
        if method_name == bstack11ll1l_opy_ (u"ࠬࡪࡩࡴࡲࡤࡸࡨ࡮ࠧዿ"):
            return bstack111l1111ll_opy_.bstack1111llllll_opy_
        if method_name == bstack11ll1l_opy_ (u"࠭ࡣ࡭ࡱࡶࡩࠬጀ"):
            return bstack111l1111ll_opy_.QUIT
        return bstack111l1111ll_opy_.NONE
    @staticmethod
    def bstack1l1l1l1l1ll_opy_(bstack11111ll111_opy_: Tuple[bstack111l1111ll_opy_, bstack1111ll11l1_opy_]):
        return bstack11ll1l_opy_ (u"ࠢ࠻ࠤጁ").join((bstack111l1111ll_opy_(bstack11111ll111_opy_[0]).name, bstack1111ll11l1_opy_(bstack11111ll111_opy_[1]).name))
    @staticmethod
    def bstack1lll111l111_opy_(bstack11111ll111_opy_: Tuple[bstack111l1111ll_opy_, bstack1111ll11l1_opy_], callback: Callable):
        bstack1l1l1l11lll_opy_ = bstack11111111l1_opy_.bstack1l1l1l1l1ll_opy_(bstack11111ll111_opy_)
        if not bstack1l1l1l11lll_opy_ in bstack11111111l1_opy_.bstack1l1l1l1ll1l_opy_:
            bstack11111111l1_opy_.bstack1l1l1l1ll1l_opy_[bstack1l1l1l11lll_opy_] = []
        bstack11111111l1_opy_.bstack1l1l1l1ll1l_opy_[bstack1l1l1l11lll_opy_].append(callback)
    @staticmethod
    def bstack1ll1l1llll1_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1ll1l1lllll_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1lll1111lll_opy_(instance: bstack11111ll11l_opy_, default_value=None):
        return bstack1111ll1lll_opy_.bstack1111lll1l1_opy_(instance, bstack11111111l1_opy_.bstack1l1llll11ll_opy_, default_value)
    @staticmethod
    def bstack1ll1l1ll1l1_opy_(instance: bstack11111ll11l_opy_) -> bool:
        return True
    @staticmethod
    def bstack1lll111l1l1_opy_(instance: bstack11111ll11l_opy_, default_value=None):
        return bstack1111ll1lll_opy_.bstack1111lll1l1_opy_(instance, bstack11111111l1_opy_.bstack1l1llll11l1_opy_, default_value)
    @staticmethod
    def bstack1lll11111l1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1ll1lll1l11_opy_(method_name: str, *args):
        if not bstack11111111l1_opy_.bstack1ll1l1llll1_opy_(method_name):
            return False
        if not bstack11111111l1_opy_.bstack1l1l1l1l111_opy_ in bstack11111111l1_opy_.bstack1l1l1lll1ll_opy_(*args):
            return False
        bstack1ll1l1l11l1_opy_ = bstack11111111l1_opy_.bstack1ll1l11llll_opy_(*args)
        return bstack1ll1l1l11l1_opy_ and bstack11ll1l_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣጂ") in bstack1ll1l1l11l1_opy_ and bstack11ll1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥጃ") in bstack1ll1l1l11l1_opy_[bstack11ll1l_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥጄ")]
    @staticmethod
    def bstack1ll1llllll1_opy_(method_name: str, *args):
        if not bstack11111111l1_opy_.bstack1ll1l1llll1_opy_(method_name):
            return False
        if not bstack11111111l1_opy_.bstack1l1l1l1l111_opy_ in bstack11111111l1_opy_.bstack1l1l1lll1ll_opy_(*args):
            return False
        bstack1ll1l1l11l1_opy_ = bstack11111111l1_opy_.bstack1ll1l11llll_opy_(*args)
        return (
            bstack1ll1l1l11l1_opy_
            and bstack11ll1l_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦጅ") in bstack1ll1l1l11l1_opy_
            and bstack11ll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡦࡶ࡮ࡶࡴࠣጆ") in bstack1ll1l1l11l1_opy_[bstack11ll1l_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨጇ")]
        )
    @staticmethod
    def bstack1l1l1lll1ll_opy_(*args):
        return str(bstack11111111l1_opy_.bstack1lll11111l1_opy_(*args)).lower()