<template>
    <div class="hero text-center">
        <img class="hero-img" src="https://res.cloudinary.com/manascode/image/upload/v1595652449/final-gallery_y64bwl.webp" alt="Image-hero">
        <div class="gallery-hero">
            <SliderGallery/>
        </div>
        <div class="gallery-text-hero">
            <h1 class="gallery-text-h1">INTERNATIONAL</h1> 
            <h1 class="gallery-text-h1">ART  SHOWCASE</h1>
        </div>
    </div>
</template>

<script>
import SliderGallery from '../common/SliderGallery'
export default {
    name: "Hero",
    components : {
        SliderGallery
    }
}
</script>
<style>
.hero{
    position: relative;
    width: 100%;
    height: 690px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.hero-img{
    width: 100%;
    height: 690px;
    object-fit: cover;
}
.gallery-hero{
    /* background-color: #FF0000; */
    width: 300px;
    height: 250px;
    position: absolute;
    top: 10.5rem;
}
.gallery-text-hero{
 position: absolute;
 bottom: 1rem;
}
.gallery-text-h1{
    font-size: 5rem!important;
    color: #fff;
}
@media only screen and (max-width: 648px){
    .gallery-text-hero{
    position: absolute;
    bottom: 3rem;
    
    }
    .gallery-text-h1{
    font-size: 3rem!important;
    }
}
@media only screen and (max-width: 375px){
    .gallery-text-hero{
    position: absolute;
    bottom: 4rem;
    
    }
    .gallery-text-h1{
    font-size: 2.5rem!important;
    }
}
</style>