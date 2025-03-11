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
import json
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack111l11l11l_opy_ import bstack111l11l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l1ll_opy_ import bstack1lll1l1111l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11l1l_opy_ import bstack11111l1111_opy_
from browserstack_sdk.sdk_cli.bstack1llll11lll1_opy_ import bstack111111lll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l111l_opy_ import bstack1111111111_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1lll1_opy_ import bstack1llll1ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1ll1_opy_ import bstack1lll1l111ll_opy_
from browserstack_sdk.sdk_cli.bstack1llll111ll1_opy_ import bstack1lllll11lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1llll_opy_ import bstack1llll111111_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1l1l_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack11ll1lllll_opy_ import bstack11ll1lllll_opy_, bstack11ll11ll1_opy_, bstack1111lll1_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack11111l1ll1_opy_ import bstack111111ll1l_opy_
from browserstack_sdk.sdk_cli.bstack111111l1l1_opy_ import bstack1llll111lll_opy_
from browserstack_sdk.sdk_cli.bstack1111llll11_opy_ import bstack1111ll1lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1ll1l_opy_ import bstack11111111l1_opy_
from bstack_utils.helper import Notset, bstack1lll11lll1l_opy_, get_cli_dir, bstack1llllll1ll1_opy_, bstack11ll111l11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from bstack_utils.helper import Notset, bstack1lll11lll1l_opy_, get_cli_dir, bstack1llllll1ll1_opy_, bstack11ll111l11_opy_, bstack1lll111l_opy_, bstack1l11l1l1ll_opy_, bstack1lll11ll11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll1111ll_opy_, bstack1llllll11l1_opy_, bstack1llll1lll1l_opy_, bstack1lllllllll1_opy_
from browserstack_sdk.sdk_cli.bstack1111llll11_opy_ import bstack11111ll11l_opy_, bstack111l1111ll_opy_, bstack1111ll11l1_opy_
from bstack_utils.constants import *
from bstack_utils import bstack1l111l11ll_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1l11llllll_opy_, bstack1l11l11ll1_opy_
logger = bstack1l111l11ll_opy_.get_logger(__name__, bstack1l111l11ll_opy_.bstack1lll1ll11ll_opy_())
def bstack1lllll1ll1l_opy_(bs_config):
    bstack11111l1l1l_opy_ = None
    bstack1lllll1l1l1_opy_ = None
    try:
        bstack1lllll1l1l1_opy_ = get_cli_dir()
        bstack11111l1l1l_opy_ = bstack1llllll1ll1_opy_(bstack1lllll1l1l1_opy_)
        bstack1lllllll111_opy_ = bstack1lll11lll1l_opy_(bstack11111l1l1l_opy_, bstack1lllll1l1l1_opy_, bs_config)
        bstack11111l1l1l_opy_ = bstack1lllllll111_opy_ if bstack1lllllll111_opy_ else bstack11111l1l1l_opy_
        if not bstack11111l1l1l_opy_:
            raise ValueError(bstack11ll1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨ࡙ࠥࡄࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡔࡆ࡚ࡈࠣ࿠"))
    except Exception as ex:
        logger.debug(bstack11ll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡲࡡࡵࡧࡶࡸࠥࡨࡩ࡯ࡣࡵࡽࠥࢁࡽࠣ࿡").format(ex))
        bstack11111l1l1l_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡕࡇࡔࡉࠤ࿢"))
        if bstack11111l1l1l_opy_:
            logger.debug(bstack11ll1l_opy_ (u"ࠢࡇࡣ࡯ࡰ࡮ࡴࡧࠡࡤࡤࡧࡰࠦࡴࡰࠢࡖࡈࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡑࡃࡗࡌࠥ࡬ࡲࡰ࡯ࠣࡩࡳࡼࡩࡳࡱࡱࡱࡪࡴࡴ࠻ࠢࠥ࿣") + str(bstack11111l1l1l_opy_) + bstack11ll1l_opy_ (u"ࠣࠤ࿤"))
        else:
            logger.debug(bstack11ll1l_opy_ (u"ࠤࡑࡳࠥࡼࡡ࡭࡫ࡧࠤࡘࡊࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡓࡅ࡙ࡎࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡨࡲࡻ࡯ࡲࡰࡰࡰࡩࡳࡺ࠻ࠡࡵࡨࡸࡺࡶࠠ࡮ࡣࡼࠤࡧ࡫ࠠࡪࡰࡦࡳࡲࡶ࡬ࡦࡶࡨ࠲ࠧ࿥"))
    return bstack11111l1l1l_opy_, bstack1lllll1l1l1_opy_
bstack1llll1ll1ll_opy_ = bstack11ll1l_opy_ (u"ࠥ࠽࠾࠿࠹ࠣ࿦")
bstack1lllll11ll1_opy_ = bstack11ll1l_opy_ (u"ࠦࡷ࡫ࡡࡥࡻࠥ࿧")
bstack111111llll_opy_ = bstack11ll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤ࡙ࡅࡔࡕࡌࡓࡓࡥࡉࡅࠤ࿨")
bstack1lll1l11l1l_opy_ = bstack11ll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡌࡊࡕࡗࡉࡓࡥࡁࡅࡆࡕࠦ࿩")
bstack1l1l1ll1l1_opy_ = bstack11ll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠥ࿪")
bstack1llll1l11l1_opy_ = re.compile(bstack11ll1l_opy_ (u"ࡳࠤࠫࡃ࡮࠯࠮ࠫࠪࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡽࡄࡖ࠭࠳࠰ࠢ࿫"))
bstack1llllll1111_opy_ = bstack11ll1l_opy_ (u"ࠤࡧࡩࡻ࡫࡬ࡰࡲࡰࡩࡳࡺࠢ࿬")
bstack1lll1llll11_opy_ = [
    bstack11ll11ll1_opy_.bstack1ll111l1ll_opy_,
    bstack11ll11ll1_opy_.CONNECT,
    bstack11ll11ll1_opy_.bstack1l111l1ll1_opy_,
]
class SDKCLI:
    _1llllll1l11_opy_ = None
    process: Union[None, Any]
    bstack1lll11lll11_opy_: bool
    bstack11111l1l11_opy_: bool
    bstack111111111l_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1llll1l1l11_opy_: Union[None, grpc.Channel]
    bstack1llll11111l_opy_: str
    test_framework: TestFramework
    bstack1111llll11_opy_: bstack1111ll1lll_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1lll1l1l1l1_opy_: bstack1llll1llll1_opy_
    accessibility: bstack11111l1111_opy_
    ai: bstack111111lll1_opy_
    bstack111111l111_opy_: bstack1111111111_opy_
    bstack1lll1llll1l_opy_: List[bstack1lll1l1111l_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1lll1ll1l1l_opy_: Any
    bstack1lll11lllll_opy_: Dict[str, timedelta]
    bstack1llll11ll11_opy_: str
    bstack111l11l11l_opy_: bstack111l11l1l1_opy_
    def __new__(cls):
        if not cls._1llllll1l11_opy_:
            cls._1llllll1l11_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1llllll1l11_opy_
    def __init__(self):
        self.process = None
        self.bstack1lll11lll11_opy_ = False
        self.bstack1llll1l1l11_opy_ = None
        self.bstack1lll11ll11l_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1lll1l11l1l_opy_, None)
        self.bstack1lll1lll11l_opy_ = os.environ.get(bstack111111llll_opy_, bstack11ll1l_opy_ (u"ࠥࠦ࿭")) == bstack11ll1l_opy_ (u"ࠦࠧ࿮")
        self.bstack11111l1l11_opy_ = False
        self.bstack111111111l_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1lll1ll1l1l_opy_ = None
        self.test_framework = None
        self.bstack1111llll11_opy_ = None
        self.bstack1llll11111l_opy_=bstack11ll1l_opy_ (u"ࠧࠨ࿯")
        self.session_framework = None
        self.logger = bstack1l111l11ll_opy_.get_logger(self.__class__.__name__, bstack1l111l11ll_opy_.bstack1lll1ll11ll_opy_())
        self.bstack1lll11lllll_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack111l11l11l_opy_ = bstack111l11l1l1_opy_()
        self.bstack111111ll11_opy_ = None
        self.bstack1llll11l1ll_opy_ = None
        self.bstack1lll1l1l1l1_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1lll1llll1l_opy_ = []
    def bstack11lll1ll11_opy_(self):
        return os.environ.get(bstack1l1l1ll1l1_opy_).lower().__eq__(bstack11ll1l_opy_ (u"ࠨࡴࡳࡷࡨࠦ࿰"))
    def is_enabled(self, config):
        if bstack11ll1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ࿱") in config and str(config[bstack11ll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ࿲")]).lower() != bstack11ll1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ࿳"):
            return False
        bstack111111l11l_opy_ = [bstack11ll1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥ࿴"), bstack11ll1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣ࿵")]
        bstack1lllll111l1_opy_ = config.get(bstack11ll1l_opy_ (u"ࠧ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠣ࿶")) in bstack111111l11l_opy_ or os.environ.get(bstack11ll1l_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧ࿷")) in bstack111111l11l_opy_
        os.environ[bstack11ll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡉࡔࡡࡕ࡙ࡓࡔࡉࡏࡉࠥ࿸")] = str(bstack1lllll111l1_opy_) # bstack1llllll111l_opy_ bstack1llll1lll11_opy_ VAR to bstack1llllllllll_opy_ is binary running
        return bstack1lllll111l1_opy_
    def bstack1l1111l1l_opy_(self):
        for event in bstack1lll1llll11_opy_:
            bstack11ll1lllll_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack11ll1lllll_opy_.logger.debug(bstack11ll1l_opy_ (u"ࠣࡽࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࢃࠠ࠾ࡀࠣࡿࡦࡸࡧࡴࡿࠣࠦ࿹") + str(kwargs) + bstack11ll1l_opy_ (u"ࠤࠥ࿺"))
            )
        bstack11ll1lllll_opy_.register(bstack11ll11ll1_opy_.bstack1ll111l1ll_opy_, self.__1llllll11ll_opy_)
        bstack11ll1lllll_opy_.register(bstack11ll11ll1_opy_.CONNECT, self.__1lllllll1l1_opy_)
        bstack11ll1lllll_opy_.register(bstack11ll11ll1_opy_.bstack1l111l1ll1_opy_, self.__1llll1ll1l1_opy_)
        bstack11ll1lllll_opy_.register(bstack11ll11ll1_opy_.bstack111ll11ll_opy_, self.__1lllll11111_opy_)
    def bstack11111l1l_opy_(self):
        return not self.bstack1lll1lll11l_opy_ and os.environ.get(bstack111111llll_opy_, bstack11ll1l_opy_ (u"ࠥࠦ࿻")) != bstack11ll1l_opy_ (u"ࠦࠧ࿼")
    def is_running(self):
        if self.bstack1lll1lll11l_opy_:
            return self.bstack1lll11lll11_opy_
        else:
            return bool(self.bstack1llll1l1l11_opy_)
    def bstack1llll11l11l_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1lll1llll1l_opy_) and cli.is_running()
    def __1llll11llll_opy_(self, bstack1lll11llll1_opy_=10):
        if self.bstack1lll11ll11l_opy_:
            return
        bstack1lll1111l_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1lll1l11l1l_opy_, self.cli_listen_addr)
        self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡡࠢ࿽") + str(id(self)) + bstack11ll1l_opy_ (u"ࠨ࡝ࠡࡥࡲࡲࡳ࡫ࡣࡵ࡫ࡱ࡫ࠧ࿾"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack11ll1l_opy_ (u"ࠢࡨࡴࡳࡧ࠳࡫࡮ࡢࡤ࡯ࡩࡤ࡮ࡴࡵࡲࡢࡴࡷࡵࡸࡺࠤ࿿"), 0), (bstack11ll1l_opy_ (u"ࠣࡩࡵࡴࡨ࠴ࡥ࡯ࡣࡥࡰࡪࡥࡨࡵࡶࡳࡷࡤࡶࡲࡰࡺࡼࠦက"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1lll11llll1_opy_)
        self.bstack1llll1l1l11_opy_ = channel
        self.bstack1lll11ll11l_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1llll1l1l11_opy_)
        self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡤࡱࡱࡲࡪࡩࡴࠣခ"), datetime.now() - bstack1lll1111l_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1lll1l11l1l_opy_] = self.cli_listen_addr
        self.logger.debug(bstack11ll1l_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡦࡳࡳࡴࡥࡤࡶࡨࡨ࠿ࠦࡩࡴࡡࡦ࡬࡮ࡲࡤࡠࡲࡵࡳࡨ࡫ࡳࡴ࠿ࠥဂ") + str(self.bstack11111l1l_opy_()) + bstack11ll1l_opy_ (u"ࠦࠧဃ"))
    def __1llll1ll1l1_opy_(self, event_name):
        if self.bstack11111l1l_opy_():
            self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡳࡵࡱࡳࡴ࡮ࡴࡧࠡࡅࡏࡍࠧင"))
        self.__1lll1l1l11l_opy_()
    def __1lllll11111_opy_(self, event_name, bstack1llll1lllll_opy_ = None, bstack11l1lll1l_opy_=1):
        if bstack11l1lll1l_opy_ == 1:
            self.logger.error(bstack11ll1l_opy_ (u"ࠨࡓࡰ࡯ࡨࡸ࡭࡯࡮ࡨࠢࡺࡩࡳࡺࠠࡸࡴࡲࡲ࡬ࠨစ"))
        bstack1lllll111ll_opy_ = Path(bstack1llllllll1l_opy_ (u"ࠢࡼࡵࡨࡰ࡫࠴ࡣ࡭࡫ࡢࡨ࡮ࡸࡽ࠰ࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࡵ࠱࡮ࡸࡵ࡮ࠣဆ"))
        if self.bstack1lllll1l1l1_opy_ and bstack1lllll111ll_opy_.exists():
            with open(bstack1lllll111ll_opy_, bstack11ll1l_opy_ (u"ࠨࡴࠪဇ"), encoding=bstack11ll1l_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨဈ")) as fp:
                data = json.load(fp)
                try:
                    bstack1lll111l_opy_(bstack11ll1l_opy_ (u"ࠪࡔࡔ࡙ࡔࠨဉ"), bstack1l11l1l1ll_opy_(bstack111111lll_opy_), data, {
                        bstack11ll1l_opy_ (u"ࠫࡦࡻࡴࡩࠩည"): (self.config[bstack11ll1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧဋ")], self.config[bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩဌ")])
                    })
                except Exception as e:
                    logger.debug(bstack1l11l11ll1_opy_.format(str(e)))
            bstack1lllll111ll_opy_.unlink()
        sys.exit(bstack11l1lll1l_opy_)
    @measure(event_name=EVENTS.bstack1llll1l1lll_opy_, stage=STAGE.bstack1111l111_opy_)
    def __1llllll11ll_opy_(self, event_name: str, data):
        from bstack_utils.bstack1ll11ll111_opy_ import bstack1lll11ll1l1_opy_
        self.bstack1llll11111l_opy_, self.bstack1lllll1l1l1_opy_ = bstack1lllll1ll1l_opy_(data.bs_config)
        os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡗࡓࡋࡗࡅࡇࡒࡅࡠࡆࡌࡖࠬဍ")] = self.bstack1lllll1l1l1_opy_
        if not self.bstack1llll11111l_opy_ or not self.bstack1lllll1l1l1_opy_:
            raise ValueError(bstack11ll1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡷ࡬ࡪࠦࡓࡅࡍࠣࡇࡑࡏࠠࡣ࡫ࡱࡥࡷࡿࠢဎ"))
        if self.bstack11111l1l_opy_():
            self.__1lllllll1l1_opy_(event_name, bstack1111lll1_opy_())
            return
        try:
            bstack1lll11ll1l1_opy_.end(EVENTS.bstack1ll11l1l1_opy_.value, EVENTS.bstack1ll11l1l1_opy_.value + bstack11ll1l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤဏ"), EVENTS.bstack1ll11l1l1_opy_.value + bstack11ll1l_opy_ (u"ࠥ࠾ࡪࡴࡤࠣတ"), status=True, failure=None, test_name=None)
            logger.debug(bstack11ll1l_opy_ (u"ࠦࡈࡵ࡭ࡱ࡮ࡨࡸࡪࠦࡓࡅࡍࠣࡗࡪࡺࡵࡱ࠰ࠥထ"))
        except Exception as e:
            logger.debug(bstack11ll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡣࡵ࡯࡮ࡴࡧࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࠦࡻࡾࠤဒ").format(e))
        start = datetime.now()
        is_started = self.__1lll1ll1lll_opy_()
        self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠨࡳࡱࡣࡺࡲࡤࡺࡩ࡮ࡧࠥဓ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1llll11llll_opy_()
            self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࡠࡶ࡬ࡱࡪࠨန"), datetime.now() - start)
            start = datetime.now()
            self.__1lll1lll111_opy_(data)
            self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠣࡵࡷࡥࡷࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡶ࡬ࡱࡪࠨပ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1llll1ll111_opy_, stage=STAGE.bstack1111l111_opy_)
    def __1lllllll1l1_opy_(self, event_name: str, data: bstack1111lll1_opy_):
        if not self.bstack11111l1l_opy_():
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡩ࡯࡯ࡰࡨࡧࡹࡀࠠ࡯ࡱࡷࠤࡦࠦࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࠨဖ"))
            return
        bin_session_id = os.environ.get(bstack111111llll_opy_)
        start = datetime.now()
        self.__1llll11llll_opy_()
        self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠥࡧࡴࡴ࡮ࡦࡥࡷࡣࡹ࡯࡭ࡦࠤဗ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡨࡵ࡮࡯ࡧࡦࡸࡪࡪࠠࡵࡱࠣࡩࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡉࡌࡊࠢࠥဘ") + str(bin_session_id) + bstack11ll1l_opy_ (u"ࠧࠨမ"))
        start = datetime.now()
        self.__1llll11ll1l_opy_()
        self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡴࡪ࡯ࡨࠦယ"), datetime.now() - start)
    def __1llll111l11_opy_(self):
        if not self.bstack1lll11ll11l_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡤࡣࡱࡲࡴࡺࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡧࠣࡱࡴࡪࡵ࡭ࡧࡶࠦရ"))
            return
        bstack1llllll1lll_opy_ = {
            bstack11ll1l_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧလ"): (bstack1lllll11lll_opy_, bstack1llll111111_opy_, bstack11111111l1_opy_),
            bstack11ll1l_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦဝ"): (bstack1llll1ll11l_opy_, bstack1lll1l111ll_opy_, bstack1llll111lll_opy_),
        }
        if not self.bstack111111ll11_opy_ and self.session_framework in bstack1llllll1lll_opy_:
            bstack11111111ll_opy_, bstack1lll1lll1ll_opy_, bstack1llll11l111_opy_ = bstack1llllll1lll_opy_[self.session_framework]
            bstack1lllll1llll_opy_ = bstack1lll1lll1ll_opy_()
            self.bstack1llll11l1ll_opy_ = bstack1lllll1llll_opy_
            self.bstack111111ll11_opy_ = bstack1llll11l111_opy_
            self.bstack1lll1llll1l_opy_.append(bstack1lllll1llll_opy_)
            self.bstack1lll1llll1l_opy_.append(bstack11111111ll_opy_(self.bstack1llll11l1ll_opy_))
        if not self.bstack1lll1l1l1l1_opy_ and self.config_observability and self.config_observability.success: # bstack1lll1l1ll11_opy_
            self.bstack1lll1l1l1l1_opy_ = bstack1llll1llll1_opy_(self.bstack111111ll11_opy_, self.bstack1llll11l1ll_opy_) # bstack1lll1l1lll1_opy_
            self.bstack1lll1llll1l_opy_.append(self.bstack1lll1l1l1l1_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack11111l1111_opy_(self.bstack111111ll11_opy_, self.bstack1llll11l1ll_opy_)
            self.bstack1lll1llll1l_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack11ll1l_opy_ (u"ࠥࡷࡪࡲࡦࡉࡧࡤࡰࠧသ"), False) == True:
            self.ai = bstack111111lll1_opy_()
            self.bstack1lll1llll1l_opy_.append(self.ai)
        if not self.percy and self.bstack1lll1ll1l1l_opy_ and self.bstack1lll1ll1l1l_opy_.success:
            self.percy = bstack1111111111_opy_(self.bstack1lll1ll1l1l_opy_)
            self.bstack1lll1llll1l_opy_.append(self.percy)
        for mod in self.bstack1lll1llll1l_opy_:
            if not mod.bstack1lll1l111l1_opy_():
                mod.configure(self.bstack1lll11ll11l_opy_, self.config, self.cli_bin_session_id, self.bstack111l11l11l_opy_)
    def __1111111ll1_opy_(self):
        for mod in self.bstack1lll1llll1l_opy_:
            if mod.bstack1lll1l111l1_opy_():
                mod.configure(self.bstack1lll11ll11l_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1lllll1l1ll_opy_, stage=STAGE.bstack1111l111_opy_)
    def __1lll1lll111_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack11111l1l11_opy_:
            return
        self.__1lll11ll1ll_opy_(data)
        bstack1lll1111l_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack11ll1l_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࠦဟ")
        req.sdk_language = bstack11ll1l_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧဠ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1llll1l11l1_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠨ࡛ࠣအ") + str(id(self)) + bstack11ll1l_opy_ (u"ࠢ࡞ࠢࡰࡥ࡮ࡴ࠭ࡱࡴࡲࡧࡪࡹࡳ࠻ࠢࡶࡸࡦࡸࡴࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨဢ"))
            r = self.bstack1lll11ll11l_opy_.StartBinSession(req)
            self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡵࡣࡵࡸࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥဣ"), datetime.now() - bstack1lll1111l_opy_)
            os.environ[bstack111111llll_opy_] = r.bin_session_id
            self.__1lll1l11111_opy_(r)
            self.__1llll111l11_opy_()
            self.bstack111l11l11l_opy_.start()
            self.bstack11111l1l11_opy_ = True
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤ࡞ࠦဤ") + str(id(self)) + bstack11ll1l_opy_ (u"ࠥࡡࠥࡳࡡࡪࡰ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡩ࡯࡯ࡰࡨࡧࡹ࡫ࡤࠣဥ"))
        except grpc.bstack1lll1lllll1_opy_ as bstack1lll1ll1111_opy_:
            self.logger.error(bstack11ll1l_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡸ࡮ࡳࡥࡰࡧࡸࡸ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨဦ") + str(bstack1lll1ll1111_opy_) + bstack11ll1l_opy_ (u"ࠧࠨဧ"))
            traceback.print_exc()
            raise bstack1lll1ll1111_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥဨ") + str(e) + bstack11ll1l_opy_ (u"ࠢࠣဩ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack111111l1ll_opy_, stage=STAGE.bstack1111l111_opy_)
    def __1llll11ll1l_opy_(self):
        if not self.bstack11111l1l_opy_() or not self.cli_bin_session_id or self.bstack111111111l_opy_:
            return
        bstack1lll1111l_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨဪ"), bstack11ll1l_opy_ (u"ࠩ࠳ࠫါ")))
        try:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠥ࡟ࠧာ") + str(id(self)) + bstack11ll1l_opy_ (u"ࠦࡢࠦࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡤࡱࡱࡲࡪࡩࡴࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࠨိ"))
            r = self.bstack1lll11ll11l_opy_.ConnectBinSession(req)
            self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡧࡴࡴ࡮ࡦࡥࡷࡣࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠤီ"), datetime.now() - bstack1lll1111l_opy_)
            self.__1lll1l11111_opy_(r)
            self.__1llll111l11_opy_()
            self.bstack111l11l11l_opy_.start()
            self.bstack111111111l_opy_ = True
            self.logger.debug(bstack11ll1l_opy_ (u"ࠨ࡛ࠣု") + str(id(self)) + bstack11ll1l_opy_ (u"ࠢ࡞ࠢࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡧࡴࡴ࡮ࡦࡥࡷࡩࡩࠨူ"))
        except grpc.bstack1lll1lllll1_opy_ as bstack1lll1ll1111_opy_:
            self.logger.error(bstack11ll1l_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡵ࡫ࡰࡩࡴ࡫ࡵࡵ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥေ") + str(bstack1lll1ll1111_opy_) + bstack11ll1l_opy_ (u"ࠤࠥဲ"))
            traceback.print_exc()
            raise bstack1lll1ll1111_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢဳ") + str(e) + bstack11ll1l_opy_ (u"ࠦࠧဴ"))
            traceback.print_exc()
            raise e
    def __1lll1l11111_opy_(self, r):
        self.bstack1111111l11_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack11ll1l_opy_ (u"ࠧࡻ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡶࡩࡷࡼࡥࡳࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠦဵ") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack11ll1l_opy_ (u"ࠨࡥ࡮ࡲࡷࡽࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࡬࡯ࡶࡰࡧࠦံ"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack11ll1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕ࡫ࡲࡤࡻࠣ࡭ࡸࠦࡳࡦࡰࡷࠤࡴࡴ࡬ࡺࠢࡤࡷࠥࡶࡡࡳࡶࠣࡳ࡫ࠦࡴࡩࡧࠣࠦࡈࡵ࡮࡯ࡧࡦࡸࡇ࡯࡮ࡔࡧࡶࡷ࡮ࡵ࡮࠭ࠤࠣࡥࡳࡪࠠࡵࡪ࡬ࡷࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡪࡵࠣࡥࡱࡹ࡯ࠡࡷࡶࡩࡩࠦࡢࡺࠢࡖࡸࡦࡸࡴࡃ࡫ࡱࡗࡪࡹࡳࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡔࡩࡧࡵࡩ࡫ࡵࡲࡦ࠮ࠣࡒࡴࡴࡥࠡࡪࡤࡲࡩࡲࡩ࡯ࡩࠣ࡭ࡸࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ့")
        self.bstack1lll1ll1l1l_opy_ = getattr(r, bstack11ll1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧး"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ္࡛࡙࠭")] = self.config_testhub.jwt
        os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ်")] = self.config_testhub.build_hashed_id
    def bstack1lll1llllll_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1lll11lll11_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack11111l11ll_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack11111l11ll_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1lll1llllll_opy_(event_name=EVENTS.bstack1111111l1l_opy_, stage=STAGE.bstack1111l111_opy_)
    def __1lll1ll1lll_opy_(self, bstack1lll11llll1_opy_=10):
        if self.bstack1lll11lll11_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡸࡺࡡࡳࡶ࠽ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡸࡵ࡯ࡰ࡬ࡲ࡬ࠨျ"))
            return True
        self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡹࡴࡢࡴࡷࠦြ"))
        if os.getenv(bstack11ll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡈࡒ࡛ࠨွ")) == bstack1llllll1111_opy_:
            self.cli_bin_session_id = bstack1llllll1111_opy_
            self.cli_listen_addr = bstack11ll1l_opy_ (u"ࠢࡶࡰ࡬ࡼ࠿࠵ࡴ࡮ࡲ࠲ࡷࡩࡱ࠭ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠯ࠨࡷ࠳ࡹ࡯ࡤ࡭ࠥှ") % (self.cli_bin_session_id)
            self.bstack1lll11lll11_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1llll11111l_opy_, bstack11ll1l_opy_ (u"ࠣࡵࡧ࡯ࠧဿ")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack11111l11l1_opy_ compat for text=True in bstack1llll1l11ll_opy_ python
            encoding=bstack11ll1l_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣ၀"),
            bufsize=1,
            close_fds=True,
        )
        bstack1lllll1l111_opy_ = threading.Thread(target=self.__1lll11ll111_opy_, args=(bstack1lll11llll1_opy_,))
        bstack1lllll1l111_opy_.start()
        bstack1lllll1l111_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡶࡴࡦࡽ࡮࠻ࠢࡵࡩࡹࡻࡲ࡯ࡥࡲࡨࡪࡃࡻࡴࡧ࡯ࡪ࠳ࡶࡲࡰࡥࡨࡷࡸ࠴ࡲࡦࡶࡸࡶࡳࡩ࡯ࡥࡧࢀࠤࡴࡻࡴ࠾ࡽࡶࡩࡱ࡬࠮ࡱࡴࡲࡧࡪࡹࡳ࠯ࡵࡷࡨࡴࡻࡴ࠯ࡴࡨࡥࡩ࠮ࠩࡾࠢࡨࡶࡷࡃࠢ၁") + str(self.process.stderr.read()) + bstack11ll1l_opy_ (u"ࠦࠧ၂"))
        if not self.bstack1lll11lll11_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡡࠢ၃") + str(id(self)) + bstack11ll1l_opy_ (u"ࠨ࡝ࠡࡥ࡯ࡩࡦࡴࡵࡱࠤ၄"))
            self.__1lll1l1l11l_opy_()
        self.logger.debug(bstack11ll1l_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡰࡳࡱࡦࡩࡸࡹ࡟ࡳࡧࡤࡨࡾࡀࠠࠣ၅") + str(self.bstack1lll11lll11_opy_) + bstack11ll1l_opy_ (u"ࠣࠤ၆"))
        return self.bstack1lll11lll11_opy_
    def __1lll11ll111_opy_(self, bstack1lll1ll1l11_opy_=10):
        bstack1lll11l1lll_opy_ = time.time()
        while self.process and time.time() - bstack1lll11l1lll_opy_ < bstack1lll1ll1l11_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack11ll1l_opy_ (u"ࠤ࡬ࡨࡂࠨ၇") in line:
                    self.cli_bin_session_id = line.split(bstack11ll1l_opy_ (u"ࠥ࡭ࡩࡃࠢ၈"))[-1:][0].strip()
                    self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡨࡲࡩࡠࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥ࠼ࠥ၉") + str(self.cli_bin_session_id) + bstack11ll1l_opy_ (u"ࠧࠨ၊"))
                    continue
                if bstack11ll1l_opy_ (u"ࠨ࡬ࡪࡵࡷࡩࡳࡃࠢ။") in line:
                    self.cli_listen_addr = line.split(bstack11ll1l_opy_ (u"ࠢ࡭࡫ࡶࡸࡪࡴ࠽ࠣ၌"))[-1:][0].strip()
                    self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡥ࡯࡭ࡤࡲࡩࡴࡶࡨࡲࡤࡧࡤࡥࡴ࠽ࠦ၍") + str(self.cli_listen_addr) + bstack11ll1l_opy_ (u"ࠤࠥ၎"))
                    continue
                if bstack11ll1l_opy_ (u"ࠥࡴࡴࡸࡴ࠾ࠤ၏") in line:
                    port = line.split(bstack11ll1l_opy_ (u"ࠦࡵࡵࡲࡵ࠿ࠥၐ"))[-1:][0].strip()
                    self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡶ࡯ࡳࡶ࠽ࠦၑ") + str(port) + bstack11ll1l_opy_ (u"ࠨࠢၒ"))
                    continue
                if line.strip() == bstack1lllll11ll1_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack11ll1l_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡈࡏࡅࡌࡥࡉࡐࡡࡖࡘࡗࡋࡁࡎࠤၓ"), bstack11ll1l_opy_ (u"ࠣ࠳ࠥၔ")) == bstack11ll1l_opy_ (u"ࠤ࠴ࠦၕ"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1lll11lll11_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳ࠼ࠣࠦၖ") + str(e) + bstack11ll1l_opy_ (u"ࠦࠧၗ"))
        return False
    @measure(event_name=EVENTS.bstack1lllllll1ll_opy_, stage=STAGE.bstack1111l111_opy_)
    def __1lll1l1l11l_opy_(self):
        if self.bstack1llll1l1l11_opy_:
            self.bstack111l11l11l_opy_.stop()
            start = datetime.now()
            if self.bstack1lllll1111l_opy_():
                self.cli_bin_session_id = None
                if self.bstack111111111l_opy_:
                    self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠧࡹࡴࡰࡲࡢࡷࡪࡹࡳࡪࡱࡱࡣࡹ࡯࡭ࡦࠤၘ"), datetime.now() - start)
                else:
                    self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠨࡳࡵࡱࡳࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡺࡩ࡮ࡧࠥၙ"), datetime.now() - start)
            self.__1111111ll1_opy_()
            start = datetime.now()
            self.bstack1llll1l1l11_opy_.close()
            self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠢࡥ࡫ࡶࡧࡴࡴ࡮ࡦࡥࡷࡣࡹ࡯࡭ࡦࠤၚ"), datetime.now() - start)
            self.bstack1llll1l1l11_opy_ = None
        if self.process:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡵࡷࡳࡵࠨၛ"))
            start = datetime.now()
            self.process.terminate()
            self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠤ࡮࡭ࡱࡲ࡟ࡵ࡫ࡰࡩࠧၜ"), datetime.now() - start)
            self.process = None
            if self.bstack1lll1lll11l_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack1l1lll11l1_opy_()
                self.logger.info(
                    bstack11ll1l_opy_ (u"࡚ࠥ࡮ࡹࡩࡵࠢ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾࠢࡷࡳࠥࡼࡩࡦࡹࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡵࡵࡲࡵ࠮ࠣ࡭ࡳࡹࡩࡨࡪࡷࡷ࠱ࠦࡡ࡯ࡦࠣࡱࡦࡴࡹࠡ࡯ࡲࡶࡪࠦࡤࡦࡤࡸ࡫࡬࡯࡮ࡨࠢ࡬ࡲ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴࠠࡢ࡮࡯ࠤࡦࡺࠠࡰࡰࡨࠤࡵࡲࡡࡤࡧࠤࡠࡳࠨၝ").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack11ll1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪၞ")] = self.config_testhub.build_hashed_id
        self.bstack1lll11lll11_opy_ = False
    def __1lll11ll1ll_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack11ll1l_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢၟ")] = selenium.__version__
            data.frameworks.append(bstack11ll1l_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣၠ"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack11ll1l_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦၡ")] = __version__
            data.frameworks.append(bstack11ll1l_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧၢ"))
        except:
            pass
    def bstack1llllllll11_opy_(self, hub_url: str, platform_index: int, bstack1l111lll1l_opy_: Any):
        if self.bstack1111llll11_opy_:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡶ࡯࡮ࡶࡰࡦࡦࠣࡷࡪࡺࡵࡱࠢࡶࡩࡱ࡫࡮ࡪࡷࡰ࠾ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡳࡦࡶࠣࡹࡵࠨၣ"))
            return
        try:
            bstack1lll1111l_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack11ll1l_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧၤ")
            self.bstack1111llll11_opy_ = bstack1llll111lll_opy_(
                hub_url,
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1lll1lll1l1_opy_={bstack11ll1l_opy_ (u"ࠦࡨࡸࡥࡢࡶࡨࡣࡴࡶࡴࡪࡱࡱࡷࡤ࡬ࡲࡰ࡯ࡢࡧࡦࡶࡳࠣၥ"): bstack1l111lll1l_opy_}
            )
            def bstack1llll1l1111_opy_(self):
                return
            if self.config.get(bstack11ll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠢၦ"), True):
                Service.start = bstack1llll1l1111_opy_
                Service.stop = bstack1llll1l1111_opy_
            def get_accessibility_results(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results(driver, framework_name=framework)
            def get_accessibility_results_summary(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results_summary(driver, framework_name=framework)
            def perform_scan(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.perform_scan(driver, method=None, framework_name=framework)
            WebDriver.getAccessibilityResults = get_accessibility_results
            WebDriver.get_accessibility_results = get_accessibility_results
            WebDriver.getAccessibilityResultsSummary = get_accessibility_results_summary
            WebDriver.get_accessibility_results_summary = get_accessibility_results_summary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢၧ"), datetime.now() - bstack1lll1111l_opy_)
        except Exception as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࡵࡱࠢࡶࡩࡱ࡫࡮ࡪࡷࡰ࠾ࠥࠨၨ") + str(e) + bstack11ll1l_opy_ (u"ࠣࠤၩ"))
    def bstack1llllll1l1l_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack1lll1lllll_opy_
            self.bstack1111llll11_opy_ = bstack11111111l1_opy_(
                platform_index,
                framework_name=bstack11ll1l_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨၪ"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࡸࡴࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠼ࠣࠦၫ") + str(e) + bstack11ll1l_opy_ (u"ࠦࠧၬ"))
            pass
    def bstack1llll1111l1_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡹ࡫ࡪࡲࡳࡩࡩࠦࡳࡦࡶࡸࡴࠥࡶࡹࡵࡧࡶࡸ࠿ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡴࡧࡷࠤࡺࡶࠢၭ"))
            return
        if bstack11ll111l11_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack11ll1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨၮ"): pytest.__version__ }, [bstack11ll1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦၯ")])
            return
        try:
            import pytest
            self.test_framework = bstack111111ll1l_opy_({ bstack11ll1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣၰ"): pytest.__version__ }, [bstack11ll1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤၱ")])
        except Exception as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࡸࡴࠥࡶࡹࡵࡧࡶࡸ࠿ࠦࠢၲ") + str(e) + bstack11ll1l_opy_ (u"ࠦࠧၳ"))
        self.bstack1lll1ll11l1_opy_()
    def bstack1lll1ll11l1_opy_(self):
        if not self.bstack11lll1ll11_opy_():
            return
        bstack1l1l1l1111_opy_ = None
        def bstack1l1ll1l11_opy_(config, startdir):
            return bstack11ll1l_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࠱ࡿࠥၴ").format(bstack11ll1l_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧၵ"))
        def bstack111l111l_opy_():
            return
        def bstack11ll11l1_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack11ll1l_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸࠧၶ"):
                return bstack11ll1l_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢၷ")
            else:
                return bstack1l1l1l1111_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack1l1l1l1111_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack1l1ll1l11_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack111l111l_opy_
            Config.getoption = bstack11ll11l1_opy_
        except Exception as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡵࡥ࡫ࠤࡵࡿࡴࡦࡵࡷࠤࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠦࡦࡰࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠼ࠣࠦၸ") + str(e) + bstack11ll1l_opy_ (u"ࠥࠦၹ"))
    def bstack1lll1l11lll_opy_(self):
        bstack1111111lll_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack1111111lll_opy_, dict):
            if cli.config_observability:
                bstack1111111lll_opy_.update(
                    {bstack11ll1l_opy_ (u"ࠦࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠦၺ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack11ll1l_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡹ࡟ࡵࡱࡢࡻࡷࡧࡰࠣၻ") in accessibility.get(bstack11ll1l_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢၼ"), {}):
                    bstack1lll1ll111l_opy_ = accessibility.get(bstack11ll1l_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣၽ"))
                    bstack1lll1ll111l_opy_.update({ bstack11ll1l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡵࡗࡳ࡜ࡸࡡࡱࠤၾ"): bstack1lll1ll111l_opy_.pop(bstack11ll1l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡶࡣࡹࡵ࡟ࡸࡴࡤࡴࠧၿ")) })
                bstack1111111lll_opy_.update({bstack11ll1l_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠥႀ"): accessibility })
        return bstack1111111lll_opy_
    @measure(event_name=EVENTS.bstack1lllll11l11_opy_, stage=STAGE.bstack1111l111_opy_)
    def bstack1lllll1111l_opy_(self, bstack1lllll1ll11_opy_: str = None, bstack1lll1l1l111_opy_: str = None, bstack11l1lll1l_opy_: int = None):
        if not self.cli_bin_session_id or not self.bstack1lll11ll11l_opy_:
            return
        bstack1lll1111l_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if bstack11l1lll1l_opy_:
            req.bstack11l1lll1l_opy_ = bstack11l1lll1l_opy_
        if bstack1lllll1ll11_opy_:
            req.bstack1lllll1ll11_opy_ = bstack1lllll1ll11_opy_
        if bstack1lll1l1l111_opy_:
            req.bstack1lll1l1l111_opy_ = bstack1lll1l1l111_opy_
        try:
            r = self.bstack1lll11ll11l_opy_.StopBinSession(req)
            self.bstack1111l1111_opy_(bstack11ll1l_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡸࡴࡶ࡟ࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧႁ"), datetime.now() - bstack1lll1111l_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack1111l1111_opy_(self, key: str, value: timedelta):
        tag = bstack11ll1l_opy_ (u"ࠧࡩࡨࡪ࡮ࡧ࠱ࡵࡸ࡯ࡤࡧࡶࡷࠧႂ") if self.bstack11111l1l_opy_() else bstack11ll1l_opy_ (u"ࠨ࡭ࡢ࡫ࡱ࠱ࡵࡸ࡯ࡤࡧࡶࡷࠧႃ")
        self.bstack1lll11lllll_opy_[bstack11ll1l_opy_ (u"ࠢ࠻ࠤႄ").join([tag + bstack11ll1l_opy_ (u"ࠣ࠯ࠥႅ") + str(id(self)), key])] += value
    def bstack1l1lll11l1_opy_(self):
        if not os.getenv(bstack11ll1l_opy_ (u"ࠤࡇࡉࡇ࡛ࡇࡠࡒࡈࡖࡋࠨႆ"), bstack11ll1l_opy_ (u"ࠥ࠴ࠧႇ")) == bstack11ll1l_opy_ (u"ࠦ࠶ࠨႈ"):
            return
        bstack1lllll1l11l_opy_ = dict()
        bstack1111l1l11l_opy_ = []
        if self.test_framework:
            bstack1111l1l11l_opy_.extend(list(self.test_framework.bstack1111l1l11l_opy_.values()))
        if self.bstack1111llll11_opy_:
            bstack1111l1l11l_opy_.extend(list(self.bstack1111llll11_opy_.bstack1111l1l11l_opy_.values()))
        for instance in bstack1111l1l11l_opy_:
            if not instance.platform_index in bstack1lllll1l11l_opy_:
                bstack1lllll1l11l_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1lllll1l11l_opy_[instance.platform_index]
            for k, v in instance.bstack1lll1l11ll1_opy_().items():
                report[k] += v
                report[k.split(bstack11ll1l_opy_ (u"ࠧࡀࠢႉ"))[0]] += v
        bstack1llll111l1l_opy_ = sorted([(k, v) for k, v in self.bstack1lll11lllll_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1lllllll11l_opy_ = 0
        for r in bstack1llll111l1l_opy_:
            bstack1llll1l1ll1_opy_ = r[1].total_seconds()
            bstack1lllllll11l_opy_ += bstack1llll1l1ll1_opy_
            self.logger.debug(bstack11ll1l_opy_ (u"ࠨ࡛ࡱࡧࡵࡪࡢࠦࡣ࡭࡫࠽ࡿࡷࡡ࠰࡞ࡿࡀࠦႊ") + str(bstack1llll1l1ll1_opy_) + bstack11ll1l_opy_ (u"ࠢࠣႋ"))
        self.logger.debug(bstack11ll1l_opy_ (u"ࠣ࠯࠰ࠦႌ"))
        bstack1llll11l1l1_opy_ = []
        for platform_index, report in bstack1lllll1l11l_opy_.items():
            bstack1llll11l1l1_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1llll11l1l1_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack11l1lllll1_opy_ = set()
        bstack1lll1l11l11_opy_ = 0
        for r in bstack1llll11l1l1_opy_:
            bstack1llll1l1ll1_opy_ = r[2].total_seconds()
            bstack1lll1l11l11_opy_ += bstack1llll1l1ll1_opy_
            bstack11l1lllll1_opy_.add(r[0])
            self.logger.debug(bstack11ll1l_opy_ (u"ࠤ࡞ࡴࡪࡸࡦ࡞ࠢࡷࡩࡸࡺ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠯ࡾࡶࡠ࠶࡝ࡾ࠼ࡾࡶࡠ࠷࡝ࡾ࠿ႍࠥ") + str(bstack1llll1l1ll1_opy_) + bstack11ll1l_opy_ (u"ࠥࠦႎ"))
        if self.bstack11111l1l_opy_():
            self.logger.debug(bstack11ll1l_opy_ (u"ࠦ࠲࠳ࠢႏ"))
            self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡡࡰࡦࡴࡩࡡࠥࡩ࡬ࡪ࠼ࡦ࡬࡮ࡲࡤ࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠿ࡾࡸࡴࡺࡡ࡭ࡡࡦࡰ࡮ࢃࠠࡵࡧࡶࡸ࠿ࡶ࡬ࡢࡶࡩࡳࡷࡳࡳ࠮ࡽࡶࡸࡷ࠮ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠫࢀࡁࠧ႐") + str(bstack1lll1l11l11_opy_) + bstack11ll1l_opy_ (u"ࠨࠢ႑"))
        else:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠢ࡜ࡲࡨࡶ࡫ࡣࠠࡤ࡮࡬࠾ࡲࡧࡩ࡯࠯ࡳࡶࡴࡩࡥࡴࡵࡀࠦ႒") + str(bstack1lllllll11l_opy_) + bstack11ll1l_opy_ (u"ࠣࠤ႓"))
        self.logger.debug(bstack11ll1l_opy_ (u"ࠤ࠰࠱ࠧ႔"))
    def bstack1111111l11_opy_(self, r):
        if r is not None and getattr(r, bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࠫ႕"), None) and getattr(r.testhub, bstack11ll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫ႖"), None):
            errors = json.loads(r.testhub.errors.decode(bstack11ll1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦ႗")))
            for bstack11111l111l_opy_, err in errors.items():
                if err[bstack11ll1l_opy_ (u"࠭ࡴࡺࡲࡨࠫ႘")] == bstack11ll1l_opy_ (u"ࠧࡪࡰࡩࡳࠬ႙"):
                    self.logger.info(err[bstack11ll1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩႚ")])
                else:
                    self.logger.error(err[bstack11ll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪႛ")])
cli = SDKCLI()