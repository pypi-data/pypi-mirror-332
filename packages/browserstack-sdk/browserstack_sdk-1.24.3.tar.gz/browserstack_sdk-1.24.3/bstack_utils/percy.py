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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack11lll1ll1_opy_, bstack1l1l11l1l1_opy_
from bstack_utils.measure import measure
class bstack1ll1l111l_opy_:
  working_dir = os.getcwd()
  bstack1l1l11111_opy_ = False
  config = {}
  binary_path = bstack11lll_opy_ (u"ࠧࠨᮐ")
  bstack11l1l1ll111_opy_ = bstack11lll_opy_ (u"ࠨࠩᮑ")
  bstack1lll111111_opy_ = False
  bstack11l1l1111l1_opy_ = None
  bstack11l1l11llll_opy_ = {}
  bstack11l1l111l11_opy_ = 300
  bstack11l11ll111l_opy_ = False
  logger = None
  bstack11l1ll11111_opy_ = False
  bstack11ll1lllll_opy_ = False
  percy_build_id = None
  bstack11l11ll1111_opy_ = bstack11lll_opy_ (u"ࠩࠪᮒ")
  bstack11l1l1l11ll_opy_ = {
    bstack11lll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪᮓ") : 1,
    bstack11lll_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬᮔ") : 2,
    bstack11lll_opy_ (u"ࠬ࡫ࡤࡨࡧࠪᮕ") : 3,
    bstack11lll_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠭ᮖ") : 4
  }
  def __init__(self) -> None: pass
  def bstack11l1l11l11l_opy_(self):
    bstack11l1l11ll1l_opy_ = bstack11lll_opy_ (u"ࠧࠨᮗ")
    bstack11l1l1111ll_opy_ = sys.platform
    bstack11l11lll111_opy_ = bstack11lll_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧᮘ")
    if re.match(bstack11lll_opy_ (u"ࠤࡧࡥࡷࡽࡩ࡯ࡾࡰࡥࡨࠦ࡯ࡴࠤᮙ"), bstack11l1l1111ll_opy_) != None:
      bstack11l1l11ll1l_opy_ = bstack1l1111111ll_opy_ + bstack11lll_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡳࡸࡾ࠮ࡻ࡫ࡳࠦᮚ")
      self.bstack11l11ll1111_opy_ = bstack11lll_opy_ (u"ࠫࡲࡧࡣࠨᮛ")
    elif re.match(bstack11lll_opy_ (u"ࠧࡳࡳࡸ࡫ࡱࢀࡲࡹࡹࡴࡾࡰ࡭ࡳ࡭ࡷࡽࡥࡼ࡫ࡼ࡯࡮ࡽࡤࡦࡧࡼ࡯࡮ࡽࡹ࡬ࡲࡨ࡫ࡼࡦ࡯ࡦࢀࡼ࡯࡮࠴࠴ࠥᮜ"), bstack11l1l1111ll_opy_) != None:
      bstack11l1l11ll1l_opy_ = bstack1l1111111ll_opy_ + bstack11lll_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳ࡷࡪࡰ࠱ࡾ࡮ࡶࠢᮝ")
      bstack11l11lll111_opy_ = bstack11lll_opy_ (u"ࠢࡱࡧࡵࡧࡾ࠴ࡥࡹࡧࠥᮞ")
      self.bstack11l11ll1111_opy_ = bstack11lll_opy_ (u"ࠨࡹ࡬ࡲࠬᮟ")
    else:
      bstack11l1l11ll1l_opy_ = bstack1l1111111ll_opy_ + bstack11lll_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯࡯࡭ࡳࡻࡸ࠯ࡼ࡬ࡴࠧᮠ")
      self.bstack11l11ll1111_opy_ = bstack11lll_opy_ (u"ࠪࡰ࡮ࡴࡵࡹࠩᮡ")
    return bstack11l1l11ll1l_opy_, bstack11l11lll111_opy_
  def bstack11l1l111ll1_opy_(self):
    try:
      bstack11l11ll1ll1_opy_ = [os.path.join(expanduser(bstack11lll_opy_ (u"ࠦࢃࠨᮢ")), bstack11lll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᮣ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack11l11ll1ll1_opy_:
        if(self.bstack11l1l11l1l1_opy_(path)):
          return path
      raise bstack11lll_opy_ (u"ࠨࡕ࡯ࡣ࡯ࡦࡪࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠥᮤ")
    except Exception as e:
      self.logger.error(bstack11lll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨࠤࡵࡧࡴࡩࠢࡩࡳࡷࠦࡰࡦࡴࡦࡽࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࠲ࠦࡻࡾࠤᮥ").format(e))
  def bstack11l1l11l1l1_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  @measure(event_name=EVENTS.bstack1l111111l11_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
  def bstack11l1l1lll1l_opy_(self, bstack11l1l11ll1l_opy_, bstack11l11lll111_opy_):
    try:
      bstack11l11llllll_opy_ = self.bstack11l1l111ll1_opy_()
      bstack11l1l1l111l_opy_ = os.path.join(bstack11l11llllll_opy_, bstack11lll_opy_ (u"ࠨࡲࡨࡶࡨࡿ࠮ࡻ࡫ࡳࠫᮦ"))
      bstack11l1l1l1111_opy_ = os.path.join(bstack11l11llllll_opy_, bstack11l11lll111_opy_)
      if os.path.exists(bstack11l1l1l1111_opy_):
        self.logger.info(bstack11lll_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡴ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠦᮧ").format(bstack11l1l1l1111_opy_))
        return bstack11l1l1l1111_opy_
      if os.path.exists(bstack11l1l1l111l_opy_):
        self.logger.info(bstack11lll_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡽ࡭ࡵࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡽࢀ࠰ࠥࡻ࡮ࡻ࡫ࡳࡴ࡮ࡴࡧࠣᮨ").format(bstack11l1l1l111l_opy_))
        return self.bstack11l11ll11l1_opy_(bstack11l1l1l111l_opy_, bstack11l11lll111_opy_)
      self.logger.info(bstack11lll_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡵࡳࡲࠦࡻࡾࠤᮩ").format(bstack11l1l11ll1l_opy_))
      response = bstack1l1l11l1l1_opy_(bstack11lll_opy_ (u"ࠬࡍࡅࡕ᮪ࠩ"), bstack11l1l11ll1l_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack11l1l1l111l_opy_, bstack11lll_opy_ (u"࠭ࡷࡣ᮫ࠩ")) as file:
          file.write(response.content)
        self.logger.info(bstack11lll_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥࡧࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡥࡳࡪࠠࡴࡣࡹࡩࡩࠦࡡࡵࠢࡾࢁࠧᮬ").format(bstack11l1l1l111l_opy_))
        return self.bstack11l11ll11l1_opy_(bstack11l1l1l111l_opy_, bstack11l11lll111_opy_)
      else:
        raise(bstack11lll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡴࡩࡧࠣࡪ࡮ࡲࡥ࠯ࠢࡖࡸࡦࡺࡵࡴࠢࡦࡳࡩ࡫࠺ࠡࡽࢀࠦᮭ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11lll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࡀࠠࡼࡿࠥᮮ").format(e))
  def bstack11l1l11lll1_opy_(self, bstack11l1l11ll1l_opy_, bstack11l11lll111_opy_):
    try:
      retry = 2
      bstack11l1l1l1111_opy_ = None
      bstack11l11ll11ll_opy_ = False
      while retry > 0:
        bstack11l1l1l1111_opy_ = self.bstack11l1l1lll1l_opy_(bstack11l1l11ll1l_opy_, bstack11l11lll111_opy_)
        bstack11l11ll11ll_opy_ = self.bstack11l1l1l1l11_opy_(bstack11l1l11ll1l_opy_, bstack11l11lll111_opy_, bstack11l1l1l1111_opy_)
        if bstack11l11ll11ll_opy_:
          break
        retry -= 1
      return bstack11l1l1l1111_opy_, bstack11l11ll11ll_opy_
    except Exception as e:
      self.logger.error(bstack11lll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡧࡦࡶࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡳࡥࡹ࡮ࠢᮯ").format(e))
    return bstack11l1l1l1111_opy_, False
  def bstack11l1l1l1l11_opy_(self, bstack11l1l11ll1l_opy_, bstack11l11lll111_opy_, bstack11l1l1l1111_opy_, bstack11l1ll11l11_opy_ = 0):
    if bstack11l1ll11l11_opy_ > 1:
      return False
    if bstack11l1l1l1111_opy_ == None or os.path.exists(bstack11l1l1l1111_opy_) == False:
      self.logger.warn(bstack11lll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡴࡦࡺࡨࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧ࠰ࠥࡸࡥࡵࡴࡼ࡭ࡳ࡭ࠠࡥࡱࡺࡲࡱࡵࡡࡥࠤ᮰"))
      return False
    bstack11l1l11111l_opy_ = bstack11lll_opy_ (u"ࠧࡤ࠮ࠫࡂࡳࡩࡷࡩࡹ࡝࠱ࡦࡰ࡮ࠦ࡜ࡥ࠰࡟ࡨ࠰࠴࡜ࡥ࠭ࠥ᮱")
    command = bstack11lll_opy_ (u"࠭ࡻࡾࠢ࠰࠱ࡻ࡫ࡲࡴ࡫ࡲࡲࠬ᮲").format(bstack11l1l1l1111_opy_)
    bstack11l1l111111_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack11l1l11111l_opy_, bstack11l1l111111_opy_) != None:
      return True
    else:
      self.logger.error(bstack11lll_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡤࡪࡨࡧࡰࠦࡦࡢ࡫࡯ࡩࡩࠨ᮳"))
      return False
  def bstack11l11ll11l1_opy_(self, bstack11l1l1l111l_opy_, bstack11l11lll111_opy_):
    try:
      working_dir = os.path.dirname(bstack11l1l1l111l_opy_)
      shutil.unpack_archive(bstack11l1l1l111l_opy_, working_dir)
      bstack11l1l1l1111_opy_ = os.path.join(working_dir, bstack11l11lll111_opy_)
      os.chmod(bstack11l1l1l1111_opy_, 0o755)
      return bstack11l1l1l1111_opy_
    except Exception as e:
      self.logger.error(bstack11lll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡺࡴࡺࡪࡲࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠤ᮴"))
  def bstack11l1l1ll1ll_opy_(self):
    try:
      bstack11l1l111lll_opy_ = self.config.get(bstack11lll_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ᮵"))
      bstack11l1l1ll1ll_opy_ = bstack11l1l111lll_opy_ or (bstack11l1l111lll_opy_ is None and self.bstack1l1l11111_opy_)
      if not bstack11l1l1ll1ll_opy_ or self.config.get(bstack11lll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭᮶"), None) not in bstack11lllllllll_opy_:
        return False
      self.bstack1lll111111_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11lll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡨࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨ᮷").format(e))
  def bstack11l11lll1l1_opy_(self):
    try:
      bstack11l11lll1l1_opy_ = self.percy_capture_mode
      return bstack11l11lll1l1_opy_
    except Exception as e:
      self.logger.error(bstack11lll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡩࡴࠡࡲࡨࡶࡨࡿࠠࡤࡣࡳࡸࡺࡸࡥࠡ࡯ࡲࡨࡪ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨ᮸").format(e))
  def init(self, bstack1l1l11111_opy_, config, logger):
    self.bstack1l1l11111_opy_ = bstack1l1l11111_opy_
    self.config = config
    self.logger = logger
    if not self.bstack11l1l1ll1ll_opy_():
      return
    self.bstack11l1l11llll_opy_ = config.get(bstack11lll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡔࡶࡴࡪࡱࡱࡷࠬ᮹"), {})
    self.percy_capture_mode = config.get(bstack11lll_opy_ (u"ࠧࡱࡧࡵࡧࡾࡉࡡࡱࡶࡸࡶࡪࡓ࡯ࡥࡧࠪᮺ"))
    try:
      bstack11l1l11ll1l_opy_, bstack11l11lll111_opy_ = self.bstack11l1l11l11l_opy_()
      bstack11l1l1l1111_opy_, bstack11l11ll11ll_opy_ = self.bstack11l1l11lll1_opy_(bstack11l1l11ll1l_opy_, bstack11l11lll111_opy_)
      if bstack11l11ll11ll_opy_:
        self.binary_path = bstack11l1l1l1111_opy_
        thread = Thread(target=self.bstack11l1ll1111l_opy_)
        thread.start()
      else:
        self.bstack11l1ll11111_opy_ = True
        self.logger.error(bstack11lll_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡳࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦࡦࡰࡷࡱࡨࠥ࠳ࠠࡼࡿ࠯ࠤ࡚ࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡐࡦࡴࡦࡽࠧᮻ").format(bstack11l1l1l1111_opy_))
    except Exception as e:
      self.logger.error(bstack11lll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᮼ").format(e))
  def bstack11l11llll11_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11lll_opy_ (u"ࠪࡰࡴ࡭ࠧᮽ"), bstack11lll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡰࡴ࡭ࠧᮾ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11lll_opy_ (u"ࠧࡖࡵࡴࡪ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࡵࠣࡥࡹࠦࡻࡾࠤᮿ").format(logfile))
      self.bstack11l1l1ll111_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11lll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࠢࡳࡥࡹ࡮ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᯀ").format(e))
  @measure(event_name=EVENTS.bstack1l11111ll11_opy_, stage=STAGE.bstack1lll1l1l11_opy_)
  def bstack11l1ll1111l_opy_(self):
    bstack11l1l1lllll_opy_ = self.bstack11l1l111l1l_opy_()
    if bstack11l1l1lllll_opy_ == None:
      self.bstack11l1ll11111_opy_ = True
      self.logger.error(bstack11lll_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠭ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻࠥᯁ"))
      return False
    command_args = [bstack11lll_opy_ (u"ࠣࡣࡳࡴ࠿࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠤᯂ") if self.bstack1l1l11111_opy_ else bstack11lll_opy_ (u"ࠩࡨࡼࡪࡩ࠺ࡴࡶࡤࡶࡹ࠭ᯃ")]
    bstack11l1llllll1_opy_ = self.bstack11l11lllll1_opy_()
    if bstack11l1llllll1_opy_ != None:
      command_args.append(bstack11lll_opy_ (u"ࠥ࠱ࡨࠦࡻࡾࠤᯄ").format(bstack11l1llllll1_opy_))
    env = os.environ.copy()
    env[bstack11lll_opy_ (u"ࠦࡕࡋࡒࡄ࡛ࡢࡘࡔࡑࡅࡏࠤᯅ")] = bstack11l1l1lllll_opy_
    env[bstack11lll_opy_ (u"࡚ࠧࡈࡠࡄࡘࡍࡑࡊ࡟ࡖࡗࡌࡈࠧᯆ")] = os.environ.get(bstack11lll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᯇ"), bstack11lll_opy_ (u"ࠧࠨᯈ"))
    bstack11l1ll111l1_opy_ = [self.binary_path]
    self.bstack11l11llll11_opy_()
    self.bstack11l1l1111l1_opy_ = self.bstack11l11ll1l11_opy_(bstack11l1ll111l1_opy_ + command_args, env)
    self.logger.debug(bstack11lll_opy_ (u"ࠣࡕࡷࡥࡷࡺࡩ࡯ࡩࠣࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠤᯉ"))
    bstack11l1ll11l11_opy_ = 0
    while self.bstack11l1l1111l1_opy_.poll() == None:
      bstack11l1l1l1ll1_opy_ = self.bstack11l11llll1l_opy_()
      if bstack11l1l1l1ll1_opy_:
        self.logger.debug(bstack11lll_opy_ (u"ࠤࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠧᯊ"))
        self.bstack11l11ll111l_opy_ = True
        return True
      bstack11l1ll11l11_opy_ += 1
      self.logger.debug(bstack11lll_opy_ (u"ࠥࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡕࡩࡹࡸࡹࠡ࠯ࠣࡿࢂࠨᯋ").format(bstack11l1ll11l11_opy_))
      time.sleep(2)
    self.logger.error(bstack11lll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽ࠱ࠦࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡌࡡࡪ࡮ࡨࡨࠥࡧࡦࡵࡧࡵࠤࢀࢃࠠࡢࡶࡷࡩࡲࡶࡴࡴࠤᯌ").format(bstack11l1ll11l11_opy_))
    self.bstack11l1ll11111_opy_ = True
    return False
  def bstack11l11llll1l_opy_(self, bstack11l1ll11l11_opy_ = 0):
    if bstack11l1ll11l11_opy_ > 10:
      return False
    try:
      bstack11l1l1lll11_opy_ = os.environ.get(bstack11lll_opy_ (u"ࠬࡖࡅࡓࡅ࡜ࡣࡘࡋࡒࡗࡇࡕࡣࡆࡊࡄࡓࡇࡖࡗࠬᯍ"), bstack11lll_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵࡬ࡰࡥࡤࡰ࡭ࡵࡳࡵ࠼࠸࠷࠸࠾ࠧᯎ"))
      bstack11l1l1l1l1l_opy_ = bstack11l1l1lll11_opy_ + bstack1l1111l11l1_opy_
      response = requests.get(bstack11l1l1l1l1l_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack11lll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩ࠭ᯏ"), {}).get(bstack11lll_opy_ (u"ࠨ࡫ࡧࠫᯐ"), None)
      return True
    except:
      self.logger.debug(bstack11lll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡲࡦࡦࠣࡻ࡭࡯࡬ࡦࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡨࡦࡣ࡯ࡸ࡭ࠦࡣࡩࡧࡦ࡯ࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠢᯑ"))
      return False
  def bstack11l1l111l1l_opy_(self):
    bstack11l1l1l1lll_opy_ = bstack11lll_opy_ (u"ࠪࡥࡵࡶࠧᯒ") if self.bstack1l1l11111_opy_ else bstack11lll_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᯓ")
    bstack11l1ll111ll_opy_ = bstack11lll_opy_ (u"ࠧࡻ࡮ࡥࡧࡩ࡭ࡳ࡫ࡤࠣᯔ") if self.config.get(bstack11lll_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᯕ")) is None else True
    bstack11ll11l1lll_opy_ = bstack11lll_opy_ (u"ࠢࡢࡲ࡬࠳ࡦࡶࡰࡠࡲࡨࡶࡨࡿ࠯ࡨࡧࡷࡣࡵࡸ࡯࡫ࡧࡦࡸࡤࡺ࡯࡬ࡧࡱࡃࡳࡧ࡭ࡦ࠿ࡾࢁࠫࡺࡹࡱࡧࡀࡿࢂࠬࡰࡦࡴࡦࡽࡂࢁࡽࠣᯖ").format(self.config[bstack11lll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᯗ")], bstack11l1l1l1lll_opy_, bstack11l1ll111ll_opy_)
    if self.percy_capture_mode:
      bstack11ll11l1lll_opy_ += bstack11lll_opy_ (u"ࠤࠩࡴࡪࡸࡣࡺࡡࡦࡥࡵࡺࡵࡳࡧࡢࡱࡴࡪࡥ࠾ࡽࢀࠦᯘ").format(self.percy_capture_mode)
    uri = bstack11lll1ll1_opy_(bstack11ll11l1lll_opy_)
    try:
      response = bstack1l1l11l1l1_opy_(bstack11lll_opy_ (u"ࠪࡋࡊ࡚ࠧᯙ"), uri, {}, {bstack11lll_opy_ (u"ࠫࡦࡻࡴࡩࠩᯚ"): (self.config[bstack11lll_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᯛ")], self.config[bstack11lll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᯜ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1lll111111_opy_ = data.get(bstack11lll_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨᯝ"))
        self.percy_capture_mode = data.get(bstack11lll_opy_ (u"ࠨࡲࡨࡶࡨࡿ࡟ࡤࡣࡳࡸࡺࡸࡥࡠ࡯ࡲࡨࡪ࠭ᯞ"))
        os.environ[bstack11lll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧᯟ")] = str(self.bstack1lll111111_opy_)
        os.environ[bstack11lll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࡠࡅࡄࡔ࡙࡛ࡒࡆࡡࡐࡓࡉࡋࠧᯠ")] = str(self.percy_capture_mode)
        if bstack11l1ll111ll_opy_ == bstack11lll_opy_ (u"ࠦࡺࡴࡤࡦࡨ࡬ࡲࡪࡪࠢᯡ") and str(self.bstack1lll111111_opy_).lower() == bstack11lll_opy_ (u"ࠧࡺࡲࡶࡧࠥᯢ"):
          self.bstack11ll1lllll_opy_ = True
        if bstack11lll_opy_ (u"ࠨࡴࡰ࡭ࡨࡲࠧᯣ") in data:
          return data[bstack11lll_opy_ (u"ࠢࡵࡱ࡮ࡩࡳࠨᯤ")]
        else:
          raise bstack11lll_opy_ (u"ࠨࡖࡲ࡯ࡪࡴࠠࡏࡱࡷࠤࡋࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽࠨᯥ").format(data)
      else:
        raise bstack11lll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡵ࡫ࡲࡤࡻࠣࡸࡴࡱࡥ࡯࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥࡹࡴࡢࡶࡸࡷࠥ࠳ࠠࡼࡿ࠯ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡂࡰࡦࡼࠤ࠲ࠦࡻࡾࠤ᯦").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11lll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡴࡷࡵࡪࡦࡥࡷࠦᯧ").format(e))
  def bstack11l11lllll1_opy_(self):
    bstack11l1l1l11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11lll_opy_ (u"ࠦࡵ࡫ࡲࡤࡻࡆࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠢᯨ"))
    try:
      if bstack11lll_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ᯩ") not in self.bstack11l1l11llll_opy_:
        self.bstack11l1l11llll_opy_[bstack11lll_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧᯪ")] = 2
      with open(bstack11l1l1l11l1_opy_, bstack11lll_opy_ (u"ࠧࡸࠩᯫ")) as fp:
        json.dump(self.bstack11l1l11llll_opy_, fp)
      return bstack11l1l1l11l1_opy_
    except Exception as e:
      self.logger.error(bstack11lll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡨࡸࡥࡢࡶࡨࠤࡵ࡫ࡲࡤࡻࠣࡧࡴࡴࡦ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᯬ").format(e))
  def bstack11l11ll1l11_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack11l11ll1111_opy_ == bstack11lll_opy_ (u"ࠩࡺ࡭ࡳ࠭ᯭ"):
        bstack11l11lll1ll_opy_ = [bstack11lll_opy_ (u"ࠪࡧࡲࡪ࠮ࡦࡺࡨࠫᯮ"), bstack11lll_opy_ (u"ࠫ࠴ࡩࠧᯯ")]
        cmd = bstack11l11lll1ll_opy_ + cmd
      cmd = bstack11lll_opy_ (u"ࠬࠦࠧᯰ").join(cmd)
      self.logger.debug(bstack11lll_opy_ (u"ࠨࡒࡶࡰࡱ࡭ࡳ࡭ࠠࡼࡿࠥᯱ").format(cmd))
      with open(self.bstack11l1l1ll111_opy_, bstack11lll_opy_ (u"ࠢࡢࠤ᯲")) as bstack11l1l11ll11_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack11l1l11ll11_opy_, text=True, stderr=bstack11l1l11ll11_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack11l1ll11111_opy_ = True
      self.logger.error(bstack11lll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺࠢࡺ࡭ࡹ࡮ࠠࡤ࡯ࡧࠤ࠲ࠦࡻࡾ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿ᯳ࠥ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack11l11ll111l_opy_:
        self.logger.info(bstack11lll_opy_ (u"ࠤࡖࡸࡴࡶࡰࡪࡰࡪࠤࡕ࡫ࡲࡤࡻࠥ᯴"))
        cmd = [self.binary_path, bstack11lll_opy_ (u"ࠥࡩࡽ࡫ࡣ࠻ࡵࡷࡳࡵࠨ᯵")]
        self.bstack11l11ll1l11_opy_(cmd)
        self.bstack11l11ll111l_opy_ = False
    except Exception as e:
      self.logger.error(bstack11lll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡲࡴࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡨࡵ࡭࡮ࡣࡱࡨࠥ࠳ࠠࡼࡿ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦ᯶").format(cmd, e))
  def bstack111l1l1l1_opy_(self):
    if not self.bstack1lll111111_opy_:
      return
    try:
      bstack11l1l11l1ll_opy_ = 0
      while not self.bstack11l11ll111l_opy_ and bstack11l1l11l1ll_opy_ < self.bstack11l1l111l11_opy_:
        if self.bstack11l1ll11111_opy_:
          self.logger.info(bstack11lll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡪࡦ࡯࡬ࡦࡦࠥ᯷"))
          return
        time.sleep(1)
        bstack11l1l11l1ll_opy_ += 1
      os.environ[bstack11lll_opy_ (u"࠭ࡐࡆࡔࡆ࡝ࡤࡈࡅࡔࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࠬ᯸")] = str(self.bstack11l1l1llll1_opy_())
      self.logger.info(bstack11lll_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡳࡦࡶࡸࡴࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤࠣ᯹"))
    except Exception as e:
      self.logger.error(bstack11lll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤ᯺").format(e))
  def bstack11l1l1llll1_opy_(self):
    if self.bstack1l1l11111_opy_:
      return
    try:
      bstack11l11ll1lll_opy_ = [platform[bstack11lll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ᯻")].lower() for platform in self.config.get(bstack11lll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭᯼"), [])]
      bstack11l1l1ll1l1_opy_ = sys.maxsize
      bstack11l1l11l111_opy_ = bstack11lll_opy_ (u"ࠫࠬ᯽")
      for browser in bstack11l11ll1lll_opy_:
        if browser in self.bstack11l1l1l11ll_opy_:
          bstack11l11lll11l_opy_ = self.bstack11l1l1l11ll_opy_[browser]
        if bstack11l11lll11l_opy_ < bstack11l1l1ll1l1_opy_:
          bstack11l1l1ll1l1_opy_ = bstack11l11lll11l_opy_
          bstack11l1l11l111_opy_ = browser
      return bstack11l1l11l111_opy_
    except Exception as e:
      self.logger.error(bstack11lll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡢࡦࡵࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨ᯾").format(e))
  @classmethod
  def bstack11l11ll1_opy_(self):
    return os.getenv(bstack11lll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫ᯿"), bstack11lll_opy_ (u"ࠧࡇࡣ࡯ࡷࡪ࠭ᰀ")).lower()
  @classmethod
  def bstack11lll1lll1_opy_(self):
    return os.getenv(bstack11lll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬᰁ"), bstack11lll_opy_ (u"ࠩࠪᰂ"))
  @classmethod
  def bstack1l1lllllll1_opy_(cls, value):
    cls.bstack11ll1lllll_opy_ = value
  @classmethod
  def bstack11l1l1ll11l_opy_(cls):
    return cls.bstack11ll1lllll_opy_
  @classmethod
  def bstack1ll11111l1l_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack11l11ll1l1l_opy_(cls):
    return cls.percy_build_id