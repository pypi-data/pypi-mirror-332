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
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack11111l1lll_opy_ import (
    bstack1111l1l111_opy_,
    bstack1111ll111l_opy_,
    bstack11111lll11_opy_,
    bstack1111l1llll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l1ll1_opy_ import bstack111111l111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_, bstack1llll11lll1_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack111l111lll_opy_ import bstack111l11l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1llll1l_opy_ import bstack1lllll11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1lll1_opy_ import bstack1111111l11_opy_
from browserstack_sdk.sdk_cli.bstack1llll1111l1_opy_ import bstack1lll1l11l1l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack11l1lll1_opy_ import bstack1lll1ll1lll_opy_
import grpc
import traceback
import json
class bstack1llllll11ll_opy_(bstack111l11l1ll_opy_):
    bstack1ll1lll11l1_opy_ = False
    bstack1ll1lll1ll1_opy_ = bstack11lll_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸࠢႷ")
    bstack1lll11111l1_opy_ = bstack11lll_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧ࠱ࡻࡪࡨࡤࡳ࡫ࡹࡩࡷࠨႸ")
    bstack1ll1l1ll11l_opy_ = bstack11lll_opy_ (u"ࠦࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣ࡮ࡴࡩࡵࠤႹ")
    bstack1lll1111ll1_opy_ = bstack11lll_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤ࡯ࡳࡠࡵࡦࡥࡳࡴࡩ࡯ࡩࠥႺ")
    bstack1ll1ll1ll11_opy_ = bstack11lll_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡥࡨࡢࡵࡢࡹࡷࡲࠢႻ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1lllllllll1_opy_, bstack1llllll1ll1_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        if not self.is_enabled():
            return
        self.bstack1ll1ll1ll1l_opy_ = bstack1llllll1ll1_opy_
        bstack1lllllllll1_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111ll1111_opy_, bstack1111ll111l_opy_.PRE), self.bstack1ll1llll111_opy_)
        TestFramework.bstack1ll1l1lll1l_opy_((bstack1lll1lll1ll_opy_.TEST, bstack1lll1lll11l_opy_.PRE), self.bstack1ll1lll1lll_opy_)
        TestFramework.bstack1ll1l1lll1l_opy_((bstack1lll1lll1ll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1lll111l11l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1lll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1lll1111l1l_opy_(instance, args)
        test_framework = f.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll1ll1l111_opy_)
        if bstack11lll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫႼ") in instance.bstack1lll111111l_opy_:
            platform_index = f.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll1lll1111_opy_)
            self.accessibility = self.bstack11l1l1lll_opy_(tags) and self.bstack1l11l1lll_opy_(self.config[bstack11lll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫႽ")][platform_index])
        else:
            capabilities = self.bstack1ll1ll1ll1l_opy_.bstack1ll1l1lllll_opy_(f, instance, bstack1111llll11_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack11lll_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡦࡰࡷࡱࡨࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤႾ") + str(kwargs) + bstack11lll_opy_ (u"ࠥࠦႿ"))
                return
            self.accessibility = self.bstack11l1l1lll_opy_(tags) and self.bstack1l11l1lll_opy_(capabilities)
        if self.bstack1ll1ll1ll1l_opy_.bstack1ll1ll1l11l_opy_ and self.bstack1ll1ll1ll1l_opy_.bstack1ll1ll1l11l_opy_.values():
            bstack1ll1lll11ll_opy_ = list(self.bstack1ll1ll1ll1l_opy_.bstack1ll1ll1l11l_opy_.values())
            if bstack1ll1lll11ll_opy_ and isinstance(bstack1ll1lll11ll_opy_[0], (list, tuple)) and bstack1ll1lll11ll_opy_[0]:
                bstack1ll1ll11ll1_opy_ = bstack1ll1lll11ll_opy_[0][0]
                if callable(bstack1ll1ll11ll1_opy_):
                    page = bstack1ll1ll11ll1_opy_()
                    def bstack11l1ll1l11_opy_():
                        self.get_accessibility_results(page, bstack11lll_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣჀ"))
                    def bstack1ll1l1lll11_opy_():
                        self.get_accessibility_results_summary(page, bstack11lll_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤჁ"))
                    setattr(page, bstack11lll_opy_ (u"ࠨࡧࡦࡶࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡔࡨࡷࡺࡲࡴࡴࠤჂ"), bstack11l1ll1l11_opy_)
                    setattr(page, bstack11lll_opy_ (u"ࠢࡨࡧࡷࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡕࡩࡸࡻ࡬ࡵࡕࡸࡱࡲࡧࡲࡺࠤჃ"), bstack1ll1l1lll11_opy_)
        self.logger.debug(bstack11lll_opy_ (u"ࠣࡵ࡫ࡳࡺࡲࡤࠡࡴࡸࡲࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡼࡡ࡭ࡷࡨࡁࠧჄ") + str(self.accessibility) + bstack11lll_opy_ (u"ࠤࠥჅ"))
    def bstack1ll1llll111_opy_(
        self,
        f: bstack111111l111_opy_,
        driver: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            bstack11lll1l11l_opy_ = datetime.now()
            self.bstack1ll1ll11l11_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠥࡥ࠶࠷ࡹ࠻࡫ࡱ࡭ࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡣࡰࡰࡩ࡭࡬ࠨ჆"), datetime.now() - bstack11lll1l11l_opy_)
            if (
                not f.bstack1lll1111111_opy_(method_name)
                or f.bstack1ll1ll1111l_opy_(method_name, *args)
                or f.bstack1ll1l1ll1ll_opy_(method_name, *args)
            ):
                return
            if not f.bstack11111l11l1_opy_(instance, bstack1llllll11ll_opy_.bstack1ll1l1ll11l_opy_, False):
                if not bstack1llllll11ll_opy_.bstack1ll1lll11l1_opy_:
                    self.logger.warning(bstack11lll_opy_ (u"ࠦࡠࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࠢჇ") + str(f.platform_index) + bstack11lll_opy_ (u"ࠧࡣࠠࡢ࠳࠴ࡽࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡭ࡧࡶࡦࠢࡱࡳࡹࠦࡢࡦࡧࡱࠤࡸ࡫ࡴࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡷࡪࡹࡳࡪࡱࡱࠦ჈"))
                    bstack1llllll11ll_opy_.bstack1ll1lll11l1_opy_ = True
                return
            bstack1ll1ll1l1ll_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1ll1ll1l1ll_opy_:
                platform_index = f.bstack11111l11l1_opy_(instance, bstack111111l111_opy_.bstack1ll1lll1111_opy_, 0)
                self.logger.debug(bstack11lll_opy_ (u"ࠨ࡮ࡰࠢࡤ࠵࠶ࡿࠠࡴࡥࡵ࡭ࡵࡺࡳࠡࡨࡲࡶࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࡻࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࠦ჉") + str(f.framework_name) + bstack11lll_opy_ (u"ࠢࠣ჊"))
                return
            bstack1ll1l1ll1l1_opy_ = f.bstack1ll1lllllll_opy_(*args)
            if not bstack1ll1l1ll1l1_opy_:
                self.logger.debug(bstack11lll_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࠥ჋") + str(method_name) + bstack11lll_opy_ (u"ࠤࠥ჌"))
                return
            bstack1lll1111l11_opy_ = f.bstack11111l11l1_opy_(instance, bstack1llllll11ll_opy_.bstack1ll1ll1ll11_opy_, False)
            if bstack1ll1l1ll1l1_opy_ == bstack11lll_opy_ (u"ࠥ࡫ࡪࡺࠢჍ") and not bstack1lll1111l11_opy_:
                f.bstack1111ll11ll_opy_(instance, bstack1llllll11ll_opy_.bstack1ll1ll1ll11_opy_, True)
            if not bstack1lll1111l11_opy_:
                self.logger.debug(bstack11lll_opy_ (u"ࠦࡳࡵࠠࡖࡔࡏࠤࡱࡵࡡࡥࡧࡧࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦ࠿ࠥ჎") + str(bstack1ll1l1ll1l1_opy_) + bstack11lll_opy_ (u"ࠧࠨ჏"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(bstack1ll1l1ll1l1_opy_, [])
            if not scripts_to_run:
                self.logger.debug(bstack11lll_opy_ (u"ࠨ࡮ࡰࠢࡤ࠵࠶ࡿࠠࡴࡥࡵ࡭ࡵࡺࡳࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀࠤࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࡀࠦა") + str(bstack1ll1l1ll1l1_opy_) + bstack11lll_opy_ (u"ࠢࠣბ"))
                return
            self.logger.info(bstack11lll_opy_ (u"ࠣࡴࡸࡲࡳ࡯࡮ࡨࠢࡾࡰࡪࡴࠨࡴࡥࡵ࡭ࡵࡺࡳࡠࡶࡲࡣࡷࡻ࡮ࠪࡿࠣࡷࡨࡸࡩࡱࡶࡶࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࢁࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦ࠿ࠥგ") + str(bstack1ll1l1ll1l1_opy_) + bstack11lll_opy_ (u"ࠤࠥდ"))
            scripts = [(s, bstack1ll1ll1l1ll_opy_[s]) for s in scripts_to_run if s in bstack1ll1ll1l1ll_opy_]
            for bstack1ll1llll11l_opy_, bstack1lll111l1ll_opy_ in scripts:
                try:
                    bstack11lll1l11l_opy_ = datetime.now()
                    if bstack1ll1llll11l_opy_ == bstack11lll_opy_ (u"ࠥࡷࡨࡧ࡮ࠣე"):
                        result = self.perform_scan(driver, method=bstack1ll1l1ll1l1_opy_, framework_name=f.framework_name)
                    instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࠥვ") + bstack1ll1llll11l_opy_, datetime.now() - bstack11lll1l11l_opy_)
                    if isinstance(result, dict) and not result.get(bstack11lll_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸࠨზ"), True):
                        self.logger.warning(bstack11lll_opy_ (u"ࠨࡳ࡬࡫ࡳࠤࡪࡾࡥࡤࡷࡷ࡭ࡳ࡭ࠠࡳࡧࡰࡥ࡮ࡴࡩ࡯ࡩࠣࡷࡨࡸࡩࡱࡶࡶ࠾ࠥࠨთ") + str(result) + bstack11lll_opy_ (u"ࠢࠣი"))
                        break
                except Exception as e:
                    self.logger.error(bstack11lll_opy_ (u"ࠣࡧࡵࡶࡴࡸࠠࡦࡺࡨࡧࡺࡺࡩ࡯ࡩࠣࡷࡨࡸࡩࡱࡶࡀࡿࡸࡩࡲࡪࡲࡷࡣࡳࡧ࡭ࡦࡿࠣࡩࡷࡸ࡯ࡳ࠿ࠥკ") + str(e) + bstack11lll_opy_ (u"ࠤࠥლ"))
        except Exception as e:
            self.logger.error(bstack11lll_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫ࠠࡦࡴࡵࡳࡷࡃࠢმ") + str(e) + bstack11lll_opy_ (u"ࠦࠧნ"))
    def bstack1lll111l11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll11lll1_opy_,
        bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        if not self.accessibility:
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡡ࠲࠳ࡼࠤࡳࡵࡴࠡࡧࡱࡥࡧࡲࡥࡥࠤო"))
            return
        driver = self.bstack1ll1ll1ll1l_opy_.bstack1ll1ll11111_opy_(f, instance, bstack1111llll11_opy_, *args, **kwargs)
        test_name = f.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll1lll1l11_opy_)
        if not test_name:
            self.logger.debug(bstack11lll_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡮ࡢ࡯ࡨࠦპ"))
            return
        test_uuid = f.bstack11111l11l1_opy_(instance, TestFramework.bstack1ll1llll1l1_opy_)
        if not test_uuid:
            self.logger.debug(bstack11lll_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡶࡷ࡬ࡨࠧჟ"))
            return
        if isinstance(self.bstack1ll1ll1ll1l_opy_, bstack1111111l11_opy_):
            framework_name = bstack11lll_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬრ")
        else:
            framework_name = bstack11lll_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫს")
        self.bstack11lll111l_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll1lll1l1l_opy_ = bstack1lll1ll1lll_opy_.bstack1lll111l111_opy_(EVENTS.bstack1l1lllll1l_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack11lll_opy_ (u"ࠥࡴࡪࡸࡦࡰࡴࡰࡣࡸࡩࡡ࡯࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࠦტ"))
            return
        bstack11lll1l11l_opy_ = datetime.now()
        bstack1lll111l1ll_opy_ = self.scripts.get(framework_name, {}).get(bstack11lll_opy_ (u"ࠦࡸࡩࡡ࡯ࠤუ"), None)
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠧࡴࡥࡤࡲࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧფ") + str(framework_name) + bstack11lll_opy_ (u"ࠨࠠࠣქ"))
            return
        instance = bstack11111lll11_opy_.bstack11111lllll_opy_(driver)
        if instance:
            if not bstack11111lll11_opy_.bstack11111l11l1_opy_(instance, bstack1llllll11ll_opy_.bstack1lll1111ll1_opy_, False):
                bstack11111lll11_opy_.bstack1111ll11ll_opy_(instance, bstack1llllll11ll_opy_.bstack1lll1111ll1_opy_, True)
            else:
                self.logger.info(bstack11lll_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠࡢ࡮ࡵࡩࡦࡪࡹࠡ࡫ࡱࠤࡵࡸ࡯ࡨࡴࡨࡷࡸࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿࠣࡱࡪࡺࡨࡰࡦࡀࠦღ") + str(method) + bstack11lll_opy_ (u"ࠣࠤყ"))
                return
        self.logger.info(bstack11lll_opy_ (u"ࠤࡳࡩࡷ࡬࡯ࡳ࡯ࡢࡷࡨࡧ࡮࠻ࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡃࠢშ") + str(method) + bstack11lll_opy_ (u"ࠥࠦჩ"))
        if framework_name == bstack11lll_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨც"):
            result = self.bstack1ll1ll1ll1l_opy_.bstack1ll1l1llll1_opy_(driver, bstack1lll111l1ll_opy_)
        else:
            result = driver.execute_async_script(bstack1lll111l1ll_opy_, {bstack11lll_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠧძ"): method if method else bstack11lll_opy_ (u"ࠨࠢწ")})
        bstack1lll1ll1lll_opy_.end(EVENTS.bstack1l1lllll1l_opy_.value, bstack1ll1lll1l1l_opy_+bstack11lll_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢჭ"), bstack1ll1lll1l1l_opy_+bstack11lll_opy_ (u"ࠣ࠼ࡨࡲࡩࠨხ"), True, None, command=method)
        if instance:
            bstack11111lll11_opy_.bstack1111ll11ll_opy_(instance, bstack1llllll11ll_opy_.bstack1lll1111ll1_opy_, False)
            instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠤࡤ࠵࠶ࡿ࠺ࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࠨჯ"), datetime.now() - bstack11lll1l11l_opy_)
        return result
    @measure(event_name=EVENTS.bstack1l1l11ll11_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11lll_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࡳ࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠧჰ"))
            return
        bstack1lll111l1ll_opy_ = self.scripts.get(framework_name, {}).get(bstack11lll_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠣჱ"), None)
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫࠥࡹࡣࡳ࡫ࡳࡸࠥ࡬࡯ࡳࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࡀࠦჲ") + str(framework_name) + bstack11lll_opy_ (u"ࠨࠢჳ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11lll1l11l_opy_ = datetime.now()
        if framework_name == bstack11lll_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫჴ"):
            result = self.bstack1ll1ll1ll1l_opy_.bstack1ll1l1llll1_opy_(driver, bstack1lll111l1ll_opy_)
        else:
            result = driver.execute_async_script(bstack1lll111l1ll_opy_)
        instance = bstack11111lll11_opy_.bstack11111lllll_opy_(driver)
        if instance:
            instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡶࡪࡹࡵ࡭ࡶࡶࠦჵ"), datetime.now() - bstack11lll1l11l_opy_)
        return result
    @measure(event_name=EVENTS.bstack1lll11ll_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack11lll_opy_ (u"ࠤࡪࡩࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡲࡦࡵࡸࡰࡹࡹ࡟ࡴࡷࡰࡱࡦࡸࡹ࠻ࠢࡤ࠵࠶ࡿࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠧჶ"))
            return
        bstack1lll111l1ll_opy_ = self.scripts.get(framework_name, {}).get(bstack11lll_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠢჷ"), None)
        if not bstack1lll111l1ll_opy_:
            self.logger.debug(bstack11lll_opy_ (u"ࠦࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠪࠤࡸࡩࡲࡪࡲࡷࠤ࡫ࡵࡲࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࠥჸ") + str(framework_name) + bstack11lll_opy_ (u"ࠧࠨჹ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11lll1l11l_opy_ = datetime.now()
        if framework_name == bstack11lll_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪჺ"):
            result = self.bstack1ll1ll1ll1l_opy_.bstack1ll1l1llll1_opy_(driver, bstack1lll111l1ll_opy_)
        else:
            result = driver.execute_async_script(bstack1lll111l1ll_opy_)
        instance = bstack11111lll11_opy_.bstack11111lllll_opy_(driver)
        if instance:
            instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠢࡢ࠳࠴ࡽ࠿࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵࡢࡷࡺࡳ࡭ࡢࡴࡼࠦ჻"), datetime.now() - bstack11lll1l11l_opy_)
        return result
    @measure(event_name=EVENTS.bstack1ll1lllll1l_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def bstack1ll1ll1llll_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack111l11l11l_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack111l11l1l1_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack11lll_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥჼ") + str(r) + bstack11lll_opy_ (u"ࠤࠥჽ"))
            else:
                self.bstack1ll1llllll1_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣჾ") + str(e) + bstack11lll_opy_ (u"ࠦࠧჿ"))
            traceback.print_exc()
            raise e
    def bstack1ll1llllll1_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡲ࡯ࡢࡦࡢࡧࡴࡴࡦࡪࡩ࠽ࠤࡦ࠷࠱ࡺࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧᄀ"))
            return False
        if result.accessibility.options:
            options = result.accessibility.options
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1ll1ll111ll_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1ll1lll1ll1_opy_ and command.module == self.bstack1lll11111l1_opy_:
                        if command.method and not command.method in bstack1ll1ll111ll_opy_:
                            bstack1ll1ll111ll_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1ll1ll111ll_opy_[command.method]:
                            bstack1ll1ll111ll_opy_[command.method][command.name] = list()
                        bstack1ll1ll111ll_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1ll1ll111ll_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1ll1ll11l11_opy_(
        self,
        f: bstack111111l111_opy_,
        exec: Tuple[bstack1111l1llll_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1ll1ll1ll1l_opy_, bstack1111111l11_opy_) and method_name != bstack11lll_opy_ (u"࠭ࡣࡰࡰࡱࡩࡨࡺࠧᄁ"):
            return
        if bstack11111lll11_opy_.bstack1111ll1l11_opy_(instance, bstack1llllll11ll_opy_.bstack1ll1l1ll11l_opy_):
            return
        if not f.bstack1lll11111ll_opy_(instance):
            if not bstack1llllll11ll_opy_.bstack1ll1lll11l1_opy_:
                self.logger.warning(bstack11lll_opy_ (u"ࠢࡢ࠳࠴ࡽࠥ࡬࡬ࡰࡹࠣࡨ࡮ࡹࡡࡣ࡮ࡨࡨࠥ࡬࡯ࡳࠢࡱࡳࡳ࠳ࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥ࡯࡮ࡧࡴࡤࠦᄂ"))
                bstack1llllll11ll_opy_.bstack1ll1lll11l1_opy_ = True
            return
        if f.bstack1ll1ll111l1_opy_(method_name, *args):
            bstack1ll1ll11lll_opy_ = False
            desired_capabilities = f.bstack1lll1111lll_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1ll1l1ll111_opy_(instance)
                platform_index = f.bstack11111l11l1_opy_(instance, bstack111111l111_opy_.bstack1ll1lll1111_opy_, 0)
                bstack1ll1ll1lll1_opy_ = datetime.now()
                r = self.bstack1ll1ll1llll_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠣࡩࡵࡴࡨࡀࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡣࡰࡰࡩ࡭࡬ࠨᄃ"), datetime.now() - bstack1ll1ll1lll1_opy_)
                bstack1ll1ll11lll_opy_ = r.success
            else:
                self.logger.error(bstack11lll_opy_ (u"ࠤࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡨࡪࡹࡩࡳࡧࡧࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࡀࠦᄄ") + str(desired_capabilities) + bstack11lll_opy_ (u"ࠥࠦᄅ"))
            f.bstack1111ll11ll_opy_(instance, bstack1llllll11ll_opy_.bstack1ll1l1ll11l_opy_, bstack1ll1ll11lll_opy_)
    def bstack11l1l1lll_opy_(self, test_tags):
        bstack1ll1ll1llll_opy_ = self.config.get(bstack11lll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᄆ"))
        if not bstack1ll1ll1llll_opy_:
            return True
        try:
            include_tags = bstack1ll1ll1llll_opy_[bstack11lll_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᄇ")] if bstack11lll_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᄈ") in bstack1ll1ll1llll_opy_ and isinstance(bstack1ll1ll1llll_opy_[bstack11lll_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᄉ")], list) else []
            exclude_tags = bstack1ll1ll1llll_opy_[bstack11lll_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᄊ")] if bstack11lll_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧᄋ") in bstack1ll1ll1llll_opy_ and isinstance(bstack1ll1ll1llll_opy_[bstack11lll_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᄌ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack11lll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦᄍ") + str(error))
        return False
    def bstack1l11l1lll_opy_(self, caps):
        try:
            bstack1ll1ll11l1l_opy_ = caps.get(bstack11lll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᄎ"), {}).get(bstack11lll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪᄏ"), caps.get(bstack11lll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧᄐ"), bstack11lll_opy_ (u"ࠨࠩᄑ")))
            if bstack1ll1ll11l1l_opy_:
                self.logger.warning(bstack11lll_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨᄒ"))
                return False
            browser = caps.get(bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᄓ"), bstack11lll_opy_ (u"ࠫࠬᄔ")).lower()
            if browser != bstack11lll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬᄕ"):
                self.logger.warning(bstack11lll_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤᄖ"))
                return False
            browser_version = caps.get(bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᄗ"))
            if browser_version and browser_version != bstack11lll_opy_ (u"ࠨ࡮ࡤࡸࡪࡹࡴࠨᄘ") and int(browser_version.split(bstack11lll_opy_ (u"ࠩ࠱ࠫᄙ"))[0]) <= 98:
                self.logger.warning(bstack11lll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡭ࡲࡦࡣࡷࡩࡷࠦࡴࡩࡣࡱࠤ࠾࠾࠮ࠣᄚ"))
                return False
            bstack1ll1lll111l_opy_ = caps.get(bstack11lll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᄛ"), {}).get(bstack11lll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᄜ"))
            if bstack1ll1lll111l_opy_ and bstack11lll_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪᄝ") in bstack1ll1lll111l_opy_.get(bstack11lll_opy_ (u"ࠧࡢࡴࡪࡷࠬᄞ"), []):
                self.logger.warning(bstack11lll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥᄟ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack11lll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡤࡰ࡮ࡪࡡࡵࡧࠣࡥ࠶࠷ࡹࠡࡵࡸࡴࡵࡵࡲࡵࠢ࠽ࠦᄠ") + str(error))
            return False
    def bstack11lll111l_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll1lll1l1l_opy_ = None
        try:
            bstack1lll111l1l1_opy_ = {
                bstack11lll_opy_ (u"ࠪࡸ࡭࡚ࡥࡴࡶࡕࡹࡳ࡛ࡵࡪࡦࠪᄡ"): test_uuid,
                bstack11lll_opy_ (u"ࠫࡹ࡮ࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᄢ"): os.environ.get(bstack11lll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᄣ"), bstack11lll_opy_ (u"࠭ࠧᄤ")),
                bstack11lll_opy_ (u"ࠧࡵࡪࡍࡻࡹ࡚࡯࡬ࡧࡱࠫᄥ"): os.environ.get(bstack11lll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᄦ"), bstack11lll_opy_ (u"ࠩࠪᄧ"))
            }
            self.logger.debug(bstack11lll_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡡࡷ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭ᄨ") + str(bstack1lll111l1l1_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            bstack1lll111l1ll_opy_ = self.scripts.get(framework_name, {}).get(bstack11lll_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤᄩ"), None)
            if not bstack1lll111l1ll_opy_:
                self.logger.debug(bstack11lll_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࠧࡴࡣࡹࡩࡗ࡫ࡳࡶ࡮ࡷࡷࠬࠦࡳࡤࡴ࡬ࡴࡹࠦࡦࡰࡴࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࡁࠧᄪ") + str(framework_name) + bstack11lll_opy_ (u"ࠨࠠࠣᄫ"))
                return
            bstack1ll1lll1l1l_opy_ = bstack1lll1ll1lll_opy_.bstack1lll111l111_opy_(EVENTS.bstack1ll1llll1ll_opy_.value)
            self.bstack1ll1ll1l1l1_opy_(driver, bstack1lll111l1ll_opy_, bstack1lll111l1l1_opy_, framework_name)
            self.logger.info(bstack11lll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠥᄬ"))
            bstack1lll1ll1lll_opy_.end(EVENTS.bstack1ll1llll1ll_opy_.value, bstack1ll1lll1l1l_opy_+bstack11lll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᄭ"), bstack1ll1lll1l1l_opy_+bstack11lll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᄮ"), True, None, command=bstack11lll_opy_ (u"ࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨᄯ"),test_name=name)
        except Exception as bstack1ll1lllll11_opy_:
            self.logger.error(bstack11lll_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡩ࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨᄰ") + bstack11lll_opy_ (u"ࠧࡹࡴࡳࠪࡳࡥࡹ࡮ࠩࠣᄱ") + bstack11lll_opy_ (u"ࠨࠠࡆࡴࡵࡳࡷࠦ࠺ࠣᄲ") + str(bstack1ll1lllll11_opy_))
            bstack1lll1ll1lll_opy_.end(EVENTS.bstack1ll1llll1ll_opy_.value, bstack1ll1lll1l1l_opy_+bstack11lll_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᄳ"), bstack1ll1lll1l1l_opy_+bstack11lll_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᄴ"), False, bstack1ll1lllll11_opy_, command=bstack11lll_opy_ (u"ࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧᄵ"),test_name=name)
    def bstack1ll1ll1l1l1_opy_(self, driver, bstack1lll111l1ll_opy_, bstack1lll111l1l1_opy_, framework_name):
        if framework_name == bstack11lll_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᄶ"):
            self.bstack1ll1ll1ll1l_opy_.bstack1ll1l1llll1_opy_(driver, bstack1lll111l1ll_opy_, bstack1lll111l1l1_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1lll111l1ll_opy_, bstack1lll111l1l1_opy_))
    def _1lll1111l1l_opy_(self, instance: bstack1llll11lll1_opy_, args: Tuple) -> list:
        bstack11lll_opy_ (u"ࠦࠧࠨࡅࡹࡶࡵࡥࡨࡺࠠࡵࡣࡪࡷࠥࡨࡡࡴࡧࡧࠤࡴࡴࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯࠳ࠨࠢࠣᄷ")
        if bstack11lll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩᄸ") in instance.bstack1lll111111l_opy_:
            return args[2].tags if hasattr(args[2], bstack11lll_opy_ (u"࠭ࡴࡢࡩࡶࠫᄹ")) else []
        if hasattr(args[0], bstack11lll_opy_ (u"ࠧࡰࡹࡱࡣࡲࡧࡲ࡬ࡧࡵࡷࠬᄺ")):
            return [marker.name for marker in args[0].own_markers]
        return []