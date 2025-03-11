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
    bstack1111l1llll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l1ll1_opy_ import bstack111111l111_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack111l111lll_opy_ import bstack111l11l1ll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1lllllll1l1_opy_(bstack111l11l1ll_opy_):
    bstack1ll1lll11l1_opy_ = False
    def __init__(self):
        super().__init__()
        bstack111111l111_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111ll1111_opy_, bstack1111ll111l_opy_.PRE), self.bstack1ll1l11lll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1l11lll1_opy_(
        self,
        f: bstack111111l111_opy_,
        driver: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1ll1l1l11ll_opy_(hub_url):
            if not bstack1lllllll1l1_opy_.bstack1ll1lll11l1_opy_:
                self.logger.warning(bstack11lll_opy_ (u"ࠣ࡮ࡲࡧࡦࡲࠠࡴࡧ࡯ࡪ࠲࡮ࡥࡢ࡮ࠣࡪࡱࡵࡷࠡࡦ࡬ࡷࡦࡨ࡬ࡦࡦࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡩ࡯ࡨࡵࡥࠥࡹࡥࡴࡵ࡬ࡳࡳࡹࠠࡩࡷࡥࡣࡺࡸ࡬࠾ࠤᄻ") + str(hub_url) + bstack11lll_opy_ (u"ࠤࠥᄼ"))
                bstack1lllllll1l1_opy_.bstack1ll1lll11l1_opy_ = True
            return
        bstack1ll1l1ll1l1_opy_ = f.bstack1ll1lllllll_opy_(*args)
        bstack1ll1l1l1lll_opy_ = f.bstack1ll1l1l1l11_opy_(*args)
        if bstack1ll1l1ll1l1_opy_ and bstack1ll1l1ll1l1_opy_.lower() == bstack11lll_opy_ (u"ࠥࡪ࡮ࡴࡤࡦ࡮ࡨࡱࡪࡴࡴࠣᄽ") and bstack1ll1l1l1lll_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1ll1l1l1lll_opy_.get(bstack11lll_opy_ (u"ࠦࡺࡹࡩ࡯ࡩࠥᄾ"), None), bstack1ll1l1l1lll_opy_.get(bstack11lll_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࠦᄿ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack11lll_opy_ (u"ࠨࡻࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࢃ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠢࡲࡶࠥࡧࡲࡨࡵ࠱ࡹࡸ࡯࡮ࡨ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡳࡷࠦࡡࡳࡩࡶ࠲ࡻࡧ࡬ࡶࡧࡀࠦᅀ") + str(locator_value) + bstack11lll_opy_ (u"ࠢࠣᅁ"))
                return
            def bstack1111l1l11l_opy_(driver, bstack1ll1l11llll_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1ll1l11llll_opy_(driver, *args, **kwargs)
                    response = self.bstack1ll1l1l1ll1_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack11lll_opy_ (u"ࠣࡵࡸࡧࡨ࡫ࡳࡴ࠯ࡶࡧࡷ࡯ࡰࡵ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࠦᅂ") + str(locator_value) + bstack11lll_opy_ (u"ࠤࠥᅃ"))
                    else:
                        self.logger.warning(bstack11lll_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶ࠱ࡳࡵ࠭ࡴࡥࡵ࡭ࡵࡺ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦࡿࠣࡶࡪࡹࡰࡰࡰࡶࡩࡂࠨᅄ") + str(response) + bstack11lll_opy_ (u"ࠦࠧᅅ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1ll1l1l1l1l_opy_(
                        driver, bstack1ll1l11llll_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1111l1l11l_opy_.__name__ = bstack1ll1l1ll1l1_opy_
            return bstack1111l1l11l_opy_
    def __1ll1l1l1l1l_opy_(
        self,
        driver,
        bstack1ll1l11llll_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1ll1l1l1ll1_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack11lll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳ࡨࡦࡣ࡯࡭ࡳ࡭࠭ࡵࡴ࡬࡫࡬࡫ࡲࡦࡦ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࠧᅆ") + str(locator_value) + bstack11lll_opy_ (u"ࠨࠢᅇ"))
                bstack1ll1l1l111l_opy_ = self.bstack1ll1l1l1111_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack11lll_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡪࡨࡥࡱ࡯࡮ࡨ࠯ࡵࡩࡸࡻ࡬ࡵ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࢁࠥ࡮ࡥࡢ࡮࡬ࡲ࡬ࡥࡲࡦࡵࡸࡰࡹࡃࠢᅈ") + str(bstack1ll1l1l111l_opy_) + bstack11lll_opy_ (u"ࠣࠤᅉ"))
                if bstack1ll1l1l111l_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack11lll_opy_ (u"ࠤࡸࡷ࡮ࡴࡧࠣᅊ"): bstack1ll1l1l111l_opy_.locator_type,
                            bstack11lll_opy_ (u"ࠥࡺࡦࡲࡵࡦࠤᅋ"): bstack1ll1l1l111l_opy_.locator_value,
                        }
                    )
                    return bstack1ll1l11llll_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack11lll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡎࡥࡄࡆࡄࡘࡋࠧᅌ"), False):
                    self.logger.info(bstack1lll11lllll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳ࡨࡦࡣ࡯࡭ࡳ࡭࠭ࡳࡧࡶࡹࡱࡺ࠭࡮࡫ࡶࡷ࡮ࡴࡧ࠻ࠢࡶࡰࡪ࡫ࡰࠩ࠵࠳࠭ࠥࡲࡥࡵࡶ࡬ࡲ࡬ࠦࡹࡰࡷࠣ࡭ࡳࡹࡰࡦࡥࡷࠤࡹ࡮ࡥࠡࡤࡵࡳࡼࡹࡥࡳࠢࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࠥࡲ࡯ࡨࡵࠥᅍ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack11lll_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭࡯ࡱ࠰ࡷࡨࡸࡩࡱࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࢂࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠾ࠤᅎ") + str(response) + bstack11lll_opy_ (u"ࠢࠣᅏ"))
        except Exception as err:
            self.logger.warning(bstack11lll_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡶࡪࡹࡵ࡭ࡶ࠽ࠤࡪࡸࡲࡰࡴ࠽ࠤࠧᅐ") + str(err) + bstack11lll_opy_ (u"ࠤࠥᅑ"))
        raise exception
    @measure(event_name=EVENTS.bstack1ll1l1l11l1_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def bstack1ll1l1l1ll1_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack11lll_opy_ (u"ࠥ࠴ࠧᅒ"),
    ):
        self.bstack111l11l11l_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack11lll_opy_ (u"ࠦࠧᅓ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack111l11l1l1_opy_.AISelfHealStep(req)
            self.logger.info(bstack11lll_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᅔ") + str(r) + bstack11lll_opy_ (u"ࠨࠢᅕ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᅖ") + str(e) + bstack11lll_opy_ (u"ࠣࠤᅗ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1ll1l11ll1l_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def bstack1ll1l1l1111_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack11lll_opy_ (u"ࠤ࠳ࠦᅘ")):
        self.bstack111l11l11l_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack111l11l1l1_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack11lll_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧᅙ") + str(r) + bstack11lll_opy_ (u"ࠦࠧᅚ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᅛ") + str(e) + bstack11lll_opy_ (u"ࠨࠢᅜ"))
            traceback.print_exc()
            raise e