<script>
	let clickcounter = 0;
	export let seconds = 0;
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
        seconds = 0;
		timerId = setInterval(() => {
			seconds += 1;
		}, 1000);
	};
	let stop = () => {
		clearInterval(timerId);
		timerId = null;
        console.log(seconds);
	};
</script>

<button on:touchstart={update}>
	{(clickcounter%2!=0)? 'Stop' : 'Start'}
</button>
