# Copyright 2013 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2

from portage.tests import TestCase
from portage.tests.resolver.ResolverPlayground import (ResolverPlayground,
	ResolverPlaygroundTestCase)

class SlotChangeWithoutRevBumpTestCase(TestCase):

	def testSlotChangeWithoutRevBump(self):

		ebuilds = {
			"app-arch/libarchive-3.1.1" : {
				"EAPI": "5",
				"SLOT": "0/13"
			},
			"app-arch/libarchive-3.0.4-r1" : {
				"EAPI": "5",
				"SLOT": "0"
			},
			"kde-base/ark-4.10.0" : {
				"EAPI": "5",
				"DEPEND": "app-arch/libarchive:=",
				"RDEPEND": "app-arch/libarchive:="
			},
		}

		installed = {
			"app-arch/libarchive-3.1.1" : {
				"EAPI": "5",
				"SLOT": "0"
			},

			"kde-base/ark-4.10.0" : {
				"EAPI": "5",
				"DEPEND": "app-arch/libarchive:0/0=",
				"RDEPEND": "app-arch/libarchive:0/0="
			},
		}

		world = ["kde-base/ark"]

		test_cases = (

			# Demonstrate bug #456208, where a sub-slot change
			# without revbump needs to trigger a rebuild.
			ResolverPlaygroundTestCase(
				["kde-base/ark"],
				options = {"--oneshot": True},
				success = True,
				mergelist = ['app-arch/libarchive-3.1.1', "kde-base/ark-4.10.0"]),

		)

		playground = ResolverPlayground(ebuilds=ebuilds,
			installed=installed, world=world, debug=False)
		try:
			for test_case in test_cases:
				playground.run_TestCase(test_case)
				self.assertEqual(test_case.test_success, True, test_case.fail_msg)
		finally:
			playground.cleanup()
