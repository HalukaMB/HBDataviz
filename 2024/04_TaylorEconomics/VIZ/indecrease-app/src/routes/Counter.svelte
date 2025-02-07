<script lang="ts">
	import { spring } from 'svelte/motion';
	import taylorstart from '$lib/images/taylor-singing.png';
	import taylorstop from '$lib/images/TaylorStart-removebg-preview.png';

	let clickcounter = 0;
	let seconds = 0;
	let timerId = null;
	let dollars = 0;
	let dollars_to_earn = 20;
	$: dollars = 5.85 * seconds;

	function update() {
		console.log('clicked');
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
	$: offset = displayed_count;
</script>

<div class="taylorstartstop">
	{#if clickcounter % 2 != 0}
		<img src={taylorstart} type="image/png" alt="Taylor Swift singt" />
	{:else}
		<img src={taylorstop} type="image/png" alt="Taylor Swift steht" />
	{/if}
</div>
<div>
	Schätzen Sie, wie lange Taylor Swift braucht, bis sie {dollars_to_earn} Dollar verdient hat.
</div>
<div class="counter">
	<div class="counter-viewport">
		<div class="counter-digits" style="transform: translate(0, {100 * offset}%)">
			<strong class="hidden" aria-hidden="true">{(Math.floor(seconds + 1) * 10) / 10}</strong>
			{#if clickcounter % 2 != 0}
				<strong>{Math.floor(seconds * 10) / 10} s</strong>
			{:else}
				<strong>$ {Math.floor(dollars * 10) / 10}</strong>
			{/if}
		</div>
	</div>
	<div class="commentfield">
		{#if clickcounter % 2 == 0 && clickcounter != 0}
			{#if dollars / dollars_to_earn < 0.8}
				<div>Naja, das wäre ein bisschen sehr schnell.</div>
			{:else if dollars / dollars_to_earn > 1.2}
				<div>Taylor ist da schneller.</div>
			{:else}
				<div>Recht gut geschätzt.</div>
			{/if}
		{:else}
			<div></div>
		{/if}
	</div>
</div>
<div class="counter-button-div">
	<button on:click={update}>
		{clickcounter % 2 != 0 ? 'Stop' : 'Start'}
	</button>
</div>

<style>
	.counter {
		width: 90%;
		display: flex;
		border-top: 1px solid rgba(0, 0, 0, 0.1);
		border-bottom: 1px solid rgba(0, 0, 0, 0.1);
		padding: 0.5em;
		margin: 1rem 0;
	}

	.counter-button-div button {
		width: 5em;
		height: 2em;
		border-radius: 0.2em;

		padding: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		border: 0;
		background-color: transparent;
		touch-action: manipulation;
		font-size: 2rem;
		white-space: nowrap;
		color: white;
		background-color: #ef7c00;
		border-color: #ef7c00;
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

	img {
		object-fit: contain;
		height: 170px;
		width: auto; /*maintain aspect ratio*/
		max-width: 500px;
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
