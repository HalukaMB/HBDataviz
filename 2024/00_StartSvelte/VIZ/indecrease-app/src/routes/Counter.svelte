<script lang="ts">
	import { spring } from 'svelte/motion';
	let clickcounter = 0;
	 let tenseconds = 0;
	let timerId = null;

	function update() {
		clickcounter += 1;
		console.log('clicked: ', clickcounter);
		if (clickcounter % 2 == 0) {
			stop();
		}
		if (clickcounter % 2 == 1) {
			start();
		}
	}
	let start = () => {
        tenseconds = 0;
		timerId = setInterval(() => {
			tenseconds += 0.1;
		}, 100);
	};
	let stop = () => {
		clearInterval(timerId);
		timerId = null;
        console.log(tenseconds);
	};

	let count = 0;

	//
	const displayed_count = spring();
	$: displayed_count.set(count);
	$: offset = modulo($displayed_count, 1);

	function modulo(n: number, m: number) {
		// handle negative numbers
		return ((n % m) + m) % m;
	}
</script>

<div class="counter">


	<div class="counter-viewport">
		<div class="counter-digits" style="transform: translate(0, {100 * offset}%)">
			<strong class="hidden" aria-hidden="true">{(10*Math.floor(tenseconds + 1))/10}</strong>
			<strong>{10*Math.floor(tenseconds)}</strong>
		</div>
	</div>
	<button on:touchstart={update}>
		{(clickcounter%2!=0)? 'Stop' : 'Start'}
	</button>

</div>

<style>
	.counter {
		display: flex;
		border-top: 1px solid rgba(0, 0, 0, 0.1);
		border-bottom: 1px solid rgba(0, 0, 0, 0.1);
		margin: 1rem 0;
	}

	.counter button {
		width: 2em;
		padding: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		border: 0;
		background-color: transparent;
		touch-action: manipulation;
		font-size: 2rem;
	}

	.counter button:hover {
		background-color: var(--color-bg-1);
	}

	svg {
		width: 25%;
		height: 25%;
	}

	path {
		vector-effect: non-scaling-stroke;
		stroke-width: 2px;
		stroke: #444;
	}

	.counter-viewport {
		width: 8em;
		height: 4em;
		overflow: hidden;
		text-align: center;
		position: relative;
	}

	.counter-viewport strong {
		position: absolute;
		display: flex;
		width: 100%;
		height: 100%;
		font-weight: 400;
		color: var(--color-theme-1);
		font-size: 4rem;
		align-items: center;
		justify-content: center;
	}

	.counter-digits {
		position: absolute;
		width: 100%;
		height: 100%;
	}

	.hidden {
		top: -100%;
		user-select: none;
	}
</style>
