import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vitest/config';

module.exports = {
	root: 'src',
	build: {
	  outDir: '../dist'
	}
  }
export default defineConfig({
	plugins: [sveltekit()],
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	}
});


