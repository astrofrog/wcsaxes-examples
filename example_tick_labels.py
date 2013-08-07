import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from astropy.wcs import WCS
from astropy.io import fits
from astropy import units as u

from wcsaxes.wcsaxes import WCSAxes

hdu = fits.open('msx.fits')[0]

def get_basic():
    fig = plt.figure()
    ax = WCSAxes(fig, [0.1, 0.1, 0.8, 0.8], wcs=WCS(hdu.header))
    fig.add_axes(ax)
    ax.imshow(hdu.data, origin='lower', vmin=0, vmax=1.e-4)
    ax.grid(color='white')
    return fig, ax

fig, ax = get_basic()
ax.set_title("Default settings")
fig.savefig('tick_labels_default.png')

fig, ax = get_basic()
ax.coords['glon'].set_major_formatter('d.ddddd')
ax.coords['glat'].set_major_formatter('d.ddd')
ax.set_title("Decimal formatting")
fig.savefig('tick_labels_decimal.png')

fig, ax = get_basic()
ax.coords['glon'].set_major_formatter('dd:mm:ss.sss')
ax.coords['glat'].set_major_formatter('dd:mm:ss.ss')
ax.set_title("Sub-arcsecond formatting")
fig.savefig('tick_labels_sexagesimal_subarcsecond.png')

fig, ax = get_basic()
ax.coords['glon'].set_major_formatter('dd:mm')
ax.coords['glat'].set_major_formatter('dd:mm')
ax.set_title("Arcminute formatting")
fig.savefig('tick_labels_sexagesimal_arcminute.png')

fig, ax = get_basic()
ax.coords['glon'].set_major_formatter('dd:mm')
ax.coords['glat'].set_major_formatter('dd:mm')
ax.coords['glon'].set_ticks(spacing=10. * u.arcmin)
ax.coords['glat'].set_ticks(spacing=5. * u.arcmin)
ax.set_title("Custom spacing")
fig.savefig('tick_labels_custom_spacing.png')

fig, ax = get_basic()
ax.coords['glon'].set_major_formatter('dd:mm')
ax.coords['glat'].set_major_formatter('dd:mm')
ax.coords['glon'].set_ticks(values=[-0.2, 0., 0.2])
ax.coords['glat'].set_ticks(values=[-0.2, 0., 0.2])
ax.set_title("Custom spacing")
fig.savefig('tick_labels_custom_values.png')

