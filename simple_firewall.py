'''
Udacity: ud436/sdn-firewall
Professor: Nick Feamsteres
'''

################################################################################
# The Pyretic Project                                                          #
# frenetic-lang.org/pyretic                                                    #
# author: Joshua Reich (jreich@cs.princeton.edu)                               #
################################################################################
# Licensed to the Pyretic Project by one or more contributors. See the         #
# NOTICES file distributed with this work for additional information           #
# regarding copyright and ownership. The Pyretic Project licenses this         #
# file to you under the following license.                                     #
#                                                                              #
# Redistribution and use in source and binary forms, with or without           #
# modification, are permitted provided the following conditions are met:       #
# - Redistributions of source code must retain the above copyright             #
#   notice, this list of conditions and the following disclaimer.              #
# - Redistributions in binary form must reproduce the above copyright          #
#   notice, this list of conditions and the following disclaimer in            #
#   the documentation or other materials provided with the distribution.       #
# - The names of the copyright holds and contributors may not be used to       #
#   endorse or promote products derived from this work without specific        #
#   prior written permission.                                                  #
#                                                                              #
# Unless required by applicable law or agreed to in writing, software          #
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT    #
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the     #
# LICENSE file distributed with this work for specific language governing      #
# permissions and limitations under the License.                               #
################################################################################

from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.modules.mac_learner  
	
def firewall(self):

	def AddRule (switch, srcmac, value=True):
		self.firewall[(switch, srcmac)]=value
		print "Adding Firewall rule in %s: %s" % (switch, srcmac)
		self.policy = parallel([ (match(switch=switch) &
				          match(srcmac=srcmac))
				         for (switch, srcmac)
				         in self.firewall.keys()])
	self.AddRule = AddRule
	
	def initialize():
	#Initialize the firewall
		print "initializing firewall"
		self.firewall = {}

		self.AddRule(1, MAC('00:00:00:00:00:01'))
		self.AddRule(1, MAC('00:00:00:00:00:02'))
	
	initialize()


def main():
	return dynamic(firewall)() >> dynamic(learn)()
	
