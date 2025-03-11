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
from browserstack_sdk.sdk_cli.bstack111l111lll_opy_ import bstack111l11l1ll_opy_
from browserstack_sdk.sdk_cli.bstack11111l1lll_opy_ import (
    bstack1111l1l111_opy_,
    bstack1111ll111l_opy_,
    bstack11111lll11_opy_,
    bstack1111l1llll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l1ll1_opy_ import bstack111111l111_opy_
from browserstack_sdk.sdk_cli.bstack1llll1111l1_opy_ import bstack1lll1l11l1l_opy_
from browserstack_sdk.sdk_cli.bstack11111l1l1l_opy_ import bstack11111l11ll_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack111l111lll_opy_ import bstack111l11l1ll_opy_
import weakref
class bstack1ll1l111l11_opy_(bstack111l11l1ll_opy_):
    bstack1ll1l11l111_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1111l1llll_opy_]]
    bstack1ll1ll1l11l_opy_: Dict[str, Tuple[Callable, bstack1111l1llll_opy_]]
    def __init__(self, bstack1ll1l11l111_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.bstack1ll1ll1l11l_opy_ = dict()
        self.bstack1ll1l111111_opy_ = dict()
        self.bstack1ll1l11l111_opy_ = bstack1ll1l11l111_opy_
        self.frameworks = frameworks
        bstack1lll1l11l1l_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111l11111_opy_, bstack1111ll111l_opy_.POST), self.__1ll1l11l1l1_opy_)
        if any(bstack111111l111_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack111111l111_opy_.bstack1ll1l1lll1l_opy_(
                (bstack1111l1l111_opy_.bstack1111ll1111_opy_, bstack1111ll111l_opy_.PRE), self.__1ll1l111l1l_opy_
            )
            bstack111111l111_opy_.bstack1ll1l1lll1l_opy_(
                (bstack1111l1l111_opy_.QUIT, bstack1111ll111l_opy_.POST), self.__1ll1l1111ll_opy_
            )
    def __1ll1l11l1l1_opy_(
        self,
        f: bstack1lll1l11l1l_opy_,
        bstack1ll1l111lll_opy_: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack11lll_opy_ (u"ࠢ࡯ࡧࡺࡣࡵࡧࡧࡦࠤᅝ"):
                return
            contexts = bstack1ll1l111lll_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.bstack1ll1ll1l11l_opy_:
                        for page in context.bstack1ll1ll1l11l_opy_:
                            if bstack11lll_opy_ (u"ࠣࡣࡥࡳࡺࡺ࠺ࡣ࡮ࡤࡲࡰࠨᅞ") in page.url:
                                self.logger.debug(bstack11lll_opy_ (u"ࠤࡖࡸࡴࡸࡩ࡯ࡩࠣࡸ࡭࡫ࠠ࡯ࡧࡺࠤࡵࡧࡧࡦࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠦᅟ"))
                                self.bstack1ll1ll1l11l_opy_[instance.ref()] = weakref.ref(page), instance
                                bstack11111lll11_opy_.bstack1111ll11ll_opy_(instance, self.bstack1ll1l11l111_opy_, True)
                                self.logger.debug(bstack11lll_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡲࡤ࡫ࡪࡥࡩ࡯࡫ࡷ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᅠ") + str(instance.ref()) + bstack11lll_opy_ (u"ࠦࠧᅡ"))
        except Exception as e:
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺ࡯ࡳ࡫ࡱ࡫ࠥࡴࡥࡸࠢࡳࡥ࡬࡫ࠠ࠻ࠤᅢ"),e)
    def __1ll1l111l1l_opy_(
        self,
        f: bstack111111l111_opy_,
        driver: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack11111lll11_opy_.bstack11111l11l1_opy_(instance, self.bstack1ll1l11l111_opy_, False):
            return
        if not f.bstack1ll1l1l11ll_opy_(f.hub_url(driver)):
            self.bstack1ll1l111111_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack11111lll11_opy_.bstack1111ll11ll_opy_(instance, self.bstack1ll1l11l111_opy_, True)
            self.logger.debug(bstack11lll_opy_ (u"ࠨ࡟ࡠࡱࡱࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡩ࡯࡫ࡷ࠾ࠥࡴ࡯࡯ࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡦࡵ࡭ࡻ࡫ࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᅣ") + str(instance.ref()) + bstack11lll_opy_ (u"ࠢࠣᅤ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack11111lll11_opy_.bstack1111ll11ll_opy_(instance, self.bstack1ll1l11l111_opy_, True)
        self.logger.debug(bstack11lll_opy_ (u"ࠣࡡࡢࡳࡳࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠ࡫ࡱ࡭ࡹࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᅥ") + str(instance.ref()) + bstack11lll_opy_ (u"ࠤࠥᅦ"))
    def __1ll1l1111ll_opy_(
        self,
        f: bstack111111l111_opy_,
        driver: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1ll1l11l11l_opy_(instance)
        self.logger.debug(bstack11lll_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡵࡺ࡯ࡴ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᅧ") + str(instance.ref()) + bstack11lll_opy_ (u"ࠦࠧᅨ"))
    def bstack1ll1l11ll11_opy_(self, context: bstack11111l11ll_opy_, reverse=True) -> List[Tuple[Callable, bstack1111l1llll_opy_]]:
        matches = []
        if self.bstack1ll1ll1l11l_opy_:
            for data in self.bstack1ll1ll1l11l_opy_.values():
                if data[1].bstack1ll1l11l1ll_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack111111l111_opy_.bstack1lll11111ll_opy_(data[1])
                    and data[1].bstack1ll1l11l1ll_opy_(context)
                    and getattr(data[0](), bstack11lll_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠤᅩ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack111l111111_opy_, reverse=reverse)
    def bstack1ll1l11111l_opy_(self, context: bstack11111l11ll_opy_, reverse=True) -> List[Tuple[Callable, bstack1111l1llll_opy_]]:
        matches = []
        for data in self.bstack1ll1l111111_opy_.values():
            if (
                data[1].bstack1ll1l11l1ll_opy_(context)
                and getattr(data[0](), bstack11lll_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᅪ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack111l111111_opy_, reverse=reverse)
    def bstack1ll1l111ll1_opy_(self, instance: bstack1111l1llll_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1ll1l11l11l_opy_(self, instance: bstack1111l1llll_opy_) -> bool:
        if self.bstack1ll1l111ll1_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack11111lll11_opy_.bstack1111ll11ll_opy_(instance, self.bstack1ll1l11l111_opy_, False)
            return True
        return False