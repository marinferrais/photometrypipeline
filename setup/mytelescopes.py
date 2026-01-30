"""
Personal Photometry Pipeline Configuation File
2016-11-01, mommermiscience@gmail.com
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

# telescope/instrument configurations

trappist_sud_param = {
    'telescope_instrument' : 'Trappist-S', # telescope/instrument name
    'telescope_keyword'    : 'TRAPPIST',  # telescope/instrument keyword
    'observatory_code'     : 'I40',         # MPC observatory code
    'secpix'               : (0.64, 0.64 ), # pixel size (arcsec)
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
                              'Exo': None, 'I+z': None, 'Clear': None, 'z': 'z'},
                             # filtername translation dictionary
    'exptime'              : 'EXPTIME', # exposure time keyword (s)
    'airmass'              : 'AIRMASS', # airmass keyword


    # source extractor settings
    'source_minarea'       : 9, # default sextractor source minimum N_pixels
    'source_snr': 3, # default sextractor source snr for registration
    'aprad_default'        : 4, # default aperture radius in px
    'aprad_range'          : [2, 13], # [minimum, maximum] aperture radius (px)
    'sex-config-file'      : rootpath+'/setup/trappist_S.sex',
    'mask_file'            : {},
    #                        mask files as a function of x,y binning

    # registration settings (Scamp)
    'scamp-config-file'    : rootpath+'/setup/trappist_S.scamp',
    'reg_max_mag'          : 16,
    'reg_search_radius'    : 0.2, # deg
    'source_tolerance': 'high',

    # swarp settings
    'copy_keywords'        : ('OBSERVAT,INSTRUME,EXPTIME,OBJECT,' +
                              'DATE-OBS,RA,DEC,AIRMASS,TEL_KEYW,BINX,BINY,' +
                              'FILTERS,MJD-MOBS'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file'    : rootpath+'/setup/trappist_S.swarp',

    # default catalog settings
    'astrometry_catalogs'  : ['GAIA'],
    #'astrometry_catalogs'  : ['GAIA', 'TGAS', 'USNO-B1.0', '2MASS'],
    'photometry_catalogs'  : ['PANSTARRS', 'SDSS-R9', 'APASS9']
}

trappist_sud_ESO_param = {
    'telescope_instrument' : 'Trappist-S', # telescope/instrument name
    'telescope_keyword'    : 'TRAPPIST-S',  # telescope/instrument keyword
    'observatory_code'     : 'I40',         # MPC observatory code
    'secpix'               : (0.64, 0.64 ), # pixel size (arcsec)
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
    'radec_separator'      : 'XXX',   # RA/Dec hms separator, use 'XXX'
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
                              'Exo': None, 'I+z': None, 'Clear': None},
                             # filtername translation dictionary
    'exptime'              : 'EXPTIME', # exposure time keyword (s)
    'airmass'              : 'AIRMASS', # airmass keyword


    # source extractor settings
    'source_minarea'       : 9, # default sextractor source minimum N_pixels
    'source_snr': 3, # default sextractor source snr for registration
    'aprad_default'        : 4, # default aperture radius in px
    'aprad_range'          : [2, 13], # [minimum, maximum] aperture radius (px)
    'sex-config-file'      : rootpath+'/setup/trappist_S.sex',
    'mask_file'            : {},
    #                        mask files as a function of x,y binning

    # registration settings (Scamp)
    'scamp-config-file'    : rootpath+'/setup/trappist_S.scamp',
    'reg_max_mag'          : 16,
    'reg_search_radius'    : 0.2, # deg
    'source_tolerance': 'high',

    # swarp settings
    'copy_keywords'        : ('OBSERVAT,INSTRUME,EXPTIME,OBJECT,' +
                              'DATE-OBS,RA,DEC,AIRMASS,TEL_KEYW,BINX,BINY,' +
                              'FILTERS,MJD-MOBS'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file'    : rootpath+'/setup/trappist_S.swarp',

    # default catalog settings
    'astrometry_catalogs'  : ['GAIA'],
    'photometry_catalogs'  : ['PANSTARRS', 'SDSS-R9', 'APASS9']
}


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
                              'SDSSzp' : 'z', 'z' : 'z', 'OH': None, 'CN': None,
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


specu_europa_param = {
    'telescope_instrument' : 'SPECULOOS2', # telescope/instrument name
    'telescope_keyword'    : 'SPECULOOS-EUROPA',  # telescope/instrument keyword
    #'observatory_code'     : 'W75',         # MPC observatory code
    'observatory_code'     : '309',         # MPC observatory code
    'secpix'               : (0.35, 0.35 ), # pixel size (arcsec)
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
    'radec_separator'      : 'XXX',   # RA/Dec hms separator, use 'XXX'
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
                              'I+z': None,'Clear': None},
                             # filtername translation dictionary
    'exptime'              : 'EXPTIME', # exposure time keyword (s)
    'airmass'              : 'AIRMASS', # airmass keyword


    # source extractor settings
    'source_minarea'       : 9, # default sextractor source minimum N_pixels
    'source_snr': 3, # default sextractor source snr for registration
    'aprad_default'        : 4, # default aperture radius in px
    'aprad_range'          : [2, 13], # [minimum, maximum] aperture radius (px)
    'sex-config-file'      : rootpath+'/setup/specu2.sex',
    'mask_file'            : {},
    #                        mask files as a function of x,y binning

    # registration settings (Scamp)
    'scamp-config-file'    : rootpath+'/setup/specu2.scamp',
    'reg_max_mag'          : 16,
    'reg_search_radius'    : 0.2, # deg
    'source_tolerance': 'high',

    # swarp settings
    'copy_keywords'        : ('OBSERVAT,INSTRUME,EXPTIME,OBJECT,' +
                              'DATE-OBS,RA,DEC,AIRMASS,TEL_KEYW,BINX,BINY,' +
                              'FILTERS,MJD-MOBS'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file'    : rootpath+'/setup/specu2.swarp',

    # default catalog settings
    'astrometry_catalogs'  : ['GAIA'],
    'photometry_catalogs'  : ['SDSS-R9', 'PANSTARRS', 'APASS9']
}


SNO_Artemis_param = {
    'telescope_instrument' : 'SNO_Artemis', # telescope/instrument name
    'telescope_keyword'    : 'ACP->Artemis',  # telescope/instrument keyword
    'observatory_code'     : '954',         # MPC observatory code
    'secpix'               : (0.35, 0.35), # pixel size (arcsec)
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
                              'SDSSzp' : 'z',
                              'g' : 'g', 'r' : 'r', 'i' : 'i', 'z' : 'z', 'u':'u',
                               'OH': None, 'CN': None,
                              'UC': None, 'NH': None, 'BC': None,
                              'C2': None, 'C3': None, 'CO+': None,
                              'H2O+': None, 'GC': None, 'RC': None, 'exoBB': None,
                              'Exo': None,'I+z': None,'Clear': None,'zcut': None},
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
    #'photometry_catalogs'  : ['SDSS-R9', 'PANSTARRS', 'APASS9']
    'photometry_catalogs'  : ['PANSTARRS', 'SDSS-R13', 'APASS9']
}

C2PU_omicron_param = {
    'telescope_instrument' : 'C2PU/Omicron', # telescope/instrument name
    'telescope_keyword'    : 'C2PU/Omicron',  # telescope/instrument keyword
    'observatory_code'     : '010',         # MPC observatory code
    'secpix'               : (0.235, 0.235), # pixel size (arcsec)
                                            # before binning
    'ext_coeff'            : 0.05,          # typical extinction coefficient


    # image orientation preferences
    'flipx'                : True,
    'flipy'                : False,
    'rotate'               : -1.5,

    # instrument-specific FITS header keywords
    'binning'              : ('BINX', 'BINY'),
                           # binning in x/y, '_blankN' denotes that both axes
                           # are listed in one keyword, sep. by blanks
    'extent'               : ('NAXIS1', 'NAXIS2'),   # N_pixels in x/y
    'ra'                   : 'RA_D',  # telescope pointing, RA
    'dec'                  : 'DEC_D', # telescope pointin, Dec
    'radec_separator'      : 'XXX',   # RA/Dec hms separator, use 'XXX'
                                    # if already in degrees
    'date_keyword'         : 'DATE-OBS', # obs date/time
                                         # keyword; use
                                         # 'date|time' if
                                         # separate
    'obsmidtime_jd'        : 'JD', # obs midtime jd keyword
                                         # (usually provided by
                                         # pp_prepare
    'object'               : 'OBJECT',  # object name keyword
    'filter'               : 'INSTFILT',  # filter keyword
    'filter_translations'  : {'V': 'V', 'R': 'R', 'Rc': 'R', 'B': 'B', 'VR': None,
                              'I': 'I', 'Ic': 'I', 'SDSSup' : 'u', 'SDSSgp' : 'g',
                              'SDSSrp' : 'r','SDSSrp+' : 'r', 'SDSSip' : 'i',
                              'SDSSzp' : 'z', 'OH': None, 'CN': None,
                              'UC': None, 'NH': None, 'BC': None,
                              'C2': None, 'C3': None, 'CO+': None,
                              'H2O+': None, 'GC': None, 'RC': None, 'exoBB': None,
                              'Exo': None,'I+z': None,'Clear': None,'zcut': None},
                             # filtername translation dictionary
    'exptime'              : 'EXPTIME', # exposure time keyword (s)
    'airmass'              : 'AIRMASS', # airmass keyword


    # source extractor settings
    'source_minarea'       : 9, # default sextractor source minimum N_pixels
    'source_snr': 3, # default sextractor source snr for registration
    'aprad_default'        : 4, # default aperture radius in px
    'aprad_range'          : [4, 13], # [minimum, maximum] aperture radius (px)
    'sex-config-file'      : rootpath+'/setup/trappist_N.sex',
    'mask_file'            : {},
    #                        mask files as a function of x,y binning

    # registration settings (Scamp)
    'scamp-config-file'    : rootpath+'/setup/trappist_N.scamp',
    'reg_max_mag'          : 16,
    'reg_search_radius'    : 0.4, # deg
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
    #'photometry_catalogs'  : ['SDSS-R9', 'PANSTARRS', 'APASS9']
    'photometry_catalogs'  : ['PANSTARRS', 'SDSS-R9', 'APASS9']
}



NTT_EFOSC_param = {
    'telescope_instrument' : 'EFOSC', # telescope/instrument name
    'telescope_keyword'    : 'ESO-NTT',  # telescope/instrument keyword
    'observatory_code'     : '809',         # MPC observatory code
    'secpix'               : (0.12, 0.12), # pixel size (arcsec)
                                            # before binning
    'ext_coeff'            : 0.05,          # typical extinction coefficient


    # image orientation preferences
    'flipx'                : False,
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
    'obsmidtime_jd'        : 'MJD_OBS', # obs midtime jd keyword
                                         # (usually provided by
                                         # pp_prepare
    'object'               : 'OBJECT',  # object name keyword
    'filter'               : 'HIERARCH ESO INS FILT1 NAME',  # filter keyword
    'filter_translations'  : {'r#784' : 'R'},
                             # filtername translation dictionary
    'exptime'              : 'EXPTIME', # exposure time keyword (s)
    'airmass'              : 'HIERARCH ESO TEL AIRM END', # airmass keyword


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
    #'photometry_catalogs'  : ['SDSS-R9', 'PANSTARRS', 'APASS9']
    'photometry_catalogs'  : ['PANSTARRS', 'SDSS-R9', 'APASS9']
}


janus_sud_param = {
    'telescope_instrument' : 'Janus Sud', # telescope/instrument name
    'telescope_keyword'    : 'ZWO ASI1600MM-Cool',  # telescope/instrument keyword
    'observatory_code'     : '',         # MPC observatory code
    'secpix'               : (0.42, 0.42 ), # pixel size (arcsec)
                                            # before binning
    'ext_coeff'            : 0.05,          # typical extinction coefficient


    # image orientation preferences
    'flipx'                : True,
    'flipy'                : False,
    'rotate'               : 0,

    # instrument-specific FITS header keywords
    'binning'              : ('X1', 'Y1'),
                           # binning in x/y, '_blankN' denotes that both axes
                           # are listed in one keyword, sep. by blanks
    'extent'               : ('NAXIS1', 'NAXIS2'),   # N_pixels in x/y
    'ra'                   : 'RA',  # telescope pointing, RA
    'dec'                  : 'DEC', # telescope pointin, Dec
    'radec_separator'      : 'XXX',   # RA/Dec hms separator, use 'XXX'
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
                              'I+z': None,'Clear': None},
                             # filtername translation dictionary
    'exptime'              : 'EXPOSURE', # exposure time keyword (s)
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
    'photometry_catalogs'  : ['SDSS-R9', 'PANSTARRS', 'APASS9']
}




liverpool2m_param = {
    'telescope_instrument' : 'LT2m', # telescope/instrument name
    'telescope_keyword'    : 'Liverpool Telescope',  # telescope/instrument keyword
    'observatory_code'     : 'J13',         # MPC observatory code
    'secpix'               : (0.15185, 0.15185), # pixel size (arcsec)
                                            # before binning
    'ext_coeff'            : 0.05,          # typical extinction coefficient


    # image orientation preferences
    'flipx'                : True,
    'flipy'                : False,
    'rotate'               : 0,

    # instrument-specific FITS header keywords
    'binning'              : ('CCDXBIN', 'CCDYBIN'),
                           # binning in x/y, '_blankN' denotes that both axes
                           # are listed in one keyword, sep. by blanks
    'extent'               : ('NAXIS1', 'NAXIS2'),   # N_pixels in x/y
    'ra'                   : 'RA',  # telescope pointing, RA
    'dec'                  : 'DEC', # telescope pointin, Dec
    'radec_separator'      : ':',   # RA/Dec hms separator, use 'XXX'
                                    # if already in degrees
    'date_keyword'         : 'DATE-OBS', # obs date/time
                                         # keyword; use
                                         # 'date|time' if
                                         # separate
    'obsmidtime_jd'        : 'JD', # obs midtime jd keyword
                                         # (usually provided by
                                         # pp_prepare
    'object'               : 'OBJECT',  # object name keyword
    'filter'               : 'FILTER1',  # filter keyword
    'filter_translations'  : {'SDSS-R':'r','SDSS-I':'i'},
                             # filtername translation dictionary
    'exptime'              : 'EXPTIME', # exposure time keyword (s)
    'airmass'              : 'AIRMASS', # airmass keyword


    # source extractor settings
    'source_minarea'       : 9, # default sextractor source minimum N_pixels
    'source_snr': 3, # default sextractor source snr for registration
    'aprad_default'        : 4, # default aperture radius in px
    'aprad_range'          : [2, 13], # [minimum, maximum] aperture radius (px)
    'sex-config-file'      : rootpath+'/setup/LT2m.sex',
    'mask_file'            : {},
    #                        mask files as a function of x,y binning

    # registration settings (Scamp)
    'scamp-config-file'    : rootpath+'/setup/LT2m.scamp',
    'reg_max_mag'          : 16,
    'reg_search_radius'    : 0.2, # deg
    'source_tolerance': 'high',

    # swarp settings
    'copy_keywords'        : ('OBSERVAT,INSTRUME,EXPTIME,OBJECT,' +
                              'DATE-OBS,RA,DEC,AIRMASS,TEL_KEYW,BINX,BINY,' +
                              'FILTERS,MJD-MOBS'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file'    : rootpath+'/setup/LT2m.swarp',

    # default catalog settings
    'astrometry_catalogs'  : ['GAIA'],
    #'photometry_catalogs'  : ['SDSS-R9', 'PANSTARRS', 'APASS9']
    'photometry_catalogs'  : ['PANSTARRS', 'SDSS-R9', 'APASS9']
}

spacewatch_09m_param = {
    'telescope_instrument' : 'Spacewatch Mosaic Camera', # telescope/instrument name
    'telescope_keyword'    : 'Spacewatch 0.9-m f/3 prime focus',  # telescope/instrument keyword
    'observatory_code'     : '691',         # MPC observatory code
    'secpix'               : (1.0, 1.0), # pixel size (arcsec)
                                            # before binning
    'ext_coeff'            : 0.05,          # typical extinction coefficient


    # image orientation preferences
    'flipx'                : True,
    'flipy'                : False,
    'rotate'               : 0,

    # instrument-specific FITS header keywords
    'binning'              : ('Bin1', 'Bin2'),
                           # binning in x/y, '_blankN' denotes that both axes
                           # are listed in one keyword, sep. by blanks
    'extent'               : ('NAXIS1', 'NAXIS2'),   # N_pixels in x/y
    'ra'                   : 'RA',  # telescope pointing, RA
    'dec'                  : 'DEC', # telescope pointin, Dec
    'radec_separator'      : ':',   # RA/Dec hms separator, use 'XXX'
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
    'filter_translations'  : {'Schott OG-515': None},
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
    #'photometry_catalogs'  : ['SDSS-R13', 'PANSTARRS', 'APASS9']
    #'photometry_catalogs'  : ['SDSS-R9', 'PANSTARRS', 'APASS9']
    'photometry_catalogs'  : ['PANSTARRS', 'SDSS-R9', 'APASS9']
    #'photometry_catalogs'  : ['APASS9', 'PANSTARRS', 'SDSS-R9']
}


# add telescope configurations to 'official' telescopes.py

implemented_telescopes.append('TRAPPIST-South')
implemented_telescopes.append('NTT_EFOSC')
implemented_telescopes.append('SPECULOOS_Europa')
implemented_telescopes.append('SNO_Artemis')
implemented_telescopes.append('C2PU/Omicron')
implemented_telescopes.append('TRAPPIST-North')
implemented_telescopes.append('Trappist')
implemented_telescopes.append('LT2m')
implemented_telescopes.append('Spacewatch-0.9m')


# translate INSTRUME (or others, see _pp_conf.py) header keyword into
#   PP telescope keyword
# example: INSTRUME keyword in header is 'mytel'
instrument_identifiers['EFOSC'] = 'ESO'
instrument_identifiers['FLI-New'] = 'TRAPPIST'
instrument_identifiers['TRAPPISTS'] = 'TRAPPIST-S'
instrument_identifiers['Omicron Prime Focus (OPF)'] = 'C2PU/Omicron'
#instrument_identifiers['CCD-23156'] = 'Artemis'
instrument_identifiers['CCD-23156'] = 'ACP->Artemis'
instrument_identifiers['SPECULOOS2'] = 'SPECULOOS-EUROPA'
instrument_identifiers['Andor Tech'] = 'ACP->NTM'
instrument_identifiers['IO:O'] = 'LT2m' 
#instrument_identifiers['Spacewatch Mosaic Camera'] = 'Spacewatch-0.9m' 
instrument_identifiers['Spacewatch Mosaic Camera'] = 'Spacewatch 0.9-m f/3 prime focus'


# translate telescope keyword into parameter set defined here
telescope_parameters['TRAPPIST'] = trappist_sud_param
telescope_parameters['TRAPPIST-S'] = trappist_sud_ESO_param
telescope_parameters['ACP->NTM'] = trappist_nord_param
telescope_parameters['SPECULOOS-EUROPA'] = specu_europa_param
#telescope_parameters['Artemis'] = SNO_Artemis_param
telescope_parameters['ACP->Artemis'] = SNO_Artemis_param
telescope_parameters['C2PU/Omicron'] = C2PU_omicron_param
telescope_parameters['ESO-NTT'] = NTT_EFOSC_param
telescope_parameters['LT2m'] = liverpool2m_param
#telescope_parameters['Spacewatch-0.9m'] = spacewatch_09m_param
telescope_parameters['Spacewatch 0.9-m f/3 prime focus'] = spacewatch_09m_param
