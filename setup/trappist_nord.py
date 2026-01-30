"""
Photometry Pipeline Configuation File for TRAPPIST-North
"""

# Photometry Pipeline
# Copyright (C) 2016-2018  Michael Mommert, mommermiscience@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see
# <http://www.gnu.org/licenses/>.


trappist_nord_param = {
    'telescope_instrument' : 'Trappist', # telescope/instrument name
    'telescope_keyword'    : 'ACP->NTM',  # telescope/instrument keyword
    'observatory_code'     : 'Z53',         # MPC observatory code
    'secpix'               : (0.60, 0.60 ), # pixel size (arcsec)
                                            # before binning
    'ext_coeff'            : 0.05,          # typical extinction coefficient


    # image orientation preferences
    'flipx'                : True,
    'flipy'                : False,
    'rotate'               : 0,

    # instrument-specific FITS header keywords
    'binning'              : ('XBINNING', 'YBINNING'),
                           # binning in x/y, '_blankN' denotes that both axes
                           # are listed in one keyword, sep. by blanks
    'extent'               : ('NAXIS1', 'NAXIS2'),   # N_pixels in x/y
    'ra'                   : 'RA',  # telescope pointing, RA
    'dec'                  : 'DEC', # telescope pointin, Dec
    'radec_separator'      : ' ',   # RA/Dec hms separator, use 'XXX'
                                    # if already in degrees
    'date_keyword'         : 'DATE-OBS', # obs date/time
                                         # keyword; use
                                         # 'date|time' if
                                         # separate
    'obsmidtime_jd'        : 'JD', # obs midtime jd keyword
                                         # (usually provided by
                                         # pp_prepare
    'object'               : 'OBJECT',  # object name keyword
    'filter'               : 'FILTER',  # filter keyword
    'filter_translations'  : {'V': 'V', 'R': 'R', 'Rc': 'R', 'B': 'B', 'VR': None,
                              'I': 'I', 'Ic': 'I', 'SDSSup' : 'u', 'SDSSgp' : 'g',
                              'SDSSrp' : 'r', 'SDSSip' : 'i',
                              'SDSSzp' : 'z', 'OH': None, 'CN': None,
                              'UC': None, 'NH': None, 'BC': None,
                              'C2': None, 'C3': None, 'CO+': None,
                              'H2O+': None, 'GC': None, 'RC': None, 'exoBB': None,
                              'Exo': None, 'I+z': None,'Clear': None},
                             # filtername translation dictionary
    'exptime'              : 'EXPTIME', # exposure time keyword (s)
    'airmass'              : 'AIRMASS', # airmass keyword


    # source extractor settings
    'source_minarea'       : 9, # default sextractor source minimum N_pixels
    'source_snr': 3, # default sextractor source snr for registration
    'aprad_default'        : 4, # default aperture radius in px
    'aprad_range'          : [2, 13], # [minimum, maximum] aperture radius (px)
    'sex-config-file'      : rootpath+'/setup/trappist_N.sex',
    'mask_file'            : {},
    #                        mask files as a function of x,y binning

    # registration settings (Scamp)
    'scamp-config-file'    : rootpath+'/setup/trappist_N.scamp',
    'reg_max_mag'          : 16,
    'reg_search_radius'    : 0.2, # deg
    'source_tolerance': 'high',

    # swarp settings
    'copy_keywords'        : ('OBSERVAT,INSTRUME,EXPTIME,OBJECT,' +
                              'DATE-OBS,RA,DEC,AIRMASS,TEL_KEYW,BINX,BINY,' +
                              'FILTERS,MJD-MOBS'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file'    : rootpath+'/setup/trappist_N.swarp',

    # default catalog settings
    'astrometry_catalogs'  : ['GAIA'],
    'photometry_catalogs'  : ['PANSTARRS', 'SDSS-R9', 'APASS9']
}


# add telescope parameters to according lists and dictionaries
implemented_telescopes.append('TRAPPIST-North')
instrument_identifiers['= "Andor Tech"'] = 'ACP->NTM'
telescope_parameters['ACP->NTM'] = trappist_nord_param
