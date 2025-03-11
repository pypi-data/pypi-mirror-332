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
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11llllllll1_opy_, bstack11llllll11l_opy_
import tempfile
import json
bstack11l1llll1l1_opy_ = os.getenv(bstack11lll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡈࡡࡉࡍࡑࡋࠢᬃ"), None) or os.path.join(tempfile.gettempdir(), bstack11lll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡤࡦࡤࡸ࡫࠳ࡲ࡯ࡨࠤᬄ"))
bstack11l1ll1ll11_opy_ = os.path.join(bstack11lll_opy_ (u"ࠣ࡮ࡲ࡫ࠧᬅ"), bstack11lll_opy_ (u"ࠩࡶࡨࡰ࠳ࡣ࡭࡫࠰ࡨࡪࡨࡵࡨ࠰࡯ࡳ࡬࠭ᬆ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11lll_opy_ (u"ࠪࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭ᬇ"),
      datefmt=bstack11lll_opy_ (u"ࠫࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࡛ࠩᬈ"),
      stream=sys.stdout
    )
  return logger
def bstack111111111l_opy_():
  bstack11l1llll1ll_opy_ = os.environ.get(bstack11lll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡉࡋࡂࡖࡉࠥᬉ"), bstack11lll_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧᬊ"))
  return logging.DEBUG if bstack11l1llll1ll_opy_.lower() == bstack11lll_opy_ (u"ࠢࡵࡴࡸࡩࠧᬋ") else logging.INFO
def bstack1ll111l111l_opy_():
  global bstack11l1llll1l1_opy_
  if os.path.exists(bstack11l1llll1l1_opy_):
    os.remove(bstack11l1llll1l1_opy_)
  if os.path.exists(bstack11l1ll1ll11_opy_):
    os.remove(bstack11l1ll1ll11_opy_)
def bstack1l111l11_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack11lll1l1l_opy_(config, log_level):
  bstack11l1lllllll_opy_ = log_level
  if bstack11lll_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪᬌ") in config and config[bstack11lll_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫᬍ")] in bstack11llllllll1_opy_:
    bstack11l1lllllll_opy_ = bstack11llllllll1_opy_[config[bstack11lll_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬᬎ")]]
  if config.get(bstack11lll_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭ᬏ"), False):
    logging.getLogger().setLevel(bstack11l1lllllll_opy_)
    return bstack11l1lllllll_opy_
  global bstack11l1llll1l1_opy_
  bstack1l111l11_opy_()
  bstack11l1ll1llll_opy_ = logging.Formatter(
    fmt=bstack11lll_opy_ (u"ࠬࠫࠨࡢࡵࡦࡸ࡮ࡳࡥࠪࡵࠣ࡟ࠪ࠮࡮ࡢ࡯ࡨ࠭ࡸࡣ࡛ࠦࠪ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩ࠮ࡹ࡝ࠡ࠯ࠣࠩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࡳࠨᬐ"),
    datefmt=bstack11lll_opy_ (u"࡚࠭ࠥ࠯ࠨࡱ࠲ࠫࡤࡕࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࡝ࠫᬑ"),
  )
  bstack11l1lll11ll_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11l1llll1l1_opy_)
  file_handler.setFormatter(bstack11l1ll1llll_opy_)
  bstack11l1lll11ll_opy_.setFormatter(bstack11l1ll1llll_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11l1lll11ll_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11lll_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶ࠳ࡸࡥ࡮ࡱࡷࡩ࠳ࡸࡥ࡮ࡱࡷࡩࡤࡩ࡯࡯ࡰࡨࡧࡹ࡯࡯࡯ࠩᬒ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11l1lll11ll_opy_.setLevel(bstack11l1lllllll_opy_)
  logging.getLogger().addHandler(bstack11l1lll11ll_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11l1lllllll_opy_
def bstack11l1lll1111_opy_(config):
  try:
    bstack11l1lll1ll1_opy_ = set(bstack11llllll11l_opy_)
    bstack11l1lll111l_opy_ = bstack11lll_opy_ (u"ࠨࠩᬓ")
    with open(bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬᬔ")) as bstack11l1lll11l1_opy_:
      bstack11l1lll1l11_opy_ = bstack11l1lll11l1_opy_.read()
      bstack11l1lll111l_opy_ = re.sub(bstack11lll_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃࠨ࠴ࠪࠥ࡞ࡱࠫᬕ"), bstack11lll_opy_ (u"ࠫࠬᬖ"), bstack11l1lll1l11_opy_, flags=re.M)
      bstack11l1lll111l_opy_ = re.sub(
        bstack11lll_opy_ (u"ࡷ࠭࡞ࠩ࡞ࡶ࠯࠮ࡅࠨࠨᬗ") + bstack11lll_opy_ (u"࠭ࡼࠨᬘ").join(bstack11l1lll1ll1_opy_) + bstack11lll_opy_ (u"ࠧࠪ࠰࠭ࠨࠬᬙ"),
        bstack11lll_opy_ (u"ࡳࠩ࡟࠶࠿࡛ࠦࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪᬚ"),
        bstack11l1lll111l_opy_, flags=re.M | re.I
      )
    def bstack11l1llll111_opy_(dic):
      bstack11l1lllll1l_opy_ = {}
      for key, value in dic.items():
        if key in bstack11l1lll1ll1_opy_:
          bstack11l1lllll1l_opy_[key] = bstack11lll_opy_ (u"ࠩ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭ᬛ")
        else:
          if isinstance(value, dict):
            bstack11l1lllll1l_opy_[key] = bstack11l1llll111_opy_(value)
          else:
            bstack11l1lllll1l_opy_[key] = value
      return bstack11l1lllll1l_opy_
    bstack11l1lllll1l_opy_ = bstack11l1llll111_opy_(config)
    return {
      bstack11lll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ᬜ"): bstack11l1lll111l_opy_,
      bstack11lll_opy_ (u"ࠫ࡫࡯࡮ࡢ࡮ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧᬝ"): json.dumps(bstack11l1lllll1l_opy_)
    }
  except Exception as e:
    return {}
def bstack11l1ll1l1l1_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack11lll_opy_ (u"ࠬࡲ࡯ࡨࠩᬞ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11l1llllll1_opy_ = os.path.join(log_dir, bstack11lll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡣࡰࡰࡩ࡭࡬ࡹࠧᬟ"))
  if not os.path.exists(bstack11l1llllll1_opy_):
    bstack11l1lll1l1l_opy_ = {
      bstack11lll_opy_ (u"ࠢࡪࡰ࡬ࡴࡦࡺࡨࠣᬠ"): str(inipath),
      bstack11lll_opy_ (u"ࠣࡴࡲࡳࡹࡶࡡࡵࡪࠥᬡ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack11lll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵ࠱࡮ࡸࡵ࡮ࠨᬢ")), bstack11lll_opy_ (u"ࠪࡻࠬᬣ")) as bstack11l1lllll11_opy_:
      bstack11l1lllll11_opy_.write(json.dumps(bstack11l1lll1l1l_opy_))
def bstack11l1ll1l1ll_opy_():
  try:
    bstack11l1llllll1_opy_ = os.path.join(os.getcwd(), bstack11lll_opy_ (u"ࠫࡱࡵࡧࠨᬤ"), bstack11lll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫᬥ"))
    if os.path.exists(bstack11l1llllll1_opy_):
      with open(bstack11l1llllll1_opy_, bstack11lll_opy_ (u"࠭ࡲࠨᬦ")) as bstack11l1lllll11_opy_:
        bstack11l1ll1lll1_opy_ = json.load(bstack11l1lllll11_opy_)
      return bstack11l1ll1lll1_opy_.get(bstack11lll_opy_ (u"ࠧࡪࡰ࡬ࡴࡦࡺࡨࠨᬧ"), bstack11lll_opy_ (u"ࠨࠩᬨ")), bstack11l1ll1lll1_opy_.get(bstack11lll_opy_ (u"ࠩࡵࡳࡴࡺࡰࡢࡶ࡫ࠫᬩ"), bstack11lll_opy_ (u"ࠪࠫᬪ"))
  except:
    pass
  return None, None
def bstack11l1ll1ll1l_opy_():
  try:
    bstack11l1llllll1_opy_ = os.path.join(os.getcwd(), bstack11lll_opy_ (u"ࠫࡱࡵࡧࠨᬫ"), bstack11lll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫᬬ"))
    if os.path.exists(bstack11l1llllll1_opy_):
      os.remove(bstack11l1llllll1_opy_)
  except:
    pass
def bstack1ll1ll1l11_opy_(config):
  from bstack_utils.helper import bstack11lll111l1_opy_
  global bstack11l1llll1l1_opy_
  try:
    if config.get(bstack11lll_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨᬭ"), False):
      return
    uuid = os.getenv(bstack11lll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᬮ")) if os.getenv(bstack11lll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᬯ")) else bstack11lll111l1_opy_.get_property(bstack11lll_opy_ (u"ࠤࡶࡨࡰࡘࡵ࡯ࡋࡧࠦᬰ"))
    if not uuid or uuid == bstack11lll_opy_ (u"ࠪࡲࡺࡲ࡬ࠨᬱ"):
      return
    bstack11l1lll1lll_opy_ = [bstack11lll_opy_ (u"ࠫࡷ࡫ࡱࡶ࡫ࡵࡩࡲ࡫࡮ࡵࡵ࠱ࡸࡽࡺࠧᬲ"), bstack11lll_opy_ (u"ࠬࡖࡩࡱࡨ࡬ࡰࡪ࠭ᬳ"), bstack11lll_opy_ (u"࠭ࡰࡺࡲࡵࡳ࡯࡫ࡣࡵ࠰ࡷࡳࡲࡲ᬴ࠧ"), bstack11l1llll1l1_opy_, bstack11l1ll1ll11_opy_]
    bstack11ll1111111_opy_, root_path = bstack11l1ll1l1ll_opy_()
    if bstack11ll1111111_opy_ != None:
      bstack11l1lll1lll_opy_.append(bstack11ll1111111_opy_)
    if root_path != None:
      bstack11l1lll1lll_opy_.append(os.path.join(root_path, bstack11lll_opy_ (u"ࠧࡤࡱࡱࡪࡹ࡫ࡳࡵ࠰ࡳࡽࠬᬵ")))
    bstack1l111l11_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11lll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠮࡮ࡲ࡫ࡸ࠳ࠧᬶ") + uuid + bstack11lll_opy_ (u"ࠩ࠱ࡸࡦࡸ࠮ࡨࡼࠪᬷ"))
    with tarfile.open(output_file, bstack11lll_opy_ (u"ࠥࡻ࠿࡭ࡺࠣᬸ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11l1lll1lll_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11l1lll1111_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11l1llll11l_opy_ = data.encode()
        tarinfo.size = len(bstack11l1llll11l_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11l1llll11l_opy_))
    bstack111l11111_opy_ = MultipartEncoder(
      fields= {
        bstack11lll_opy_ (u"ࠫࡩࡧࡴࡢࠩᬹ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11lll_opy_ (u"ࠬࡸࡢࠨᬺ")), bstack11lll_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳ࡽ࠳ࡧࡻ࡫ࡳࠫᬻ")),
        bstack11lll_opy_ (u"ࠧࡤ࡮࡬ࡩࡳࡺࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᬼ"): uuid
      }
    )
    response = requests.post(
      bstack11lll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡸࡴࡱࡵࡡࡥ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡩ࡬ࡪࡧࡱࡸ࠲ࡲ࡯ࡨࡵ࠲ࡹࡵࡲ࡯ࡢࡦࠥᬽ"),
      data=bstack111l11111_opy_,
      headers={bstack11lll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨᬾ"): bstack111l11111_opy_.content_type},
      auth=(config[bstack11lll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᬿ")], config[bstack11lll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᭀ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11lll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡺࡶ࡬ࡰࡣࡧࠤࡱࡵࡧࡴ࠼ࠣࠫᭁ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11lll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥ࡯ࡦ࡬ࡲ࡬ࠦ࡬ࡰࡩࡶ࠾ࠬᭂ") + str(e))
  finally:
    try:
      bstack1ll111l111l_opy_()
      bstack11l1ll1ll1l_opy_()
    except:
      pass