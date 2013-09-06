window._skel_config = {
	prefix: '/style/style',
	resetCSS: true,
	boxModel: 'border',
	containers: 1100,
	grid: {
		gutters: 40
	},
	breakpoints: {
		'wide': {
			range: '1660-'
		},
		'normal': {
			range: '-1659'
		},
		'narrow': {
			range: '-1100',
			containers: 630,
			viewportWidt5: 1000
		},
		'narrower': {
			range: '-500',
			containers: 'fluid',
			lockViewport: true,
			grid: {
				gutters: 10
			}
		},
		'mobile': {
			range: '-480',
			containers: 'fluid',
			lockViewport: true,
			grid: {
				gutters: 5
			}
		}
	}
};