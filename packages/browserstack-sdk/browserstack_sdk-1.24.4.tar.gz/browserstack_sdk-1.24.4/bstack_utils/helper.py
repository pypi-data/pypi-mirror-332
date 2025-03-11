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
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
import urllib
from urllib.parse import urlparse
import copy
import zipfile
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack1l1111l1l11_opy_, bstack1l11ll1l1_opy_, bstack11l1111l_opy_, bstack1l11l111_opy_,
                                    bstack1l1111l11ll_opy_, bstack1l111111lll_opy_, bstack1l11111l1ll_opy_, bstack1l111l11ll1_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack111l1ll1l_opy_, bstack11l1ll11l1_opy_
from bstack_utils.proxy import bstack1111l11ll_opy_, bstack1l11ll1l1l_opy_
from bstack_utils.constants import *
from bstack_utils import bstack1l111l11ll_opy_
from browserstack_sdk._version import __version__
bstack1l1l11lll_opy_ = Config.bstack11l1lll11_opy_()
logger = bstack1l111l11ll_opy_.get_logger(__name__, bstack1l111l11ll_opy_.bstack1lll1ll11ll_opy_())
def bstack1l11l11ll1l_opy_(config):
    return config[bstack11ll1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪᢖ")]
def bstack1l11l11l1l1_opy_(config):
    return config[bstack11ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᢗ")]
def bstack1lll11ll11_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack11ll1l1ll1l_opy_(obj):
    values = []
    bstack11ll1llll1l_opy_ = re.compile(bstack11ll1l_opy_ (u"ࡵࠦࡣࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࡟ࡨ࠰ࠪࠢᢘ"), re.I)
    for key in obj.keys():
        if bstack11ll1llll1l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack11lll11l11l_opy_(config):
    tags = []
    tags.extend(bstack11ll1l1ll1l_opy_(os.environ))
    tags.extend(bstack11ll1l1ll1l_opy_(config))
    return tags
def bstack11ll1llllll_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack11lll111ll1_opy_(bstack11ll1l1l11l_opy_):
    if not bstack11ll1l1l11l_opy_:
        return bstack11ll1l_opy_ (u"ࠫࠬᢙ")
    return bstack11ll1l_opy_ (u"ࠧࢁࡽࠡࠪࡾࢁ࠮ࠨᢚ").format(bstack11ll1l1l11l_opy_.name, bstack11ll1l1l11l_opy_.email)
def bstack1l111lll11l_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack11llll11l11_opy_ = repo.common_dir
        info = {
            bstack11ll1l_opy_ (u"ࠨࡳࡩࡣࠥᢛ"): repo.head.commit.hexsha,
            bstack11ll1l_opy_ (u"ࠢࡴࡪࡲࡶࡹࡥࡳࡩࡣࠥᢜ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11ll1l_opy_ (u"ࠣࡤࡵࡥࡳࡩࡨࠣᢝ"): repo.active_branch.name,
            bstack11ll1l_opy_ (u"ࠤࡷࡥ࡬ࠨᢞ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11ll1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡷࡩࡷࠨᢟ"): bstack11lll111ll1_opy_(repo.head.commit.committer),
            bstack11ll1l_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡸࡪࡸ࡟ࡥࡣࡷࡩࠧᢠ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11ll1l_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࠧᢡ"): bstack11lll111ll1_opy_(repo.head.commit.author),
            bstack11ll1l_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡥࡤࡢࡶࡨࠦᢢ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11ll1l_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣᢣ"): repo.head.commit.message,
            bstack11ll1l_opy_ (u"ࠣࡴࡲࡳࡹࠨᢤ"): repo.git.rev_parse(bstack11ll1l_opy_ (u"ࠤ࠰࠱ࡸ࡮࡯ࡸ࠯ࡷࡳࡵࡲࡥࡷࡧ࡯ࠦᢥ")),
            bstack11ll1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡰࡰࡢ࡫࡮ࡺ࡟ࡥ࡫ࡵࠦᢦ"): bstack11llll11l11_opy_,
            bstack11ll1l_opy_ (u"ࠦࡼࡵࡲ࡬ࡶࡵࡩࡪࡥࡧࡪࡶࡢࡨ࡮ࡸࠢᢧ"): subprocess.check_output([bstack11ll1l_opy_ (u"ࠧ࡭ࡩࡵࠤᢨ"), bstack11ll1l_opy_ (u"ࠨࡲࡦࡸ࠰ࡴࡦࡸࡳࡦࠤᢩ"), bstack11ll1l_opy_ (u"ࠢ࠮࠯ࡪ࡭ࡹ࠳ࡣࡰ࡯ࡰࡳࡳ࠳ࡤࡪࡴࠥᢪ")]).strip().decode(
                bstack11ll1l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧ᢫")),
            bstack11ll1l_opy_ (u"ࠤ࡯ࡥࡸࡺ࡟ࡵࡣࡪࠦ᢬"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11ll1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡶࡣࡸ࡯࡮ࡤࡧࡢࡰࡦࡹࡴࡠࡶࡤ࡫ࠧ᢭"): repo.git.rev_list(
                bstack11ll1l_opy_ (u"ࠦࢀࢃ࠮࠯ࡽࢀࠦ᢮").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack11lllll111l_opy_ = []
        for remote in remotes:
            bstack11llll11111_opy_ = {
                bstack11ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᢯"): remote.name,
                bstack11ll1l_opy_ (u"ࠨࡵࡳ࡮ࠥᢰ"): remote.url,
            }
            bstack11lllll111l_opy_.append(bstack11llll11111_opy_)
        bstack11llll111ll_opy_ = {
            bstack11ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᢱ"): bstack11ll1l_opy_ (u"ࠣࡩ࡬ࡸࠧᢲ"),
            **info,
            bstack11ll1l_opy_ (u"ࠤࡵࡩࡲࡵࡴࡦࡵࠥᢳ"): bstack11lllll111l_opy_
        }
        bstack11llll111ll_opy_ = bstack11ll1l11l11_opy_(bstack11llll111ll_opy_)
        return bstack11llll111ll_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11ll1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡳࡵࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡇࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᢴ").format(err))
        return {}
def bstack11ll1l11l11_opy_(bstack11llll111ll_opy_):
    bstack11ll1l1l1l1_opy_ = bstack11lll11lll1_opy_(bstack11llll111ll_opy_)
    if bstack11ll1l1l1l1_opy_ and bstack11ll1l1l1l1_opy_ > bstack1l1111l11ll_opy_:
        bstack11ll1l1lll1_opy_ = bstack11ll1l1l1l1_opy_ - bstack1l1111l11ll_opy_
        bstack11ll1ll1ll1_opy_ = bstack11lll1ll1ll_opy_(bstack11llll111ll_opy_[bstack11ll1l_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᢵ")], bstack11ll1l1lll1_opy_)
        bstack11llll111ll_opy_[bstack11ll1l_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨᢶ")] = bstack11ll1ll1ll1_opy_
        logger.info(bstack11ll1l_opy_ (u"ࠨࡔࡩࡧࠣࡧࡴࡳ࡭ࡪࡶࠣ࡬ࡦࡹࠠࡣࡧࡨࡲࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤ࠯ࠢࡖ࡭ࡿ࡫ࠠࡰࡨࠣࡧࡴࡳ࡭ࡪࡶࠣࡥ࡫ࡺࡥࡳࠢࡷࡶࡺࡴࡣࡢࡶ࡬ࡳࡳࠦࡩࡴࠢࡾࢁࠥࡑࡂࠣᢷ")
                    .format(bstack11lll11lll1_opy_(bstack11llll111ll_opy_) / 1024))
    return bstack11llll111ll_opy_
def bstack11lll11lll1_opy_(bstack11l111l1_opy_):
    try:
        if bstack11l111l1_opy_:
            bstack11lllll1ll1_opy_ = json.dumps(bstack11l111l1_opy_)
            bstack11ll1lll1l1_opy_ = sys.getsizeof(bstack11lllll1ll1_opy_)
            return bstack11ll1lll1l1_opy_
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠢࡔࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭ࠠࡸࡪ࡬ࡰࡪࠦࡣࡢ࡮ࡦࡹࡱࡧࡴࡪࡰࡪࠤࡸ࡯ࡺࡦࠢࡲࡪࠥࡐࡓࡐࡐࠣࡳࡧࡰࡥࡤࡶ࠽ࠤࢀࢃࠢᢸ").format(e))
    return -1
def bstack11lll1ll1ll_opy_(field, bstack11llll11l1l_opy_):
    try:
        bstack11llll11lll_opy_ = len(bytes(bstack1l111111lll_opy_, bstack11ll1l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᢹ")))
        bstack11llll1111l_opy_ = bytes(field, bstack11ll1l_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᢺ"))
        bstack11lll11l1l1_opy_ = len(bstack11llll1111l_opy_)
        bstack11llll1ll1l_opy_ = ceil(bstack11lll11l1l1_opy_ - bstack11llll11l1l_opy_ - bstack11llll11lll_opy_)
        if bstack11llll1ll1l_opy_ > 0:
            bstack11lll1l1l11_opy_ = bstack11llll1111l_opy_[:bstack11llll1ll1l_opy_].decode(bstack11ll1l_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᢻ"), errors=bstack11ll1l_opy_ (u"ࠫ࡮࡭࡮ࡰࡴࡨࠫᢼ")) + bstack1l111111lll_opy_
            return bstack11lll1l1l11_opy_
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡸࡷࡻ࡮ࡤࡣࡷ࡭ࡳ࡭ࠠࡧ࡫ࡨࡰࡩ࠲ࠠ࡯ࡱࡷ࡬࡮ࡴࡧࠡࡹࡤࡷࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤࠡࡪࡨࡶࡪࡀࠠࡼࡿࠥᢽ").format(e))
    return field
def bstack11l1l1ll1l_opy_():
    env = os.environ
    if (bstack11ll1l_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡖࡔࡏࠦᢾ") in env and len(env[bstack11ll1l_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠧᢿ")]) > 0) or (
            bstack11ll1l_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡋࡓࡒࡋࠢᣀ") in env and len(env[bstack11ll1l_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠣᣁ")]) > 0):
        return {
            bstack11ll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᣂ"): bstack11ll1l_opy_ (u"ࠦࡏ࡫࡮࡬࡫ࡱࡷࠧᣃ"),
            bstack11ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᣄ"): env.get(bstack11ll1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᣅ")),
            bstack11ll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᣆ"): env.get(bstack11ll1l_opy_ (u"ࠣࡌࡒࡆࡤࡔࡁࡎࡇࠥᣇ")),
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᣈ"): env.get(bstack11ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᣉ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠦࡈࡏࠢᣊ")) == bstack11ll1l_opy_ (u"ࠧࡺࡲࡶࡧࠥᣋ") and bstack1ll1llll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡉࡉࠣᣌ"))):
        return {
            bstack11ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᣍ"): bstack11ll1l_opy_ (u"ࠣࡅ࡬ࡶࡨࡲࡥࡄࡋࠥᣎ"),
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᣏ"): env.get(bstack11ll1l_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᣐ")),
            bstack11ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᣑ"): env.get(bstack11ll1l_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡐࡏࡃࠤᣒ")),
            bstack11ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᣓ"): env.get(bstack11ll1l_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࠥᣔ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠣࡅࡌࠦᣕ")) == bstack11ll1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᣖ") and bstack1ll1llll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࠥᣗ"))):
        return {
            bstack11ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᣘ"): bstack11ll1l_opy_ (u"࡚ࠧࡲࡢࡸ࡬ࡷࠥࡉࡉࠣᣙ"),
            bstack11ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᣚ"): env.get(bstack11ll1l_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡗࡆࡄࡢ࡙ࡗࡒࠢᣛ")),
            bstack11ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᣜ"): env.get(bstack11ll1l_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᣝ")),
            bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᣞ"): env.get(bstack11ll1l_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᣟ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠧࡉࡉࠣᣠ")) == bstack11ll1l_opy_ (u"ࠨࡴࡳࡷࡨࠦᣡ") and env.get(bstack11ll1l_opy_ (u"ࠢࡄࡋࡢࡒࡆࡓࡅࠣᣢ")) == bstack11ll1l_opy_ (u"ࠣࡥࡲࡨࡪࡹࡨࡪࡲࠥᣣ"):
        return {
            bstack11ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᣤ"): bstack11ll1l_opy_ (u"ࠥࡇࡴࡪࡥࡴࡪ࡬ࡴࠧᣥ"),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᣦ"): None,
            bstack11ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᣧ"): None,
            bstack11ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᣨ"): None
        }
    if env.get(bstack11ll1l_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆࡗࡇࡎࡄࡊࠥᣩ")) and env.get(bstack11ll1l_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡈࡕࡍࡎࡋࡗࠦᣪ")):
        return {
            bstack11ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᣫ"): bstack11ll1l_opy_ (u"ࠥࡆ࡮ࡺࡢࡶࡥ࡮ࡩࡹࠨᣬ"),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᣭ"): env.get(bstack11ll1l_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡉࡌࡘࡤࡎࡔࡕࡒࡢࡓࡗࡏࡇࡊࡐࠥᣮ")),
            bstack11ll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᣯ"): None,
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᣰ"): env.get(bstack11ll1l_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᣱ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠤࡆࡍࠧᣲ")) == bstack11ll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᣳ") and bstack1ll1llll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠦࡉࡘࡏࡏࡇࠥᣴ"))):
        return {
            bstack11ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᣵ"): bstack11ll1l_opy_ (u"ࠨࡄࡳࡱࡱࡩࠧ᣶"),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᣷"): env.get(bstack11ll1l_opy_ (u"ࠣࡆࡕࡓࡓࡋ࡟ࡃࡗࡌࡐࡉࡥࡌࡊࡐࡎࠦ᣸")),
            bstack11ll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᣹"): None,
            bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᣺"): env.get(bstack11ll1l_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤ᣻"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠧࡉࡉࠣ᣼")) == bstack11ll1l_opy_ (u"ࠨࡴࡳࡷࡨࠦ᣽") and bstack1ll1llll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࠥ᣾"))):
        return {
            bstack11ll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨ᣿"): bstack11ll1l_opy_ (u"ࠤࡖࡩࡲࡧࡰࡩࡱࡵࡩࠧᤀ"),
            bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᤁ"): env.get(bstack11ll1l_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡐࡔࡊࡅࡓࡏ࡚ࡂࡖࡌࡓࡓࡥࡕࡓࡎࠥᤂ")),
            bstack11ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᤃ"): env.get(bstack11ll1l_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᤄ")),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᤅ"): env.get(bstack11ll1l_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡋࡇࠦᤆ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠤࡆࡍࠧᤇ")) == bstack11ll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᤈ") and bstack1ll1llll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠦࡌࡏࡔࡍࡃࡅࡣࡈࡏࠢᤉ"))):
        return {
            bstack11ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᤊ"): bstack11ll1l_opy_ (u"ࠨࡇࡪࡶࡏࡥࡧࠨᤋ"),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᤌ"): env.get(bstack11ll1l_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡗࡕࡐࠧᤍ")),
            bstack11ll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᤎ"): env.get(bstack11ll1l_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᤏ")),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᤐ"): env.get(bstack11ll1l_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡏࡄࠣᤑ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠨࡃࡊࠤᤒ")) == bstack11ll1l_opy_ (u"ࠢࡵࡴࡸࡩࠧᤓ") and bstack1ll1llll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࠦᤔ"))):
        return {
            bstack11ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᤕ"): bstack11ll1l_opy_ (u"ࠥࡆࡺ࡯࡬ࡥ࡭࡬ࡸࡪࠨᤖ"),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᤗ"): env.get(bstack11ll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᤘ")),
            bstack11ll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᤙ"): env.get(bstack11ll1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡐࡆࡈࡅࡍࠤᤚ")) or env.get(bstack11ll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡎࡂࡏࡈࠦᤛ")),
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᤜ"): env.get(bstack11ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᤝ"))
        }
    if bstack1ll1llll11_opy_(env.get(bstack11ll1l_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨᤞ"))):
        return {
            bstack11ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᤟"): bstack11ll1l_opy_ (u"ࠨࡖࡪࡵࡸࡥࡱࠦࡓࡵࡷࡧ࡭ࡴࠦࡔࡦࡣࡰࠤࡘ࡫ࡲࡷ࡫ࡦࡩࡸࠨᤠ"),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᤡ"): bstack11ll1l_opy_ (u"ࠣࡽࢀࡿࢂࠨᤢ").format(env.get(bstack11ll1l_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬᤣ")), env.get(bstack11ll1l_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࡊࡆࠪᤤ"))),
            bstack11ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᤥ"): env.get(bstack11ll1l_opy_ (u"࡙࡙ࠧࡔࡖࡈࡑࡤࡊࡅࡇࡋࡑࡍ࡙ࡏࡏࡏࡋࡇࠦᤦ")),
            bstack11ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᤧ"): env.get(bstack11ll1l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢᤨ"))
        }
    if bstack1ll1llll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࠥᤩ"))):
        return {
            bstack11ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᤪ"): bstack11ll1l_opy_ (u"ࠥࡅࡵࡶࡶࡦࡻࡲࡶࠧᤫ"),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᤬"): bstack11ll1l_opy_ (u"ࠧࢁࡽ࠰ࡲࡵࡳ࡯࡫ࡣࡵ࠱ࡾࢁ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠦ᤭").format(env.get(bstack11ll1l_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡗࡕࡐࠬ᤮")), env.get(bstack11ll1l_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡄࡇࡈࡕࡕࡏࡖࡢࡒࡆࡓࡅࠨ᤯")), env.get(bstack11ll1l_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡔࡗࡕࡊࡆࡅࡗࡣࡘࡒࡕࡈࠩᤰ")), env.get(bstack11ll1l_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭ᤱ"))),
            bstack11ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᤲ"): env.get(bstack11ll1l_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᤳ")),
            bstack11ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᤴ"): env.get(bstack11ll1l_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᤵ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠢࡂ࡜ࡘࡖࡊࡥࡈࡕࡖࡓࡣ࡚࡙ࡅࡓࡡࡄࡋࡊࡔࡔࠣᤶ")) and env.get(bstack11ll1l_opy_ (u"ࠣࡖࡉࡣࡇ࡛ࡉࡍࡆࠥᤷ")):
        return {
            bstack11ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᤸ"): bstack11ll1l_opy_ (u"ࠥࡅࡿࡻࡲࡦࠢࡆࡍ᤹ࠧ"),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᤺"): bstack11ll1l_opy_ (u"ࠧࢁࡽࡼࡿ࠲ࡣࡧࡻࡩ࡭ࡦ࠲ࡶࡪࡹࡵ࡭ࡶࡶࡃࡧࡻࡩ࡭ࡦࡌࡨࡂࢁࡽ᤻ࠣ").format(env.get(bstack11ll1l_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡊࡔ࡛ࡎࡅࡃࡗࡍࡔࡔࡓࡆࡔ࡙ࡉࡗ࡛ࡒࡊࠩ᤼")), env.get(bstack11ll1l_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡕࡘࡏࡋࡇࡆࡘࠬ᤽")), env.get(bstack11ll1l_opy_ (u"ࠨࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠨ᤾"))),
            bstack11ll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᤿"): env.get(bstack11ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥ᥀")),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᥁"): env.get(bstack11ll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧ᥂"))
        }
    if any([env.get(bstack11ll1l_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦ᥃")), env.get(bstack11ll1l_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡖࡊ࡙ࡏࡍࡘࡈࡈࡤ࡙ࡏࡖࡔࡆࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࠨ᥄")), env.get(bstack11ll1l_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡘࡕࡕࡓࡅࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࠧ᥅"))]):
        return {
            bstack11ll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᥆"): bstack11ll1l_opy_ (u"ࠥࡅ࡜࡙ࠠࡄࡱࡧࡩࡇࡻࡩ࡭ࡦࠥ᥇"),
            bstack11ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᥈"): env.get(bstack11ll1l_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡒࡘࡆࡑࡏࡃࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦ᥉")),
            bstack11ll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᥊"): env.get(bstack11ll1l_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧ᥋")),
            bstack11ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᥌"): env.get(bstack11ll1l_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢ᥍"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡐࡸࡱࡧ࡫ࡲࠣ᥎")):
        return {
            bstack11ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᥏"): bstack11ll1l_opy_ (u"ࠧࡈࡡ࡮ࡤࡲࡳࠧᥐ"),
            bstack11ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᥑ"): env.get(bstack11ll1l_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡘࡥࡴࡷ࡯ࡸࡸ࡛ࡲ࡭ࠤᥒ")),
            bstack11ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᥓ"): env.get(bstack11ll1l_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡶ࡬ࡴࡸࡴࡋࡱࡥࡒࡦࡳࡥࠣᥔ")),
            bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᥕ"): env.get(bstack11ll1l_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡑࡹࡲࡨࡥࡳࠤᥖ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࠨᥗ")) or env.get(bstack11ll1l_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣᥘ")):
        return {
            bstack11ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᥙ"): bstack11ll1l_opy_ (u"࡙ࠣࡨࡶࡨࡱࡥࡳࠤᥚ"),
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᥛ"): env.get(bstack11ll1l_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᥜ")),
            bstack11ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᥝ"): bstack11ll1l_opy_ (u"ࠧࡓࡡࡪࡰࠣࡔ࡮ࡶࡥ࡭࡫ࡱࡩࠧᥞ") if env.get(bstack11ll1l_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣᥟ")) else None,
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᥠ"): env.get(bstack11ll1l_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡊࡍ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᥡ"))
        }
    if any([env.get(bstack11ll1l_opy_ (u"ࠤࡊࡇࡕࡥࡐࡓࡑࡍࡉࡈ࡚ࠢᥢ")), env.get(bstack11ll1l_opy_ (u"ࠥࡋࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦᥣ")), env.get(bstack11ll1l_opy_ (u"ࠦࡌࡕࡏࡈࡎࡈࡣࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦᥤ"))]):
        return {
            bstack11ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᥥ"): bstack11ll1l_opy_ (u"ࠨࡇࡰࡱࡪࡰࡪࠦࡃ࡭ࡱࡸࡨࠧᥦ"),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᥧ"): None,
            bstack11ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᥨ"): env.get(bstack11ll1l_opy_ (u"ࠤࡓࡖࡔࡐࡅࡄࡖࡢࡍࡉࠨᥩ")),
            bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᥪ"): env.get(bstack11ll1l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᥫ"))
        }
    if env.get(bstack11ll1l_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࠣᥬ")):
        return {
            bstack11ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᥭ"): bstack11ll1l_opy_ (u"ࠢࡔࡪ࡬ࡴࡵࡧࡢ࡭ࡧࠥ᥮"),
            bstack11ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᥯"): env.get(bstack11ll1l_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᥰ")),
            bstack11ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᥱ"): bstack11ll1l_opy_ (u"ࠦࡏࡵࡢࠡࠥࡾࢁࠧᥲ").format(env.get(bstack11ll1l_opy_ (u"࡙ࠬࡈࡊࡒࡓࡅࡇࡒࡅࡠࡌࡒࡆࡤࡏࡄࠨᥳ"))) if env.get(bstack11ll1l_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡍࡓࡇࡥࡉࡅࠤᥴ")) else None,
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᥵"): env.get(bstack11ll1l_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ᥶"))
        }
    if bstack1ll1llll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠤࡑࡉ࡙ࡒࡉࡇ࡛ࠥ᥷"))):
        return {
            bstack11ll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣ᥸"): bstack11ll1l_opy_ (u"ࠦࡓ࡫ࡴ࡭࡫ࡩࡽࠧ᥹"),
            bstack11ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᥺"): env.get(bstack11ll1l_opy_ (u"ࠨࡄࡆࡒࡏࡓ࡞ࡥࡕࡓࡎࠥ᥻")),
            bstack11ll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᥼"): env.get(bstack11ll1l_opy_ (u"ࠣࡕࡌࡘࡊࡥࡎࡂࡏࡈࠦ᥽")),
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᥾"): env.get(bstack11ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧ᥿"))
        }
    if bstack1ll1llll11_opy_(env.get(bstack11ll1l_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡆࡉࡔࡊࡑࡑࡗࠧᦀ"))):
        return {
            bstack11ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᦁ"): bstack11ll1l_opy_ (u"ࠨࡇࡪࡶࡋࡹࡧࠦࡁࡤࡶ࡬ࡳࡳࡹࠢᦂ"),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᦃ"): bstack11ll1l_opy_ (u"ࠣࡽࢀ࠳ࢀࢃ࠯ࡢࡥࡷ࡭ࡴࡴࡳ࠰ࡴࡸࡲࡸ࠵ࡻࡾࠤᦄ").format(env.get(bstack11ll1l_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡖࡉࡗ࡜ࡅࡓࡡࡘࡖࡑ࠭ᦅ")), env.get(bstack11ll1l_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡖࡊࡖࡏࡔࡋࡗࡓࡗ࡟ࠧᦆ")), env.get(bstack11ll1l_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠫᦇ"))),
            bstack11ll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᦈ"): env.get(bstack11ll1l_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡗࡐࡔࡎࡊࡑࡕࡗࠣᦉ")),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᦊ"): env.get(bstack11ll1l_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠࡔࡘࡒࡤࡏࡄࠣᦋ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠤࡆࡍࠧᦌ")) == bstack11ll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᦍ") and env.get(bstack11ll1l_opy_ (u"࡛ࠦࡋࡒࡄࡇࡏࠦᦎ")) == bstack11ll1l_opy_ (u"ࠧ࠷ࠢᦏ"):
        return {
            bstack11ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᦐ"): bstack11ll1l_opy_ (u"ࠢࡗࡧࡵࡧࡪࡲࠢᦑ"),
            bstack11ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᦒ"): bstack11ll1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࡾࢁࠧᦓ").format(env.get(bstack11ll1l_opy_ (u"࡚ࠪࡊࡘࡃࡆࡎࡢ࡙ࡗࡒࠧᦔ"))),
            bstack11ll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᦕ"): None,
            bstack11ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᦖ"): None,
        }
    if env.get(bstack11ll1l_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡘࡈࡖࡘࡏࡏࡏࠤᦗ")):
        return {
            bstack11ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᦘ"): bstack11ll1l_opy_ (u"ࠣࡖࡨࡥࡲࡩࡩࡵࡻࠥᦙ"),
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᦚ"): None,
            bstack11ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᦛ"): env.get(bstack11ll1l_opy_ (u"࡙ࠦࡋࡁࡎࡅࡌࡘ࡞ࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡏࡃࡐࡉࠧᦜ")),
            bstack11ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᦝ"): env.get(bstack11ll1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᦞ"))
        }
    if any([env.get(bstack11ll1l_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࠥᦟ")), env.get(bstack11ll1l_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡚ࡘࡌࠣᦠ")), env.get(bstack11ll1l_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠢᦡ")), env.get(bstack11ll1l_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡔࡆࡃࡐࠦᦢ"))]):
        return {
            bstack11ll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᦣ"): bstack11ll1l_opy_ (u"ࠧࡉ࡯࡯ࡥࡲࡹࡷࡹࡥࠣᦤ"),
            bstack11ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᦥ"): None,
            bstack11ll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᦦ"): env.get(bstack11ll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᦧ")) or None,
            bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᦨ"): env.get(bstack11ll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᦩ"), 0)
        }
    if env.get(bstack11ll1l_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᦪ")):
        return {
            bstack11ll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᦫ"): bstack11ll1l_opy_ (u"ࠨࡇࡰࡅࡇࠦ᦬"),
            bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᦭"): None,
            bstack11ll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᦮"): env.get(bstack11ll1l_opy_ (u"ࠤࡊࡓࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢ᦯")),
            bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᦰ"): env.get(bstack11ll1l_opy_ (u"ࠦࡌࡕ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡆࡓ࡚ࡔࡔࡆࡔࠥᦱ"))
        }
    if env.get(bstack11ll1l_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᦲ")):
        return {
            bstack11ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᦳ"): bstack11ll1l_opy_ (u"ࠢࡄࡱࡧࡩࡋࡸࡥࡴࡪࠥᦴ"),
            bstack11ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᦵ"): env.get(bstack11ll1l_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᦶ")),
            bstack11ll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᦷ"): env.get(bstack11ll1l_opy_ (u"ࠦࡈࡌ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋࠢᦸ")),
            bstack11ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᦹ"): env.get(bstack11ll1l_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᦺ"))
        }
    return {bstack11ll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᦻ"): None}
def get_host_info():
    return {
        bstack11ll1l_opy_ (u"ࠣࡪࡲࡷࡹࡴࡡ࡮ࡧࠥᦼ"): platform.node(),
        bstack11ll1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦᦽ"): platform.system(),
        bstack11ll1l_opy_ (u"ࠥࡸࡾࡶࡥࠣᦾ"): platform.machine(),
        bstack11ll1l_opy_ (u"ࠦࡻ࡫ࡲࡴ࡫ࡲࡲࠧᦿ"): platform.version(),
        bstack11ll1l_opy_ (u"ࠧࡧࡲࡤࡪࠥᧀ"): platform.architecture()[0]
    }
def bstack1ll11l1l_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack11lll1111ll_opy_():
    if bstack1l1l11lll_opy_.get_property(bstack11ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧᧁ")):
        return bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᧂ")
    return bstack11ll1l_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠧᧃ")
def bstack11lllll1111_opy_(driver):
    info = {
        bstack11ll1l_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨᧄ"): driver.capabilities,
        bstack11ll1l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧᧅ"): driver.session_id,
        bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬᧆ"): driver.capabilities.get(bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᧇ"), None),
        bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᧈ"): driver.capabilities.get(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᧉ"), None),
        bstack11ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ᧊"): driver.capabilities.get(bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨ᧋"), None),
    }
    if bstack11lll1111ll_opy_() == bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ᧌"):
        if bstack11ll11ll1l_opy_():
            info[bstack11ll1l_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬ᧍")] = bstack11ll1l_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ᧎")
        elif driver.capabilities.get(bstack11ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᧏"), {}).get(bstack11ll1l_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫ᧐"), False):
            info[bstack11ll1l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩ᧑")] = bstack11ll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭᧒")
        else:
            info[bstack11ll1l_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫ᧓")] = bstack11ll1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭᧔")
    return info
def bstack11ll11ll1l_opy_():
    if bstack1l1l11lll_opy_.get_property(bstack11ll1l_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ᧕")):
        return True
    if bstack1ll1llll11_opy_(os.environ.get(bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ᧖"), None)):
        return True
    return False
def bstack1lll111l_opy_(bstack11lll1l1ll1_opy_, url, data, config):
    headers = config.get(bstack11ll1l_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ᧗"), None)
    proxies = bstack1111l11ll_opy_(config, url)
    auth = config.get(bstack11ll1l_opy_ (u"ࠨࡣࡸࡸ࡭࠭᧘"), None)
    response = requests.request(
            bstack11lll1l1ll1_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11lll111ll_opy_(bstack1l1l1l11l_opy_, size):
    bstack1llll1l1ll_opy_ = []
    while len(bstack1l1l1l11l_opy_) > size:
        bstack111ll111_opy_ = bstack1l1l1l11l_opy_[:size]
        bstack1llll1l1ll_opy_.append(bstack111ll111_opy_)
        bstack1l1l1l11l_opy_ = bstack1l1l1l11l_opy_[size:]
    bstack1llll1l1ll_opy_.append(bstack1l1l1l11l_opy_)
    return bstack1llll1l1ll_opy_
def bstack11lll1l1lll_opy_(message, bstack11lll11l1ll_opy_=False):
    os.write(1, bytes(message, bstack11ll1l_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨ᧙")))
    os.write(1, bytes(bstack11ll1l_opy_ (u"ࠪࡠࡳ࠭᧚"), bstack11ll1l_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ᧛")))
    if bstack11lll11l1ll_opy_:
        with open(bstack11ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠲ࡵ࠱࠲ࡻ࠰ࠫ᧜") + os.environ[bstack11ll1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬ᧝")] + bstack11ll1l_opy_ (u"ࠧ࠯࡮ࡲ࡫ࠬ᧞"), bstack11ll1l_opy_ (u"ࠨࡣࠪ᧟")) as f:
            f.write(message + bstack11ll1l_opy_ (u"ࠩ࡟ࡲࠬ᧠"))
def bstack1ll11ll111l_opy_():
    return os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭᧡")].lower() == bstack11ll1l_opy_ (u"ࠫࡹࡸࡵࡦࠩ᧢")
def bstack1l11l1l1ll_opy_(bstack11lll1lll1l_opy_):
    return bstack11ll1l_opy_ (u"ࠬࢁࡽ࠰ࡽࢀࠫ᧣").format(bstack1l1111l1l11_opy_, bstack11lll1lll1l_opy_)
def bstack1l1ll1111l_opy_():
    return bstack11l111ll1l_opy_().replace(tzinfo=None).isoformat() + bstack11ll1l_opy_ (u"࡚࠭ࠨ᧤")
def bstack11ll1l111ll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11ll1l_opy_ (u"࡛ࠧࠩ᧥"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11ll1l_opy_ (u"ࠨ࡜ࠪ᧦")))).total_seconds() * 1000
def bstack11llll1l1l1_opy_(timestamp):
    return bstack11ll1ll1l1l_opy_(timestamp).isoformat() + bstack11ll1l_opy_ (u"ࠩ࡝ࠫ᧧")
def bstack11ll1l11ll1_opy_(bstack1l1111111l1_opy_):
    date_format = bstack11ll1l_opy_ (u"ࠪࠩ࡞ࠫ࡭ࠦࡦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗ࠳ࠫࡦࠨ᧨")
    bstack11ll1ll1111_opy_ = datetime.datetime.strptime(bstack1l1111111l1_opy_, date_format)
    return bstack11ll1ll1111_opy_.isoformat() + bstack11ll1l_opy_ (u"ࠫ࡟࠭᧩")
def bstack11lllll11l1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ᧪")
    else:
        return bstack11ll1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭᧫")
def bstack1ll1llll11_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11ll1l_opy_ (u"ࠧࡵࡴࡸࡩࠬ᧬")
def bstack11llllll111_opy_(val):
    return val.__str__().lower() == bstack11ll1l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ᧭")
def bstack111ll1l1ll_opy_(bstack11llll1l1ll_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack11llll1l1ll_opy_ as e:
                print(bstack11ll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡿࢂࠦ࠭࠿ࠢࡾࢁ࠿ࠦࡻࡾࠤ᧮").format(func.__name__, bstack11llll1l1ll_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack11lll1lll11_opy_(bstack11ll1l11l1l_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack11ll1l11l1l_opy_(cls, *args, **kwargs)
            except bstack11llll1l1ll_opy_ as e:
                print(bstack11ll1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࢀࢃࠠ࠮ࡀࠣࡿࢂࡀࠠࡼࡿࠥ᧯").format(bstack11ll1l11l1l_opy_.__name__, bstack11llll1l1ll_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack11lll1lll11_opy_
    else:
        return decorator
def bstack11lll1ll11_opy_(bstack111l1l1ll1_opy_):
    if os.getenv(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧ᧰")) is not None:
        return bstack1ll1llll11_opy_(os.getenv(bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ᧱")))
    if bstack11ll1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ᧲") in bstack111l1l1ll1_opy_ and bstack11llllll111_opy_(bstack111l1l1ll1_opy_[bstack11ll1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᧳")]):
        return False
    if bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ᧴") in bstack111l1l1ll1_opy_ and bstack11llllll111_opy_(bstack111l1l1ll1_opy_[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᧵")]):
        return False
    return True
def bstack11ll111l11_opy_():
    try:
        from pytest_bdd import reporting
        bstack11lll11llll_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠥ᧶"), None)
        return bstack11lll11llll_opy_ is None or bstack11lll11llll_opy_ == bstack11ll1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣ᧷")
    except Exception as e:
        return False
def bstack1l1111lll_opy_(hub_url, CONFIG):
    if bstack1l11l1llll_opy_() <= version.parse(bstack11ll1l_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬ᧸")):
        if hub_url:
            return bstack11ll1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢ᧹") + hub_url + bstack11ll1l_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦ᧺")
        return bstack11l1111l_opy_
    if hub_url:
        return bstack11ll1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥ᧻") + hub_url + bstack11ll1l_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥ᧼")
    return bstack1l11l111_opy_
def bstack11lll1111l1_opy_():
    return isinstance(os.getenv(bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡐ࡚ࡍࡉࡏࠩ᧽")), str)
def bstack1llll1lll1_opy_(url):
    return urlparse(url).hostname
def bstack1l1lllll1l_opy_(hostname):
    for bstack11llll111_opy_ in bstack1l11ll1l1_opy_:
        regex = re.compile(bstack11llll111_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11lll1l1l1l_opy_(bstack11lllll11ll_opy_, file_name, logger):
    bstack1l1llll1ll_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠫࢃ࠭᧾")), bstack11lllll11ll_opy_)
    try:
        if not os.path.exists(bstack1l1llll1ll_opy_):
            os.makedirs(bstack1l1llll1ll_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠬࢄࠧ᧿")), bstack11lllll11ll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11ll1l_opy_ (u"࠭ࡷࠨᨀ")):
                pass
            with open(file_path, bstack11ll1l_opy_ (u"ࠢࡸ࠭ࠥᨁ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack111l1ll1l_opy_.format(str(e)))
def bstack11llllllll1_opy_(file_name, key, value, logger):
    file_path = bstack11lll1l1l1l_opy_(bstack11ll1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᨂ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1l1ll11l11_opy_ = json.load(open(file_path, bstack11ll1l_opy_ (u"ࠩࡵࡦࠬᨃ")))
        else:
            bstack1l1ll11l11_opy_ = {}
        bstack1l1ll11l11_opy_[key] = value
        with open(file_path, bstack11ll1l_opy_ (u"ࠥࡻ࠰ࠨᨄ")) as outfile:
            json.dump(bstack1l1ll11l11_opy_, outfile)
def bstack1111ll11_opy_(file_name, logger):
    file_path = bstack11lll1l1l1l_opy_(bstack11ll1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᨅ"), file_name, logger)
    bstack1l1ll11l11_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11ll1l_opy_ (u"ࠬࡸࠧᨆ")) as bstack1ll111l11_opy_:
            bstack1l1ll11l11_opy_ = json.load(bstack1ll111l11_opy_)
    return bstack1l1ll11l11_opy_
def bstack111l1lll1_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡪ࡮ࡲࡥ࠻ࠢࠪᨇ") + file_path + bstack11ll1l_opy_ (u"ࠧࠡࠩᨈ") + str(e))
def bstack1l11l1llll_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11ll1l_opy_ (u"ࠣ࠾ࡑࡓ࡙࡙ࡅࡕࡀࠥᨉ")
def bstack1l111l1ll_opy_(config):
    if bstack11ll1l_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᨊ") in config:
        del (config[bstack11ll1l_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᨋ")])
        return False
    if bstack1l11l1llll_opy_() < version.parse(bstack11ll1l_opy_ (u"ࠫ࠸࠴࠴࠯࠲ࠪᨌ")):
        return False
    if bstack1l11l1llll_opy_() >= version.parse(bstack11ll1l_opy_ (u"ࠬ࠺࠮࠲࠰࠸ࠫᨍ")):
        return True
    if bstack11ll1l_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ᨎ") in config and config[bstack11ll1l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᨏ")] is False:
        return False
    else:
        return True
def bstack1ll1111111_opy_(args_list, bstack11ll1lll111_opy_):
    index = -1
    for value in bstack11ll1lll111_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack11l1l1l11l_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack11l1l1l11l_opy_ = bstack11l1l1l11l_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11ll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᨐ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᨑ"), exception=exception)
    def bstack111l11ll1l_opy_(self):
        if self.result != bstack11ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᨒ"):
            return None
        if isinstance(self.exception_type, str) and bstack11ll1l_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢᨓ") in self.exception_type:
            return bstack11ll1l_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨᨔ")
        return bstack11ll1l_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢᨕ")
    def bstack11lll11ll11_opy_(self):
        if self.result != bstack11ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᨖ"):
            return None
        if self.bstack11l1l1l11l_opy_:
            return self.bstack11l1l1l11l_opy_
        return bstack11ll1ll111l_opy_(self.exception)
def bstack11ll1ll111l_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack11ll1l1llll_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack11l1ll1l_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack111lllll1_opy_(config, logger):
    try:
        import playwright
        bstack11lll1ll111_opy_ = playwright.__file__
        bstack11lllll1l11_opy_ = os.path.split(bstack11lll1ll111_opy_)
        bstack11ll1lll11l_opy_ = bstack11lllll1l11_opy_[0] + bstack11ll1l_opy_ (u"ࠨ࠱ࡧࡶ࡮ࡼࡥࡳ࠱ࡳࡥࡨࡱࡡࡨࡧ࠲ࡰ࡮ࡨ࠯ࡤ࡮࡬࠳ࡨࡲࡩ࠯࡬ࡶࠫᨗ")
        os.environ[bstack11ll1l_opy_ (u"ࠩࡊࡐࡔࡈࡁࡍࡡࡄࡋࡊࡔࡔࡠࡊࡗࡘࡕࡥࡐࡓࡑ࡛࡝ᨘࠬ")] = bstack1l11ll1l1l_opy_(config)
        with open(bstack11ll1lll11l_opy_, bstack11ll1l_opy_ (u"ࠪࡶࠬᨙ")) as f:
            bstack11ll1l1l1_opy_ = f.read()
            bstack11lll111lll_opy_ = bstack11ll1l_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠪᨚ")
            bstack11lllll1l1l_opy_ = bstack11ll1l1l1_opy_.find(bstack11lll111lll_opy_)
            if bstack11lllll1l1l_opy_ == -1:
              process = subprocess.Popen(bstack11ll1l_opy_ (u"ࠧࡴࡰ࡮ࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠤᨛ"), shell=True, cwd=bstack11lllll1l11_opy_[0])
              process.wait()
              bstack11ll1lllll1_opy_ = bstack11ll1l_opy_ (u"࠭ࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࠦࡀ࠭᨜")
              bstack11ll1l1111l_opy_ = bstack11ll1l_opy_ (u"ࠢࠣࠤࠣࡠࠧࡻࡳࡦࠢࡶࡸࡷ࡯ࡣࡵ࡞ࠥ࠿ࠥࡩ࡯࡯ࡵࡷࠤࢀࠦࡢࡰࡱࡷࡷࡹࡸࡡࡱࠢࢀࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠨࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠧࠪ࠽ࠣ࡭࡫ࠦࠨࡱࡴࡲࡧࡪࡹࡳ࠯ࡧࡱࡺ࠳ࡍࡌࡐࡄࡄࡐࡤࡇࡇࡆࡐࡗࡣࡍ࡚ࡔࡑࡡࡓࡖࡔ࡞࡙ࠪࠢࡥࡳࡴࡺࡳࡵࡴࡤࡴ࠭࠯࠻ࠡࠤࠥࠦ᨝")
              bstack1l1111111ll_opy_ = bstack11ll1l1l1_opy_.replace(bstack11ll1lllll1_opy_, bstack11ll1l1111l_opy_)
              with open(bstack11ll1lll11l_opy_, bstack11ll1l_opy_ (u"ࠨࡹࠪ᨞")) as f:
                f.write(bstack1l1111111ll_opy_)
    except Exception as e:
        logger.error(bstack11l1ll11l1_opy_.format(str(e)))
def bstack1l11111l11_opy_():
  try:
    bstack1l111111l11_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯࠲࡯ࡹ࡯࡯ࠩ᨟"))
    bstack11ll1l1l1ll_opy_ = []
    if os.path.exists(bstack1l111111l11_opy_):
      with open(bstack1l111111l11_opy_) as f:
        bstack11ll1l1l1ll_opy_ = json.load(f)
      os.remove(bstack1l111111l11_opy_)
    return bstack11ll1l1l1ll_opy_
  except:
    pass
  return []
def bstack1l1l1111l1_opy_(bstack11lll1llll_opy_):
  try:
    bstack11ll1l1l1ll_opy_ = []
    bstack1l111111l11_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰ࠳ࡰࡳࡰࡰࠪᨠ"))
    if os.path.exists(bstack1l111111l11_opy_):
      with open(bstack1l111111l11_opy_) as f:
        bstack11ll1l1l1ll_opy_ = json.load(f)
    bstack11ll1l1l1ll_opy_.append(bstack11lll1llll_opy_)
    with open(bstack1l111111l11_opy_, bstack11ll1l_opy_ (u"ࠫࡼ࠭ᨡ")) as f:
        json.dump(bstack11ll1l1l1ll_opy_, f)
  except:
    pass
def bstack1llllll1l_opy_(logger, bstack11lllllll1l_opy_ = False):
  try:
    test_name = os.environ.get(bstack11ll1l_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨᨢ"), bstack11ll1l_opy_ (u"࠭ࠧᨣ"))
    if test_name == bstack11ll1l_opy_ (u"ࠧࠨᨤ"):
        test_name = threading.current_thread().__dict__.get(bstack11ll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡃࡦࡧࡣࡹ࡫ࡳࡵࡡࡱࡥࡲ࡫ࠧᨥ"), bstack11ll1l_opy_ (u"ࠩࠪᨦ"))
    bstack11lll111l1l_opy_ = bstack11ll1l_opy_ (u"ࠪ࠰ࠥ࠭ᨧ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack11lllllll1l_opy_:
        bstack1l111l1l11_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᨨ"), bstack11ll1l_opy_ (u"ࠬ࠶ࠧᨩ"))
        bstack111lll1ll_opy_ = {bstack11ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᨪ"): test_name, bstack11ll1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᨫ"): bstack11lll111l1l_opy_, bstack11ll1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᨬ"): bstack1l111l1l11_opy_}
        bstack11lllllllll_opy_ = []
        bstack11lll1l11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡳࡴࡵࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᨭ"))
        if os.path.exists(bstack11lll1l11l1_opy_):
            with open(bstack11lll1l11l1_opy_) as f:
                bstack11lllllllll_opy_ = json.load(f)
        bstack11lllllllll_opy_.append(bstack111lll1ll_opy_)
        with open(bstack11lll1l11l1_opy_, bstack11ll1l_opy_ (u"ࠪࡻࠬᨮ")) as f:
            json.dump(bstack11lllllllll_opy_, f)
    else:
        bstack111lll1ll_opy_ = {bstack11ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᨯ"): test_name, bstack11ll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᨰ"): bstack11lll111l1l_opy_, bstack11ll1l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᨱ"): str(multiprocessing.current_process().name)}
        if bstack11ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫᨲ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack111lll1ll_opy_)
  except Exception as e:
      logger.warn(bstack11ll1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡴࡾࡺࡥࡴࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᨳ").format(e))
def bstack111l1111l_opy_(error_message, test_name, index, logger):
  try:
    bstack11lll1llll1_opy_ = []
    bstack111lll1ll_opy_ = {bstack11ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᨴ"): test_name, bstack11ll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᨵ"): error_message, bstack11ll1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᨶ"): index}
    bstack11ll1l1l111_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ᨷ"))
    if os.path.exists(bstack11ll1l1l111_opy_):
        with open(bstack11ll1l1l111_opy_) as f:
            bstack11lll1llll1_opy_ = json.load(f)
    bstack11lll1llll1_opy_.append(bstack111lll1ll_opy_)
    with open(bstack11ll1l1l111_opy_, bstack11ll1l_opy_ (u"࠭ࡷࠨᨸ")) as f:
        json.dump(bstack11lll1llll1_opy_, f)
  except Exception as e:
    logger.warn(bstack11ll1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡵࡳࡧࡵࡴࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᨹ").format(e))
def bstack1l11l111l_opy_(bstack11lllll111_opy_, name, logger):
  try:
    bstack111lll1ll_opy_ = {bstack11ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᨺ"): name, bstack11ll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᨻ"): bstack11lllll111_opy_, bstack11ll1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᨼ"): str(threading.current_thread()._name)}
    return bstack111lll1ll_opy_
  except Exception as e:
    logger.warn(bstack11ll1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡢࡦࡪࡤࡺࡪࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣᨽ").format(e))
  return
def bstack11llll111l1_opy_():
    return platform.system() == bstack11ll1l_opy_ (u"ࠬ࡝ࡩ࡯ࡦࡲࡻࡸ࠭ᨾ")
def bstack11ll1l1ll_opy_(bstack11ll1l11lll_opy_, config, logger):
    bstack11llll1ll11_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack11ll1l11lll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡱࡺࡥࡳࠢࡦࡳࡳ࡬ࡩࡨࠢ࡮ࡩࡾࡹࠠࡣࡻࠣࡶࡪ࡭ࡥࡹࠢࡰࡥࡹࡩࡨ࠻ࠢࡾࢁࠧᨿ").format(e))
    return bstack11llll1ll11_opy_
def bstack11ll1ll11ll_opy_(bstack11lll1ll11l_opy_, bstack11llll1lll1_opy_):
    bstack11lll11ll1l_opy_ = version.parse(bstack11lll1ll11l_opy_)
    bstack11ll1l1ll11_opy_ = version.parse(bstack11llll1lll1_opy_)
    if bstack11lll11ll1l_opy_ > bstack11ll1l1ll11_opy_:
        return 1
    elif bstack11lll11ll1l_opy_ < bstack11ll1l1ll11_opy_:
        return -1
    else:
        return 0
def bstack11l111ll1l_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack11ll1ll1l1l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack11ll1ll1lll_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1lll1l111_opy_(options, framework, bstack1l1l11ll1_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11ll1l_opy_ (u"ࠧࡨࡧࡷࠫᩀ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1l1111l11l_opy_ = caps.get(bstack11ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᩁ"))
    bstack1l11111111l_opy_ = True
    bstack111llll1l_opy_ = os.environ[bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᩂ")]
    if bstack11llllll111_opy_(caps.get(bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪ࡝࠳ࡄࠩᩃ"))) or bstack11llllll111_opy_(caps.get(bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫࡟ࡸ࠵ࡦࠫᩄ"))):
        bstack1l11111111l_opy_ = False
    if bstack1l111l1ll_opy_({bstack11ll1l_opy_ (u"ࠧࡻࡳࡦ࡙࠶ࡇࠧᩅ"): bstack1l11111111l_opy_}):
        bstack1l1111l11l_opy_ = bstack1l1111l11l_opy_ or {}
        bstack1l1111l11l_opy_[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᩆ")] = bstack11ll1ll1lll_opy_(framework)
        bstack1l1111l11l_opy_[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᩇ")] = bstack1ll11ll111l_opy_()
        bstack1l1111l11l_opy_[bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫᩈ")] = bstack111llll1l_opy_
        bstack1l1111l11l_opy_[bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫᩉ")] = bstack1l1l11ll1_opy_
        if getattr(options, bstack11ll1l_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫᩊ"), None):
            options.set_capability(bstack11ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᩋ"), bstack1l1111l11l_opy_)
        else:
            options[bstack11ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᩌ")] = bstack1l1111l11l_opy_
    else:
        if getattr(options, bstack11ll1l_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧᩍ"), None):
            options.set_capability(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᩎ"), bstack11ll1ll1lll_opy_(framework))
            options.set_capability(bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᩏ"), bstack1ll11ll111l_opy_())
            options.set_capability(bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫᩐ"), bstack111llll1l_opy_)
            options.set_capability(bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫᩑ"), bstack1l1l11ll1_opy_)
        else:
            options[bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬᩒ")] = bstack11ll1ll1lll_opy_(framework)
            options[bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᩓ")] = bstack1ll11ll111l_opy_()
            options[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨᩔ")] = bstack111llll1l_opy_
            options[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨᩕ")] = bstack1l1l11ll1_opy_
    return options
def bstack11lll11111l_opy_(bstack11llllll1l1_opy_, framework):
    bstack1l1l11ll1_opy_ = bstack1l1l11lll_opy_.get_property(bstack11ll1l_opy_ (u"ࠣࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡖࡒࡐࡆࡘࡇ࡙ࡥࡍࡂࡒࠥᩖ"))
    if bstack11llllll1l1_opy_ and len(bstack11llllll1l1_opy_.split(bstack11ll1l_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨᩗ"))) > 1:
        ws_url = bstack11llllll1l1_opy_.split(bstack11ll1l_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩᩘ"))[0]
        if bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧᩙ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack11lll1l111l_opy_ = json.loads(urllib.parse.unquote(bstack11llllll1l1_opy_.split(bstack11ll1l_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᩚ"))[1]))
            bstack11lll1l111l_opy_ = bstack11lll1l111l_opy_ or {}
            bstack111llll1l_opy_ = os.environ[bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᩛ")]
            bstack11lll1l111l_opy_[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᩜ")] = str(framework) + str(__version__)
            bstack11lll1l111l_opy_[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᩝ")] = bstack1ll11ll111l_opy_()
            bstack11lll1l111l_opy_[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫᩞ")] = bstack111llll1l_opy_
            bstack11lll1l111l_opy_[bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫ᩟")] = bstack1l1l11ll1_opy_
            bstack11llllll1l1_opy_ = bstack11llllll1l1_opy_.split(bstack11ll1l_opy_ (u"ࠫࡨࡧࡰࡴ࠿᩠ࠪ"))[0] + bstack11ll1l_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᩡ") + urllib.parse.quote(json.dumps(bstack11lll1l111l_opy_))
    return bstack11llllll1l1_opy_
def bstack1ll111111l_opy_():
    global bstack1ll11l1ll_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1ll11l1ll_opy_ = BrowserType.connect
    return bstack1ll11l1ll_opy_
def bstack1l11l11l1_opy_(framework_name):
    global bstack1lll1l1ll_opy_
    bstack1lll1l1ll_opy_ = framework_name
    return framework_name
def bstack1lll1lllll_opy_(self, *args, **kwargs):
    global bstack1ll11l1ll_opy_
    try:
        global bstack1lll1l1ll_opy_
        if bstack11ll1l_opy_ (u"࠭ࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶࠪᩢ") in kwargs:
            kwargs[bstack11ll1l_opy_ (u"ࠧࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷࠫᩣ")] = bstack11lll11111l_opy_(
                kwargs.get(bstack11ll1l_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬᩤ"), None),
                bstack1lll1l1ll_opy_
            )
    except Exception as e:
        logger.error(bstack11ll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫ࡩࡳࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡗࡉࡑࠠࡤࡣࡳࡷ࠿ࠦࡻࡾࠤᩥ").format(str(e)))
    return bstack1ll11l1ll_opy_(self, *args, **kwargs)
def bstack11llll11ll1_opy_(bstack11lll11l111_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1111l11ll_opy_(bstack11lll11l111_opy_, bstack11ll1l_opy_ (u"ࠥࠦᩦ"))
        if proxies and proxies.get(bstack11ll1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥᩧ")):
            parsed_url = urlparse(proxies.get(bstack11ll1l_opy_ (u"ࠧ࡮ࡴࡵࡲࡶࠦᩨ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11ll1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡍࡵࡳࡵࠩᩩ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11ll1l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖ࡯ࡳࡶࠪᩪ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11ll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫᩫ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11ll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬᩬ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1l111111ll_opy_(bstack11lll11l111_opy_):
    bstack11llll1l11l_opy_ = {
        bstack1l111l11ll1_opy_[bstack11ll1ll11l1_opy_]: bstack11lll11l111_opy_[bstack11ll1ll11l1_opy_]
        for bstack11ll1ll11l1_opy_ in bstack11lll11l111_opy_
        if bstack11ll1ll11l1_opy_ in bstack1l111l11ll1_opy_
    }
    bstack11llll1l11l_opy_[bstack11ll1l_opy_ (u"ࠥࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠥᩭ")] = bstack11llll11ll1_opy_(bstack11lll11l111_opy_, bstack1l1l11lll_opy_.get_property(bstack11ll1l_opy_ (u"ࠦࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠦᩮ")))
    bstack11lll111l11_opy_ = [element.lower() for element in bstack1l11111l1ll_opy_]
    bstack11llll1llll_opy_(bstack11llll1l11l_opy_, bstack11lll111l11_opy_)
    return bstack11llll1l11l_opy_
def bstack11llll1llll_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11ll1l_opy_ (u"ࠧ࠰ࠪࠫࠬࠥᩯ")
    for value in d.values():
        if isinstance(value, dict):
            bstack11llll1llll_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack11llll1llll_opy_(item, keys)
def bstack11lll1l1111_opy_():
    bstack11ll1ll1l11_opy_ = [os.environ.get(bstack11ll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡉࡍࡇࡖࡣࡉࡏࡒࠣᩰ")), os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠢࡿࠤᩱ")), bstack11ll1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᩲ")), os.path.join(bstack11ll1l_opy_ (u"ࠩ࠲ࡸࡲࡶࠧᩳ"), bstack11ll1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᩴ"))]
    for path in bstack11ll1ll1l11_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11ll1l_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࠪࠦ᩵") + str(path) + bstack11ll1l_opy_ (u"ࠧ࠭ࠠࡦࡺ࡬ࡷࡹࡹ࠮ࠣ᩶"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11ll1l_opy_ (u"ࠨࡇࡪࡸ࡬ࡲ࡬ࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰࡶࠤ࡫ࡵࡲࠡࠩࠥ᩷") + str(path) + bstack11ll1l_opy_ (u"ࠢࠨࠤ᩸"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11ll1l_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࠧࠣ᩹") + str(path) + bstack11ll1l_opy_ (u"ࠤࠪࠤࡦࡲࡲࡦࡣࡧࡽࠥ࡮ࡡࡴࠢࡷ࡬ࡪࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡤࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸ࠴ࠢ᩺"))
            else:
                logger.debug(bstack11ll1l_opy_ (u"ࠥࡇࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧࠣࠫࠧ᩻") + str(path) + bstack11ll1l_opy_ (u"ࠦࠬࠦࡷࡪࡶ࡫ࠤࡼࡸࡩࡵࡧࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴ࠮ࠣ᩼"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11ll1l_opy_ (u"ࠧࡕࡰࡦࡴࡤࡸ࡮ࡵ࡮ࠡࡵࡸࡧࡨ࡫ࡥࡥࡧࡧࠤ࡫ࡵࡲࠡࠩࠥ᩽") + str(path) + bstack11ll1l_opy_ (u"ࠨࠧ࠯ࠤ᩾"))
            return path
        except Exception as e:
            logger.debug(bstack11ll1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡶࡲࠣࡪ࡮ࡲࡥࠡࠩࡾࡴࡦࡺࡨࡾࠩ࠽ࠤ᩿ࠧ") + str(e) + bstack11ll1l_opy_ (u"ࠣࠤ᪀"))
    logger.debug(bstack11ll1l_opy_ (u"ࠤࡄࡰࡱࠦࡰࡢࡶ࡫ࡷࠥ࡬ࡡࡪ࡮ࡨࡨ࠳ࠨ᪁"))
    return None
@measure(event_name=EVENTS.bstack1l1111lll1l_opy_, stage=STAGE.bstack1111l111_opy_)
def bstack1lll11lll1l_opy_(binary_path, bstack1lllll1l1l1_opy_, bs_config):
    logger.debug(bstack11ll1l_opy_ (u"ࠥࡇࡺࡸࡲࡦࡰࡷࠤࡈࡒࡉࠡࡒࡤࡸ࡭ࠦࡦࡰࡷࡱࡨ࠿ࠦࡻࡾࠤ᪂").format(binary_path))
    bstack11llllll11l_opy_ = bstack11ll1l_opy_ (u"ࠫࠬ᪃")
    bstack11lll1l11ll_opy_ = {
        bstack11ll1l_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ᪄"): __version__,
        bstack11ll1l_opy_ (u"ࠨ࡯ࡴࠤ᪅"): platform.system(),
        bstack11ll1l_opy_ (u"ࠢࡰࡵࡢࡥࡷࡩࡨࠣ᪆"): platform.machine(),
        bstack11ll1l_opy_ (u"ࠣࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳࠨ᪇"): bstack11ll1l_opy_ (u"ࠩ࠳ࠫ᪈"),
        bstack11ll1l_opy_ (u"ࠥࡷࡩࡱ࡟࡭ࡣࡱ࡫ࡺࡧࡧࡦࠤ᪉"): bstack11ll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ᪊")
    }
    try:
        if binary_path:
            bstack11lll1l11ll_opy_[bstack11ll1l_opy_ (u"ࠬࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠪ᪋")] = subprocess.check_output([binary_path, bstack11ll1l_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢ᪌")]).strip().decode(bstack11ll1l_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭᪍"))
        response = requests.request(
            bstack11ll1l_opy_ (u"ࠨࡉࡈࡘࠬ᪎"),
            url=bstack1l11l1l1ll_opy_(bstack1l111l1111l_opy_),
            headers=None,
            auth=(bs_config[bstack11ll1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ᪏")], bs_config[bstack11ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭᪐")]),
            json=None,
            params=bstack11lll1l11ll_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11ll1l_opy_ (u"ࠫࡺࡸ࡬ࠨ᪑") in data.keys() and bstack11ll1l_opy_ (u"ࠬࡻࡰࡥࡣࡷࡩࡩࡥࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠫ᪒") in data.keys():
            logger.debug(bstack11ll1l_opy_ (u"ࠨࡎࡦࡧࡧࠤࡹࡵࠠࡶࡲࡧࡥࡹ࡫ࠠࡣ࡫ࡱࡥࡷࡿࠬࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡥ࡭ࡳࡧࡲࡺࠢࡹࡩࡷࡹࡩࡰࡰ࠽ࠤࢀࢃࠢ᪓").format(bstack11lll1l11ll_opy_[bstack11ll1l_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ᪔")]))
            bstack11ll1lll1ll_opy_ = bstack11lllll1lll_opy_(data[bstack11ll1l_opy_ (u"ࠨࡷࡵࡰࠬ᪕")], bstack1lllll1l1l1_opy_)
            bstack11llllll11l_opy_ = os.path.join(bstack1lllll1l1l1_opy_, bstack11ll1lll1ll_opy_)
            os.chmod(bstack11llllll11l_opy_, 0o777) # bstack11llll1l111_opy_ permission
            return bstack11llllll11l_opy_
    except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡥࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡴࡥࡸࠢࡖࡈࡐࠦࡻࡾࠤ᪖").format(e))
    return binary_path
@measure(event_name=EVENTS.bstack1l111l111ll_opy_, stage=STAGE.bstack1111l111_opy_)
def bstack11lllll1lll_opy_(bstack1l111111111_opy_, bstack11ll1llll11_opy_):
    logger.debug(bstack11ll1l_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬ࡲࡰ࡯࠽ࠤࠧ᪗") + str(bstack1l111111111_opy_) + bstack11ll1l_opy_ (u"ࠦࠧ᪘"))
    zip_path = os.path.join(bstack11ll1llll11_opy_, bstack11ll1l_opy_ (u"ࠧࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࡡࡩ࡭ࡱ࡫࠮ࡻ࡫ࡳࠦ᪙"))
    bstack11ll1lll1ll_opy_ = bstack11ll1l_opy_ (u"࠭ࠧ᪚")
    with requests.get(bstack1l111111111_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11ll1l_opy_ (u"ࠢࡸࡤࠥ᪛")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11ll1l_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡦࡦࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠥ᪜"))
    with zipfile.ZipFile(zip_path, bstack11ll1l_opy_ (u"ࠩࡵࠫ᪝")) as zip_ref:
        bstack11lll111111_opy_ = zip_ref.namelist()
        if len(bstack11lll111111_opy_) > 0:
            bstack11ll1lll1ll_opy_ = bstack11lll111111_opy_[0] # bstack11lllllll11_opy_ bstack1l11111l111_opy_ will be bstack11lll1ll1l1_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack11ll1llll11_opy_)
        logger.debug(bstack11ll1l_opy_ (u"ࠥࡊ࡮ࡲࡥࡴࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡧࡻࡸࡷࡧࡣࡵࡧࡧࠤࡹࡵࠠࠨࠤ᪞") + str(bstack11ll1llll11_opy_) + bstack11ll1l_opy_ (u"ࠦࠬࠨ᪟"))
    os.remove(zip_path)
    return bstack11ll1lll1ll_opy_
def get_cli_dir():
    bstack11llllll1ll_opy_ = bstack11lll1l1111_opy_()
    if bstack11llllll1ll_opy_:
        bstack1lllll1l1l1_opy_ = os.path.join(bstack11llllll1ll_opy_, bstack11ll1l_opy_ (u"ࠧࡩ࡬ࡪࠤ᪠"))
        if not os.path.exists(bstack1lllll1l1l1_opy_):
            os.makedirs(bstack1lllll1l1l1_opy_, mode=0o777, exist_ok=True)
        return bstack1lllll1l1l1_opy_
    else:
        raise FileNotFoundError(bstack11ll1l_opy_ (u"ࠨࡎࡰࠢࡺࡶ࡮ࡺࡡࡣ࡮ࡨࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡪࡴࡸࠠࡵࡪࡨࠤࡘࡊࡋࠡࡤ࡬ࡲࡦࡸࡹ࠯ࠤ᪡"))
def bstack1llllll1ll1_opy_(bstack1lllll1l1l1_opy_):
    bstack11ll1l_opy_ (u"ࠢࠣࠤࡊࡩࡹࠦࡴࡩࡧࠣࡴࡦࡺࡨࠡࡨࡲࡶࠥࡺࡨࡦࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡯࡮ࠡࡣࠣࡻࡷ࡯ࡴࡢࡤ࡯ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹ࠯ࠤࠥࠦ᪢")
    bstack11lll1lllll_opy_ = [
        os.path.join(bstack1lllll1l1l1_opy_, f)
        for f in os.listdir(bstack1lllll1l1l1_opy_)
        if os.path.isfile(os.path.join(bstack1lllll1l1l1_opy_, f)) and f.startswith(bstack11ll1l_opy_ (u"ࠣࡤ࡬ࡲࡦࡸࡹ࠮ࠤ᪣"))
    ]
    if len(bstack11lll1lllll_opy_) > 0:
        return max(bstack11lll1lllll_opy_, key=os.path.getmtime) # get bstack11ll1l111l1_opy_ binary
    return bstack11ll1l_opy_ (u"ࠤࠥ᪤")