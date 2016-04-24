# Copyright 2015-2016 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2

doc = """Metadata plug-in module for repoman.
Performs metadata checks on packages."""
__doc__ = doc[:]


module_spec = {
	'name': 'metadata',
	'description': doc,
	'provides':{
		'pkg-metadata': {
			'name': "pkgmetadata",
			'sourcefile': "pkgmetadata",
			'class': "PkgMetadata",
			'description': doc,
			'functions': ['check'],
			'func_desc': {
			},
			'mod_kwargs': ['repo_settings', 'qatracker', 'options', 'metadata_dtd',
			],
			'func_kwargs': {'xpkg': None, 'checkdir': None, 'checkdirlist': None,
				'repolevel': None, 'muselist': 'Future',
			},
		},
		'ebuild-metadata': {
			'name': "ebuild_metadata",
			'sourcefile': "ebuild_metadata",
			'class': "EbuildMetadata",
			'description': doc,
			'functions': ['check'],
			'func_desc': {
			},
			'mod_kwargs': ['qatracker',
			],
			'func_kwargs': {'ebuild': None, 'catdir': None, 'live_ebuild': None,
				'xpkg': None, 'y_ebuild': None,
			},
		},
		'description-metadata': {
			'name': "description",
			'sourcefile': "description",
			'class': "DescriptionChecks",
			'description': doc,
			'functions': ['check'],
			'func_desc': {
			},
			'mod_kwargs': ['qatracker',
			],
			'func_kwargs': {'ebuild': None, 'pkg': 'Future',
			},
		},
		'license-metadata': {
			'name': "license",
			'sourcefile': "license",
			'class': "LicenseChecks",
			'description': doc,
			'functions': ['check'],
			'func_desc': {
			},
			'mod_kwargs': ['qatracker', 'repo_metadata',
			],
			'func_kwargs': {'xpkg': None, 'ebuild': None, 'y_ebuild': None,
				'badlicsyntax': None,
			},
		},
		'restrict-metadata': {
			'name': "restrict",
			'sourcefile': "restrict",
			'class': "RestrictChecks",
			'description': doc,
			'functions': ['check'],
			'func_desc': {
			},
			'mod_kwargs': ['qatracker',
			],
			'func_kwargs': {'xpkg': None, 'ebuild': None, 'y_ebuild': None,
			},
		},
		'unused-metadata': {
			'name': "unused",
			'sourcefile': "unused",
			'class': "UnusedCheck",
			'description': doc,
			'functions': ['check'],
			'func_desc': {
			},
			'mod_kwargs': ['qatracker',
			],
			'func_kwargs': {'xpkg': None, 'muselist': None, 'used_useflags': None,
				'validity_future': None,
			},
		},
	}
}

