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
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack111l111lll_opy_ import bstack111l11l1ll_opy_
from browserstack_sdk.sdk_cli.bstack11111l1lll_opy_ import (
    bstack1111l1l111_opy_,
    bstack1111ll111l_opy_,
    bstack1111l1llll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l1ll1_opy_ import bstack111111l111_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1l1l11111l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack11l1lll1_opy_ import bstack1lll1ll1lll_opy_
class bstack1llll1llll1_opy_(bstack111l11l1ll_opy_):
    bstack1l1ll1l11l1_opy_ = bstack11lll_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣ࡮ࡴࡩࡵࠤቛ")
    bstack1l1ll1111ll_opy_ = bstack11lll_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡢࡴࡷࠦቜ")
    bstack1l1ll11lll1_opy_ = bstack11lll_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡱࡳࠦቝ")
    def __init__(self, bstack1lllll111l1_opy_):
        super().__init__()
        bstack111111l111_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111l11111_opy_, bstack1111ll111l_opy_.PRE), self.bstack1l1l1llll1l_opy_)
        bstack111111l111_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111ll1111_opy_, bstack1111ll111l_opy_.PRE), self.bstack1ll1l11lll1_opy_)
        bstack111111l111_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111ll1111_opy_, bstack1111ll111l_opy_.POST), self.bstack1l1l1lll1l1_opy_)
        bstack111111l111_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111ll1111_opy_, bstack1111ll111l_opy_.POST), self.bstack1l1l1lll11l_opy_)
        bstack111111l111_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.QUIT, bstack1111ll111l_opy_.POST), self.bstack1l1ll1l11ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1l1llll1l_opy_(
        self,
        f: bstack111111l111_opy_,
        driver: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll_opy_ (u"ࠧࡥ࡟ࡪࡰ࡬ࡸࡤࡥࠢ቞"):
            return
        def wrapped(driver, init, *args, **kwargs):
            self.bstack1l1ll11l11l_opy_(instance, f, kwargs)
            self.logger.debug(bstack11lll_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷ࠴ࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾ࠽ࡼࡨ࠱ࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࢁ࠿ࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧ቟") + str(kwargs) + bstack11lll_opy_ (u"ࠢࠣበ"))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
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
        instance, method_name = exec
        if f.bstack11111l11l1_opy_(instance, bstack1llll1llll1_opy_.bstack1l1ll1l11l1_opy_, False):
            return
        if not f.bstack1111ll1l11_opy_(instance, bstack111111l111_opy_.bstack1ll1lll1111_opy_):
            return
        platform_index = f.bstack11111l11l1_opy_(instance, bstack111111l111_opy_.bstack1ll1lll1111_opy_)
        if f.bstack1ll1ll111l1_opy_(method_name, *args) and len(args) > 1:
            bstack11lll1l11l_opy_ = datetime.now()
            hub_url = bstack111111l111_opy_.hub_url(driver)
            self.logger.warning(bstack11lll_opy_ (u"ࠣࡪࡸࡦࡤࡻࡲ࡭࠿ࠥቡ") + str(hub_url) + bstack11lll_opy_ (u"ࠤࠥቢ"))
            bstack1l1ll11111l_opy_ = args[1][bstack11lll_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤባ")] if isinstance(args[1], dict) and bstack11lll_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥቤ") in args[1] else None
            bstack1l1ll11l111_opy_ = bstack11lll_opy_ (u"ࠧࡧ࡬ࡸࡣࡼࡷࡒࡧࡴࡤࡪࠥብ")
            if isinstance(bstack1l1ll11111l_opy_, dict):
                bstack11lll1l11l_opy_ = datetime.now()
                r = self.bstack1l1ll111ll1_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡩ࡯࡫ࡷࠦቦ"), datetime.now() - bstack11lll1l11l_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack11lll_opy_ (u"ࠢࡴࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭࠺ࠡࠤቧ") + str(r) + bstack11lll_opy_ (u"ࠣࠤቨ"))
                        return
                    if r.hub_url:
                        f.bstack1l1ll111111_opy_(instance, driver, r.hub_url)
                        f.bstack1111ll11ll_opy_(instance, bstack1llll1llll1_opy_.bstack1l1ll1l11l1_opy_, True)
                except Exception as e:
                    self.logger.error(bstack11lll_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣቩ"), e)
    def bstack1l1l1lll1l1_opy_(
        self,
        f: bstack111111l111_opy_,
        driver: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack111111l111_opy_.session_id(driver)
            if session_id:
                bstack1l1ll1l1111_opy_ = bstack11lll_opy_ (u"ࠥࡿࢂࡀࡳࡵࡣࡵࡸࠧቪ").format(session_id)
                bstack1lll1ll1lll_opy_.mark(bstack1l1ll1l1111_opy_)
    def bstack1l1l1lll11l_opy_(
        self,
        f: bstack111111l111_opy_,
        driver: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.bstack11111l11l1_opy_(instance, bstack1llll1llll1_opy_.bstack1l1ll1111ll_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack111111l111_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack11lll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡨࡶࡤࡢࡹࡷࡲ࠽ࠣቫ") + str(hub_url) + bstack11lll_opy_ (u"ࠧࠨቬ"))
            return
        framework_session_id = bstack111111l111_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack11lll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤ࠾ࠤቭ") + str(framework_session_id) + bstack11lll_opy_ (u"ࠢࠣቮ"))
            return
        if bstack111111l111_opy_.bstack1l1l1llllll_opy_(*args) == bstack111111l111_opy_.bstack1l1l1lllll1_opy_:
            bstack1l1ll11l1ll_opy_ = bstack11lll_opy_ (u"ࠣࡽࢀ࠾ࡪࡴࡤࠣቯ").format(framework_session_id)
            bstack1l1ll1l1111_opy_ = bstack11lll_opy_ (u"ࠤࡾࢁ࠿ࡹࡴࡢࡴࡷࠦተ").format(framework_session_id)
            bstack1lll1ll1lll_opy_.end(
                label=bstack11lll_opy_ (u"ࠥࡷࡩࡱ࠺ࡥࡴ࡬ࡺࡪࡸ࠺ࡱࡱࡶࡸ࠲࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡢࡶ࡬ࡳࡳࠨቱ"),
                start=bstack1l1ll1l1111_opy_,
                end=bstack1l1ll11l1ll_opy_,
                status=True,
                failure=None
            )
            bstack11lll1l11l_opy_ = datetime.now()
            r = self.bstack1l1ll1l1l11_opy_(
                ref,
                f.bstack11111l11l1_opy_(instance, bstack111111l111_opy_.bstack1ll1lll1111_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶࠥቲ"), datetime.now() - bstack11lll1l11l_opy_)
            f.bstack1111ll11ll_opy_(instance, bstack1llll1llll1_opy_.bstack1l1ll1111ll_opy_, r.success)
    def bstack1l1ll1l11ll_opy_(
        self,
        f: bstack111111l111_opy_,
        driver: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.bstack11111l11l1_opy_(instance, bstack1llll1llll1_opy_.bstack1l1ll11lll1_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack111111l111_opy_.session_id(driver)
        hub_url = bstack111111l111_opy_.hub_url(driver)
        bstack11lll1l11l_opy_ = datetime.now()
        r = self.bstack1l1ll11l1l1_opy_(
            ref,
            f.bstack11111l11l1_opy_(instance, bstack111111l111_opy_.bstack1ll1lll1111_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1llllllll1_opy_(bstack11lll_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲࠥታ"), datetime.now() - bstack11lll1l11l_opy_)
        f.bstack1111ll11ll_opy_(instance, bstack1llll1llll1_opy_.bstack1l1ll11lll1_opy_, r.success)
    @measure(event_name=EVENTS.bstack1l1lll1ll1_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def bstack1l1llll11ll_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack11lll_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡹࡨࡦࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࠼ࠣࠦቴ") + str(req) + bstack11lll_opy_ (u"ࠢࠣት"))
        try:
            r = self.bstack111l11l1l1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11lll_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࡶࡹࡨࡩࡥࡴࡵࡀࠦቶ") + str(r.success) + bstack11lll_opy_ (u"ࠤࠥቷ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣቸ") + str(e) + bstack11lll_opy_ (u"ࠦࠧቹ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll1111l1_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def bstack1l1ll111ll1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack111l11l11l_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack11lll_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡪࡰ࡬ࡸ࠿ࠦࠢቺ") + str(req) + bstack11lll_opy_ (u"ࠨࠢቻ"))
        try:
            r = self.bstack111l11l1l1_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack11lll_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࡵࡸࡧࡨ࡫ࡳࡴ࠿ࠥቼ") + str(r.success) + bstack11lll_opy_ (u"ࠣࠤች"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢቾ") + str(e) + bstack11lll_opy_ (u"ࠥࠦቿ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll11llll_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def bstack1l1ll1l1l11_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack111l11l11l_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11lll_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡣࡵࡸ࠿ࠦࠢኀ") + str(req) + bstack11lll_opy_ (u"ࠧࠨኁ"))
        try:
            r = self.bstack111l11l1l1_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack11lll_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣኂ") + str(r) + bstack11lll_opy_ (u"ࠢࠣኃ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨኄ") + str(e) + bstack11lll_opy_ (u"ࠤࠥኅ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll111lll_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def bstack1l1ll11l1l1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack111l11l11l_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11lll_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲ࠽ࠤࠧኆ") + str(req) + bstack11lll_opy_ (u"ࠦࠧኇ"))
        try:
            r = self.bstack111l11l1l1_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack11lll_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢኈ") + str(r) + bstack11lll_opy_ (u"ࠨࠢ኉"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧኊ") + str(e) + bstack11lll_opy_ (u"ࠣࠤኋ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack11l1llllll_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
    def bstack1l1ll11l11l_opy_(self, instance: bstack1111l1llll_opy_, f: bstack111111l111_opy_, kwargs):
        bstack1l1l1llll11_opy_ = version.parse(f.framework_version)
        bstack1l1ll11ll1l_opy_ = kwargs.get(bstack11lll_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥኌ"))
        bstack1l1ll11ll11_opy_ = kwargs.get(bstack11lll_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥኍ"))
        bstack1l1lll1llll_opy_ = {}
        bstack1l1l1lll1ll_opy_ = {}
        bstack1l1ll111l11_opy_ = None
        bstack1l1ll1l111l_opy_ = {}
        if bstack1l1ll11ll11_opy_ is not None or bstack1l1ll11ll1l_opy_ is not None: # check top level caps
            if bstack1l1ll11ll11_opy_ is not None:
                bstack1l1ll1l111l_opy_[bstack11lll_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ኎")] = bstack1l1ll11ll11_opy_
            if bstack1l1ll11ll1l_opy_ is not None and callable(getattr(bstack1l1ll11ll1l_opy_, bstack11lll_opy_ (u"ࠧࡺ࡯ࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢ኏"))):
                bstack1l1ll1l111l_opy_[bstack11lll_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡢࡵࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩነ")] = bstack1l1ll11ll1l_opy_.to_capabilities()
        response = self.bstack1l1llll11ll_opy_(f.platform_index, instance.ref(), json.dumps(bstack1l1ll1l111l_opy_).encode(bstack11lll_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨኑ")))
        if response is not None and response.capabilities:
            bstack1l1lll1llll_opy_ = json.loads(response.capabilities.decode(bstack11lll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢኒ")))
            if not bstack1l1lll1llll_opy_: # empty caps bstack1l1llll1111_opy_ bstack1l1lll1lll1_opy_ bstack1l1lll1ll1l_opy_ bstack1llll1lllll_opy_ or error in processing
                return
            bstack1l1ll111l11_opy_ = f.bstack1llllll1l11_opy_[bstack11lll_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࡢࡪࡷࡵ࡭ࡠࡥࡤࡴࡸࠨና")](bstack1l1lll1llll_opy_)
        if bstack1l1ll11ll1l_opy_ is not None and bstack1l1l1llll11_opy_ >= version.parse(bstack11lll_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩኔ")):
            bstack1l1l1lll1ll_opy_ = None
        if (
                not bstack1l1ll11ll1l_opy_ and not bstack1l1ll11ll11_opy_
        ) or (
                bstack1l1l1llll11_opy_ < version.parse(bstack11lll_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪን"))
        ):
            bstack1l1l1lll1ll_opy_ = {}
            bstack1l1l1lll1ll_opy_.update(bstack1l1lll1llll_opy_)
        self.logger.info(bstack1l1l11111l_opy_)
        if os.environ.get(bstack11lll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠣኖ")).lower().__eq__(bstack11lll_opy_ (u"ࠨࡴࡳࡷࡨࠦኗ")):
            kwargs.update(
                {
                    bstack11lll_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥኘ"): f.bstack1l1ll111l1l_opy_,
                }
            )
        if bstack1l1l1llll11_opy_ >= version.parse(bstack11lll_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨኙ")):
            if bstack1l1ll11ll11_opy_ is not None:
                del kwargs[bstack11lll_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤኚ")]
            kwargs.update(
                {
                    bstack11lll_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦኛ"): bstack1l1ll111l11_opy_,
                    bstack11lll_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣኜ"): True,
                    bstack11lll_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧኝ"): None,
                }
            )
        elif bstack1l1l1llll11_opy_ >= version.parse(bstack11lll_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬኞ")):
            kwargs.update(
                {
                    bstack11lll_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢኟ"): bstack1l1l1lll1ll_opy_,
                    bstack11lll_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤአ"): bstack1l1ll111l11_opy_,
                    bstack11lll_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨኡ"): True,
                    bstack11lll_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥኢ"): None,
                }
            )
        elif bstack1l1l1llll11_opy_ >= version.parse(bstack11lll_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫኣ")):
            kwargs.update(
                {
                    bstack11lll_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧኤ"): bstack1l1l1lll1ll_opy_,
                    bstack11lll_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥእ"): True,
                    bstack11lll_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢኦ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack11lll_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣኧ"): bstack1l1l1lll1ll_opy_,
                    bstack11lll_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨከ"): True,
                    bstack11lll_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥኩ"): None,
                }
            )