#
# Copyright 2008,2009 Free Software Foundation, Inc.
#
# This application is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This application is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

# The presence of this file turns this directory into a Python package

'''
This is the GNU Radio OFDM module. Place your Python package
description here (python/__init__.py).
'''
from __future__ import unicode_literals

# import swig generated symbols into the ofdm namespace
try:
    # this might fail if the module is python-only
    from .ofdm_swig import *
except ImportError:
    pass

# import any pure python here
from .fbmc_insert_preamble_vcvc import fbmc_insert_preamble_vcvc
from .fbmc_overlapping_parallel_to_serial_vcc import fbmc_overlapping_parallel_to_serial_vcc
from .fbmc_overlapping_serial_to_parallel_cvc import fbmc_overlapping_serial_to_parallel_cvc
from .fbmc_vector_reshape_vcvc import fbmc_vector_reshape_vcvc
from .fbmc_remove_preamble_vcvc import fbmc_remove_preamble_vcvc
from .fbmc_channel_hier_cc import fbmc_channel_hier_cc
from .fbmc_receiver_hier_cb import fbmc_receiver_hier_cb
from .fbmc_transmitter_hier_bc import fbmc_transmitter_hier_bc
from .fbmc_symbol_estimation_vcb import fbmc_symbol_estimation_vcb
from .fbmc_symbol_creation_bvc import fbmc_symbol_creation_bvc
from .ber_reference_source_grc import ber_reference_source_grc
from .ofdm_frame_sampler_grc import ofdm_frame_sampler
from .fbmc_frame_sampler_grc import fbmc_frame_sampler
from .fbmc_transmitter_demo import fbmc_transmitter_demo
from .fbmc_receiver_demo import fbmc_receiver_demo
from .fbmc_transmitter_multiuser_bc import fbmc_transmitter_multiuser_bc
from .fbmc_receiver_multiuser_cb import fbmc_receiver_multiuser_cb
from .scfdma_transmitter_bc import scfdma_transmitter_bc
from .scfdma_receiver_cb import scfdma_receiver_cb
from .fbmc_insert_preamble_mu_vcvc import fbmc_insert_preamble_mu_vcvc
# from scfdma_transmitter_bc import scfdma_transmitter_bc
from .scfdma_receiver_cb import scfdma_receiver_cb
from .fbmc_insert_preamble_mu_vcvc import fbmc_insert_preamble_mu_vcvc

#

# ----------------------------------------------------------------
# Tail of workaround
# if _RTLD_GLOBAL != 0:
#     sys.setdlopenflags(_dlopenflags)      # Restore original flags
# ----------------------------------------------------------------
