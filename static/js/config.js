window._skel_config = {
	prefix: 'style/style',
	resetCSS: true,
	boxModel: 'border',
	containers: 1180,
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
			range: '-1200',
			containers: 960,
			viewportWidth: 1080
		},
		'narrower': {
			range: '-960',
			containers: 'fluid',
			lockViewport: true,
			grid: {
				gutters: 10,
				collapse: true
			}
		},
		'mobile': {
			range: '-480',
			containers: 'fluid',
			lockViewport: true,
			grid: {
				gutters: 5,
				collapse: true
			}
		}
	}
};