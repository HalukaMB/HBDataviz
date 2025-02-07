<script lang="ts">
	import { spring } from 'svelte/motion';
	import taylorstart from '$lib/images/taylor-singing.png';
	import taylorstop from '$lib/images/TaylorStop-removebg-preview.png';

	let clickcounter = 0;
	let seconds = 0;
	let timerId = null;

	function update() {
		console.log("clicked")
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
		seconds = 0;
		timerId = setInterval(() => {
			seconds += 0.1;
		}, 100);
	};
	let stop = () => {
		clearInterval(timerId);
		timerId = null;
		console.log(seconds);
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

<div class="taylorstartstop">
	{#if (clickcounter % 2 != 0)}
		<img src={taylorstart} type="image/png" alt="Taylor Swift läuft"/>
	{:else}
		<img src={taylorstop} type="image/png"  alt="Taylor Swift steht"/>
	{/if}
</div>

<div class="counter">
	<div class="counter-viewport">
		<div class="counter-digits" style="transform: translate(0, {100 * offset}%)">
			<strong class="hidden" aria-hidden="true">{Math.floor(seconds * 5.85 + 0.1)}</strong>
			<strong>$ {Math.floor(seconds * 5.85)}</strong>
		</div>
	</div>
</div>
<div class="counter">
	<button on:click={update}>
		{clickcounter % 2 != 0 ? 'Stop' : 'Start'}
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
	.taylorstartstop {
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 1rem 0;
		min-height: 3em;
		min-width: 3em;

	}

	img{
		object-fit: contain;
		height:170px;
    width:auto;/*maintain aspect ratio*/
    max-width:500px;
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
		width: 16em;
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
		color: #e87511;
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
