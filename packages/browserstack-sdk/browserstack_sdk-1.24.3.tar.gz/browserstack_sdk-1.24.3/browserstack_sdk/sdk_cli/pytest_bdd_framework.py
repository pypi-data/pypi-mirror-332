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
from datetime import datetime, timezone
from pyexpat import features
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack11111l1l1l_opy_ import bstack1111ll11l1_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1lll1ll_opy_,
    bstack1llll11lll1_opy_,
    bstack1lll1lll11l_opy_,
    bstack1l11lll1lll_opy_,
    bstack1lll11l1ll1_opy_,
)
import traceback
from bstack_utils.bstack11l1lll1_opy_ import bstack1lll1ll1lll_opy_
from bstack_utils.constants import EVENTS
class PytestBDDFramework(TestFramework):
    bstack1l11lll1l1l_opy_ = bstack11lll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢገ")
    bstack1l11ll111ll_opy_ = bstack11lll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࠨጉ")
    bstack1l1l11111l1_opy_ = bstack11lll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣጊ")
    bstack1l11ll1llll_opy_ = bstack11lll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥ࡬ࡢࡵࡷࡣࡸࡺࡡࡳࡶࡨࡨࠧጋ")
    bstack1l1l11ll11l_opy_ = bstack11lll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟࡭ࡣࡶࡸࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࠢጌ")
    bstack1l1l11l1l1l_opy_: bool
    bstack1l11ll1ll11_opy_ = [
        bstack1lll1lll1ll_opy_.BEFORE_ALL,
        bstack1lll1lll1ll_opy_.AFTER_ALL,
        bstack1lll1lll1ll_opy_.BEFORE_EACH,
        bstack1lll1lll1ll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1l11llll1l1_opy_: Dict[str, str],
        bstack1lll111111l_opy_: List[str]=[bstack11lll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤግ")],
    ):
        super().__init__(bstack1lll111111l_opy_, bstack1l11llll1l1_opy_)
        self.bstack1l1l11l1l1l_opy_ = any(bstack11lll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥጎ") in item.lower() for item in bstack1lll111111l_opy_)
    def track_event(
        self,
        context: bstack1l11lll1lll_opy_,
        test_framework_state: bstack1lll1lll1ll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1lll1ll_opy_.NONE:
            self.logger.warning(bstack11lll_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫ࡤࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࠣጏ") + str(test_hook_state) + bstack11lll_opy_ (u"ࠣࠤጐ"))
            return
        if not self.bstack1l1l11l1l1l_opy_:
            self.logger.warning(bstack11lll_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠿ࠥ጑") + str(str(self.bstack1lll111111l_opy_)) + bstack11lll_opy_ (u"ࠥࠦጒ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11lll_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨጓ") + str(kwargs) + bstack11lll_opy_ (u"ࠧࠨጔ"))
            return
        instance = self.__1l1l11l1l11_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11lll_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡡࡳࡩࡶࡁࠧጕ") + str(args) + bstack11lll_opy_ (u"ࠢࠣ጖"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l11ll1ll11_opy_ and test_hook_state == bstack1lll1lll11l_opy_.PRE:
                bstack1ll1lll1l1l_opy_ = bstack1lll1ll1lll_opy_.bstack1lll111l111_opy_(EVENTS.bstack11llll11l_opy_.value)
                name = str(EVENTS.bstack11llll11l_opy_.name)+bstack11lll_opy_ (u"ࠣ࠼ࠥ጗")+str(test_framework_state.name)
                TestFramework.bstack1l1l1111l11_opy_(instance, name, bstack1ll1lll1l1l_opy_)
        except Exception as e:
            self.logger.debug(bstack11lll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࠦࡥࡳࡴࡲࡶࠥࡶࡲࡦ࠼ࠣࡿࢂࠨጘ").format(e))
        try:
            if test_framework_state == bstack1lll1lll1ll_opy_.TEST:
                if not TestFramework.bstack1111ll1l11_opy_(instance, TestFramework.bstack1l11ll11ll1_opy_) and test_hook_state == bstack1lll1lll11l_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1l1l111lll1_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack11lll_opy_ (u"ࠥࡰࡴࡧࡤࡦࡦࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥጙ") + str(test_hook_state) + bstack11lll_opy_ (u"ࠦࠧጚ"))
                if test_hook_state == bstack1lll1lll11l_opy_.PRE and not TestFramework.bstack1111ll1l11_opy_(instance, TestFramework.bstack1ll1111ll1l_opy_):
                    TestFramework.bstack1111ll11ll_opy_(instance, TestFramework.bstack1ll1111ll1l_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1l1l11llll1_opy_(instance, args)
                    self.logger.debug(bstack11lll_opy_ (u"ࠧࡹࡥࡵࠢࡷࡩࡸࡺ࠭ࡴࡶࡤࡶࡹࠦࡦࡰࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥጛ") + str(test_hook_state) + bstack11lll_opy_ (u"ࠨࠢጜ"))
                elif test_hook_state == bstack1lll1lll11l_opy_.POST and not TestFramework.bstack1111ll1l11_opy_(instance, TestFramework.bstack1ll111llll1_opy_):
                    TestFramework.bstack1111ll11ll_opy_(instance, TestFramework.bstack1ll111llll1_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11lll_opy_ (u"ࠢࡴࡧࡷࠤࡹ࡫ࡳࡵ࠯ࡨࡲࡩࠦࡦࡰࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥጝ") + str(test_hook_state) + bstack11lll_opy_ (u"ࠣࠤጞ"))
            elif test_framework_state == bstack1lll1lll1ll_opy_.STEP:
                if test_hook_state == bstack1lll1lll11l_opy_.PRE:
                    PytestBDDFramework.__1l11ll11l11_opy_(instance, args)
                elif test_hook_state == bstack1lll1lll11l_opy_.POST:
                    PytestBDDFramework.__1l1l11ll111_opy_(instance, args)
            elif test_framework_state == bstack1lll1lll1ll_opy_.LOG and test_hook_state == bstack1lll1lll11l_opy_.POST:
                PytestBDDFramework.__1l1l1l11111_opy_(instance, *args)
            elif test_framework_state == bstack1lll1lll1ll_opy_.LOG_REPORT and test_hook_state == bstack1lll1lll11l_opy_.POST:
                self.__1l11ll1l111_opy_(instance, *args)
            elif test_framework_state in PytestBDDFramework.bstack1l11ll1ll11_opy_:
                self.__1l11l1llll1_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11lll_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥጟ") + str(instance.ref()) + bstack11lll_opy_ (u"ࠥࠦጠ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1l1l1l111l1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l11ll1ll11_opy_ and test_hook_state == bstack1lll1lll11l_opy_.POST:
                name = str(EVENTS.bstack11llll11l_opy_.name)+bstack11lll_opy_ (u"ࠦ࠿ࠨጡ")+str(test_framework_state.name)
                bstack1ll1lll1l1l_opy_ = TestFramework.bstack1l11lll1111_opy_(instance, name)
                bstack1lll1ll1lll_opy_.end(EVENTS.bstack11llll11l_opy_.value, bstack1ll1lll1l1l_opy_+bstack11lll_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧጢ"), bstack1ll1lll1l1l_opy_+bstack11lll_opy_ (u"ࠨ࠺ࡦࡰࡧࠦጣ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11lll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢጤ").format(e))
    def bstack1ll11111lll_opy_(self):
        return self.bstack1l1l11l1l1l_opy_
    def __1l1l111111l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11lll_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡴࡷ࡯ࡸࠧጥ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll11l1l1l1_opy_(rep, [bstack11lll_opy_ (u"ࠤࡺ࡬ࡪࡴࠢጦ"), bstack11lll_opy_ (u"ࠥࡳࡺࡺࡣࡰ࡯ࡨࠦጧ"), bstack11lll_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦጨ"), bstack11lll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧጩ"), bstack11lll_opy_ (u"ࠨࡳ࡬࡫ࡳࡴࡪࡪࠢጪ"), bstack11lll_opy_ (u"ࠢ࡭ࡱࡱ࡫ࡷ࡫ࡰࡳࡶࡨࡼࡹࠨጫ")])
        return None
    def __1l11ll1l111_opy_(self, instance: bstack1llll11lll1_opy_, *args):
        result = self.__1l1l111111l_opy_(*args)
        if not result:
            return
        failure = None
        bstack111l11ll1l_opy_ = None
        if result.get(bstack11lll_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤጬ"), None) == bstack11lll_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤጭ") and len(args) > 1 and getattr(args[1], bstack11lll_opy_ (u"ࠥࡩࡽࡩࡩ࡯ࡨࡲࠦጮ"), None) is not None:
            failure = [{bstack11lll_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧጯ"): [args[1].excinfo.exconly(), result.get(bstack11lll_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦጰ"), None)]}]
            bstack111l11ll1l_opy_ = bstack11lll_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢጱ") if bstack11lll_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥጲ") in getattr(args[1].excinfo, bstack11lll_opy_ (u"ࠣࡶࡼࡴࡪࡴࡡ࡮ࡧࠥጳ"), bstack11lll_opy_ (u"ࠤࠥጴ")) else bstack11lll_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦጵ")
        bstack1l1l111l111_opy_ = result.get(bstack11lll_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧጶ"), TestFramework.bstack1l1l111ll1l_opy_)
        if bstack1l1l111l111_opy_ != TestFramework.bstack1l1l111ll1l_opy_:
            TestFramework.bstack1111ll11ll_opy_(instance, TestFramework.bstack1ll11ll1l1l_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1l11ll11lll_opy_(instance, {
            TestFramework.bstack1l1ll1l1ll1_opy_: failure,
            TestFramework.bstack1l11ll1lll1_opy_: bstack111l11ll1l_opy_,
            TestFramework.bstack1l1ll1lll11_opy_: bstack1l1l111l111_opy_,
        })
    def __1l1l11l1l11_opy_(
        self,
        context: bstack1l11lll1lll_opy_,
        test_framework_state: bstack1lll1lll1ll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1lll1ll_opy_.SETUP_FIXTURE:
            instance = self.__1l1l11l11l1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1l11ll1l11l_opy_ bstack1l1l11lll1l_opy_ this to be bstack11lll_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧጷ")
            if test_framework_state == bstack1lll1lll1ll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1l1l111l11l_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1lll1ll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11lll_opy_ (u"ࠨ࡮ࡰࡦࡨࠦጸ"), None), bstack11lll_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢጹ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11lll_opy_ (u"ࠣࡰࡲࡨࡪࠨጺ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack11lll_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤጻ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack11111lllll_opy_(target) if target else None
        return instance
    def __1l11l1llll1_opy_(
        self,
        instance: bstack1llll11lll1_opy_,
        test_framework_state: bstack1lll1lll1ll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1l11lll1l11_opy_ = TestFramework.bstack11111l11l1_opy_(instance, PytestBDDFramework.bstack1l11ll111ll_opy_, {})
        if not key in bstack1l11lll1l11_opy_:
            bstack1l11lll1l11_opy_[key] = []
        bstack1l1l111ll11_opy_ = TestFramework.bstack11111l11l1_opy_(instance, PytestBDDFramework.bstack1l1l11111l1_opy_, {})
        if not key in bstack1l1l111ll11_opy_:
            bstack1l1l111ll11_opy_[key] = []
        bstack1l1l1111lll_opy_ = {
            PytestBDDFramework.bstack1l11ll111ll_opy_: bstack1l11lll1l11_opy_,
            PytestBDDFramework.bstack1l1l11111l1_opy_: bstack1l1l111ll11_opy_,
        }
        if test_hook_state == bstack1lll1lll11l_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack11lll_opy_ (u"ࠥ࡯ࡪࡿࠢጼ"): key,
                TestFramework.bstack1l1l11ll1l1_opy_: uuid4().__str__(),
                TestFramework.bstack1l1l1111l1l_opy_: TestFramework.bstack1l1l11lll11_opy_,
                TestFramework.bstack1l1l11l1ll1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1l11lllll11_opy_: [],
                TestFramework.bstack1l1l11lllll_opy_: hook_name
            }
            bstack1l11lll1l11_opy_[key].append(hook)
            bstack1l1l1111lll_opy_[PytestBDDFramework.bstack1l11ll1llll_opy_] = key
        elif test_hook_state == bstack1lll1lll11l_opy_.POST:
            bstack1l11lll11ll_opy_ = bstack1l11lll1l11_opy_.get(key, [])
            hook = bstack1l11lll11ll_opy_.pop() if bstack1l11lll11ll_opy_ else None
            if hook:
                result = self.__1l1l111111l_opy_(*args)
                if result:
                    bstack1l1l11ll1ll_opy_ = result.get(bstack11lll_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧጽ"), TestFramework.bstack1l1l11lll11_opy_)
                    if bstack1l1l11ll1ll_opy_ != TestFramework.bstack1l1l11lll11_opy_:
                        hook[TestFramework.bstack1l1l1111l1l_opy_] = bstack1l1l11ll1ll_opy_
                hook[TestFramework.bstack1l1l11l1111_opy_] = datetime.now(tz=timezone.utc)
                bstack1l1l111ll11_opy_[key].append(hook)
                bstack1l1l1111lll_opy_[PytestBDDFramework.bstack1l1l11ll11l_opy_] = key
        TestFramework.bstack1l11ll11lll_opy_(instance, bstack1l1l1111lll_opy_)
        self.logger.debug(bstack11lll_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡭ࡵ࡯࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡱࡥࡺࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪ࠽ࡼࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤࡾࠢ࡫ࡳࡴࡱࡳࡠࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡀࠦጾ") + str(bstack1l1l111ll11_opy_) + bstack11lll_opy_ (u"ࠨࠢጿ"))
    def __1l1l11l11l1_opy_(
        self,
        context: bstack1l11lll1lll_opy_,
        test_framework_state: bstack1lll1lll1ll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll11l1l1l1_opy_(args[0], [bstack11lll_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨፀ"), bstack11lll_opy_ (u"ࠣࡣࡵ࡫ࡳࡧ࡭ࡦࠤፁ"), bstack11lll_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤፂ"), bstack11lll_opy_ (u"ࠥ࡭ࡩࡹࠢፃ"), bstack11lll_opy_ (u"ࠦࡺࡴࡩࡵࡶࡨࡷࡹࠨፄ"), bstack11lll_opy_ (u"ࠧࡨࡡࡴࡧ࡬ࡨࠧፅ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack11lll_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧፆ")) else fixturedef.get(bstack11lll_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨፇ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11lll_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࠨፈ")) else None
        node = request.node if hasattr(request, bstack11lll_opy_ (u"ࠤࡱࡳࡩ࡫ࠢፉ")) else None
        target = request.node.nodeid if hasattr(node, bstack11lll_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥፊ")) else None
        baseid = fixturedef.get(bstack11lll_opy_ (u"ࠦࡧࡧࡳࡦ࡫ࡧࠦፋ"), None) or bstack11lll_opy_ (u"ࠧࠨፌ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11lll_opy_ (u"ࠨ࡟ࡱࡻࡩࡹࡳࡩࡩࡵࡧࡰࠦፍ")):
            target = PytestBDDFramework.__1l1l1l1111l_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11lll_opy_ (u"ࠢ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠤፎ")) else None
            if target and not TestFramework.bstack11111lllll_opy_(target):
                self.__1l1l111l11l_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11lll_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡸࡦࡸࡧࡦࡶࡀࡿࡹࡧࡲࡨࡧࡷࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࡀࡿ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࡿࠣࡲࡴࡪࡥ࠾ࡽࡱࡳࡩ࡫ࡽࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࠥፏ") + str(test_hook_state) + bstack11lll_opy_ (u"ࠤࠥፐ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11lll_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡩ࡫ࡦ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࢃࠠࡴࡥࡲࡴࡪࡃࡻࡴࡥࡲࡴࡪࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣፑ") + str(target) + bstack11lll_opy_ (u"ࠦࠧፒ"))
            return None
        instance = TestFramework.bstack11111lllll_opy_(target)
        if not instance:
            self.logger.warning(bstack11lll_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࠡࡧࡹࡩࡳࡺ࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾ࠰ࡾࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࢂࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤࡧࡧࡳࡦ࡫ࡧࡁࢀࡨࡡࡴࡧ࡬ࡨࢂࠦࡴࡢࡴࡪࡩࡹࡃࠢፓ") + str(target) + bstack11lll_opy_ (u"ࠨࠢፔ"))
            return None
        bstack1l1l1l111ll_opy_ = TestFramework.bstack11111l11l1_opy_(instance, PytestBDDFramework.bstack1l11lll1l1l_opy_, {})
        if os.getenv(bstack11lll_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡆࡊ࡚ࡗ࡙ࡗࡋࡓࠣፕ"), bstack11lll_opy_ (u"ࠣ࠳ࠥፖ")) == bstack11lll_opy_ (u"ࠤ࠴ࠦፗ"):
            bstack1l11l1lllll_opy_ = bstack11lll_opy_ (u"ࠥ࠾ࠧፘ").join((scope, fixturename))
            bstack1l11lll1ll1_opy_ = datetime.now(tz=timezone.utc)
            bstack1l11ll1l1l1_opy_ = {
                bstack11lll_opy_ (u"ࠦࡰ࡫ࡹࠣፙ"): bstack1l11l1lllll_opy_,
                bstack11lll_opy_ (u"ࠧࡺࡡࡨࡵࠥፚ"): PytestBDDFramework.__1l11ll11l1l_opy_(request.node, scenario),
                bstack11lll_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫ࠢ፛"): fixturedef,
                bstack11lll_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨ፜"): scope,
                bstack11lll_opy_ (u"ࠣࡶࡼࡴࡪࠨ፝"): None,
            }
            try:
                if test_hook_state == bstack1lll1lll11l_opy_.POST and callable(getattr(args[-1], bstack11lll_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨ፞"), None)):
                    bstack1l11ll1l1l1_opy_[bstack11lll_opy_ (u"ࠥࡸࡾࡶࡥࠣ፟")] = TestFramework.bstack1ll11llllll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1lll11l_opy_.PRE:
                bstack1l11ll1l1l1_opy_[bstack11lll_opy_ (u"ࠦࡺࡻࡩࡥࠤ፠")] = uuid4().__str__()
                bstack1l11ll1l1l1_opy_[PytestBDDFramework.bstack1l1l11l1ll1_opy_] = bstack1l11lll1ll1_opy_
            elif test_hook_state == bstack1lll1lll11l_opy_.POST:
                bstack1l11ll1l1l1_opy_[PytestBDDFramework.bstack1l1l11l1111_opy_] = bstack1l11lll1ll1_opy_
            if bstack1l11l1lllll_opy_ in bstack1l1l1l111ll_opy_:
                bstack1l1l1l111ll_opy_[bstack1l11l1lllll_opy_].update(bstack1l11ll1l1l1_opy_)
                self.logger.debug(bstack11lll_opy_ (u"ࠧࡻࡰࡥࡣࡷࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࠨ፡") + str(bstack1l1l1l111ll_opy_[bstack1l11l1lllll_opy_]) + bstack11lll_opy_ (u"ࠨࠢ።"))
            else:
                bstack1l1l1l111ll_opy_[bstack1l11l1lllll_opy_] = bstack1l11ll1l1l1_opy_
                self.logger.debug(bstack11lll_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡂࢁࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࢂࠦࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴ࠿ࠥ፣") + str(len(bstack1l1l1l111ll_opy_)) + bstack11lll_opy_ (u"ࠣࠤ፤"))
        TestFramework.bstack1111ll11ll_opy_(instance, PytestBDDFramework.bstack1l11lll1l1l_opy_, bstack1l1l1l111ll_opy_)
        self.logger.debug(bstack11lll_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡࡨ࡬ࡼࡹࡻࡲࡦࡵࡀࡿࡱ࡫࡮ࠩࡶࡵࡥࡨࡱࡥࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࡶ࠭ࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤ፥") + str(instance.ref()) + bstack11lll_opy_ (u"ࠥࠦ፦"))
        return instance
    def __1l1l111l11l_opy_(
        self,
        context: bstack1l11lll1lll_opy_,
        test_framework_state: bstack1lll1lll1ll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1111ll11l1_opy_.create_context(target)
        ob = bstack1llll11lll1_opy_(ctx, self.bstack1lll111111l_opy_, self.bstack1l11llll1l1_opy_, test_framework_state)
        TestFramework.bstack1l11ll11lll_opy_(ob, {
            TestFramework.bstack1ll1ll1l111_opy_: context.test_framework_name,
            TestFramework.bstack1ll11l1l111_opy_: context.test_framework_version,
            TestFramework.bstack1l1l11111ll_opy_: [],
            PytestBDDFramework.bstack1l11lll1l1l_opy_: {},
            PytestBDDFramework.bstack1l1l11111l1_opy_: {},
            PytestBDDFramework.bstack1l11ll111ll_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1111ll11ll_opy_(ob, TestFramework.bstack1l11lllllll_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1111ll11ll_opy_(ob, TestFramework.bstack1ll1lll1111_opy_, context.platform_index)
        TestFramework.bstack1111l11lll_opy_[ctx.id] = ob
        self.logger.debug(bstack11lll_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥࡩࡴࡹ࠰࡬ࡨࡂࢁࡣࡵࡺ࠱࡭ࡩࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࡼࡶࡤࡶ࡬࡫ࡴࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦࡵࡀࠦ፧") + str(TestFramework.bstack1111l11lll_opy_.keys()) + bstack11lll_opy_ (u"ࠧࠨ፨"))
        return ob
    @staticmethod
    def __1l1l11llll1_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11lll_opy_ (u"࠭ࡩࡥࠩ፩"): id(step),
                bstack11lll_opy_ (u"ࠧࡵࡧࡻࡸࠬ፪"): step.name,
                bstack11lll_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩ፫"): step.keyword,
            })
        meta = {
            bstack11lll_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪ፬"): {
                bstack11lll_opy_ (u"ࠪࡲࡦࡳࡥࠨ፭"): feature.name,
                bstack11lll_opy_ (u"ࠫࡵࡧࡴࡩࠩ፮"): feature.filename,
                bstack11lll_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ፯"): feature.description
            },
            bstack11lll_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ፰"): {
                bstack11lll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ፱"): scenario.name
            },
            bstack11lll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧ፲"): steps,
            bstack11lll_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫ፳"): PytestBDDFramework.__1l11llll11l_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1l11ll1ll1l_opy_: meta
            }
        )
    @staticmethod
    def __1l11ll11l11_opy_(instance, args):
        request, bstack1l1l1111ll1_opy_ = args
        bstack1l11lll11l1_opy_ = id(bstack1l1l1111ll1_opy_)
        bstack1l11llll1ll_opy_ = instance.data[TestFramework.bstack1l11ll1ll1l_opy_]
        step = next(filter(lambda st: st[bstack11lll_opy_ (u"ࠪ࡭ࡩ࠭፴")] == bstack1l11lll11l1_opy_, bstack1l11llll1ll_opy_[bstack11lll_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪ፵")]), None)
        step.update({
            bstack11lll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ፶"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1l11llll1ll_opy_[bstack11lll_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ፷")]) if st[bstack11lll_opy_ (u"ࠧࡪࡦࠪ፸")] == step[bstack11lll_opy_ (u"ࠨ࡫ࡧࠫ፹")]), None)
        if index is not None:
            bstack1l11llll1ll_opy_[bstack11lll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨ፺")][index] = step
        instance.data[TestFramework.bstack1l11ll1ll1l_opy_] = bstack1l11llll1ll_opy_
    @staticmethod
    def __1l1l11ll111_opy_(instance, args):
        bstack11lll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡸࡪࡨࡲࠥࡲࡥ࡯ࠢࡤࡶ࡬ࡹࠠࡪࡵࠣ࠶࠱ࠦࡩࡵࠢࡶ࡭࡬ࡴࡩࡧ࡫ࡨࡷࠥࡺࡨࡦࡴࡨࠤ࡮ࡹࠠ࡯ࡱࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡦࡸࡧࡴࠢࡤࡶࡪࠦ࠭ࠡ࡝ࡵࡩࡶࡻࡥࡴࡶ࠯ࠤࡸࡺࡥࡱ࡟ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮࡬ࠠࡢࡴࡪࡷࠥࡧࡲࡦࠢ࠶ࠤࡹ࡮ࡥ࡯ࠢࡷ࡬ࡪࠦ࡬ࡢࡵࡷࠤࡻࡧ࡬ࡶࡧࠣ࡭ࡸࠦࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ፻")
        bstack1l11ll1l1ll_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1l1l1111ll1_opy_ = args[1]
        bstack1l11lll11l1_opy_ = id(bstack1l1l1111ll1_opy_)
        bstack1l11llll1ll_opy_ = instance.data[TestFramework.bstack1l11ll1ll1l_opy_]
        step = None
        if bstack1l11lll11l1_opy_ is not None and bstack1l11llll1ll_opy_.get(bstack11lll_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪ፼")):
            step = next(filter(lambda st: st[bstack11lll_opy_ (u"ࠬ࡯ࡤࠨ፽")] == bstack1l11lll11l1_opy_, bstack1l11llll1ll_opy_[bstack11lll_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ፾")]), None)
            step.update({
                bstack11lll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ፿"): bstack1l11ll1l1ll_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack11lll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᎀ"): bstack11lll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᎁ"),
                bstack11lll_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᎂ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack11lll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᎃ"): bstack11lll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᎄ"),
                })
        index = next((i for i, st in enumerate(bstack1l11llll1ll_opy_[bstack11lll_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬᎅ")]) if st[bstack11lll_opy_ (u"ࠧࡪࡦࠪᎆ")] == step[bstack11lll_opy_ (u"ࠨ࡫ࡧࠫᎇ")]), None)
        if index is not None:
            bstack1l11llll1ll_opy_[bstack11lll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᎈ")][index] = step
        instance.data[TestFramework.bstack1l11ll1ll1l_opy_] = bstack1l11llll1ll_opy_
    @staticmethod
    def __1l11llll11l_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack11lll_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬᎉ")):
                examples = list(node.callspec.params[bstack11lll_opy_ (u"ࠫࡤࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡨࡼࡦࡳࡰ࡭ࡧࠪᎊ")].values())
            return examples
        except:
            return []
    def bstack1ll11ll1lll_opy_(self, instance: bstack1llll11lll1_opy_, bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_]):
        bstack1l1l11l111l_opy_ = (
            PytestBDDFramework.bstack1l11ll1llll_opy_
            if bstack1111llll11_opy_[1] == bstack1lll1lll11l_opy_.PRE
            else PytestBDDFramework.bstack1l1l11ll11l_opy_
        )
        hook = PytestBDDFramework.bstack1l11ll1111l_opy_(instance, bstack1l1l11l111l_opy_)
        entries = hook.get(TestFramework.bstack1l11lllll11_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1l1l11111ll_opy_, []))
        return entries
    def bstack1ll111l111l_opy_(self, instance: bstack1llll11lll1_opy_, bstack1111llll11_opy_: Tuple[bstack1lll1lll1ll_opy_, bstack1lll1lll11l_opy_]):
        bstack1l1l11l111l_opy_ = (
            PytestBDDFramework.bstack1l11ll1llll_opy_
            if bstack1111llll11_opy_[1] == bstack1lll1lll11l_opy_.PRE
            else PytestBDDFramework.bstack1l1l11ll11l_opy_
        )
        PytestBDDFramework.bstack1l11llllll1_opy_(instance, bstack1l1l11l111l_opy_)
        TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1l1l11111ll_opy_, []).clear()
    @staticmethod
    def bstack1l11ll1111l_opy_(instance: bstack1llll11lll1_opy_, bstack1l1l11l111l_opy_: str):
        bstack1l1l1111111_opy_ = (
            PytestBDDFramework.bstack1l1l11111l1_opy_
            if bstack1l1l11l111l_opy_ == PytestBDDFramework.bstack1l1l11ll11l_opy_
            else PytestBDDFramework.bstack1l11ll111ll_opy_
        )
        bstack1l1l111l1ll_opy_ = TestFramework.bstack11111l11l1_opy_(instance, bstack1l1l11l111l_opy_, None)
        bstack1l11llll111_opy_ = TestFramework.bstack11111l11l1_opy_(instance, bstack1l1l1111111_opy_, None) if bstack1l1l111l1ll_opy_ else None
        return (
            bstack1l11llll111_opy_[bstack1l1l111l1ll_opy_][-1]
            if isinstance(bstack1l11llll111_opy_, dict) and len(bstack1l11llll111_opy_.get(bstack1l1l111l1ll_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1l11llllll1_opy_(instance: bstack1llll11lll1_opy_, bstack1l1l11l111l_opy_: str):
        hook = PytestBDDFramework.bstack1l11ll1111l_opy_(instance, bstack1l1l11l111l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1l11lllll11_opy_, []).clear()
    @staticmethod
    def __1l1l1l11111_opy_(instance: bstack1llll11lll1_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11lll_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡨࡵࡲࡥࡵࠥᎋ"), None)):
            return
        if os.getenv(bstack11lll_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡒࡏࡈࡕࠥᎌ"), bstack11lll_opy_ (u"ࠢ࠲ࠤᎍ")) != bstack11lll_opy_ (u"ࠣ࠳ࠥᎎ"):
            PytestBDDFramework.logger.warning(bstack11lll_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡪࡰࡪࠤࡨࡧࡰ࡭ࡱࡪࠦᎏ"))
            return
        bstack1l11lll111l_opy_ = {
            bstack11lll_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤ᎐"): (PytestBDDFramework.bstack1l11ll1llll_opy_, PytestBDDFramework.bstack1l11ll111ll_opy_),
            bstack11lll_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨ᎑"): (PytestBDDFramework.bstack1l1l11ll11l_opy_, PytestBDDFramework.bstack1l1l11111l1_opy_),
        }
        for when in (bstack11lll_opy_ (u"ࠧࡹࡥࡵࡷࡳࠦ᎒"), bstack11lll_opy_ (u"ࠨࡣࡢ࡮࡯ࠦ᎓"), bstack11lll_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤ᎔")):
            bstack1l11lllll1l_opy_ = args[1].get_records(when)
            if not bstack1l11lllll1l_opy_:
                continue
            records = [
                bstack1lll11l1ll1_opy_(
                    kind=TestFramework.bstack1ll111ll11l_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11lll_opy_ (u"ࠣ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨࠦ᎕")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11lll_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡦࠥ᎖")) and r.created
                        else None
                    ),
                )
                for r in bstack1l11lllll1l_opy_
                if isinstance(getattr(r, bstack11lll_opy_ (u"ࠥࡱࡪࡹࡳࡢࡩࡨࠦ᎗"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1l11ll11111_opy_, bstack1l1l1111111_opy_ = bstack1l11lll111l_opy_.get(when, (None, None))
            bstack1l11l1lll1l_opy_ = TestFramework.bstack11111l11l1_opy_(instance, bstack1l11ll11111_opy_, None) if bstack1l11ll11111_opy_ else None
            bstack1l11llll111_opy_ = TestFramework.bstack11111l11l1_opy_(instance, bstack1l1l1111111_opy_, None) if bstack1l11l1lll1l_opy_ else None
            if isinstance(bstack1l11llll111_opy_, dict) and len(bstack1l11llll111_opy_.get(bstack1l11l1lll1l_opy_, [])) > 0:
                hook = bstack1l11llll111_opy_[bstack1l11l1lll1l_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1l11lllll11_opy_ in hook:
                    hook[TestFramework.bstack1l11lllll11_opy_].extend(records)
                    continue
            logs = TestFramework.bstack11111l11l1_opy_(instance, TestFramework.bstack1l1l11111ll_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1l1l111lll1_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        bstack11ll1lll1_opy_ = request.node.nodeid
        test_name = PytestBDDFramework.__1l1l11l11ll_opy_(request.node, scenario)
        bstack1l1l111llll_opy_ = feature.filename
        if not bstack11ll1lll1_opy_ or not test_name or not bstack1l1l111llll_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1ll1llll1l1_opy_: uuid4().__str__(),
            TestFramework.bstack1l11ll11ll1_opy_: bstack11ll1lll1_opy_,
            TestFramework.bstack1ll1lll1l11_opy_: test_name,
            TestFramework.bstack1l1lllll1ll_opy_: bstack11ll1lll1_opy_,
            TestFramework.bstack1l1l111l1l1_opy_: bstack1l1l111llll_opy_,
            TestFramework.bstack1l1l11l1lll_opy_: PytestBDDFramework.__1l11ll11l1l_opy_(feature, scenario),
            TestFramework.bstack1l11ll111l1_opy_: code,
            TestFramework.bstack1l1ll1lll11_opy_: TestFramework.bstack1l1l111ll1l_opy_,
            TestFramework.bstack1l1l1ll1l11_opy_: test_name
        }
    @staticmethod
    def __1l1l11l11ll_opy_(node, scenario):
        if hasattr(node, bstack11lll_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭᎘")):
            parts = node.nodeid.rsplit(bstack11lll_opy_ (u"ࠧࡡࠢ᎙"))
            params = parts[-1]
            return bstack11lll_opy_ (u"ࠨࡻࡾࠢ࡞ࡿࢂࠨ᎚").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1l11ll11l1l_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack11lll_opy_ (u"ࠧࡵࡣࡪࡷࠬ᎛")) else []) + (list(scenario.tags) if hasattr(scenario, bstack11lll_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭᎜")) else [])
    @staticmethod
    def __1l1l1l1111l_opy_(location):
        return bstack11lll_opy_ (u"ࠤ࠽࠾ࠧ᎝").join(filter(lambda x: isinstance(x, str), location))