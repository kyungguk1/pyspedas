import os
import pyspedas
#from pytplot import tplot
from pytplot import get_data
import matplotlib.pyplot as plt


pyspedas.mms.fgm()
#tplot(['mms1_fgm_b_gse_srvy_l2_btot', 'mms1_fgm_b_gse_srvy_l2_bvec'])

mag_data = get_data('mms1_fgm_b_gse_srvy_l2_bvec')

plt.plot(mag_data.y)

path = os.path.join(
        os.environ['HOME'],
        "Downloads/test1.pdf"
        )
plt.savefig(path)
