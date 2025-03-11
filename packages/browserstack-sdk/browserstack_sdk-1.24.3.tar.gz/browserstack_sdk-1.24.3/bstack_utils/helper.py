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
from bstack_utils.constants import (bstack1l111111lll_opy_, bstack1l11l1l1l_opy_, bstack11llllll1_opy_, bstack11l11lll_opy_,
                                    bstack1l1111l11ll_opy_, bstack11llllll1l1_opy_, bstack11llllll11l_opy_, bstack11lllll1l1l_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1l1lllll_opy_, bstack11l1ll111l_opy_
from bstack_utils.proxy import bstack1lll1l11ll_opy_, bstack1ll111lll_opy_
from bstack_utils.constants import *
from bstack_utils import bstack111l11ll_opy_
from browserstack_sdk._version import __version__
bstack11lll111l1_opy_ = Config.bstack1ll1ll1l1l_opy_()
logger = bstack111l11ll_opy_.get_logger(__name__, bstack111l11ll_opy_.bstack111111111l_opy_())
def bstack1l111llllll_opy_(config):
    return config[bstack11lll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᣉ")]
def bstack1l111ll11ll_opy_(config):
    return config[bstack11lll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᣊ")]
def bstack1lll1l1l1l_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack11llll11l11_opy_(obj):
    values = []
    bstack11ll1ll111l_opy_ = re.compile(bstack11lll_opy_ (u"ࡷࠨ࡞ࡄࡗࡖࡘࡔࡓ࡟ࡕࡃࡊࡣࡡࡪࠫࠥࠤᣋ"), re.I)
    for key in obj.keys():
        if bstack11ll1ll111l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack11ll11l1l11_opy_(config):
    tags = []
    tags.extend(bstack11llll11l11_opy_(os.environ))
    tags.extend(bstack11llll11l11_opy_(config))
    return tags
def bstack11lll1l111l_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack11lll11l111_opy_(bstack11ll1l1l1ll_opy_):
    if not bstack11ll1l1l1ll_opy_:
        return bstack11lll_opy_ (u"࠭ࠧᣌ")
    return bstack11lll_opy_ (u"ࠢࡼࡿࠣࠬࢀࢃࠩࠣᣍ").format(bstack11ll1l1l1ll_opy_.name, bstack11ll1l1l1ll_opy_.email)
def bstack1l111lll1ll_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack11lllll11l1_opy_ = repo.common_dir
        info = {
            bstack11lll_opy_ (u"ࠣࡵ࡫ࡥࠧᣎ"): repo.head.commit.hexsha,
            bstack11lll_opy_ (u"ࠤࡶ࡬ࡴࡸࡴࡠࡵ࡫ࡥࠧᣏ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11lll_opy_ (u"ࠥࡦࡷࡧ࡮ࡤࡪࠥᣐ"): repo.active_branch.name,
            bstack11lll_opy_ (u"ࠦࡹࡧࡧࠣᣑ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11lll_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࠣᣒ"): bstack11lll11l111_opy_(repo.head.commit.committer),
            bstack11lll_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡺࡥࡳࡡࡧࡥࡹ࡫ࠢᣓ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11lll_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࠢᣔ"): bstack11lll11l111_opy_(repo.head.commit.author),
            bstack11lll_opy_ (u"ࠣࡣࡸࡸ࡭ࡵࡲࡠࡦࡤࡸࡪࠨᣕ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11lll_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥᣖ"): repo.head.commit.message,
            bstack11lll_opy_ (u"ࠥࡶࡴࡵࡴࠣᣗ"): repo.git.rev_parse(bstack11lll_opy_ (u"ࠦ࠲࠳ࡳࡩࡱࡺ࠱ࡹࡵࡰ࡭ࡧࡹࡩࡱࠨᣘ")),
            bstack11lll_opy_ (u"ࠧࡩ࡯࡮࡯ࡲࡲࡤ࡭ࡩࡵࡡࡧ࡭ࡷࠨᣙ"): bstack11lllll11l1_opy_,
            bstack11lll_opy_ (u"ࠨࡷࡰࡴ࡮ࡸࡷ࡫ࡥࡠࡩ࡬ࡸࡤࡪࡩࡳࠤᣚ"): subprocess.check_output([bstack11lll_opy_ (u"ࠢࡨ࡫ࡷࠦᣛ"), bstack11lll_opy_ (u"ࠣࡴࡨࡺ࠲ࡶࡡࡳࡵࡨࠦᣜ"), bstack11lll_opy_ (u"ࠤ࠰࠱࡬࡯ࡴ࠮ࡥࡲࡱࡲࡵ࡮࠮ࡦ࡬ࡶࠧᣝ")]).strip().decode(
                bstack11lll_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᣞ")),
            bstack11lll_opy_ (u"ࠦࡱࡧࡳࡵࡡࡷࡥ࡬ࠨᣟ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11lll_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡸࡥࡳࡪࡰࡦࡩࡤࡲࡡࡴࡶࡢࡸࡦ࡭ࠢᣠ"): repo.git.rev_list(
                bstack11lll_opy_ (u"ࠨࡻࡾ࠰࠱ࡿࢂࠨᣡ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack11lll1111ll_opy_ = []
        for remote in remotes:
            bstack11lll1l1lll_opy_ = {
                bstack11lll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᣢ"): remote.name,
                bstack11lll_opy_ (u"ࠣࡷࡵࡰࠧᣣ"): remote.url,
            }
            bstack11lll1111ll_opy_.append(bstack11lll1l1lll_opy_)
        bstack11lll111l11_opy_ = {
            bstack11lll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᣤ"): bstack11lll_opy_ (u"ࠥ࡫࡮ࡺࠢᣥ"),
            **info,
            bstack11lll_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨࡷࠧᣦ"): bstack11lll1111ll_opy_
        }
        bstack11lll111l11_opy_ = bstack11llll1l1ll_opy_(bstack11lll111l11_opy_)
        return bstack11lll111l11_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11lll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡵࡰࡶ࡮ࡤࡸ࡮ࡴࡧࠡࡉ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᣧ").format(err))
        return {}
def bstack11llll1l1ll_opy_(bstack11lll111l11_opy_):
    bstack11ll11l1l1l_opy_ = bstack11lll1lllll_opy_(bstack11lll111l11_opy_)
    if bstack11ll11l1l1l_opy_ and bstack11ll11l1l1l_opy_ > bstack1l1111l11ll_opy_:
        bstack11lll1l1ll1_opy_ = bstack11ll11l1l1l_opy_ - bstack1l1111l11ll_opy_
        bstack11ll11ll11l_opy_ = bstack11llll1111l_opy_(bstack11lll111l11_opy_[bstack11lll_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢᣨ")], bstack11lll1l1ll1_opy_)
        bstack11lll111l11_opy_[bstack11lll_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣᣩ")] = bstack11ll11ll11l_opy_
        logger.info(bstack11lll_opy_ (u"ࠣࡖ࡫ࡩࠥࡩ࡯࡮࡯࡬ࡸࠥ࡮ࡡࡴࠢࡥࡩࡪࡴࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦ࠱ࠤࡘ࡯ࡺࡦࠢࡲࡪࠥࡩ࡯࡮࡯࡬ࡸࠥࡧࡦࡵࡧࡵࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࢀࢃࠠࡌࡄࠥᣪ")
                    .format(bstack11lll1lllll_opy_(bstack11lll111l11_opy_) / 1024))
    return bstack11lll111l11_opy_
def bstack11lll1lllll_opy_(bstack1l1l1lll1_opy_):
    try:
        if bstack1l1l1lll1_opy_:
            bstack11ll11l111l_opy_ = json.dumps(bstack1l1l1lll1_opy_)
            bstack11ll11lllll_opy_ = sys.getsizeof(bstack11ll11l111l_opy_)
            return bstack11ll11lllll_opy_
    except Exception as e:
        logger.debug(bstack11lll_opy_ (u"ࠤࡖࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡥࡤࡰࡨࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡳࡪࡼࡨࠤࡴ࡬ࠠࡋࡕࡒࡒࠥࡵࡢ࡫ࡧࡦࡸ࠿ࠦࡻࡾࠤᣫ").format(e))
    return -1
def bstack11llll1111l_opy_(field, bstack11ll1ll11l1_opy_):
    try:
        bstack11ll1l1ll11_opy_ = len(bytes(bstack11llllll1l1_opy_, bstack11lll_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᣬ")))
        bstack11ll11llll1_opy_ = bytes(field, bstack11lll_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᣭ"))
        bstack11llll1llll_opy_ = len(bstack11ll11llll1_opy_)
        bstack11ll1l11l11_opy_ = ceil(bstack11llll1llll_opy_ - bstack11ll1ll11l1_opy_ - bstack11ll1l1ll11_opy_)
        if bstack11ll1l11l11_opy_ > 0:
            bstack11ll11ll1l1_opy_ = bstack11ll11llll1_opy_[:bstack11ll1l11l11_opy_].decode(bstack11lll_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᣮ"), errors=bstack11lll_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪ࠭ᣯ")) + bstack11llllll1l1_opy_
            return bstack11ll11ll1l1_opy_
    except Exception as e:
        logger.debug(bstack11lll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡺࡲࡶࡰࡦࡥࡹ࡯࡮ࡨࠢࡩ࡭ࡪࡲࡤ࠭ࠢࡱࡳࡹ࡮ࡩ࡯ࡩࠣࡻࡦࡹࠠࡵࡴࡸࡲࡨࡧࡴࡦࡦࠣ࡬ࡪࡸࡥ࠻ࠢࡾࢁࠧᣰ").format(e))
    return field
def bstack1l1ll1l11l_opy_():
    env = os.environ
    if (bstack11lll_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨᣱ") in env and len(env[bstack11lll_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢᣲ")]) > 0) or (
            bstack11lll_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤᣳ") in env and len(env[bstack11lll_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥᣴ")]) > 0):
        return {
            bstack11lll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᣵ"): bstack11lll_opy_ (u"ࠨࡊࡦࡰ࡮࡭ࡳࡹࠢ᣶"),
            bstack11lll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᣷"): env.get(bstack11lll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦ᣸")),
            bstack11lll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᣹"): env.get(bstack11lll_opy_ (u"ࠥࡎࡔࡈ࡟ࡏࡃࡐࡉࠧ᣺")),
            bstack11lll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᣻"): env.get(bstack11lll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ᣼"))
        }
    if env.get(bstack11lll_opy_ (u"ࠨࡃࡊࠤ᣽")) == bstack11lll_opy_ (u"ࠢࡵࡴࡸࡩࠧ᣾") and bstack1l1ll1llll_opy_(env.get(bstack11lll_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡄࡋࠥ᣿"))):
        return {
            bstack11lll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᤀ"): bstack11lll_opy_ (u"ࠥࡇ࡮ࡸࡣ࡭ࡧࡆࡍࠧᤁ"),
            bstack11lll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᤂ"): env.get(bstack11lll_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᤃ")),
            bstack11lll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᤄ"): env.get(bstack11lll_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡋࡑࡅࠦᤅ")),
            bstack11lll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᤆ"): env.get(bstack11lll_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࠧᤇ"))
        }
    if env.get(bstack11lll_opy_ (u"ࠥࡇࡎࠨᤈ")) == bstack11lll_opy_ (u"ࠦࡹࡸࡵࡦࠤᤉ") and bstack1l1ll1llll_opy_(env.get(bstack11lll_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࠧᤊ"))):
        return {
            bstack11lll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᤋ"): bstack11lll_opy_ (u"ࠢࡕࡴࡤࡺ࡮ࡹࠠࡄࡋࠥᤌ"),
            bstack11lll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᤍ"): env.get(bstack11lll_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠ࡙ࡈࡆࡤ࡛ࡒࡍࠤᤎ")),
            bstack11lll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᤏ"): env.get(bstack11lll_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᤐ")),
            bstack11lll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᤑ"): env.get(bstack11lll_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᤒ"))
        }
    if env.get(bstack11lll_opy_ (u"ࠢࡄࡋࠥᤓ")) == bstack11lll_opy_ (u"ࠣࡶࡵࡹࡪࠨᤔ") and env.get(bstack11lll_opy_ (u"ࠤࡆࡍࡤࡔࡁࡎࡇࠥᤕ")) == bstack11lll_opy_ (u"ࠥࡧࡴࡪࡥࡴࡪ࡬ࡴࠧᤖ"):
        return {
            bstack11lll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᤗ"): bstack11lll_opy_ (u"ࠧࡉ࡯ࡥࡧࡶ࡬࡮ࡶࠢᤘ"),
            bstack11lll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᤙ"): None,
            bstack11lll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᤚ"): None,
            bstack11lll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᤛ"): None
        }
    if env.get(bstack11lll_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠧᤜ")) and env.get(bstack11lll_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᤝ")):
        return {
            bstack11lll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᤞ"): bstack11lll_opy_ (u"ࠧࡈࡩࡵࡤࡸࡧࡰ࡫ࡴࠣ᤟"),
            bstack11lll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᤠ"): env.get(bstack11lll_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡋࡎ࡚࡟ࡉࡖࡗࡔࡤࡕࡒࡊࡉࡌࡒࠧᤡ")),
            bstack11lll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᤢ"): None,
            bstack11lll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᤣ"): env.get(bstack11lll_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᤤ"))
        }
    if env.get(bstack11lll_opy_ (u"ࠦࡈࡏࠢᤥ")) == bstack11lll_opy_ (u"ࠧࡺࡲࡶࡧࠥᤦ") and bstack1l1ll1llll_opy_(env.get(bstack11lll_opy_ (u"ࠨࡄࡓࡑࡑࡉࠧᤧ"))):
        return {
            bstack11lll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᤨ"): bstack11lll_opy_ (u"ࠣࡆࡵࡳࡳ࡫ࠢᤩ"),
            bstack11lll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᤪ"): env.get(bstack11lll_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡎࡌࡒࡐࠨᤫ")),
            bstack11lll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᤬"): None,
            bstack11lll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᤭"): env.get(bstack11lll_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ᤮"))
        }
    if env.get(bstack11lll_opy_ (u"ࠢࡄࡋࠥ᤯")) == bstack11lll_opy_ (u"ࠣࡶࡵࡹࡪࠨᤰ") and bstack1l1ll1llll_opy_(env.get(bstack11lll_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࠧᤱ"))):
        return {
            bstack11lll_opy_ (u"ࠥࡲࡦࡳࡥࠣᤲ"): bstack11lll_opy_ (u"ࠦࡘ࡫࡭ࡢࡲ࡫ࡳࡷ࡫ࠢᤳ"),
            bstack11lll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᤴ"): env.get(bstack11lll_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡒࡖࡌࡇࡎࡊ࡜ࡄࡘࡎࡕࡎࡠࡗࡕࡐࠧᤵ")),
            bstack11lll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᤶ"): env.get(bstack11lll_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᤷ")),
            bstack11lll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᤸ"): env.get(bstack11lll_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡍࡉࠨ᤹"))
        }
    if env.get(bstack11lll_opy_ (u"ࠦࡈࡏࠢ᤺")) == bstack11lll_opy_ (u"ࠧࡺࡲࡶࡧ᤻ࠥ") and bstack1l1ll1llll_opy_(env.get(bstack11lll_opy_ (u"ࠨࡇࡊࡖࡏࡅࡇࡥࡃࡊࠤ᤼"))):
        return {
            bstack11lll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᤽"): bstack11lll_opy_ (u"ࠣࡉ࡬ࡸࡑࡧࡢࠣ᤾"),
            bstack11lll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᤿"): env.get(bstack11lll_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢ࡙ࡗࡒࠢ᥀")),
            bstack11lll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᥁"): env.get(bstack11lll_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥ᥂")),
            bstack11lll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᥃"): env.get(bstack11lll_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡊࡆࠥ᥄"))
        }
    if env.get(bstack11lll_opy_ (u"ࠣࡅࡌࠦ᥅")) == bstack11lll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ᥆") and bstack1l1ll1llll_opy_(env.get(bstack11lll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࠨ᥇"))):
        return {
            bstack11lll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᥈"): bstack11lll_opy_ (u"ࠧࡈࡵࡪ࡮ࡧ࡯࡮ࡺࡥࠣ᥉"),
            bstack11lll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᥊"): env.get(bstack11lll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ᥋")),
            bstack11lll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᥌"): env.get(bstack11lll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡒࡁࡃࡇࡏࠦ᥍")) or env.get(bstack11lll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨ᥎")),
            bstack11lll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᥏"): env.get(bstack11lll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᥐ"))
        }
    if bstack1l1ll1llll_opy_(env.get(bstack11lll_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣᥑ"))):
        return {
            bstack11lll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᥒ"): bstack11lll_opy_ (u"ࠣࡘ࡬ࡷࡺࡧ࡬ࠡࡕࡷࡹࡩ࡯࡯ࠡࡖࡨࡥࡲࠦࡓࡦࡴࡹ࡭ࡨ࡫ࡳࠣᥓ"),
            bstack11lll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᥔ"): bstack11lll_opy_ (u"ࠥࡿࢂࢁࡽࠣᥕ").format(env.get(bstack11lll_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧᥖ")), env.get(bstack11lll_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࡌࡈࠬᥗ"))),
            bstack11lll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᥘ"): env.get(bstack11lll_opy_ (u"ࠢࡔ࡛ࡖࡘࡊࡓ࡟ࡅࡇࡉࡍࡓࡏࡔࡊࡑࡑࡍࡉࠨᥙ")),
            bstack11lll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᥚ"): env.get(bstack11lll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤᥛ"))
        }
    if bstack1l1ll1llll_opy_(env.get(bstack11lll_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࠧᥜ"))):
        return {
            bstack11lll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᥝ"): bstack11lll_opy_ (u"ࠧࡇࡰࡱࡸࡨࡽࡴࡸࠢᥞ"),
            bstack11lll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᥟ"): bstack11lll_opy_ (u"ࠢࡼࡿ࠲ࡴࡷࡵࡪࡦࡥࡷ࠳ࢀࢃ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠨᥠ").format(env.get(bstack11lll_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢ࡙ࡗࡒࠧᥡ")), env.get(bstack11lll_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡆࡉࡃࡐࡗࡑࡘࡤࡔࡁࡎࡇࠪᥢ")), env.get(bstack11lll_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡓࡍࡗࡊࠫᥣ")), env.get(bstack11lll_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨᥤ"))),
            bstack11lll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᥥ"): env.get(bstack11lll_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᥦ")),
            bstack11lll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᥧ"): env.get(bstack11lll_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᥨ"))
        }
    if env.get(bstack11lll_opy_ (u"ࠤࡄ࡞࡚ࡘࡅࡠࡊࡗࡘࡕࡥࡕࡔࡇࡕࡣࡆࡍࡅࡏࡖࠥᥩ")) and env.get(bstack11lll_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧᥪ")):
        return {
            bstack11lll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᥫ"): bstack11lll_opy_ (u"ࠧࡇࡺࡶࡴࡨࠤࡈࡏࠢᥬ"),
            bstack11lll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᥭ"): bstack11lll_opy_ (u"ࠢࡼࡿࡾࢁ࠴ࡥࡢࡶ࡫࡯ࡨ࠴ࡸࡥࡴࡷ࡯ࡸࡸࡅࡢࡶ࡫࡯ࡨࡎࡪ࠽ࡼࡿࠥ᥮").format(env.get(bstack11lll_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫ᥯")), env.get(bstack11lll_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࠧᥰ")), env.get(bstack11lll_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠪᥱ"))),
            bstack11lll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᥲ"): env.get(bstack11lll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧᥳ")),
            bstack11lll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᥴ"): env.get(bstack11lll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢ᥵"))
        }
    if any([env.get(bstack11lll_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨ᥶")), env.get(bstack11lll_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡘࡅࡔࡑࡏ࡚ࡊࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣ᥷")), env.get(bstack11lll_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢ᥸"))]):
        return {
            bstack11lll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᥹"): bstack11lll_opy_ (u"ࠧࡇࡗࡔࠢࡆࡳࡩ࡫ࡂࡶ࡫࡯ࡨࠧ᥺"),
            bstack11lll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᥻"): env.get(bstack11lll_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡔ࡚ࡈࡌࡊࡅࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ᥼")),
            bstack11lll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᥽"): env.get(bstack11lll_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢ᥾")),
            bstack11lll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᥿"): env.get(bstack11lll_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᦀ"))
        }
    if env.get(bstack11lll_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥᦁ")):
        return {
            bstack11lll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᦂ"): bstack11lll_opy_ (u"ࠢࡃࡣࡰࡦࡴࡵࠢᦃ"),
            bstack11lll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᦄ"): env.get(bstack11lll_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡓࡧࡶࡹࡱࡺࡳࡖࡴ࡯ࠦᦅ")),
            bstack11lll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᦆ"): env.get(bstack11lll_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡸ࡮࡯ࡳࡶࡍࡳࡧࡔࡡ࡮ࡧࠥᦇ")),
            bstack11lll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᦈ"): env.get(bstack11lll_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦᦉ"))
        }
    if env.get(bstack11lll_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࠣᦊ")) or env.get(bstack11lll_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥᦋ")):
        return {
            bstack11lll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᦌ"): bstack11lll_opy_ (u"࡛ࠥࡪࡸࡣ࡬ࡧࡵࠦᦍ"),
            bstack11lll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᦎ"): env.get(bstack11lll_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᦏ")),
            bstack11lll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᦐ"): bstack11lll_opy_ (u"ࠢࡎࡣ࡬ࡲࠥࡖࡩࡱࡧ࡯࡭ࡳ࡫ࠢᦑ") if env.get(bstack11lll_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥᦒ")) else None,
            bstack11lll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᦓ"): env.get(bstack11lll_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡌࡏࡔࡠࡅࡒࡑࡒࡏࡔࠣᦔ"))
        }
    if any([env.get(bstack11lll_opy_ (u"ࠦࡌࡉࡐࡠࡒࡕࡓࡏࡋࡃࡕࠤᦕ")), env.get(bstack11lll_opy_ (u"ࠧࡍࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨᦖ")), env.get(bstack11lll_opy_ (u"ࠨࡇࡐࡑࡊࡐࡊࡥࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨᦗ"))]):
        return {
            bstack11lll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᦘ"): bstack11lll_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡅ࡯ࡳࡺࡪࠢᦙ"),
            bstack11lll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᦚ"): None,
            bstack11lll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᦛ"): env.get(bstack11lll_opy_ (u"ࠦࡕࡘࡏࡋࡇࡆࡘࡤࡏࡄࠣᦜ")),
            bstack11lll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᦝ"): env.get(bstack11lll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣᦞ"))
        }
    if env.get(bstack11lll_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࠥᦟ")):
        return {
            bstack11lll_opy_ (u"ࠣࡰࡤࡱࡪࠨᦠ"): bstack11lll_opy_ (u"ࠤࡖ࡬࡮ࡶࡰࡢࡤ࡯ࡩࠧᦡ"),
            bstack11lll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᦢ"): env.get(bstack11lll_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᦣ")),
            bstack11lll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᦤ"): bstack11lll_opy_ (u"ࠨࡊࡰࡤࠣࠧࢀࢃࠢᦥ").format(env.get(bstack11lll_opy_ (u"ࠧࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠪᦦ"))) if env.get(bstack11lll_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠦᦧ")) else None,
            bstack11lll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᦨ"): env.get(bstack11lll_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᦩ"))
        }
    if bstack1l1ll1llll_opy_(env.get(bstack11lll_opy_ (u"ࠦࡓࡋࡔࡍࡋࡉ࡝ࠧᦪ"))):
        return {
            bstack11lll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᦫ"): bstack11lll_opy_ (u"ࠨࡎࡦࡶ࡯࡭࡫ࡿࠢ᦬"),
            bstack11lll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᦭"): env.get(bstack11lll_opy_ (u"ࠣࡆࡈࡔࡑࡕ࡙ࡠࡗࡕࡐࠧ᦮")),
            bstack11lll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᦯"): env.get(bstack11lll_opy_ (u"ࠥࡗࡎ࡚ࡅࡠࡐࡄࡑࡊࠨᦰ")),
            bstack11lll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᦱ"): env.get(bstack11lll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢᦲ"))
        }
    if bstack1l1ll1llll_opy_(env.get(bstack11lll_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡁࡄࡖࡌࡓࡓ࡙ࠢᦳ"))):
        return {
            bstack11lll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᦴ"): bstack11lll_opy_ (u"ࠣࡉ࡬ࡸࡍࡻࡢࠡࡃࡦࡸ࡮ࡵ࡮ࡴࠤᦵ"),
            bstack11lll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᦶ"): bstack11lll_opy_ (u"ࠥࡿࢂ࠵ࡻࡾ࠱ࡤࡧࡹ࡯࡯࡯ࡵ࠲ࡶࡺࡴࡳ࠰ࡽࢀࠦᦷ").format(env.get(bstack11lll_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡘࡋࡒࡗࡇࡕࡣ࡚ࡘࡌࠨᦸ")), env.get(bstack11lll_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡅࡑࡑࡖࡍ࡙ࡕࡒ࡚ࠩᦹ")), env.get(bstack11lll_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉ࠭ᦺ"))),
            bstack11lll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᦻ"): env.get(bstack11lll_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠ࡙ࡒࡖࡐࡌࡌࡐ࡙ࠥᦼ")),
            bstack11lll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᦽ"): env.get(bstack11lll_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠥᦾ"))
        }
    if env.get(bstack11lll_opy_ (u"ࠦࡈࡏࠢᦿ")) == bstack11lll_opy_ (u"ࠧࡺࡲࡶࡧࠥᧀ") and env.get(bstack11lll_opy_ (u"ࠨࡖࡆࡔࡆࡉࡑࠨᧁ")) == bstack11lll_opy_ (u"ࠢ࠲ࠤᧂ"):
        return {
            bstack11lll_opy_ (u"ࠣࡰࡤࡱࡪࠨᧃ"): bstack11lll_opy_ (u"ࠤ࡙ࡩࡷࡩࡥ࡭ࠤᧄ"),
            bstack11lll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᧅ"): bstack11lll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࢀࢃࠢᧆ").format(env.get(bstack11lll_opy_ (u"ࠬ࡜ࡅࡓࡅࡈࡐࡤ࡛ࡒࡍࠩᧇ"))),
            bstack11lll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᧈ"): None,
            bstack11lll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᧉ"): None,
        }
    if env.get(bstack11lll_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢ࡚ࡊࡘࡓࡊࡑࡑࠦ᧊")):
        return {
            bstack11lll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᧋"): bstack11lll_opy_ (u"ࠥࡘࡪࡧ࡭ࡤ࡫ࡷࡽࠧ᧌"),
            bstack11lll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᧍"): None,
            bstack11lll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᧎"): env.get(bstack11lll_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡒࡕࡓࡏࡋࡃࡕࡡࡑࡅࡒࡋࠢ᧏")),
            bstack11lll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᧐"): env.get(bstack11lll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢ᧑"))
        }
    if any([env.get(bstack11lll_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࠧ᧒")), env.get(bstack11lll_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡓࡎࠥ᧓")), env.get(bstack11lll_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠤ᧔")), env.get(bstack11lll_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡖࡈࡅࡒࠨ᧕"))]):
        return {
            bstack11lll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᧖"): bstack11lll_opy_ (u"ࠢࡄࡱࡱࡧࡴࡻࡲࡴࡧࠥ᧗"),
            bstack11lll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᧘"): None,
            bstack11lll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᧙"): env.get(bstack11lll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦ᧚")) or None,
            bstack11lll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ᧛"): env.get(bstack11lll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢ᧜"), 0)
        }
    if env.get(bstack11lll_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦ᧝")):
        return {
            bstack11lll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᧞"): bstack11lll_opy_ (u"ࠣࡉࡲࡇࡉࠨ᧟"),
            bstack11lll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᧠"): None,
            bstack11lll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᧡"): env.get(bstack11lll_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤ᧢")),
            bstack11lll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᧣"): env.get(bstack11lll_opy_ (u"ࠨࡇࡐࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡈࡕࡕࡏࡖࡈࡖࠧ᧤"))
        }
    if env.get(bstack11lll_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧ᧥")):
        return {
            bstack11lll_opy_ (u"ࠣࡰࡤࡱࡪࠨ᧦"): bstack11lll_opy_ (u"ࠤࡆࡳࡩ࡫ࡆࡳࡧࡶ࡬ࠧ᧧"),
            bstack11lll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᧨"): env.get(bstack11lll_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥ᧩")),
            bstack11lll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᧪"): env.get(bstack11lll_opy_ (u"ࠨࡃࡇࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤ᧫")),
            bstack11lll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᧬"): env.get(bstack11lll_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨ᧭"))
        }
    return {bstack11lll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᧮"): None}
def get_host_info():
    return {
        bstack11lll_opy_ (u"ࠥ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠧ᧯"): platform.node(),
        bstack11lll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨ᧰"): platform.system(),
        bstack11lll_opy_ (u"ࠧࡺࡹࡱࡧࠥ᧱"): platform.machine(),
        bstack11lll_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢ᧲"): platform.version(),
        bstack11lll_opy_ (u"ࠢࡢࡴࡦ࡬ࠧ᧳"): platform.architecture()[0]
    }
def bstack1ll1l1ll1_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack11ll11lll11_opy_():
    if bstack11lll111l1_opy_.get_property(bstack11lll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ᧴")):
        return bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ᧵")
    return bstack11lll_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠩ᧶")
def bstack11lll111lll_opy_(driver):
    info = {
        bstack11lll_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ᧷"): driver.capabilities,
        bstack11lll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩ᧸"): driver.session_id,
        bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧ᧹"): driver.capabilities.get(bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ᧺"), None),
        bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ᧻"): driver.capabilities.get(bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ᧼"), None),
        bstack11lll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬ᧽"): driver.capabilities.get(bstack11lll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪ᧾"), None),
    }
    if bstack11ll11lll11_opy_() == bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ᧿"):
        if bstack1l1l11111_opy_():
            info[bstack11lll_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧᨀ")] = bstack11lll_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᨁ")
        elif driver.capabilities.get(bstack11lll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᨂ"), {}).get(bstack11lll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ᨃ"), False):
            info[bstack11lll_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫᨄ")] = bstack11lll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᨅ")
        else:
            info[bstack11lll_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᨆ")] = bstack11lll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᨇ")
    return info
def bstack1l1l11111_opy_():
    if bstack11lll111l1_opy_.get_property(bstack11lll_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᨈ")):
        return True
    if bstack1l1ll1llll_opy_(os.environ.get(bstack11lll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩᨉ"), None)):
        return True
    return False
def bstack1l1l11l1l1_opy_(bstack11llll1l111_opy_, url, data, config):
    headers = config.get(bstack11lll_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᨊ"), None)
    proxies = bstack1lll1l11ll_opy_(config, url)
    auth = config.get(bstack11lll_opy_ (u"ࠪࡥࡺࡺࡨࠨᨋ"), None)
    response = requests.request(
            bstack11llll1l111_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l11lll111_opy_(bstack1l11ll111_opy_, size):
    bstack11ll1ll1ll_opy_ = []
    while len(bstack1l11ll111_opy_) > size:
        bstack11ll1lll1l_opy_ = bstack1l11ll111_opy_[:size]
        bstack11ll1ll1ll_opy_.append(bstack11ll1lll1l_opy_)
        bstack1l11ll111_opy_ = bstack1l11ll111_opy_[size:]
    bstack11ll1ll1ll_opy_.append(bstack1l11ll111_opy_)
    return bstack11ll1ll1ll_opy_
def bstack11ll1l1l111_opy_(message, bstack11ll11l1ll1_opy_=False):
    os.write(1, bytes(message, bstack11lll_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᨌ")))
    os.write(1, bytes(bstack11lll_opy_ (u"ࠬࡢ࡮ࠨᨍ"), bstack11lll_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᨎ")))
    if bstack11ll11l1ll1_opy_:
        with open(bstack11lll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭ࡰ࠳࠴ࡽ࠲࠭ᨏ") + os.environ[bstack11lll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᨐ")] + bstack11lll_opy_ (u"ࠩ࠱ࡰࡴ࡭ࠧᨑ"), bstack11lll_opy_ (u"ࠪࡥࠬᨒ")) as f:
            f.write(message + bstack11lll_opy_ (u"ࠫࡡࡴࠧᨓ"))
def bstack1ll1111llll_opy_():
    return os.environ[bstack11lll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᨔ")].lower() == bstack11lll_opy_ (u"࠭ࡴࡳࡷࡨࠫᨕ")
def bstack11lll1ll1_opy_(bstack11ll11l1lll_opy_):
    return bstack11lll_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭ᨖ").format(bstack1l111111lll_opy_, bstack11ll11l1lll_opy_)
def bstack11111lll1_opy_():
    return bstack11l111ll1l_opy_().replace(tzinfo=None).isoformat() + bstack11lll_opy_ (u"ࠨ࡜ࠪᨗ")
def bstack11ll1l1111l_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11lll_opy_ (u"ࠩ࡝ᨘࠫ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11lll_opy_ (u"ࠪ࡞ࠬᨙ")))).total_seconds() * 1000
def bstack11llll1ll11_opy_(timestamp):
    return bstack11llll111ll_opy_(timestamp).isoformat() + bstack11lll_opy_ (u"ࠫ࡟࠭ᨚ")
def bstack11lll1l11l1_opy_(bstack11lll11lll1_opy_):
    date_format = bstack11lll_opy_ (u"࡙ࠬࠫࠦ࡯ࠨࡨࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪ࠮ࠦࡨࠪᨛ")
    bstack11lll11llll_opy_ = datetime.datetime.strptime(bstack11lll11lll1_opy_, date_format)
    return bstack11lll11llll_opy_.isoformat() + bstack11lll_opy_ (u"࡚࠭ࠨ᨜")
def bstack11ll1l1ll1l_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11lll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ᨝")
    else:
        return bstack11lll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ᨞")
def bstack1l1ll1llll_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11lll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ᨟")
def bstack11ll1lllll1_opy_(val):
    return val.__str__().lower() == bstack11lll_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩᨠ")
def bstack11l111llll_opy_(bstack11ll11ll111_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack11ll11ll111_opy_ as e:
                print(bstack11lll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦᨡ").format(func.__name__, bstack11ll11ll111_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack11lll111ll1_opy_(bstack11lll1l1l11_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack11lll1l1l11_opy_(cls, *args, **kwargs)
            except bstack11ll11ll111_opy_ as e:
                print(bstack11lll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧᨢ").format(bstack11lll1l1l11_opy_.__name__, bstack11ll11ll111_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack11lll111ll1_opy_
    else:
        return decorator
def bstack1l1l1ll11l_opy_(bstack111l1l11l1_opy_):
    if os.getenv(bstack11lll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩᨣ")) is not None:
        return bstack1l1ll1llll_opy_(os.getenv(bstack11lll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪᨤ")))
    if bstack11lll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᨥ") in bstack111l1l11l1_opy_ and bstack11ll1lllll1_opy_(bstack111l1l11l1_opy_[bstack11lll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᨦ")]):
        return False
    if bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᨧ") in bstack111l1l11l1_opy_ and bstack11ll1lllll1_opy_(bstack111l1l11l1_opy_[bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᨨ")]):
        return False
    return True
def bstack11l111111_opy_():
    try:
        from pytest_bdd import reporting
        bstack11lll11l1l1_opy_ = os.environ.get(bstack11lll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠧᨩ"), None)
        return bstack11lll11l1l1_opy_ is None or bstack11lll11l1l1_opy_ == bstack11lll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥᨪ")
    except Exception as e:
        return False
def bstack1llll1llll_opy_(hub_url, CONFIG):
    if bstack1lll11l11_opy_() <= version.parse(bstack11lll_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧᨫ")):
        if hub_url:
            return bstack11lll_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤᨬ") + hub_url + bstack11lll_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨᨭ")
        return bstack11llllll1_opy_
    if hub_url:
        return bstack11lll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧᨮ") + hub_url + bstack11lll_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧᨯ")
    return bstack11l11lll_opy_
def bstack11lll1lll1l_opy_():
    return isinstance(os.getenv(bstack11lll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫᨰ")), str)
def bstack1lll11ll11_opy_(url):
    return urlparse(url).hostname
def bstack1l111l1l11_opy_(hostname):
    for bstack1lll1lll_opy_ in bstack1l11l1l1l_opy_:
        regex = re.compile(bstack1lll1lll_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll1ll1l1l_opy_(bstack11lll1ll111_opy_, file_name, logger):
    bstack11l1l11l_opy_ = os.path.join(os.path.expanduser(bstack11lll_opy_ (u"࠭ࡾࠨᨱ")), bstack11lll1ll111_opy_)
    try:
        if not os.path.exists(bstack11l1l11l_opy_):
            os.makedirs(bstack11l1l11l_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11lll_opy_ (u"ࠧࡿࠩᨲ")), bstack11lll1ll111_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11lll_opy_ (u"ࠨࡹࠪᨳ")):
                pass
            with open(file_path, bstack11lll_opy_ (u"ࠤࡺ࠯ࠧᨴ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1l1lllll_opy_.format(str(e)))
def bstack11ll1llll1l_opy_(file_name, key, value, logger):
    file_path = bstack11ll1ll1l1l_opy_(bstack11lll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᨵ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1lll111l1_opy_ = json.load(open(file_path, bstack11lll_opy_ (u"ࠫࡷࡨࠧᨶ")))
        else:
            bstack1lll111l1_opy_ = {}
        bstack1lll111l1_opy_[key] = value
        with open(file_path, bstack11lll_opy_ (u"ࠧࡽࠫࠣᨷ")) as outfile:
            json.dump(bstack1lll111l1_opy_, outfile)
def bstack11lll1ll1l_opy_(file_name, logger):
    file_path = bstack11ll1ll1l1l_opy_(bstack11lll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᨸ"), file_name, logger)
    bstack1lll111l1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11lll_opy_ (u"ࠧࡳࠩᨹ")) as bstack11l111l1l_opy_:
            bstack1lll111l1_opy_ = json.load(bstack11l111l1l_opy_)
    return bstack1lll111l1_opy_
def bstack1l11llll11_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11lll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬᨺ") + file_path + bstack11lll_opy_ (u"ࠩࠣࠫᨻ") + str(e))
def bstack1lll11l11_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11lll_opy_ (u"ࠥࡀࡓࡕࡔࡔࡇࡗࡂࠧᨼ")
def bstack11lll1111l_opy_(config):
    if bstack11lll_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᨽ") in config:
        del (config[bstack11lll_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᨾ")])
        return False
    if bstack1lll11l11_opy_() < version.parse(bstack11lll_opy_ (u"࠭࠳࠯࠶࠱࠴ࠬᨿ")):
        return False
    if bstack1lll11l11_opy_() >= version.parse(bstack11lll_opy_ (u"ࠧ࠵࠰࠴࠲࠺࠭ᩀ")):
        return True
    if bstack11lll_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨᩁ") in config and config[bstack11lll_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᩂ")] is False:
        return False
    else:
        return True
def bstack1ll1l1ll_opy_(args_list, bstack11ll1l111l1_opy_):
    index = -1
    for value in bstack11ll1l111l1_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack11l11ll1ll_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack11l11ll1ll_opy_ = bstack11l11ll1ll_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11lll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᩃ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11lll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᩄ"), exception=exception)
    def bstack111l11ll1l_opy_(self):
        if self.result != bstack11lll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᩅ"):
            return None
        if isinstance(self.exception_type, str) and bstack11lll_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤᩆ") in self.exception_type:
            return bstack11lll_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣᩇ")
        return bstack11lll_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤᩈ")
    def bstack11lll11l1ll_opy_(self):
        if self.result != bstack11lll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᩉ"):
            return None
        if self.bstack11l11ll1ll_opy_:
            return self.bstack11l11ll1ll_opy_
        return bstack11ll1lll1ll_opy_(self.exception)
def bstack11ll1lll1ll_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack11ll1ll1111_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l11lllll_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1ll1111111_opy_(config, logger):
    try:
        import playwright
        bstack11lllll11ll_opy_ = playwright.__file__
        bstack11lll1l1111_opy_ = os.path.split(bstack11lllll11ll_opy_)
        bstack11lllll111l_opy_ = bstack11lll1l1111_opy_[0] + bstack11lll_opy_ (u"ࠪ࠳ࡩࡸࡩࡷࡧࡵ࠳ࡵࡧࡣ࡬ࡣࡪࡩ࠴ࡲࡩࡣ࠱ࡦࡰ࡮࠵ࡣ࡭࡫࠱࡮ࡸ࠭ᩊ")
        os.environ[bstack11lll_opy_ (u"ࠫࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠧᩋ")] = bstack1ll111lll_opy_(config)
        with open(bstack11lllll111l_opy_, bstack11lll_opy_ (u"ࠬࡸࠧᩌ")) as f:
            bstack1llllll11_opy_ = f.read()
            bstack11ll1llll11_opy_ = bstack11lll_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬᩍ")
            bstack11ll1ll11ll_opy_ = bstack1llllll11_opy_.find(bstack11ll1llll11_opy_)
            if bstack11ll1ll11ll_opy_ == -1:
              process = subprocess.Popen(bstack11lll_opy_ (u"ࠢ࡯ࡲࡰࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠦᩎ"), shell=True, cwd=bstack11lll1l1111_opy_[0])
              process.wait()
              bstack11ll11l11l1_opy_ = bstack11lll_opy_ (u"ࠨࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࠨ࠻ࠨᩏ")
              bstack11llll1ll1l_opy_ = bstack11lll_opy_ (u"ࠤࠥࠦࠥࡢࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࡠࠧࡁࠠࡤࡱࡱࡷࡹࠦࡻࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠤࢂࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩࠬ࠿ࠥ࡯ࡦࠡࠪࡳࡶࡴࡩࡥࡴࡵ࠱ࡩࡳࡼ࠮ࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠬࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠨࠪ࠽ࠣࠦࠧࠨᩐ")
              bstack11ll1l1llll_opy_ = bstack1llllll11_opy_.replace(bstack11ll11l11l1_opy_, bstack11llll1ll1l_opy_)
              with open(bstack11lllll111l_opy_, bstack11lll_opy_ (u"ࠪࡻࠬᩑ")) as f:
                f.write(bstack11ll1l1llll_opy_)
    except Exception as e:
        logger.error(bstack11l1ll111l_opy_.format(str(e)))
def bstack11l11l11l_opy_():
  try:
    bstack11lll11ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11lll_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫᩒ"))
    bstack11lllll1111_opy_ = []
    if os.path.exists(bstack11lll11ll1l_opy_):
      with open(bstack11lll11ll1l_opy_) as f:
        bstack11lllll1111_opy_ = json.load(f)
      os.remove(bstack11lll11ll1l_opy_)
    return bstack11lllll1111_opy_
  except:
    pass
  return []
def bstack11llll1l1l_opy_(bstack11111l111_opy_):
  try:
    bstack11lllll1111_opy_ = []
    bstack11lll11ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11lll_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬᩓ"))
    if os.path.exists(bstack11lll11ll1l_opy_):
      with open(bstack11lll11ll1l_opy_) as f:
        bstack11lllll1111_opy_ = json.load(f)
    bstack11lllll1111_opy_.append(bstack11111l111_opy_)
    with open(bstack11lll11ll1l_opy_, bstack11lll_opy_ (u"࠭ࡷࠨᩔ")) as f:
        json.dump(bstack11lllll1111_opy_, f)
  except:
    pass
def bstack1l111ll1l1_opy_(logger, bstack11ll1l11ll1_opy_ = False):
  try:
    test_name = os.environ.get(bstack11lll_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪᩕ"), bstack11lll_opy_ (u"ࠨࠩᩖ"))
    if test_name == bstack11lll_opy_ (u"ࠩࠪᩗ"):
        test_name = threading.current_thread().__dict__.get(bstack11lll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡅࡨࡩࡥࡴࡦࡵࡷࡣࡳࡧ࡭ࡦࠩᩘ"), bstack11lll_opy_ (u"ࠫࠬᩙ"))
    bstack11llll11l1l_opy_ = bstack11lll_opy_ (u"ࠬ࠲ࠠࠨᩚ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack11ll1l11ll1_opy_:
        bstack11ll1l1l11_opy_ = os.environ.get(bstack11lll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᩛ"), bstack11lll_opy_ (u"ࠧ࠱ࠩᩜ"))
        bstack1l1l111111_opy_ = {bstack11lll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᩝ"): test_name, bstack11lll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᩞ"): bstack11llll11l1l_opy_, bstack11lll_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ᩟"): bstack11ll1l1l11_opy_}
        bstack11lllll1l11_opy_ = []
        bstack11lll1ll11l_opy_ = os.path.join(tempfile.gettempdir(), bstack11lll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡵࡶࡰࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰ᩠ࠪ"))
        if os.path.exists(bstack11lll1ll11l_opy_):
            with open(bstack11lll1ll11l_opy_) as f:
                bstack11lllll1l11_opy_ = json.load(f)
        bstack11lllll1l11_opy_.append(bstack1l1l111111_opy_)
        with open(bstack11lll1ll11l_opy_, bstack11lll_opy_ (u"ࠬࡽࠧᩡ")) as f:
            json.dump(bstack11lllll1l11_opy_, f)
    else:
        bstack1l1l111111_opy_ = {bstack11lll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᩢ"): test_name, bstack11lll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᩣ"): bstack11llll11l1l_opy_, bstack11lll_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᩤ"): str(multiprocessing.current_process().name)}
        if bstack11lll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭ᩥ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1l1l111111_opy_)
  except Exception as e:
      logger.warn(bstack11lll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡶࡹࡵࡧࡶࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢᩦ").format(e))
def bstack1ll111l1l1_opy_(error_message, test_name, index, logger):
  try:
    bstack11lll1l1l1l_opy_ = []
    bstack1l1l111111_opy_ = {bstack11lll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᩧ"): test_name, bstack11lll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᩨ"): error_message, bstack11lll_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᩩ"): index}
    bstack11ll1l11lll_opy_ = os.path.join(tempfile.gettempdir(), bstack11lll_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᩪ"))
    if os.path.exists(bstack11ll1l11lll_opy_):
        with open(bstack11ll1l11lll_opy_) as f:
            bstack11lll1l1l1l_opy_ = json.load(f)
    bstack11lll1l1l1l_opy_.append(bstack1l1l111111_opy_)
    with open(bstack11ll1l11lll_opy_, bstack11lll_opy_ (u"ࠨࡹࠪᩫ")) as f:
        json.dump(bstack11lll1l1l1l_opy_, f)
  except Exception as e:
    logger.warn(bstack11lll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᩬ").format(e))
def bstack1l1111lll1_opy_(bstack1l1l111l11_opy_, name, logger):
  try:
    bstack1l1l111111_opy_ = {bstack11lll_opy_ (u"ࠪࡲࡦࡳࡥࠨᩭ"): name, bstack11lll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᩮ"): bstack1l1l111l11_opy_, bstack11lll_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᩯ"): str(threading.current_thread()._name)}
    return bstack1l1l111111_opy_
  except Exception as e:
    logger.warn(bstack11lll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡤࡨ࡬ࡦࡼࡥࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᩰ").format(e))
  return
def bstack11llll1l11l_opy_():
    return platform.system() == bstack11lll_opy_ (u"ࠧࡘ࡫ࡱࡨࡴࡽࡳࠨᩱ")
def bstack11l1lll11_opy_(bstack11ll1l1lll1_opy_, config, logger):
    bstack11llll11ll1_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack11ll1l1lll1_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11lll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡬ࡵࡧࡵࠤࡨࡵ࡮ࡧ࡫ࡪࠤࡰ࡫ࡹࡴࠢࡥࡽࠥࡸࡥࡨࡧࡻࠤࡲࡧࡴࡤࡪ࠽ࠤࢀࢃࠢᩲ").format(e))
    return bstack11llll11ll1_opy_
def bstack11llll1l1l1_opy_(bstack11lll1lll11_opy_, bstack11lll111l1l_opy_):
    bstack11lll1llll1_opy_ = version.parse(bstack11lll1lll11_opy_)
    bstack11lll11l11l_opy_ = version.parse(bstack11lll111l1l_opy_)
    if bstack11lll1llll1_opy_ > bstack11lll11l11l_opy_:
        return 1
    elif bstack11lll1llll1_opy_ < bstack11lll11l11l_opy_:
        return -1
    else:
        return 0
def bstack11l111ll1l_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack11llll111ll_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack11ll1ll1l11_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1lll1l1l1_opy_(options, framework, bstack1ll1ll1ll_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11lll_opy_ (u"ࠩࡪࡩࡹ࠭ᩳ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack11ll11ll1_opy_ = caps.get(bstack11lll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᩴ"))
    bstack11ll11ll1ll_opy_ = True
    bstack111ll1lll_opy_ = os.environ[bstack11lll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ᩵")]
    if bstack11ll1lllll1_opy_(caps.get(bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡘ࠵ࡆࠫ᩶"))) or bstack11ll1lllll1_opy_(caps.get(bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡡࡺ࠷ࡨ࠭᩷"))):
        bstack11ll11ll1ll_opy_ = False
    if bstack11lll1111l_opy_({bstack11lll_opy_ (u"ࠢࡶࡵࡨ࡛࠸ࡉࠢ᩸"): bstack11ll11ll1ll_opy_}):
        bstack11ll11ll1_opy_ = bstack11ll11ll1_opy_ or {}
        bstack11ll11ll1_opy_[bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪ᩹")] = bstack11ll1ll1l11_opy_(framework)
        bstack11ll11ll1_opy_[bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᩺")] = bstack1ll1111llll_opy_()
        bstack11ll11ll1_opy_[bstack11lll_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭᩻")] = bstack111ll1lll_opy_
        bstack11ll11ll1_opy_[bstack11lll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭᩼")] = bstack1ll1ll1ll_opy_
        if getattr(options, bstack11lll_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭᩽"), None):
            options.set_capability(bstack11lll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᩾"), bstack11ll11ll1_opy_)
        else:
            options[bstack11lll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ᩿")] = bstack11ll11ll1_opy_
    else:
        if getattr(options, bstack11lll_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩ᪀"), None):
            options.set_capability(bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪ᪁"), bstack11ll1ll1l11_opy_(framework))
            options.set_capability(bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᪂"), bstack1ll1111llll_opy_())
            options.set_capability(bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭᪃"), bstack111ll1lll_opy_)
            options.set_capability(bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭᪄"), bstack1ll1ll1ll_opy_)
        else:
            options[bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ᪅")] = bstack11ll1ll1l11_opy_(framework)
            options[bstack11lll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ᪆")] = bstack1ll1111llll_opy_()
            options[bstack11lll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪ᪇")] = bstack111ll1lll_opy_
            options[bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪ᪈")] = bstack1ll1ll1ll_opy_
    return options
def bstack11ll1l11111_opy_(bstack11ll1l1l11l_opy_, framework):
    bstack1ll1ll1ll_opy_ = bstack11lll111l1_opy_.get_property(bstack11lll_opy_ (u"ࠥࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡑࡔࡒࡈ࡚ࡉࡔࡠࡏࡄࡔࠧ᪉"))
    if bstack11ll1l1l11l_opy_ and len(bstack11ll1l1l11l_opy_.split(bstack11lll_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪ᪊"))) > 1:
        ws_url = bstack11ll1l1l11l_opy_.split(bstack11lll_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫ᪋"))[0]
        if bstack11lll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ᪌") in ws_url:
            from browserstack_sdk._version import __version__
            bstack11lll11111l_opy_ = json.loads(urllib.parse.unquote(bstack11ll1l1l11l_opy_.split(bstack11lll_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭᪍"))[1]))
            bstack11lll11111l_opy_ = bstack11lll11111l_opy_ or {}
            bstack111ll1lll_opy_ = os.environ[bstack11lll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭᪎")]
            bstack11lll11111l_opy_[bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪ᪏")] = str(framework) + str(__version__)
            bstack11lll11111l_opy_[bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᪐")] = bstack1ll1111llll_opy_()
            bstack11lll11111l_opy_[bstack11lll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭᪑")] = bstack111ll1lll_opy_
            bstack11lll11111l_opy_[bstack11lll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭᪒")] = bstack1ll1ll1ll_opy_
            bstack11ll1l1l11l_opy_ = bstack11ll1l1l11l_opy_.split(bstack11lll_opy_ (u"࠭ࡣࡢࡲࡶࡁࠬ᪓"))[0] + bstack11lll_opy_ (u"ࠧࡤࡣࡳࡷࡂ࠭᪔") + urllib.parse.quote(json.dumps(bstack11lll11111l_opy_))
    return bstack11ll1l1l11l_opy_
def bstack1ll1lll11_opy_():
    global bstack11lll11l11_opy_
    from playwright._impl._browser_type import BrowserType
    bstack11lll11l11_opy_ = BrowserType.connect
    return bstack11lll11l11_opy_
def bstack1lll1ll11l_opy_(framework_name):
    global bstack1ll11ll11l_opy_
    bstack1ll11ll11l_opy_ = framework_name
    return framework_name
def bstack1llll11l1l_opy_(self, *args, **kwargs):
    global bstack11lll11l11_opy_
    try:
        global bstack1ll11ll11l_opy_
        if bstack11lll_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬ᪕") in kwargs:
            kwargs[bstack11lll_opy_ (u"ࠩࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹ࠭᪖")] = bstack11ll1l11111_opy_(
                kwargs.get(bstack11lll_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧ᪗"), None),
                bstack1ll11ll11l_opy_
            )
    except Exception as e:
        logger.error(bstack11lll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦ᪘").format(str(e)))
    return bstack11lll11l11_opy_(self, *args, **kwargs)
def bstack11lll1ll1ll_opy_(bstack11lll1l11ll_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1lll1l11ll_opy_(bstack11lll1l11ll_opy_, bstack11lll_opy_ (u"ࠧࠨ᪙"))
        if proxies and proxies.get(bstack11lll_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧ᪚")):
            parsed_url = urlparse(proxies.get(bstack11lll_opy_ (u"ࠢࡩࡶࡷࡴࡸࠨ᪛")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11lll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫ᪜")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11lll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬ᪝")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11lll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭᪞")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11lll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧ᪟")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack11l1l11ll_opy_(bstack11lll1l11ll_opy_):
    bstack11ll11l11ll_opy_ = {
        bstack11lllll1l1l_opy_[bstack11llll111l1_opy_]: bstack11lll1l11ll_opy_[bstack11llll111l1_opy_]
        for bstack11llll111l1_opy_ in bstack11lll1l11ll_opy_
        if bstack11llll111l1_opy_ in bstack11lllll1l1l_opy_
    }
    bstack11ll11l11ll_opy_[bstack11lll_opy_ (u"ࠧࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠧ᪠")] = bstack11lll1ll1ll_opy_(bstack11lll1l11ll_opy_, bstack11lll111l1_opy_.get_property(bstack11lll_opy_ (u"ࠨࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸࠨ᪡")))
    bstack11llll1lll1_opy_ = [element.lower() for element in bstack11llllll11l_opy_]
    bstack11ll1ll1ll1_opy_(bstack11ll11l11ll_opy_, bstack11llll1lll1_opy_)
    return bstack11ll11l11ll_opy_
def bstack11ll1ll1ll1_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11lll_opy_ (u"ࠢࠫࠬ࠭࠮ࠧ᪢")
    for value in d.values():
        if isinstance(value, dict):
            bstack11ll1ll1ll1_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack11ll1ll1ll1_opy_(item, keys)
def bstack11ll11lll1l_opy_():
    bstack11lll11ll11_opy_ = [os.environ.get(bstack11lll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡋࡏࡉࡘࡥࡄࡊࡔࠥ᪣")), os.path.join(os.path.expanduser(bstack11lll_opy_ (u"ࠤࢁࠦ᪤")), bstack11lll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ᪥")), os.path.join(bstack11lll_opy_ (u"ࠫ࠴ࡺ࡭ࡱࠩ᪦"), bstack11lll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᪧ"))]
    for path in bstack11lll11ll11_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11lll_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࠬࠨ᪨") + str(path) + bstack11lll_opy_ (u"ࠢࠨࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠥ᪩"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11lll_opy_ (u"ࠣࡉ࡬ࡺ࡮ࡴࡧࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸࠦࡦࡰࡴࠣࠫࠧ᪪") + str(path) + bstack11lll_opy_ (u"ࠤࠪࠦ᪫"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11lll_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࠩࠥ᪬") + str(path) + bstack11lll_opy_ (u"ࠦࠬࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡩࡣࡶࠤࡹ࡮ࡥࠡࡴࡨࡵࡺ࡯ࡲࡦࡦࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳ࠯ࠤ᪭"))
            else:
                logger.debug(bstack11lll_opy_ (u"ࠧࡉࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥ࠭ࠢ᪮") + str(path) + bstack11lll_opy_ (u"ࠨࠧࠡࡹ࡬ࡸ࡭ࠦࡷࡳ࡫ࡷࡩࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯࠰ࠥ᪯"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11lll_opy_ (u"ࠢࡐࡲࡨࡶࡦࡺࡩࡰࡰࠣࡷࡺࡩࡣࡦࡧࡧࡩࡩࠦࡦࡰࡴࠣࠫࠧ᪰") + str(path) + bstack11lll_opy_ (u"ࠣࠩ࠱ࠦ᪱"))
            return path
        except Exception as e:
            logger.debug(bstack11lll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡸࡴࠥ࡬ࡩ࡭ࡧࠣࠫࢀࡶࡡࡵࡪࢀࠫ࠿ࠦࠢ᪲") + str(e) + bstack11lll_opy_ (u"ࠥࠦ᪳"))
    logger.debug(bstack11lll_opy_ (u"ࠦࡆࡲ࡬ࠡࡲࡤࡸ࡭ࡹࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠣ᪴"))
    return None
@measure(event_name=EVENTS.bstack11llllll111_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
def bstack1lllll1llll_opy_(binary_path, bstack1llll1ll1l1_opy_, bs_config):
    logger.debug(bstack11lll_opy_ (u"ࠧࡉࡵࡳࡴࡨࡲࡹࠦࡃࡍࡋࠣࡔࡦࡺࡨࠡࡨࡲࡹࡳࡪ࠺ࠡࡽࢀ᪵ࠦ").format(binary_path))
    bstack11ll1lll1l1_opy_ = bstack11lll_opy_ (u"᪶࠭ࠧ")
    bstack11ll1lll11l_opy_ = {
        bstack11lll_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲ᪷ࠬ"): __version__,
        bstack11lll_opy_ (u"ࠣࡱࡶ᪸ࠦ"): platform.system(),
        bstack11lll_opy_ (u"ࠤࡲࡷࡤࡧࡲࡤࡪ᪹ࠥ"): platform.machine(),
        bstack11lll_opy_ (u"ࠥࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮᪺ࠣ"): bstack11lll_opy_ (u"ࠫ࠵࠭᪻"),
        bstack11lll_opy_ (u"ࠧࡹࡤ࡬ࡡ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠦ᪼"): bstack11lll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ᪽࠭")
    }
    try:
        if binary_path:
            bstack11ll1lll11l_opy_[bstack11lll_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ᪾")] = subprocess.check_output([binary_path, bstack11lll_opy_ (u"ࠣࡸࡨࡶࡸ࡯࡯࡯ࠤᪿ")]).strip().decode(bstack11lll_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᫀ"))
        response = requests.request(
            bstack11lll_opy_ (u"ࠪࡋࡊ࡚ࠧ᫁"),
            url=bstack11lll1ll1_opy_(bstack1l11111l111_opy_),
            headers=None,
            auth=(bs_config[bstack11lll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭᫂")], bs_config[bstack11lll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ᫃")]),
            json=None,
            params=bstack11ll1lll11l_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11lll_opy_ (u"࠭ࡵࡳ࡮᫄ࠪ") in data.keys() and bstack11lll_opy_ (u"ࠧࡶࡲࡧࡥࡹ࡫ࡤࡠࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭᫅") in data.keys():
            logger.debug(bstack11lll_opy_ (u"ࠣࡐࡨࡩࡩࠦࡴࡰࠢࡸࡴࡩࡧࡴࡦࠢࡥ࡭ࡳࡧࡲࡺ࠮ࠣࡧࡺࡸࡲࡦࡰࡷࠤࡧ࡯࡮ࡢࡴࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠤ᫆").format(bstack11ll1lll11l_opy_[bstack11lll_opy_ (u"ࠩࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ᫇")]))
            bstack11llll11111_opy_ = bstack11ll1lll111_opy_(data[bstack11lll_opy_ (u"ࠪࡹࡷࡲࠧ᫈")], bstack1llll1ll1l1_opy_)
            bstack11ll1lll1l1_opy_ = os.path.join(bstack1llll1ll1l1_opy_, bstack11llll11111_opy_)
            os.chmod(bstack11ll1lll1l1_opy_, 0o777) # bstack11ll1ll1lll_opy_ permission
            return bstack11ll1lll1l1_opy_
    except Exception as e:
        logger.debug(bstack11lll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠ࡯ࡧࡺࠤࡘࡊࡋࠡࡽࢀࠦ᫉").format(e))
    return binary_path
@measure(event_name=EVENTS.bstack1l1111l1l11_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
def bstack11ll1lll111_opy_(bstack11lll111111_opy_, bstack11ll1l11l1l_opy_):
    logger.debug(bstack11lll_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡗࡉࡑࠠࡣ࡫ࡱࡥࡷࡿࠠࡧࡴࡲࡱ࠿᫊ࠦࠢ") + str(bstack11lll111111_opy_) + bstack11lll_opy_ (u"ࠨࠢ᫋"))
    zip_path = os.path.join(bstack11ll1l11l1l_opy_, bstack11lll_opy_ (u"ࠢࡥࡱࡺࡲࡱࡵࡡࡥࡧࡧࡣ࡫࡯࡬ࡦ࠰ࡽ࡭ࡵࠨᫌ"))
    bstack11llll11111_opy_ = bstack11lll_opy_ (u"ࠨࠩᫍ")
    with requests.get(bstack11lll111111_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11lll_opy_ (u"ࠤࡺࡦࠧᫎ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11lll_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࡨࡨࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼ࠲ࠧ᫏"))
    with zipfile.ZipFile(zip_path, bstack11lll_opy_ (u"ࠫࡷ࠭᫐")) as zip_ref:
        bstack11lll1ll1l1_opy_ = zip_ref.namelist()
        if len(bstack11lll1ll1l1_opy_) > 0:
            bstack11llll11111_opy_ = bstack11lll1ll1l1_opy_[0] # bstack11ll1l1l1l1_opy_ bstack1l111111111_opy_ will be bstack11ll1llllll_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack11ll1l11l1l_opy_)
        logger.debug(bstack11lll_opy_ (u"ࠧࡌࡩ࡭ࡧࡶࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻࠣࡩࡽࡺࡲࡢࡥࡷࡩࡩࠦࡴࡰࠢࠪࠦ᫑") + str(bstack11ll1l11l1l_opy_) + bstack11lll_opy_ (u"ࠨࠧࠣ᫒"))
    os.remove(zip_path)
    return bstack11llll11111_opy_
def get_cli_dir():
    bstack11lll1111l1_opy_ = bstack11ll11lll1l_opy_()
    if bstack11lll1111l1_opy_:
        bstack1llll1ll1l1_opy_ = os.path.join(bstack11lll1111l1_opy_, bstack11lll_opy_ (u"ࠢࡤ࡮࡬ࠦ᫓"))
        if not os.path.exists(bstack1llll1ll1l1_opy_):
            os.makedirs(bstack1llll1ll1l1_opy_, mode=0o777, exist_ok=True)
        return bstack1llll1ll1l1_opy_
    else:
        raise FileNotFoundError(bstack11lll_opy_ (u"ࠣࡐࡲࠤࡼࡸࡩࡵࡣࡥࡰࡪࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻ࠱ࠦ᫔"))
def bstack1llll1l1l11_opy_(bstack1llll1ll1l1_opy_):
    bstack11lll_opy_ (u"ࠤࠥࠦࡌ࡫ࡴࠡࡶ࡫ࡩࠥࡶࡡࡵࡪࠣࡪࡴࡸࠠࡵࡪࡨࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡗࡉࡑࠠࡣ࡫ࡱࡥࡷࡿࠠࡪࡰࠣࡥࠥࡽࡲࡪࡶࡤࡦࡱ࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻ࠱ࠦࠧࠨ᫕")
    bstack11ll1l111ll_opy_ = [
        os.path.join(bstack1llll1ll1l1_opy_, f)
        for f in os.listdir(bstack1llll1ll1l1_opy_)
        if os.path.isfile(os.path.join(bstack1llll1ll1l1_opy_, f)) and f.startswith(bstack11lll_opy_ (u"ࠥࡦ࡮ࡴࡡࡳࡻ࠰ࠦ᫖"))
    ]
    if len(bstack11ll1l111ll_opy_) > 0:
        return max(bstack11ll1l111ll_opy_, key=os.path.getmtime) # get bstack11llll11lll_opy_ binary
    return bstack11lll_opy_ (u"ࠦࠧ᫗")