import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from astropy.wcs import WCS
from astropy.io import fits

from wcsaxes.wcsaxes import WCSAxes

hdu = fits.open('rosat.fits')[0]

fig = plt.figure()

ax = WCSAxes(fig, [0.1, 0.1, 0.8, 0.8], wcs=WCS(hdu.header))

fig.add_axes(ax)

ax.imshow(hdu.data, origin='lower', vmax=500)

# Add patch in default coordinates (pixel)
p = Circle((300, 100), radius=40, ec='yellow', fc='none')
ax.add_patch(p)

# Add patch in explicit pixel coordinates
p = Circle((400, 200), radius=40, ec='red', fc='none', transform=ax.get_transform('pixel'))
ax.add_patch(p)

# Add patch in world coordinates
p = Circle((30., 50.), radius=20., ec='green', fc='none', transform=ax.get_transform('world'))
ax.add_patch(p)

# Add another patch in world coordinates
p = Circle((30., 50.), radius=35., ec='purple', fc='none', transform=ax.get_transform('world'))
ax.add_patch(p)

# Add label in world coordinates
ax.text(-30., -70., 'hello', color='white', transform=ax.get_transform('world'))

# SHow grid
ax.grid(True)

fig.savefig('patches_allsky.png', bbox_inches='tight')