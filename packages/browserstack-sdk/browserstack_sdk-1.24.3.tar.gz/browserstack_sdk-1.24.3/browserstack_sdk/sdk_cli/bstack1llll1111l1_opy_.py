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
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack11111l1lll_opy_ import (
    bstack11111lll11_opy_,
    bstack1111l1llll_opy_,
    bstack1111l1l111_opy_,
    bstack1111ll111l_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
class bstack1lll1l11l1l_opy_(bstack11111lll11_opy_):
    bstack1l1l1l1l1l1_opy_ = bstack11lll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠤዮ")
    bstack1l1llll1l1l_opy_ = bstack11lll_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥዯ")
    bstack1l1llll1l11_opy_ = bstack11lll_opy_ (u"ࠦ࡭ࡻࡢࡠࡷࡵࡰࠧደ")
    bstack1l1lll1l1l1_opy_ = bstack11lll_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦዱ")
    bstack1l1l1l11lll_opy_ = bstack11lll_opy_ (u"ࠨࡷ࠴ࡥࡨࡼࡪࡩࡵࡵࡧࡶࡧࡷ࡯ࡰࡵࠤዲ")
    bstack1l1l1l11l11_opy_ = bstack11lll_opy_ (u"ࠢࡸ࠵ࡦࡩࡽ࡫ࡣࡶࡶࡨࡷࡨࡸࡩࡱࡶࡤࡷࡾࡴࡣࠣዳ")
    NAME = bstack11lll_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧዴ")
    bstack1l1l1l11ll1_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llllll1l11_opy_: Any
    bstack1l1l1l11l1l_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack11lll_opy_ (u"ࠤ࡯ࡥࡺࡴࡣࡩࠤድ"), bstack11lll_opy_ (u"ࠥࡧࡴࡴ࡮ࡦࡥࡷࠦዶ"), bstack11lll_opy_ (u"ࠦࡳ࡫ࡷࡠࡲࡤ࡫ࡪࠨዷ"), bstack11lll_opy_ (u"ࠧࡩ࡬ࡰࡵࡨࠦዸ"), bstack11lll_opy_ (u"ࠨࡤࡪࡵࡳࡥࡹࡩࡨࠣዹ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1111llllll_opy_(methods)
    def bstack1111l1lll1_opy_(self, instance: bstack1111l1llll_opy_, method_name: str, bstack1111l11l1l_opy_: timedelta, *args, **kwargs):
        pass
    def bstack1111ll1ll1_opy_(
        self,
        target: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1111l1ll1l_opy_, bstack1l1l1l1ll1l_opy_ = bstack1111llll11_opy_
        bstack1l1l1l1ll11_opy_ = bstack1lll1l11l1l_opy_.bstack1l1l1l1l111_opy_(bstack1111llll11_opy_)
        if bstack1l1l1l1ll11_opy_ in bstack1lll1l11l1l_opy_.bstack1l1l1l11ll1_opy_:
            bstack1l1l1l1l11l_opy_ = None
            for callback in bstack1lll1l11l1l_opy_.bstack1l1l1l11ll1_opy_[bstack1l1l1l1ll11_opy_]:
                try:
                    bstack1l1l1l1l1ll_opy_ = callback(self, target, exec, bstack1111llll11_opy_, result, *args, **kwargs)
                    if bstack1l1l1l1l11l_opy_ == None:
                        bstack1l1l1l1l11l_opy_ = bstack1l1l1l1l1ll_opy_
                except Exception as e:
                    self.logger.error(bstack11lll_opy_ (u"ࠢࡦࡴࡵࡳࡷࠦࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡥࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࠧዺ") + str(e) + bstack11lll_opy_ (u"ࠣࠤዻ"))
                    traceback.print_exc()
            if bstack1l1l1l1ll1l_opy_ == bstack1111ll111l_opy_.PRE and callable(bstack1l1l1l1l11l_opy_):
                return bstack1l1l1l1l11l_opy_
            elif bstack1l1l1l1ll1l_opy_ == bstack1111ll111l_opy_.POST and bstack1l1l1l1l11l_opy_:
                return bstack1l1l1l1l11l_opy_
    def bstack11111ll11l_opy_(
        self, method_name, previous_state: bstack1111l1l111_opy_, *args, **kwargs
    ) -> bstack1111l1l111_opy_:
        if method_name == bstack11lll_opy_ (u"ࠩ࡯ࡥࡺࡴࡣࡩࠩዼ") or method_name == bstack11lll_opy_ (u"ࠪࡧࡴࡴ࡮ࡦࡥࡷࠫዽ") or method_name == bstack11lll_opy_ (u"ࠫࡳ࡫ࡷࡠࡲࡤ࡫ࡪ࠭ዾ"):
            return bstack1111l1l111_opy_.bstack1111l11111_opy_
        if method_name == bstack11lll_opy_ (u"ࠬࡪࡩࡴࡲࡤࡸࡨ࡮ࠧዿ"):
            return bstack1111l1l111_opy_.bstack1111l1l1l1_opy_
        if method_name == bstack11lll_opy_ (u"࠭ࡣ࡭ࡱࡶࡩࠬጀ"):
            return bstack1111l1l111_opy_.QUIT
        return bstack1111l1l111_opy_.NONE
    @staticmethod
    def bstack1l1l1l1l111_opy_(bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_]):
        return bstack11lll_opy_ (u"ࠢ࠻ࠤጁ").join((bstack1111l1l111_opy_(bstack1111llll11_opy_[0]).name, bstack1111ll111l_opy_(bstack1111llll11_opy_[1]).name))
    @staticmethod
    def bstack1ll1l1lll1l_opy_(bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_], callback: Callable):
        bstack1l1l1l1ll11_opy_ = bstack1lll1l11l1l_opy_.bstack1l1l1l1l111_opy_(bstack1111llll11_opy_)
        if not bstack1l1l1l1ll11_opy_ in bstack1lll1l11l1l_opy_.bstack1l1l1l11ll1_opy_:
            bstack1lll1l11l1l_opy_.bstack1l1l1l11ll1_opy_[bstack1l1l1l1ll11_opy_] = []
        bstack1lll1l11l1l_opy_.bstack1l1l1l11ll1_opy_[bstack1l1l1l1ll11_opy_].append(callback)
    @staticmethod
    def bstack1lll1111111_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1ll1ll111l1_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1lll1111lll_opy_(instance: bstack1111l1llll_opy_, default_value=None):
        return bstack11111lll11_opy_.bstack11111l11l1_opy_(instance, bstack1lll1l11l1l_opy_.bstack1l1lll1l1l1_opy_, default_value)
    @staticmethod
    def bstack1lll11111ll_opy_(instance: bstack1111l1llll_opy_) -> bool:
        return True
    @staticmethod
    def bstack1ll1l1ll111_opy_(instance: bstack1111l1llll_opy_, default_value=None):
        return bstack11111lll11_opy_.bstack11111l11l1_opy_(instance, bstack1lll1l11l1l_opy_.bstack1l1llll1l11_opy_, default_value)
    @staticmethod
    def bstack1ll1lllllll_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1ll1ll1111l_opy_(method_name: str, *args):
        if not bstack1lll1l11l1l_opy_.bstack1lll1111111_opy_(method_name):
            return False
        if not bstack1lll1l11l1l_opy_.bstack1l1l1l11lll_opy_ in bstack1lll1l11l1l_opy_.bstack1l1l1llllll_opy_(*args):
            return False
        bstack1ll1l1l1lll_opy_ = bstack1lll1l11l1l_opy_.bstack1ll1l1l1l11_opy_(*args)
        return bstack1ll1l1l1lll_opy_ and bstack11lll_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣጂ") in bstack1ll1l1l1lll_opy_ and bstack11lll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥጃ") in bstack1ll1l1l1lll_opy_[bstack11lll_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥጄ")]
    @staticmethod
    def bstack1ll1l1ll1ll_opy_(method_name: str, *args):
        if not bstack1lll1l11l1l_opy_.bstack1lll1111111_opy_(method_name):
            return False
        if not bstack1lll1l11l1l_opy_.bstack1l1l1l11lll_opy_ in bstack1lll1l11l1l_opy_.bstack1l1l1llllll_opy_(*args):
            return False
        bstack1ll1l1l1lll_opy_ = bstack1lll1l11l1l_opy_.bstack1ll1l1l1l11_opy_(*args)
        return (
            bstack1ll1l1l1lll_opy_
            and bstack11lll_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦጅ") in bstack1ll1l1l1lll_opy_
            and bstack11lll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡦࡶ࡮ࡶࡴࠣጆ") in bstack1ll1l1l1lll_opy_[bstack11lll_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨጇ")]
        )
    @staticmethod
    def bstack1l1l1llllll_opy_(*args):
        return str(bstack1lll1l11l1l_opy_.bstack1ll1lllllll_opy_(*args)).lower()