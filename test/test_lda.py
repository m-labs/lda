import unittest
import sys

from sipyco.test.generic_rpc import GenericRPCCase
from lda.driver import dB


class GenericLdaTest:
    def test_attenuation(self):
        step = self.cont.get_att_step_size()
        attmax = self.cont.get_att_max()
        test_vector = [i*step*dB for i in range(0, int(attmax*int(1/step)+1))]
        for i in test_vector:
            with self.subTest(i=i):
                self.cont.set_attenuation(i)
                j = self.cont.get_attenuation()
                self.assertEqual(i, j)


class TestLdaSim(GenericRPCCase, GenericLdaTest):
    def setUp(self):
        GenericRPCCase.setUp(self)
        command = (sys.executable.replace("\\", "\\\\")
                            + " -m lda.aqctl_lda "
                            + "-p 3253 --simulation")
        self.cont = self.start_server("lda", command, 3253)
