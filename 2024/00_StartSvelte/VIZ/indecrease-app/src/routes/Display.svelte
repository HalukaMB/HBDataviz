<script>
    let clickcounter = 0
    let timeinseconds = 0
    const timefunction=setInterval(()=>{timeinseconds+=1;
    console.log(timeinseconds);
    },1000)


	let name = 'world';
	function update() {
		name = 'Svelte';
        clickcounter += 1
        console.log(clickcounter);
        if (clickcounter%2==0){
            stop()

        }
        if (clickcounter%2==1){
            start()

        }

	}
    let start=()=>{
        console.log("start");
        timefunction;
    }
    let stop=()=>{
        clearInterval(timefunction)
        console.log("stop");
    }


  

</script>
<button
	on:touchstart={update}
    >
  Hello {name}!
</button>

