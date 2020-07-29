<template>
    <nav class="navbar navbar-expand-xl navbar-light bg-white">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">
            <img src="https://static.wixstatic.com/media/6b110f_870f3df6604e494b85b3ed0bac7dbcaf~mv2.png/v1/fill/w_74,h_74,al_c,q_85,usm_0.66_1.00_0.01/ias-logo-final.webp" alt="logo" width="45">
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto text-center">
            <li class="nav-item">
            <router-link class="nav-link active" to="/">HOME</router-link>
            </li>
            <li class="nav-item">
            <router-link class="nav-link active" to="/ffds">CALL FOR ARTISTS</router-link>
            </li>
            <li class="nav-item">
            <router-link class="nav-link active" to="/d">CURRENT EXHIBITIONS</router-link>
            </li>
            <li class="nav-item">
            <router-link class="nav-link active" to="/f">PAST EXHIBITIONS</router-link>
            </li>
            <li class="nav-item">
            <router-link class="nav-link active" to="/fd">FEATURED ARTISTS</router-link>
            </li>
            <li class="nav-item">
            <router-link class="nav-link active" to="/art-new-market">ART MARKET NEWS</router-link>
            </li>
            <li class="nav-item">
            <router-link class="nav-link active" to="/about">ABOUT</router-link>
            </li>
            <li class="nav-item">
            <router-link class="nav-link active" to="/contact">CONTACT US</router-link>
            </li>
           
        </ul>
        </div>
    </div>
    </nav>
</template>
<script>
export default {
    name : "TheNav"
}
</script>

<style>

</style>