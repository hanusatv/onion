<script>
	import Navbar from "./Navbar.svelte";
	import Router from "svelte-spa-router";
	import Home from "./routes/Home.svelte";
	import Createelement from "./routes/Createelement.svelte";

	let routes = {
		"/": Home,
		"/createelement": Createelement,
	};
</script>

<body>
	<nav>
		<Navbar />
	</nav>
	<main class="main">
		<Router {routes} />
	</main>
</body>

<style>
</style>
