#!/usr/bin/env python
# 
# Copyright 2014 Institute for Theoretical Information Technology,
#                RWTH Aachen University
#                www.ti.rwth-aachen.de
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest
import ofdm_swig as ofdm

class qa_bit_position_dependent_ber (gr_unittest.TestCase):

  def setUp (self):
    self.tb = gr.top_block()
    
  def tearDown(self):
    self.tb = None
  
  def test_001( self ):
    vlen = 256
    N = 100000
    
    refdata = random_integers(0, 1, N)
    data = random_integers(0, 1, N)
    
    ref = numpy.array([0]*vlen)
    for x in range(len(data)):
      ref[x%vlen] += 1 if refdata[x] != data[x] else 0
      
    src0 = gr.vector_source_b( refdata.tolist() )
    src1 = gr.vector_source_b( data.tolist() )
    src2 = gr.vector_source_i( [vlen]*N )
    
    uut = ofdm.bit_position_dependent_BER( "test" )
    
    self.tb.connect( src0, ( uut, 0 ) )
    self.tb.connect( src1, ( uut, 1 ) )
    self.tb.connect( src2, ( uut, 2 ) )
    
    self.tb.run()
    
    ret = numpy.array( uut.get_cntr_vec() )
    
    self.assertTrue( (ret==ref).all() )
    
  
  def test_002( self ):
    vlen = 200
    N = 100000
    _n = N / vlen
    
    refdata = random_integers(0, 1, N)
    data = random_integers(0, 1, N)
    
    
    ref = numpy.array([0]*(vlen/2))
    for x in range(N/2, N):
      ref[x%(vlen/2)] += 1 if refdata[x] != data[x] else 0
    
    vlen = concatenate( [ [vlen]*(_n/2), [vlen/2]*(_n)] ) 
    src0 = gr.vector_source_b( refdata.tolist() )
    src1 = gr.vector_source_b( data.tolist() )
    src2 = gr.vector_source_i( vlen.tolist() )
    
    uut = ofdm.bit_position_dependent_BER( "test" )
    
    self.tb.connect( src0, ( uut, 0 ) )
    self.tb.connect( src1, ( uut, 1 ) )
    self.tb.connect( src2, ( uut, 2 ) )
    
    if os.path.exists("test_000.uint"):
      os.remove("test_000.uint")
    
    self.assertTrue( not os.path.exists("test_000.uint") )
    
    self.tb.run()
    
    ret = numpy.array( uut.get_cntr_vec() )

    self.assertTrue( (ret==ref).all() )
    
    self.assertTrue( os.path.exists("test_000.uint"))  
    
    
  def test_003( self ):
    vlen = 200
    N = 100000
    _n = N / vlen
    
    refdata = random_integers(0, 1, N)
    data = random_integers(0, 1, N)
    
    vlen = concatenate( [ [vlen]*(_n/2), [vlen/2]*(_n/2), [vlen/4]*(_n)] ) 
    src0 = gr.vector_source_b( refdata.tolist() )
    src1 = gr.vector_source_b( data.tolist() )
    src2 = gr.vector_source_i( vlen.tolist() )
    
    uut = ofdm.bit_position_dependent_BER( "test" )
    
    self.tb.connect( src0, ( uut, 0 ) )
    self.tb.connect( src1, ( uut, 1 ) )
    self.tb.connect( src2, ( uut, 2 ) )
    
    if os.path.exists("test_000.uint"):
      os.remove("test_000.uint")
    if os.path.exists("test_001.uint"):
      os.remove("test_001.uint")
      
    self.assertTrue( not os.path.exists("test_000.uint") )
    self.assertTrue( not os.path.exists("test_001.uint") )
    
    self.tb.run()
    
    self.assertTrue( os.path.exists("test_000.uint"))
    self.assertTrue( os.path.exists("test_001.uint"))

if __name__ == '__main__':
    gr_unittest.run(qa_bit_position_dependent_ber, "qa_bit_position_dependent_ber.xml")
