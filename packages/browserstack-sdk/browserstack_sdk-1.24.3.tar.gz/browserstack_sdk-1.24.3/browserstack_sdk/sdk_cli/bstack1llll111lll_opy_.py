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
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack111l111lll_opy_ import bstack111l11l1ll_opy_
from browserstack_sdk.sdk_cli.bstack11111l1lll_opy_ import (
    bstack1111l1l111_opy_,
    bstack1111ll111l_opy_,
    bstack1111l1llll_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1llll1111l1_opy_ import bstack1lll1l11l1l_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1l1l11111l_opy_
from bstack_utils.helper import bstack1ll1111llll_opy_
import threading
import os
import urllib.parse
class bstack1lll1llll11_opy_(bstack111l11l1ll_opy_):
    def __init__(self, bstack1llllll1ll1_opy_):
        super().__init__()
        bstack1lll1l11l1l_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111l11111_opy_, bstack1111ll111l_opy_.PRE), self.bstack1l1lll1l111_opy_)
        bstack1lll1l11l1l_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111l11111_opy_, bstack1111ll111l_opy_.PRE), self.bstack1l1llll1lll_opy_)
        bstack1lll1l11l1l_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111l1l1l1_opy_, bstack1111ll111l_opy_.PRE), self.bstack1l1llll11l1_opy_)
        bstack1lll1l11l1l_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111ll1111_opy_, bstack1111ll111l_opy_.PRE), self.bstack1l1lll1l1ll_opy_)
        bstack1lll1l11l1l_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.bstack1111l11111_opy_, bstack1111ll111l_opy_.PRE), self.bstack1l1llll1ll1_opy_)
        bstack1lll1l11l1l_opy_.bstack1ll1l1lll1l_opy_((bstack1111l1l111_opy_.QUIT, bstack1111ll111l_opy_.PRE), self.on_close)
        self.bstack1llllll1ll1_opy_ = bstack1llllll1ll1_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1l1lll1l111_opy_(
        self,
        f: bstack1lll1l11l1l_opy_,
        bstack1l1lllll11l_opy_: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll_opy_ (u"ࠧࡲࡡࡶࡰࡦ࡬ࠧᇧ"):
            return
        if not bstack1ll1111llll_opy_():
            self.logger.debug(bstack11lll_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡲࡡࡶࡰࡦ࡬ࠥࡳࡥࡵࡪࡲࡨ࠱ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥᇨ"))
            return
        def wrapped(bstack1l1lllll11l_opy_, launch, *args, **kwargs):
            response = self.bstack1l1llll11ll_opy_(f.platform_index, instance.ref(), json.dumps({bstack11lll_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᇩ"): True}).encode(bstack11lll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᇪ")))
            if response is not None and response.capabilities:
                if not bstack1ll1111llll_opy_():
                    browser = launch(bstack1l1lllll11l_opy_)
                    return browser
                bstack1l1lll1llll_opy_ = json.loads(response.capabilities.decode(bstack11lll_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᇫ")))
                if not bstack1l1lll1llll_opy_: # empty caps bstack1l1llll1111_opy_ bstack1l1lll1lll1_opy_ bstack1l1lll1ll1l_opy_ bstack1llll1lllll_opy_ or error in processing
                    return
                bstack1l1lll11lll_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1l1lll1llll_opy_))
                f.bstack1111ll11ll_opy_(instance, bstack1lll1l11l1l_opy_.bstack1l1llll1l11_opy_, bstack1l1lll11lll_opy_)
                f.bstack1111ll11ll_opy_(instance, bstack1lll1l11l1l_opy_.bstack1l1lll1l1l1_opy_, bstack1l1lll1llll_opy_)
                browser = bstack1l1lllll11l_opy_.connect(bstack1l1lll11lll_opy_)
                return browser
        return wrapped
    def bstack1l1llll11l1_opy_(
        self,
        f: bstack1lll1l11l1l_opy_,
        Connection: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll_opy_ (u"ࠥࡨ࡮ࡹࡰࡢࡶࡦ࡬ࠧᇬ"):
            self.logger.debug(bstack11lll_opy_ (u"ࠦࡗ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡪࡰࠣࡨ࡮ࡹࡰࡢࡶࡦ࡬ࠥࡳࡥࡵࡪࡲࡨ࠱ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥᇭ"))
            return
        if not bstack1ll1111llll_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack11lll_opy_ (u"ࠬࡶࡡࡳࡣࡰࡷࠬᇮ"), {}).get(bstack11lll_opy_ (u"࠭ࡢࡴࡒࡤࡶࡦࡳࡳࠨᇯ")):
                    bstack1l1lllll111_opy_ = args[0][bstack11lll_opy_ (u"ࠢࡱࡣࡵࡥࡲࡹࠢᇰ")][bstack11lll_opy_ (u"ࠣࡤࡶࡔࡦࡸࡡ࡮ࡵࠥᇱ")]
                    session_id = bstack1l1lllll111_opy_.get(bstack11lll_opy_ (u"ࠤࡶࡩࡸࡹࡩࡰࡰࡌࡨࠧᇲ"))
                    f.bstack1111ll11ll_opy_(instance, bstack1lll1l11l1l_opy_.bstack1l1llll1l1l_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack11lll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡧ࡭ࡸࡶࡡࡵࡥ࡫ࠤࡲ࡫ࡴࡩࡱࡧ࠾ࠥࠨᇳ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1l1llll1ll1_opy_(
        self,
        f: bstack1lll1l11l1l_opy_,
        bstack1l1lllll11l_opy_: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll_opy_ (u"ࠦࡨࡵ࡮࡯ࡧࡦࡸࠧᇴ"):
            return
        if not bstack1ll1111llll_opy_():
            self.logger.debug(bstack11lll_opy_ (u"ࠧࡘࡥࡵࡷࡵࡲ࡮ࡴࡧࠡ࡫ࡱࠤࡨࡵ࡮࡯ࡧࡦࡸࠥࡳࡥࡵࡪࡲࡨ࠱ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥᇵ"))
            return
        def wrapped(bstack1l1lllll11l_opy_, connect, *args, **kwargs):
            response = self.bstack1l1llll11ll_opy_(f.platform_index, instance.ref(), json.dumps({bstack11lll_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᇶ"): True}).encode(bstack11lll_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᇷ")))
            if response is not None and response.capabilities:
                bstack1l1lll1llll_opy_ = json.loads(response.capabilities.decode(bstack11lll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᇸ")))
                if not bstack1l1lll1llll_opy_:
                    return
                bstack1l1lll11lll_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1l1lll1llll_opy_))
                if bstack1l1lll1llll_opy_.get(bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᇹ")):
                    browser = bstack1l1lllll11l_opy_.bstack1l1lll1ll11_opy_(bstack1l1lll11lll_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1l1lll11lll_opy_
                    return connect(bstack1l1lllll11l_opy_, *args, **kwargs)
        return wrapped
    def bstack1l1llll1lll_opy_(
        self,
        f: bstack1lll1l11l1l_opy_,
        bstack1ll1l111lll_opy_: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll_opy_ (u"ࠥࡲࡪࡽ࡟ࡱࡣࡪࡩࠧᇺ"):
            return
        if not bstack1ll1111llll_opy_():
            self.logger.debug(bstack11lll_opy_ (u"ࠦࡗ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡪࡰࠣࡲࡪࡽ࡟ࡱࡣࡪࡩࠥࡳࡥࡵࡪࡲࡨ࠱ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥᇻ"))
            return
        def wrapped(bstack1ll1l111lll_opy_, bstack1l1llll111l_opy_, *args, **kwargs):
            contexts = bstack1ll1l111lll_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.bstack1ll1ll1l11l_opy_:
                        for page in context.bstack1ll1ll1l11l_opy_:
                                if bstack11lll_opy_ (u"ࠧࡧࡢࡰࡷࡷ࠾ࡧࡲࡡ࡯࡭ࠥᇼ") in page.url:
                                    return page
                    else:
                        return bstack1l1llll111l_opy_(bstack1ll1l111lll_opy_)
        return wrapped
    def bstack1l1llll11ll_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack11lll_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡹࡨࡦࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࠼ࠣࠦᇽ") + str(req) + bstack11lll_opy_ (u"ࠢࠣᇾ"))
        try:
            r = self.bstack111l11l1l1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11lll_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࡶࡹࡨࡩࡥࡴࡵࡀࠦᇿ") + str(r.success) + bstack11lll_opy_ (u"ࠤࠥሀ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣሁ") + str(e) + bstack11lll_opy_ (u"ࠦࠧሂ"))
            traceback.print_exc()
            raise e
    def bstack1l1lll1l1ll_opy_(
        self,
        f: bstack1lll1l11l1l_opy_,
        Connection: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll_opy_ (u"ࠧࡥࡳࡦࡰࡧࡣࡲ࡫ࡳࡴࡣࡪࡩࡤࡺ࡯ࡠࡵࡨࡶࡻ࡫ࡲࠣሃ"):
            return
        if not bstack1ll1111llll_opy_():
            return
        def wrapped(Connection, bstack1l1lll1l11l_opy_, *args, **kwargs):
            return bstack1l1lll1l11l_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll1l11l1l_opy_,
        bstack1l1lllll11l_opy_: object,
        exec: Tuple[bstack1111l1llll_opy_, str],
        bstack1111llll11_opy_: Tuple[bstack1111l1l111_opy_, bstack1111ll111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll_opy_ (u"ࠨࡣ࡭ࡱࡶࡩࠧሄ"):
            return
        if not bstack1ll1111llll_opy_():
            self.logger.debug(bstack11lll_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦࡣ࡭ࡱࡶࡩࠥࡳࡥࡵࡪࡲࡨ࠱ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥህ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped